from __future__ import print_function
import ctypes, sys
def is_admin():
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False
if is_admin():
    #输入代码
    Edition=("WL-ZPM-ZOUPEIMIANSHIPINJIEXI----ZPM_Edition:6.0 ; Developer_system:Microsoft-Windows-Windows-10--Professional-workstation-version ; Programming-Support-Language:Python",)
    import time as t
    import easygui as ui
    lis=["****.la","****.com","dm**.****.tv","y***.x**"]
    ui.msgbox("我的(作者)的GitHub账号:https://github.com/SunHaoranP","重要消息")
    s=ui.choicebox('选择源','我的(作者)的GitHub账号:https://github.com/SunHaoranP',lis)
    ui.msgbox(Edition,"版本号-我的(作者)的GitHub账号:https://github.com/SunHaoranP")
    if (s=="****.la"):
        csh='''
        <html>
        // 孙浩然制作
        // 孙浩然作品
            '''
        b=ui.enterbox(msg="请输入视频网站链接网址", title="我的(作者)的GitHub账号:https://github.com/SunHaoranP", default="", strip=True, image=None, root=None)
        tim=t.ctime()
        csh='''
        <!DOCTYPE html>
        <html>
            <head>
                <title>https://github.com/SunHaoranP</title>
            </head>
            <body style="background-color:152,152,152;">'''+'页面生成时间:'+tim+'''
                <b>制作者由GitHub的https://github.com/SunHaoranP制作</b>
                <iframe src="'''+"https://www.8090.la/8090/?url="+b+'"'+'''frameborder="0" allowfullscreen="true" width="100%" height="500%"></iframe>
                <h1>视频链接：'''+b+'''
                <a href="https://www.iqiyi.com/" target="_blank">爱奇艺官网</a>
                <a href="https://v.qq.com/" target="_"blank">腾讯视频官网</a>
                <a href="https://www.youku.com/" target="_"blank">优酷官网</a>
                <a href="https://www.bilibili.com/" target="_blank">bilibili官网</a>
                <a href="https://www.mgtv.com/" target="_blank">芒果TV官网</a>
                <a href="https://tv.sohu.com/" target="_blank">搜狐官网</a>
                <a href="'''+b+'"'+''' target="_blank">当前观看链接--点击跳转</a>
                <p1>保护版权，支持正版！</p1>
            </body>
        </html>
            '''
        with open("shr.html", "wt") as shr:
            shr.write(csh)
        ui.msgbox("成功","https://github.com/SunHaoranP")
        try:
            with open("C:\\SunHaoranP.log", "w") as log:
                log.write('作者的Github账号:github.com/SunHaoranP'+'时间(TIME):'+tim+"视频链接:"+b)
        except FileNotFoundError:
            ui.msgbox("路径'D: ERROR,可能没有路径D:","提示")
            ui.msgbox("如果喜欢的话打赏下我吧！！！","https://github.com/SunHaoranP")
    if (s=="****.com"):
        csh='''
        <html>
        // 孙浩然制作
        // 孙浩然作品
            '''
        b=ui.enterbox(msg="请输入视频网站链接网址", title="我的(作者)的GitHub账号:https://github.com/SunHaoranP", default="", strip=True, image=None, root=None)
        tim=t.ctime()
        csh='''
        <!DOCTYPE html>
        <html>
            <head>
                <title>https://github.com/SunHaoranP</title>
            </head>
            <body style="background-color:152,152,152;">'''+'页面生成时间:'+tim+'''
                <b>https://github.com/SunHaoranP</b>
                <iframe src="'''+"https://www.h8jx.com/jiexi.php?url="+b+'"'+'''frameborder="0" allowfullscreen="true" width="100%" height="500%"></iframe>
                <h1>视频链接：'''+b+'''
                <a href="https://www.iqiyi.com/" target="_blank">爱奇艺官网</a>
                <a href="https://v.qq.com/" target="_"blank">腾讯视频官网</a>
                <a href="https://www.youku.com/" target="_"blank">优酷官网</a>
                <a href="https://www.bilibili.com/" target="_blank">bilibili官网</a>
                <a href="https://www.mgtv.com/" target="_blank">芒果TV官网</a>
                <a href="https://tv.sohu.com/" target="_blank">搜狐官网</a>
                <a href="'''+b+'"'+''' target="_blank">当前观看链接--点击跳转</a>
                <p1>保护版权，支持正版！</p1>
            </body>
        </html>
            '''
        with open("shr.html", "wt") as shr:
            shr.write(csh)
        ui.msgbox("成功","https://github.com/SunHaoranP")
        try:
            with open("C:\\SunHaoranP.log", "w") as log:
                log.write('作者的Github账号:github.com/SunHaoranP'+'时间(TIME):'+tim+"视频链接:"+b)
            ui.msgbox("如果喜欢的话打赏下我吧！！！","https://github.com/SunHaoranP")
        except FileNotFoundError:
            ui.msgbox("路径'D: ERROR,可能没有路径D:","https://github.com/SunHaoranP")
    if (s=="dm**.****.tv"):
        csh='''
        <html>
        // 孙浩然制作
        // 孙浩然作品
            '''
        b=ui.enterbox(msg="请输入视频网站链接网址", title="我的(作者)的GitHub账号:https://github.com/SunHaoranP", default="", strip=True, image=None, root=None)
        tim=t.ctime()
        csh='''
        <!DOCTYPE html>
        <html>
            <head>
                <title>本界面由孙浩然制作</title>
            </head>
            <body style="background-color:152,152,152;">'''+'页面生成时间:'+tim+'''
                <b>https://github.com/SunHaoranP</b>
                <iframe src="'''+"https://dmjx.m3u8.tv/?url="+b+'"'+'''frameborder="0" allowfullscreen="true" width="100%" height="500%"></iframe>
                <h1>视频链接：'''+b+'''
                <a href="https://www.iqiyi.com/" target="_blank">爱奇艺官网</a>
                <a href="https://v.qq.com/" target="_"blank">腾讯视频官网</a>
                <a href="https://www.youku.com/" target="_"blank">优酷官网</a>
                <a href="https://www.bilibili.com/" target="_blank">bilibili官网</a>
                <a href="https://www.mgtv.com/" target="_blank">芒果TV官网</a>
                <a href="https://tv.sohu.com/" target="_blank">搜狐官网</a>
                <a href="'''+b+'"'+''' target="_blank">当前观看链接--点击跳转</a>
                <p1>保护版权，支持正版！</p1>
            </body>
        </html>
            '''
        with open("shr.html", "wt") as shr:
            shr.write(csh)
        try:
            with open("C:\\SunHaoranP.log", "w") as log:
                log.write('作者的Github账号:github.com/SunHaoranP'+'时间(TIME):'+tim+"视频链接:"+b)
            ui.msgbox("如果喜欢的话打赏下我吧！！！","https://github.com/SunHaoranP")
        except FileNotFoundError:
            ui.msgbox("路径'D: ERROR,可能没有路径D:","提示")
            ui.msgbox("如果喜欢的话打赏下我吧！！！","https://github.com/SunHaoranP")
    if (s=="y***.x**"):
        csh='''
        <html>
        // 孙浩然制作
        // 孙浩然作品
            '''
        b=ui.enterbox(msg="请输入视频网站链接网址", title="我的(作者)的GitHub账号:https://github.com/SunHaoranP", default="", strip=True, image=None, root=None)
        tim=t.ctime()
        csh='''
        <!DOCTYPE html>
        <html>
            <head>
                <title>https://github.com/SunHaoranP</title>
            </head>
            <body style="background-color:152,152,152;">'''+'页面生成时间:'+tim+'''
                <b>https://github.com/SunHaoranP</b>
                <iframe src="'''+"https://yemu.xyz/?url="+b+'"'+'''frameborder="0" allowfullscreen="true" width="100%" height="500%"></iframe>
                <h1>视频链接：'''+b+'''
                <a href="https://www.iqiyi.com/" target="_blank">爱奇艺官网</a>
                <a href="https://v.qq.com/" target="_"blank">腾讯视频官网</a>
                <a href="https://www.youku.com/" target="_"blank">优酷官网</a>
                <a href="https://www.bilibili.com/" target="_blank">bilibili官网</a>
                <a href="https://www.mgtv.com/" target="_blank">芒果TV官网</a>
                <a href="https://tv.sohu.com/" target="_blank">搜狐官网</a>
                <a href="'''+b+'"'+''' target="_blank">当前观看链接--点击跳转</a>
                <p1>保护版权，支持正版！</p1>
            </body>
        </html>
            '''
        with open("shr.html", "wt") as shr:
            shr.write(csh)
        try:
            with open("C:\\SunHaoranP", "w") as log:
                log.write('作者的Github账号:github.com/SunHaoranP'+'时间(TIME):'+tim+"视频链接:"+b)
            ui.msgbox("如果喜欢的话打赏下我吧！！！","https://github.com/SunHaoranP")
        except FileNotFoundError:
            ui.msgbox("路径'D: ERROR,可能没有路径D:","提示")
            ui.msgbox("如果喜欢的话打赏下我吧！！！","https://github.com/SunHaoranP")
if sys.version_info[0] == 3:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
else:#in python2.x
    ctypes.windll.shell32.ShellExecuteW(None, u"runas", unicode(sys.executable), unicode(__file__), None, 1)
            