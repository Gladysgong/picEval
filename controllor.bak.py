#! /usr/bin/env python
# coding=utf-8
import subprocess
import pymysql
import time
from lib import logUtils
from imgconf1 import *
import signal

# db = pymysql.connect(database_host,database_user,database_pass,database_data)
# cursor = db.cursor()
log_fd = open('log/log', 'a')


def get_running_id(cursor, loginfo):
    # sql = "SELECT id FROM {_table} where status=2 and runningIP='{_ip}' limit 1".format(_table=database_table,_ip=local_ip)
    sql = "SELECT id FROM {_table} where status=2 and svIP='{_ip}' limit 1".format(_table=database_table, _ip=local_ip)
    loginfo.log_info(sql)
    cursor.execute(sql)
    data = cursor.fetchone()
    if data is not None:
        return data[0]
    return -1


def get_my_id(cursor, loginfo):
    # sql = "SELECT id FROM {_table} where status=1 and runningIP='{_ip}' limit 1".format(_table=database_table,_ip=local_ip)
    sql = "SELECT id FROM {_table} where status=1 and svIP='{_ip}' limit 1".format(_table=database_table, _ip=local_ip)
    loginfo.log_info(sql)
    cursor.execute(sql)
    data = cursor.fetchone()
    if data is not None:
        return data[0]
    return -1


def get_cancel_id(cursor, loginfo):
    # sql = "SELECT id FROM {_table} where status=6 and runningIP='{_ip}' limit 1".format(_table=database_table,_ip=local_ip)
    sql = "SELECT id FROM {_table} where status=6 and svIP='{_ip}' limit 1".format(_table=database_table, _ip=local_ip)
    loginfo.log_info(sql)
    cursor.execute(sql)
    data = cursor.fetchone()
    if data is not None:
        return data[0]
    return -1


def main():
    log_fd = open('log/log', 'a')
    loginfo = logUtils.logutil(0)
    task_list = {}
    while True:
        db = pymysql.connect(database_host, database_user, database_pass, database_data)
        cursor = db.cursor()
        time.sleep(2)
        running_id = get_running_id(cursor, loginfo);
        if (running_id != -1):
            continue
        for (k, v) in list(task_list.items()):
            if (v.poll() != None):
                del task_list[k]
        mission_id = get_my_id(cursor, loginfo)
        loginfo.log_info('mission_id' + str(mission_id))
        if mission_id is not -1:
            loginfo.log_info("task start")
            # child = subprocess.Popen(['/usr/local/bin/python2', 'run.py', '%d' % mission_id], shell=False,
            #                          stdout=log_fd, stderr=log_fd, cwd=auto_path)
            child = subprocess.Popen(['/search/odin/daemon/.venv/bin/python', 'run_test.py', '%d' % mission_id], shell=False,
                                     stdout=log_fd, stderr=log_fd, cwd=auto_path)
            task_list[mission_id] = child
        cancel_id = get_cancel_id(cursor, loginfo)
        if cancel_id is -1:
            continue
        if cancel_id in task_list:
            task_list[cancel_id].send_signal(10)
            loginfo.log_info('cancel:' + str(task_list))
        else:
            sql = "UPDATE {_table} set status = 5 WHERE id = {_cancel_id}".format(_table=database_table,
                                                                                  _cancel_id=cancel_id)
            cursor.execute(sql)
            try:
                db.commit()
            except:
                db.rollback()

def sig_handler(sig, frame):
    update_errorlog("[%s] task %d has been canceled\n" % (get_now_time(), mission_id))
    set_status(5)
    sys.exit()


signal.signal(10, sig_handler)
signal.signal(15, sig_handler)


if __name__ == '__main__':
    main()
