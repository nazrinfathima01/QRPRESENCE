import cv2
from pyzbar.pyzbar import decode
from datetime import datetime

# Student database
students = {
    "101": "Alice",
    "102": "Bob",
    "103": "Carol"
}

attendance = {}  # Stores attendance

# Open webcam
cap = cv2.VideoCapture(0)
print("Starting scanner... Press 'q' to stop.")

while True:
    ret, frame = cap.read()
    for code in decode(frame):
        student_id = code.data.decode('utf-8')
        if student_id in students:
            if student_id not in attendance:
                attendance[student_id] = {
                    "name": students[student_id],
                    "time": datetime.now().strftime("%H:%M:%S")
                }
                print(f"Attendance marked: {students[student_id]} (ID: {student_id})")
    cv2.imshow("QR Scanner", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# Final Attendance Report
print("\n--- Attendance Report ---")
for sid, info in attendance.items():
    print(f"{info['name']} (ID: {sid}) - Present at {info['time']}")
