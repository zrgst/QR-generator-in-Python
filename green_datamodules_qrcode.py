# green_datamodules_qrcode.py
# Importing nessesary package(s)
import segno

# Generate the QR-code to a variable
qrcode = segno.make_qr("Hello, World!")
# Save the QR-code from variable as an image with scalin at 5
qrcode.save(
	"green_datamodules_qrcode.png",
	scale=5,
	light="#AAAAAA",
	dark="#FF6E00",
	data_dark="#005782",
	data_light="lightgreen"
	)