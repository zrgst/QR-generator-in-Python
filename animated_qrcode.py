# animated_qrcode.py
import segno
from urllib.request import urlopen

slts_qrcode = segno.make_qr("https://www.youtube.com/watch?v=hTWKbfoikeg")
nirvana_url = urlopen("https://media.giphy.com/media/LpwBqCorPvZC0/giphy.gif")
slts_qrcode.to_artistic(
	background=nirvana_url,
	target="animated_qrcode.gif",
	scale=10,
	)