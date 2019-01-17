"""
创建项目：
    conda activate xxxxx
    pip install django==1.8
    django-admin startproject xxxxxx
    启动1：
        python manage.py  runserver
    启动2：
        pycharm 启动，setting 中配置python 解释器，manage 配置参数：runserver
路由系统: urls
    创建app：
        app：负责一个具体业务或者一类具体业务的模块
        python manage.py  startapp  xxxx

    路由：
        按照具体的请求url，导入到相应的-业务处理模块的一个功能。
        django的信息控制中枢
        本质上是接受的url和相应的处理模块的一个映射。
        在接受url请求的匹配上使用了RE
        url的具体格式如urls。py中所示


"""