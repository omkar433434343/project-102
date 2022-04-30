import cv2
import dropbox
import time
import random

start_time = time.time()

def take_snapshot():
    number = random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
       ret,frame = videoCaptureObject.read()
       img_name = "img"+str(number)+".png"
       cv2.imwrite(img_name, frame)
       start_time = time.time
       result = False
    return img_name
    print("snapshot taken")
    videoCaptureObject.release()
  cv2.destroyAllWindows()
def upload_file(img_name):
    access_token ='sl.BGQJ6xCaU40tB-8mluJuMgSdzXZg--N9Bt8Bf4tKRXQdGucE7MA_7IBjQFqIYFHrKql1qNEp0OJGK5eArpYebZnBoDNPVSOBDi7wDaLCQ6AD1Bmny9SQ3-SHd1uql8OUViMGmnOizdNm'
    file =img_name
    file_from = file
    file_to="/testFolder/"+(img_name)
    dbx = dropbox.Dropbox(access_token)

    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to,mode=dropbox.files.WriteMode.overwrite)
        print("file uploaded")


def main():
    while(True):
        if ((time.time() - start_time) >= 5):
            name = take_snapshot()
            upload_file(name)

main()

print("made by om")
