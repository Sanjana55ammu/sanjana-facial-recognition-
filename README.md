👇

📚 Smart Attendance System using DeepFace & OpenCV

A real-time Face Recognition based Attendance System built in Python using DeepFace, OpenCV, and Excel for automatic attendance marking.

🚀 Features

✔ Detects faces in real-time using webcam
✔ Identifies registered users using DeepFace facial recognition
✔ Automatically marks attendance into an Excel (.xls) file
✔ Saves name, attendance status, and date
✔ Allows on-spot registration of new faces
✔ Supports multiple face recognition models
✔ Simple UI using OpenCV window

🧰 Tech Stack
Component	Technology
Face Detection	OpenCV Haar Cascade
Face Recognition	DeepFace
Data Storage	Excel via xlrd, xlwt, xlutils
Language	Python 3.x
📦 Installation & Setup
🔹 1️⃣ Install Required Libraries
pip install tensorflow
pip install opencv-python
pip install deepface
pip install xlrd
pip install xlwt
pip install xlutils


⚠ NOTE: TensorFlow installation size is large (>1GB)

🔹 2️⃣ Create Directory Structure
project-folder/
│
├── known_faces/        # Automatically created
├── attendance_excel.xls  # Auto-generated on first run
└── main.py              # The code

▶️ How It Works

🔹 When the webcam starts:
• If a face matches a registered person → Attendance marked automatically
• If face is unknown → You will see message to register

🔹 Keys to control:

Key	Action
R	Register new face
Q	Quit system
📝 Attendance Format
Name	Status	Date
Ravi	Present	2025-02-10

Stored in attendance_excel.xls automatically.

🧠 How Registration Works

1️⃣ Press R when unknown face is detected
2️⃣ Enter the person’s name in the terminal
3️⃣ The face image is saved inside:

known_faces/PersonName/PersonName_1.jpg


Next time → face will be recognized 🎯

⚠ Common Issues & Fixes
Issue	Solution
Webcam not detected	Use external camera or correct index: cv2.VideoCapture(1)
Very slow recognition	Reduce database images / use GPU
Model fails to detect face	Better lighting & direct front face
Excel not updating row properly	Ensure file is not open while running
📌 To-Do Enhancements

Add GUI (PyQt / Tkinter)

Improve recognition accuracy with face embedding model

Show confidence score on screen

Switch Excel to CSV / database system for large usage

👨‍💻 Author

Smart Attendance System Project
Made with ❤️ using AI + Python

If you'd like, I can also:

✔ Add CSV export instead of Excel
✔ Improve speed using SVM classifier
✔ Rename and organize code into .py modules
✔ Help you create a project report + PPT for college
