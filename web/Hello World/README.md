# Hello World

## Description

[题目链接](http://106.75.72.168:9999/)

无任何提示

## Solution

打开链接，只能看到 Hello World，没有其他的任何信息。打开开发者工具，可以看到有一个资源加载失败，http://106.75.72.168:9999/flag.xmas.js，我们可以尝试访问 http://106.75.72.168:9999/flag.js，发现资源可以打开，是一大段 JS 代码，格式需要处理一下。使用 [js beautifier](http://jsbeautifier.org/)对 js 进行格式化，可以得到结果：

```javascript
var Key = "7a57a5a743894a0e";
CryptoJS.pad.Iso10126 = {
    pad: function(data, blockSize) {
        var blockSizeBytes = blockSize * 4;
        var nPaddingBytes = blockSizeBytes - data.sigBytes % blockSizeBytes;
        data.concat(CryptoJS.lib.WordArray.random(nPaddingBytes - 1)).concat(CryptoJS.lib.WordArray.create([nPaddingBytes << 24], 1))
    },
    unpad: function(data) {
        var nPaddingBytes = data.words[(data.sigBytes - 1) >>> 2] & 0xff;
        data.sigBytes -= nPaddingBytes
    }
};
var aesEncrypt = function(data, keyStr, ivStr) {
    var sendData = CryptoJS.enc.Utf8.parse(data);
    var key = CryptoJS.enc.Utf8.parse(keyStr);
    var iv = CryptoJS.enc.Utf8.parse(ivStr);
    var encrypted = CryptoJS.AES.encrypt(sendData, key, {iv: iv,mode: CryptoJS.mode.CBC,padding: CryptoJS.pad.Iso10126});
    return CryptoJS.enc.Base64.stringify(encrypted.ciphertext)
};
var aesDecrypt = function(data, keyStr, ivStr) {
    var key = CryptoJS.enc.Utf8.parse(keyStr);
    var iv = CryptoJS.enc.Utf8.parse(ivStr);
    var decrypted = CryptoJS.AES.decrypt(data, key, {
        iv: iv,
        mode: CryptoJS.mode.CBC,
        padding: CryptoJS.pad.Iso10126
    });
    return decrypted.toString(CryptoJS.enc.Utf8)
};
var hint = "SSNRTPIuHLUxqtJmq8mDDPtexRU7RTjNO34tLqz+Tpw="
```

aesDecrypt(hint, Key, Key), 结果是 flag in flag.js。
