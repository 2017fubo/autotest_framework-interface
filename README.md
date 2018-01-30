# auto_test_framework-interface-web-
一个轻量级的自动化测试框架，接口，web无缝对接或者单独使用

myapp.log    //执行日志
Run_testcase.py  //主程序

├─config//配置相关
        configdb.py
        configdb_ssh.py
        configrunmode.py
││  configtestobject.py
││  database_config.ini
││  database_config_ssh.ini
││  globalconfig.py
││  runmode_config.ini
│  │  testobject_config.ini
│  │  __init__.py
│  │  
│          
├─Log   //日志方法配置
│  │  log_config.py
│  │  __init__.py
│  │  
│          
├─PublicTools  //公用方法
│  │  confighttp.py
│  │  Connect_db.py
│  │  Connect_db_ssh.py
│  │  Module_import.py
│  │  Runcase.py
│  │  TestobjectReadWriter.py
│  │  __init__.py
│  │  
│          
├─Sharelibs   //webui测试时 共享测试库（关键字封装）
│  │  exitlogin.py
│  │  __init__.py
│  │  
│          
├─Testcase//测试
│  │  __init__.py
│  │  
│  ├─Api2_0_Testcase   //接口测试case
│  │  │  HttpRequest_method.py
│  │  │  test_interface_api20_intl.py
│  │  │  test_interface_api20_out.py
│  │  │  __init__.py
│  │  │  
│  │  ├─Api2_0_Testcase_Res
│  │  │  │  Request_baseinfo.py
│  │  │  │  Request_paraminfo.py
│  │  │  │  Request_urlinfo.py
│  │  │  │  __init__.py
│  │  │  │  
│          
└─TestResult//结果报告
    │  TestResult_20180127-18H16Mresult.html
    │  
    ├─Error
    └─screenshopt
