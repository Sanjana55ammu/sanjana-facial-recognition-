import tensorflow as tf
tf.get_logger().setLevel('ERROR')
import cv2
import os
from deepface import DeepFace
import xlwt
from xlrd import open_workbook
from xlutils.copy import copy as xl_copy
from datetime import date

print("🚀 Starting Smart Attendance System")

known_faces_dir = os.path.join(os.getcwd(), "known_faces")
if not os.path.exists(known_faces_dir):
    os.makedirs(known_faces_dir)

excel_file = "attendance_excel.xls"
if not os.path.exists(excel_file):
    wb = xlwt.Workbook()
    ws = wb.add_sheet("Attendance")
    ws.write(0, 0, "Name")
    ws.write(0, 1, "Status")
    ws.write(0, 2, "Date")
    wb.save(excel_file)
    print("📘 Created new Excel file:", excel_file)

try:
    rb = open_workbook(excel_file, formatting_info=True)
    wb = xl_copy(rb)
    sheet = wb.get_sheet(0)  
except:
    wb = xlwt.Workbook()
    sheet = wb.add_sheet("Attendance")

row = sheet.last_used_row + 1 if hasattr(sheet, 'last_used_row') else 1
marked_names = set()

cam = cv2.VideoCapture(0)
if not cam.isOpened():
    raise Exception("❌ Could not access webcam")

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

print("\n📸 Camera started... Press 'q' to quit, 'r' to register new face.\n")

while True:
    ret, frame = cam.read()
    if not ret:
        print("❌ Frame not captured.")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        face_crop = frame[y:y+h, x:x+w]
        name = "Unknown"

        try:
            result = DeepFace.find(img_path=face_crop, db_path=known_faces_dir,
                                   enforce_detection=False, silent=True)
            if len(result) > 0 and len(result[0]) > 0:
                match_path = result[0].iloc[0]['identity']
                name = os.path.basename(os.path.dirname(match_path))
        except Exception:
            name = "Unknown"

        color = (0, 255, 0) if name != "Unknown" else (0, 0, 255)
        cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
        cv2.putText(frame, name if name != "Unknown" else "Unknown Face",
                    (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

        if name != "Unknown" and name not in marked_names:
            sheet.write(row, 0, name)
            sheet.write(row, 1, "Present")
            sheet.write(row, 2, str(date.today()))
            wb.save(excel_file)
            row += 1
            marked_names.add(name)
            print(f"✅ Attendance marked for {name}")

        elif name == "Unknown":
            cv2.putText(frame, "Press 'R' to register this person", (50, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    cv2.imshow("Smart Attendance System", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('r'):
        print("🆕 New face detected. Registering...")
        person_name = input("Enter name for new person: ").strip()
        if person_name:
            save_dir = os.path.join(known_faces_dir, person_name)
            os.makedirs(save_dir, exist_ok=True)
            img_path = os.path.join(save_dir, f"{person_name}_1.jpg")
            cv2.imwrite(img_path, face_crop)
            print(f"✅ {person_name} registered successfully.")
        else:
            print("❌ Name cannot be empty.")

    elif key == ord('q'):
        print("🛑 Exiting and saving attendance...")
        wb.save(excel_file)
        break

cam.release()
cv2.destroyAllWindows()
wb.save(excel_file)
print("✅ Attendance saved successfully.")