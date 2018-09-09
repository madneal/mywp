# Do you know upload？

## Description

加油吧，少年。(说了等于没说)

## Solution

这是一道上传绕过的题目，其实没有什么特别的地方。这里就是想介绍一下自己使用的一个特别好的工具，就是 [weevely](https://github.com/epinna/weevely3)。这个工具是 kali 中类似于中国菜刀的工具，功能强大。这里主要介绍一下简单的使用以及我是用的时候一个小小的坑。

打开网站，可以看到是一个图片上传的页面：

![ii2PyR.png](https://s1.ax1x.com/2018/09/09/ii2PyR.png)

没有什么特殊的地方，打开开发者工具，可以看到 html 包含了一段注释的代码：

```php
<!-- 
include($_GET['file']); 
-->
```

那么可以断定后台应该使用的是 php 了。那么可以上传一个 php 木马来连接服务器了。上传绕过的经典套路就是先生成一个木马，然后将文件后缀改为图片格式，然后在 burp 中再将文件名改过来。下面就是 weevely 的使用了。

首先在 kali 中搜索这个工具打开，先生成木马：（`weevely generate <password> <path>`）

![iiRF3Q.png](https://s1.ax1x.com/2018/09/09/iiRF3Q.png)

这样我们就在 /root/project 中生成了一个 cmd.php 木马。下面就是如何将这个马上传了。首先将这个文件的后缀名改为 jpg，然后选择图片上传，然后在 burp 中将文件名修改为 cmd.php：

![iiWDiT.png](https://s1.ax1x.com/2018/09/09/iiWDiT.png)

文件上传成功，保存在 upload/ 路径下。下面就可以通过 weevely 拿到后门了。上传之后，首先访问一下文件路径。然后通过命令：`weevely <url-path> <password>` 就可以连接远程机器了：

![iif8Tx.png](https://s1.ax1x.com/2018/09/09/iif8Tx.png)

接着就可以控制机器了，首先可以看到 upload 路径，路径即是上传的文件。可以看到 html 路径下有多个文件，比如 ctf.sql 以及 config.php。ctf.sql 是一个空文件，里面没有任何内容。打开 config.php 可以看到是一段 php 代码：

```php
<?php
error_reporting(0);
session_start();
$servername = "localhost";
$username = "ctf";
$password = "ctfctfctf";
$database = "ctf";

// 创建连接
$conn = mysql_connect($servername,$username,$password) or die(" connect to mysql error");
mysql_select_db($database);
?>
```

可以看到代码主要是一段 mysql 数据库的连接，数据库连接的信息都给出了。下面就是可以使用 sql_console 模块来进行数据库的交互了。通过 `:sql_console -u ctf -p ctfctfctf` 就可以连接数据库了。接下来可以看到数据库的信息以及表格的信息。

[![iihi9O.md.png](https://s1.ax1x.com/2018/09/09/iihi9O.md.png)](https://imgchr.com/i/iihi9O)

可以看到除了 information_schema 数据库，还有一个叫 ctf 的数据库，而且在 ctf 数据库中还有一个叫 flag 的表格。很明显，flag 很有可能就在在这个表格中。但是使用 `select * from flag` 总是提示 `[-][console] No data returned Check credentials and DB availability`。找了很多办法，但始终没办法查出来。后来才知道 weevely 无法保存数据库的状态，所以无法使用 `use datbasename` 这样的语句。其实使用 `select * from ctf.flag` 就可以拿到 flag 了啊。