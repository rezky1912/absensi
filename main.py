import csv
import os
import pickle
from datetime import datetime

import cv2
import cvzone
import face_recognition
import firebase_admin
import numpy as np
from firebase_admin import credentials, db, storage

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://absensiwajahjava-default-rtdb.firebaseio.com/",
    'storageBucket': "absensiwajahjava.appspot.com"
})

bucket = storage.bucket()

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

imgBackground = cv2.imread('Resources/background.png')

# Importing the mode images into a list
folderModePath = 'Resources/Modes'
modePathList = os.listdir(folderModePath)
imgModeList = []
for path in modePathList:
    imgModeList.append(cv2.imread(os.path.join(folderModePath, path)))
# print(len(imgModeList))

# Load the encoding file
print("Loading Encode File ...")
file = open('EncodFile.p', 'rb')
encodeListKnownWithIds = pickle.load(file)
file.close()
encodeListKnown, karyawanIds = encodeListKnownWithIds
# print(karyawanIds)
print("Encode File Loaded")

modeType = 0
counter = 0
id = -1
imgKaryawan = []
karyawan_hadir = []
is_check_in = True

if not os.path.exists("Hasil_Capture"):
    os.makedirs("Hasil_Capture")
    img_path = os.path.join("Hasil_Capture")

    # checked_in_employees = set()

while True:
    success, img = cap.read()
    checked_in_employees = set()
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    faceCurFrame = face_recognition.face_locations(imgS)
    encodeCurFrame = face_recognition.face_encodings(imgS, faceCurFrame)

    imgBackground[100:100 + 480, 44:44 + 640] = img
    imgBackground[44:44 + 633, 808:808 + 414] = imgModeList[modeType]

    if faceCurFrame:
        for encodeFace, faceLoc in zip(encodeCurFrame, faceCurFrame):
            matches = face_recognition.compare_faces(
                encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(
                encodeListKnown, encodeFace)
            # print("matches", matches)
            # print("faceDis", faceDis)

            matchIndex = np.argmin(faceDis)
            # print("Match Index", matchIndex)

            if matches[matchIndex]:
                # print("Known Face Detected")
                # print(karyawanIds[matchIndex])
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                bbox = 55 + x1, 162 + y1, x2 - x1, y2 - y1
                imgBackground = cvzone.cornerRect(imgBackground, bbox, rt=0)
                id = karyawanIds[matchIndex]
                if counter == 0:
                    cvzone.putTextRect(imgBackground, "Loading", (275, 400))
                    cv2.imshow("Face Attendance", imgBackground)
                    cv2.waitKey(1)
                    counter = 1
                    modeType = 1

        if counter != 0:

            if counter == 1:
                # Get the Data
                karyawanInfo = db.reference(f'Karyawan/{id}').get()
                print(karyawanInfo)
                # Get the Image from the storage
                blob = bucket.get_blob(f'Images/{id}.png')
                array = np.frombuffer(blob.download_as_string(), np.uint8)
                imgKaryawan = cv2.imdecode(array, cv2.COLOR_BGRA2BGR)
                # Update data of attendance
                datetimeObject = datetime.strptime(karyawanInfo['kapan_terakhir_absen'],
                                                   "%Y-%m-%d %H:%M:%S")
                secondsElapsed = (
                    datetime.now() - datetimeObject).total_seconds()
                print(secondsElapsed)
                if secondsElapsed > 30:
                    ref = db.reference(f'Karyawan/{id}')
                    karyawanInfo['total_absen'] += 1
                    ref.child('total_absen').set(
                        karyawanInfo['total_absen'])
                    ref.child('kapan_terakhir_absen').set(
                        datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                else:
                    modeType = 3
                    counter = 0
                    imgBackground[44:44 + 633, 808:808 +
                                  414] = imgModeList[modeType]

            if modeType != 3:

                if 10 < counter < 20:
                    modeType = 2

                imgBackground[44:44 + 633, 808:808 +
                              414] = imgModeList[modeType]

                if counter <= 10:
                    cv2.putText(imgBackground, str(karyawanInfo['total_absen']), (861, 125),
                                cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1)
                    cv2.putText(imgBackground, str(karyawanInfo['divisi']), (1006, 550),
                                cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)
                    cv2.putText(imgBackground, str(id), (1006, 493),
                                cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)
                    cv2.putText(imgBackground, str(karyawanInfo['total_absen']), (910, 625),
                                cv2.FONT_HERSHEY_COMPLEX, 0.6, (100, 100, 100), 1)
                    cv2.putText(imgBackground, str(karyawanInfo['tahun']), (1025, 625),
                                cv2.FONT_HERSHEY_COMPLEX, 0.6, (100, 100, 100), 1)
                    cv2.putText(imgBackground, str(karyawanInfo['Tahun_Masuk']), (1125, 625),
                                cv2.FONT_HERSHEY_COMPLEX, 0.6, (100, 100, 100), 1)

                    (w, h), _ = cv2.getTextSize(
                        karyawanInfo['name'], cv2.FONT_HERSHEY_COMPLEX, 1, 1)
                    offset = (414 - w) // 2
                    cv2.putText(imgBackground, str(karyawanInfo['name']), (808 + offset, 445),
                                cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 50), 1)

                    imgBackground[175:175 + 216, 909:909 + 223] = imgKaryawan
                counter += 1
                if counter == 5:
                    img_name = f"{karyawanInfo['name']}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
                    img_path = os.path.join("Hasil_Capture", img_name)
                    cv2.imwrite(img_path, img)
                current_time = datetime.now().time()
                if datetime.now().weekday() < 6:
                    if current_time >= datetime.strptime("08:00:00", "%H:%M:%S").time() and current_time <= datetime.strptime("20:00:00", "%H:%M:%S").time():
                        is_check_in = not is_check_in
                        if is_check_in and id not in checked_in_employees:
                            checked_in_employees.add(id)
                            csv_path = os.path.join(os.getcwd(), 'checkin.csv')
                            try:
                                with open(csv_path, 'a', newline='') as csvfile:
                                    csv_writer = csv.writer(csvfile)
                                    csv_writer.writerow((karyawanInfo['name'], datetime.now().strftime(
                                        "%Y-%m-%d %H:%M:%S"), "Check-In"))
                            except Exception as e:
                                print("Error writing to CSV:", e)
                            finally:
                                csvfile.close()
                else:
                    csv_path = os.path.join(os.getcwd(), 'checkin.csv')
                    try:
                        with open(csv_path, 'a', newline='') as csvfile:
                            csv_writer = csv.writer(csvfile)
                            csv_writer.writerow((karyawanInfo['name'], datetime.now().strftime(
                                "%Y-%m-%d %H:%M:%S"), "Check-Out"))
                            csvfile.flush()
                    except Exception as e:
                        print("Error writing to CSV:", e)
                        import traceback
                        traceback.print_exc()
                if counter >= 20:
                    counter = 0
                    modeType = 0
                    karyawanInfo = []
                    imgKaryawan = []
                    checked_in_employees.clear()
                    imgBackground[44:44 + 633, 808:808 +
                                  414] = imgModeList[modeType]

    else:
        modeType = 0
        counter = 0

    # cv2.imshow("Webcam", img)
    cv2.imshow("Face Attendance", imgBackground)
    cv2.waitKey(1)
