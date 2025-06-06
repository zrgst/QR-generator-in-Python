# rotated_qrcode.py
import segno

qrcode = segno.make_qr("Hello, World!")

qrcode_rotated = qrcode.to_pil().rotate(45, expand=True)
qrcode_rotated.save("rotated2_qrcode.png")
