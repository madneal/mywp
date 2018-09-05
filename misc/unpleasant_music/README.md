# Unpleasant music

## Description

无任何提示

## Solution

题目给了一个压缩文件，里面是一个 wav 文件。打开播放也听不出什么特别的，使用 Audacity 打开 wav 文件分析的时候，可以看到波形的形状。如果高峰为1，低谷为0，可以将波形转化为 01 数据。如果将前面几位转化一下，可以看到是 Rar。那么如何将波形转化为 01 数据呢，如果手工转的话，还不知道要到何年何月，而且还容易出错。比赛的时候也在写脚本，但是只有前面几位是正确的，到后面就不对了。后来发现一位大佬写的[代码](http://since1994.cn/?p=198)，才发现当时进入了一个死胡同，波形并没有固定的宽度。

通过脚本可以将 wav 文件转化为 rar 文件，打开 rar 文件可以看到里面有一个 nnnnoflag.txt，里面也是没有 flag 的。使用 010 editor 打开 rar 文件，

[![ipNXAf.png](https://s1.ax1x.com/2018/09/05/ipNXAf.png)](https://imgchr.com/i/ipNXAf)