import io
from PIL import Image

im = Image.open('Photos\\books_read.png')
buf = io.BytesIO()
im.save(buf, format='PNG')
byte_im = buf.getvalue()
print(byte_im)
stream = io.BytesIO(byte_im)
image = Image.open(stream).convert("RGBA")
stream.close()
image.show()
