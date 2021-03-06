#! /usr/bin/env python
#coding=utf-8

database_host="10.141.21.129"
database_data="evalplatform"
database_table="picEval_imagetaskinfo"
database_image="picEval_imagetaskinfo"
database_result = "picEval_resultinfo"
database_user="root"
database_pass="noSafeNoWork@2019"
local_ip='10.141.177.27'

# 远端启动
ip = "10.141.177.27"
user = "root"
pwd = "gpufirst@123"

# 图片路径
rootpath = r'/search/odin/daemon/evalpaltform/demo_pro'
origin_secpath = r'/static/origin/'
dest_secpath = r'/static/dest/'

auto_path = "/search/odin/daemon/evalpaltform/picEval"

#    path, start_script, port

MOD_BASE=[('/search/odin/test/offline/tf_ocr_daemon','restart_tf_ocr_daemon.sh',4101),
	 ('/search/odin/test/offline/tf_model_server','restart_tf_model_server.sh',4000),
	 ('/search/odin/test/offline/tf_detect','restart_tf_detect_daemon.sh',14002),
	 ('/search/odin/test/offline/ocr_hub','restart_ocr_hub.sh',4201),
	 ('/search/odin/test/offline/ocr_translate/ocr_trans_latest','restart_detect_trans.sh',7400),
	 ('/search/odin/test/offline/ocr_translate/tagent','restart.sh',4019),
	 ('/search/odin/test/offline/ocr_translate/img_trans','restart_img_trans.sh',4118),
	 ('/search/odin/test/offline/ocr_translate/http_gateway','restart.sh',3111),
	 ('/search/odin/test/offline/http_basic','restart.sh',30000)
	]

#bias=2013
MOD_TEST=[('/search/odin/test/offline_t/tf_ocr_daemon','restart_tf_ocr_daemon.sh',6114),
	 ('/search/odin/test/offline_t/tf_model_server','restart_tf_model_server.sh',6013),
	 ('/search/odin/test/offline_t/tf_detect','restart_tf_detect_daemon.sh',16015),
	 ('/search/odin/test/offline_t/ocr_hub','restart_ocr_hub.sh',6214),
	 ('/search/odin/test/offline_t/ocr_translate/ocr_trans_latest','restart_detect_trans.sh',9413),
	 ('/search/odin/test/offline_t/ocr_translate/tagent','restart.sh',6032),
	 ('/search/odin/test/offline_t/ocr_translate/img_trans','restart_img_trans.sh',6131),
	 ('/search/odin/test/offline_t/ocr_translate/http_gateway','restart.sh',5124),
	 ('/search/odin/test/offline_t/http_basic','restart.sh',32013)
	]
#(file, [(section,option,value),(s1,o1,v1)...])
CONF_BASE=[
("/search/odin/test/offline/tf_ocr_daemon/conf/ocr.cfg",[('OCR\Network','"ListenAddress"','":4101"'),('OCR\GPU','DeviceCount','#2'),('OCR\GPU','GPU01','#6'),('OCR\GPU','GPU02','#6'),('OCR\Task','RecogTask_ThreadCount','#2')]),
("/search/odin/test/offline/tf_detect/conf/ocr.cfg",[('Detect\Network','"ListenAddress"','":14002"'),('Detect\TfsConfig','"TfsAddress"','"127.0.0.1:4000"')]),
("/search/odin/test/offline/ocr_hub/conf/ocr_hub.cfg",[('OCRhub\Network','"ListenAddress"','":4201"'),('OCRhub\Detect\servers','"server00"','"127.0.0.1:14002"'),\
																									  ('OCRhub\Detect\servers','"server01"','"127.0.0.1:14002"'),\
																									  ('OCRhub\Detect\servers','"server02"','"127.0.0.1:14002"'),\
																									  ('OCRhub\Detect\servers','"server03"','"127.0.0.1:14002"'),\
																									  ('OCRhub\Recog\servers','"server00"','"127.0.0.1:4101"'),\
																									  ('OCRhub\Recog\servers','"server01"','"127.0.0.1:4101"'),\
																									  ('OCRhub\Recog\servers','"server02"','"127.0.0.1:4101"')]),
("/search/odin/test/offline/ocr_translate/ocr_trans_latest/conf/detect_tornado.cfg",[('base','tornado_port','7400'),('base','EN_hub_port','4201'),\
																					 								('base','CH_hub_port','4201'),\
																					 								('base','JP_hub_port','4201'),\
																					 								('base','KR_hub_port','4201'),\
																					 								('base','RU_hub_port','4201'),\
																					 								('base','FR_hub_port','4201'),\
																					 								('base','SP_hub_port','4201'),\
																					 								('base','DE_hub_port','4201'),\
																													('base','PT_hub_port','4201'),\
																													('base','IT_hub_port','4201')]),
("/search/odin/test/offline/ocr_translate/tagent/conf/config.cfg",[('main','port',':4019')]),
("/search/odin/test/offline/ocr_translate/img_trans/conf/img_trans.cfg",[('ImgTrans\Network','"ListenAddress"','":4118"'),('ImgTrans\Trans\\api','"tagent_api"','"http://127.0.0.1:4019/v1/fanyi_batch.json"')]),
("/search/odin/test/offline/ocr_translate/http_gateway/conf/config.cfg",[('main','port',':3111'),('ocr_service','ocrapi','http://127.0.0.1:7400/v6/ocr/json'),('trans_service','trans_server','127.0.0.1:4118')]),
("/search/odin/test/offline/http_basic/conf/basic_config.cfg",[('main','port',':30000'),('ocr_service','ocrapi','http://127.0.0.1:7400/v6/ocr/json')])
]

CONF_TEST=[
("/search/odin/test/offline_t/tf_ocr_daemon/conf/ocr.cfg",[('OCR\Network','"ListenAddress"','":6114"'),('OCR\GPU','DeviceCount','#2'),('OCR\GPU','GPU01','#6'),('OCR\GPU','GPU02','#6'),('OCR\Task','RecogTask_ThreadCount','#2')]),
("/search/odin/test/offline_t/tf_detect/conf/ocr.cfg",[('Detect\Network','"ListenAddress"','":16015"'),('Detect\TfsConfig','"TfsAddress"','"127.0.0.1:6013"')]),
("/search/odin/test/offline_t/ocr_hub/conf/ocr_hub.cfg",[('OCRhub\Network','"ListenAddress"','":6214"'),('OCRhub\Detect\servers','"server00"','"127.0.0.1:16015"'),\
																									  ('OCRhub\Detect\servers','"server01"','"127.0.0.1:16015"'),\
																									  ('OCRhub\Detect\servers','"server02"','"127.0.0.1:16015"'),\
																									  ('OCRhub\Detect\servers','"server03"','"127.0.0.1:16015"'),\
																									  ('OCRhub\Recog\servers','"server00"','"127.0.0.1:6114"'),\
																									  ('OCRhub\Recog\servers','"server01"','"127.0.0.1:6114"'),\
																									  ('OCRhub\Recog\servers','"server02"','"127.0.0.1:6114"')]),
("/search/odin/test/offline_t/ocr_translate/ocr_trans_latest/conf/detect_tornado.cfg",[('base','tornado_port','9413'),('base','EN_hub_port','6214'),\
																					 								  ('base','CH_hub_port','6214'),\
																					 								  ('base','JP_hub_port','6214'),\
																					 								  ('base','KR_hub_port','6214'),\
																					 								  ('base','RU_hub_port','6214'),\
																					 								  ('base','FR_hub_port','6214'),\
																					 								  ('base','SP_hub_port','6214'),\
																					 								  ('base','DE_hub_port','6214'),\
																													  ('base','PT_hub_port','6214'),\
																													  ('base','IT_hub_port','6214')]),
("/search/odin/test/offline_t/ocr_translate/tagent/conf/config.cfg",[('main','port',':6032')]),
("/search/odin/test/offline_t/ocr_translate/img_trans/conf/img_trans.cfg",[('ImgTrans\Network','"ListenAddress"','":6131"'),('ImgTrans\Trans\\api','"tagent_api"','"http://127.0.0.1:6032/v1/fanyi_batch.json"')]),
("/search/odin/test/offline_t/ocr_translate/http_gateway/conf/config.cfg",[('main','port',':5124'),('ocr_service','ocrapi','http://127.0.0.1:9413/v6/ocr/json'),('trans_service','trans_server','127.0.0.1:6131')]),
("/search/odin/test/offline_t/http_basic/conf/basic_config.cfg",[('main','port',':32013'),('ocr_service','ocrapi','http://127.0.0.1:9413/v6/ocr/json')])
]
lang_conf_b={
        'en':'/search/odin/test/offline/langs/en/conf',
    'zh-CHS':'/search/odin/test/offline/langs/ch/conf',
    'de':'/search/odin/test/offline/langs/de/conf',
    'fr':'/search/odin/test/offline/langs/fr/conf',
    'it':'/search/odin/test/offline/langs/it/conf',
    'ja':'/search/odin/test/offline/langs/ja/conf',
    'kr':'/search/odin/test/offline/langs/kr/conf',
    'pt':'/search/odin/test/offline/langs/pt/conf',
    'ru':'/search/odin/test/offline/langs/ru/conf',
    'sp':'/search/odin/test/offline/langs/sp/conf',
	}
lang_data_b={
        'en':'/search/odin/test/offline/langs/en/data',
    'zh-CHS':'/search/odin/test/offline/langs/ch/data',
    'de':'/search/odin/test/offline/langs/de/data',
    'fr':'/search/odin/test/offline/langs/fr/data',
    'it':'/search/odin/test/offline/langs/it/data',
    'ja':'/search/odin/test/offline/langs/ja/data',
    'kr':'/search/odin/test/offline/langs/kr/data',
    'pt':'/search/odin/test/offline/langs/pt/data',
    'ru':'/search/odin/test/offline/langs/ru/data',
    'sp':'/search/odin/test/offline/langs/sp/data',
	}
lang_conf_t={
    'en':'/search/odin/test/offline_t/langs/en/conf',
    'zh-CHS':'/search/odin/test/offline_t/langs/ch/conf',
    'de':'/search/odin/test/offline_t/langs/de/conf',
    'fr':'/search/odin/test/offline_t/langs/fr/conf',
    'it':'/search/odin/test/offline_t/langs/it/conf',
    'ja':'/search/odin/test/offline_t/langs/ja/conf',
    'kr':'/search/odin/test/offline_t/langs/kr/conf',
    'pt':'/search/odin/test/offline_t/langs/pt/conf',
    'ru':'/search/odin/test/offline_t/langs/ru/conf',
    'sp':'/search/odin/test/offline_t/langs/sp/conf',
	}
lang_data_t={
    'en':'/search/odin/test/offline_t/langs/en/data',
    'zh-CHS':'/search/odin/test/offline_t/langs/ch/data',
    'de':'/search/odin/test/offline_t/langs/de/data',
    'fr':'/search/odin/test/offline_t/langs/fr/data',
    'it':'/search/odin/test/offline_t/langs/it/data',
    'ja':'/search/odin/test/offline_t/langs/ja/data',
    'kr':'/search/odin/test/offline_t/langs/kr/data',
    'pt':'/search/odin/test/offline_t/langs/pt/data',
    'ru':'/search/odin/test/offline_t/langs/ru/data',
    'sp':'/search/odin/test/offline_t/langs/sp/data',
	}
