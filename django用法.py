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
    需要关注的两点：
        1，接受的URL是什么，即如何使用RE对传入  URL进行匹配
        2，已知 URL匹配到哪个处理模块

        url匹配规则;
            从上往下一个一个比对
            url格式是分级式，则按照级别一级一级往下比对，主要对应url包含子url的情况
            子url一旦被调用，则不会返回到主url
                '/one/two/three/'
            正则亦r开头，表示不需要转义，注意尖号^ 和美元符号$
                '/one/two/three/' 配对 r'^one/
                '/oo/one/two/three/'  不配对    r'^one/"
                '/one/two/three/'      配对   r'three/$
                '/oo/one/two/three/oo/'      不配对   r'three/$
                开头不需要反斜杠
            如果从上向下都没有找到合适的额匹配内容，则报错

        2.正常映射：
            把某一个符合RE的url映射到事务处理函数中去
            举例：
                from showeast import views as sv

                urlpatterns = [
                    url(r'^$', 'django_test.views.home', name='home'),
                    url(r'^blog/', include('blog.urls')),
                    url(r'^admin/', include(admin.site.urls)),
                    ]

        3.url中带参数映射
            在事务处理代码中需要有url传入参数，形如：/myurl/param中的param
            参数都是字符串形式，如果需要整数等形式需要自行转换格式。


"""

