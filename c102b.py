import cv2
import dropbox
import time 
import random
starttime=time.time()
def takesnapshot():
    number=random.randint(0,100)
    cap=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=cap.read()
        imagename='img'+str(number)+'.png'
        cv2.imwrite(imagename,frame)
        starttime=time.time
        result=False
    return imagename
    print('snapshottaken')

    videocaptureobject.release()
    cv2.destroyAllWindows()

def uploadfile(imagename):
    acesstoken='MDJ8kwptxLcAAAAAAAAAAXPPTghFBj8OHsBTH6hkV6LEOLXQN0sfO1zNdOmHqQZQ    '
    file=imagename
    filefrom=file
    fileto='/newfolder/'+imagename
    dbx=dropbox.Dropbox(acesstoken)

    with open(filefrom,'rb')as f :
        dbx.files_upload(f.read(),fileto,mode=dropbox.files.WriteMode.overwrite)
        print('fileuploaded')
def main():
    while(True):
        if((time.time()-starttime)>=300):
            name=takesnapshot()
            uploadfile(name)
main()

