
import os
os.chdir('H:\\websites\\edutrade\\FOR BATCHING')
i=1
for file in os.listdir():
    src=file
    dst=str(i)+".jpg"
    os.rename(src,dst)
    i+=1
    print('C:\\Users\\Akshat\\Desktop\\aftewr'+str(i)+".jpg")



