# gold

## Description

还在上小学的小明同学开发了一款游戏，你能通关吗？

![](https://xzfile.aliyuncs.com/media/upload/picture/20180828002227-635f3298-aa15-1.gif)

## Solution

打开开发者后台可以看到，在不停地进行 post 请求，参数为 getGold。尝试用 burp 来进行爆破，从 1 开始，到 1001，步长为2.这里有几个注意点，客户端只能有一个 session，就是你是用burp爆破的时候浏览器要关掉否则会触发后台检测，另外爆破要从0开始，不能从其他的数字开始。姿势一定要准。