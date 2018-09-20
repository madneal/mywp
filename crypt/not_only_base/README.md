# Not Only base

## Description

Not only base

## Solution`

文件的内容是 `MCJIJSGKP=ZZYXZXRMU=W3YZG3ZZ==G3HQHCUS==`

根据题目提示，可以看出来这个题目是和 base 算法有关系的，但是如果直接使用 base64 或者 base32 是无法解密的。可以看出这是栅栏密码，然后再使用 base32 来进行解密。

这个[栅栏解密](https://www.qqxiuzi.cn/bianma/zhalanmima.php)找了一圈发现时最好用的，每组字数为4，解密结果为：`MZWGCZ33JYYHIXZQJZGHSX3CGRZUKMZSPU======`。这个结果看起来比较像 base32，可以使用 base32 进行解密，得到结果：`flag{N0t_0NLy_b4sE32}`

