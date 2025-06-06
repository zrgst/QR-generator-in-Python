# certego_qrcode.py
# Importing nessesary package(s)
import segno

# Generate the QR-code to a variable
qrcode = segno.make_qr("Hello, World!")
# Save the QR-code from variable as an image with scalin at 5
qrcode.save(
	"certego_qrcode.png",
	scale=5,
	border=10,
	dark="darkorange",
	light="lightgrey",
	quiet_zone="darkblue",
	)