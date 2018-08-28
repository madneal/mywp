# comein

## description

由于运维人员失误，内网认证页面部署至了外网，不过还好，开发加了域名验证。

## [Link](http://117.50.11.83/)

![PLsPSA.png](https://s1.ax1x.com/2018/08/28/PLsPSA.png)

## Solution

题目打开开发者工具，可以看到 html 中有一段注释的 php 代码：

```php
ini_set("display_errors",0);
$uri = $_SERVER['REQUEST_URI'];
if(stripos($uri,".")){
    die("Unkonw URI.");
}
if(!parse_url($uri,PHP_URL_HOST)){
    $uri = "http://".$_SERVER['REMOTE_ADDR'].$_SERVER['REQUEST_URI'];
}
$host = parse_url($uri,PHP_URL_HOST);
if($host === "c7f.zhuque.com"){
    setcookie("AuthFlag","flag{*******");
}
```

首先需要绕过 `stripos` 函数，这个函数是要检测 $uri 是否包含 `.`，可以将符号放在第一位，则结果为 0,则会转换为 false。这里主要是进行一个 parse_url 函数的绕过。使用 burp 将 host 修改为 `.@c7f.zhuque.com/..//` 即可绕过，获得 cookie。