import pytesseract
import cv2
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# Read the image
image = cv2.imread('./81xeFGugw6L.jpg')
height,width,_ = image.shape
myconfig = r"--psm 11 --oem 3"
# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

boxes = pytesseract.image_to_boxes(image,config = myconfig)
text = pytesseract.image_to_string(image,config= myconfig)
print(text)
for box in boxes.splitlines():
    box = box.split()
    character = box[0]
    x1, y1, x2, y2 = int(box[1]), int(box[2]), int(box[3]), int(box[4])
    # Draw rectangles around the characters
    cv2.rectangle(image, (x1, height - y2), (x2, height - y1), (0, 255, 0), 2)
resize_scale = 0.7  # Scale factor (0.5 means 50% of the original size)
resized_image = cv2.resize(image, (int(width * resize_scale), int(height * resize_scale)))

# Show the resized image
cv2.imshow('img', resized_image)
cv2.waitKey(0)