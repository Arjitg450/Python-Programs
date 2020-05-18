import cv2
import pytesseract
from PIL import Image
import webbrowser
cam = cv2.VideoCapture(0)

cv2.namedWindow("test")

img_counter = 0

while True:
    ret, frame = cam.read()
    cv2.imshow("test", frame)
    if not ret:
        break
    k = cv2.waitKey(1)

    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1

cam.release()

cv2.destroyAllWindows()


value=Image.open("H:\\opencv_frame_0.png")

text = pytesseract.image_to_string(value, config='')
print("text present in images:",text)


webbrowser.open('https://www.google.co.in/search?q=Dictionary#dobs={}'.format(text))
webbrowser.open('https://www.dictionary.com/browse/{}'.format(text))
webbrowser.open('https://dictionary.cambridge.org/dictionary/english/{}'.format(text))

"""https://www.dictionary.com/browse/hi"""

"""https://dictionary.cambridge.org/dictionary/english/no"""

