# borderless_qrcode.py
# Importing nessesary package(s)
import segno

# Generate the QR-code to a variable
qrcode = segno.make_qr("Hello, World!")
# Save the QR-code from variable as an image with scalin at 5
# and no border
qrcode.save(
	"borderless_qrcode.png",
	scale=5,
	border=0
	)