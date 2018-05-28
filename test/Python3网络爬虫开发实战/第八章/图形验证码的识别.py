#识别测试
import tesserocr
from PIL import Image

image = Image.open('code_2.jpg')

image = image.convert('L')
threshold = 170
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)

image = image.point(table, '1')
result = tesserocr.image_to_text(image)
#print(image)
image.show()
print(result)
#print(type(result))

