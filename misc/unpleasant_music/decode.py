import wave as we
import numpy as np
 
wavfile =  we.open(u'music.wav',"rb")
params = wavfile.getparams()
framesra,frameswav= params[2],params[3]
datawav = wavfile.readframes(frameswav)
wavfile.close()
datause = np.fromstring(datawav,dtype = np.short)
 
result_bin=''
result_hex=''
max=0
for i in range(len(datause)-1):
    if datause[i]> max:
        max=datause[i]
    try:
        if(datause[i]<0 and datause[i+1]>=0):
            if (max-24000 >0):
                result_bin+='1'
                max=datause[i+1]
            else:
                result_bin+='0'
                max=datause[i+1]
    except:
        break
 
print result_bin    
for i in range(0,len(result_bin),4):
    result_hex+=hex(int(result_bin[i:i+4],2))[2:]
 
print result_hex
 
file_rar = open("test.rar","wb")
file_rar.write(result_hex.decode('hex'))  
file_rar.close()    
