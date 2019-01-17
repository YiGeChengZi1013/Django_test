"""
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