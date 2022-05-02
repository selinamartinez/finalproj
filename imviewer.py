from PIL import Image

# does not close window after opening
# creates new window every time
def preview():
	with Image.open('image.jpg') as img:
		img.show()