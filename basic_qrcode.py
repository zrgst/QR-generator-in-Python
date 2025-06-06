# basic_qrcode.py
# Importing nessesary package(s)
import segno

# Generate the QR-code to a variable
qrcode = segno.make_qr("Hello, World!")
# Save the QR-code from variable as an image
qrcode.save("basic_qrcode.png")



