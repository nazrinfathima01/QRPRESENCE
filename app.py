import qrcode

# Student database
students = {
    "101": "Alice",
    "102": "Bob",
    "103": "Carol"
}

# Generate QR codes
for sid, name in students.items():
    qr = qrcode.make(sid)  # Create QR code with student ID
    filename = f"{name}_{sid}.png"
    qr.save(filename)
    print(f"QR code saved: {filename}")
