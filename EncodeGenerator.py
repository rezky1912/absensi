import os
import pickle

import cv2
import face_recognition
import firebase_admin
from firebase_admin import credentials, db, storage

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://absensiwajahjava-default-rtdb.firebaseio.com/",
    'storageBucket': "absensiwajahjava.appspot.com"
})


# masukan gambar karyawan
folderPath = 'Images'
pathList = os.listdir(folderPath)
print(pathList)
imgList = []
karyawanIds = []
for Path in pathList:
    imgList.append(cv2.imread(os.path.join(folderPath, Path)))
    karyawanIds.append(os.path.splitext(Path)[0])

    fileName = f'{folderPath}/{Path}'
    bucket = storage.bucket()
    blob = bucket.blob(fileName)
    blob.upload_from_filename(fileName)

    #    print(Path)
   # print(os.path.splitext(Path)[0])
    print(karyawanIds)


def findEncodings(imagesList):
    encodeList = []
    for img in imagesList:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)

    return encodeList


print("Encoding Started .... ")
encodeListKnown = findEncodings(imgList)
encodeListKnownWithIds = [encodeListKnown, karyawanIds]
print("Encode Complete .... ")


file = open("EncodFile.p", 'wb')
pickle.dump(encodeListKnownWithIds, file)
file.close()
print("file Save")
