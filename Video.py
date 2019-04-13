import cv2  # cv2 library
video = cv2.VideoCapture(0)
a = 1  # Count the number of frames
while True:
    a = a + 1
    check, frame = video.read()  # read individual frame from video
    print(frame)
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convert the BGR image into Grayscale.Haarcascade works on grayscale
    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    # gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(img, 1.05, 5)
    for x, y, w, h in faces:
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)  # Display a rectangle around face
    cv2.imshow("Each Frame", img)  # Print each frame
    key = cv2.waitKey(1)
    if key == ord('q'):  # Exit condition when q is pressed
        break

print(type(faces))
# print(faces)

print(a)

# time.sleep(3)
# video.release()
# cv2.imshow("First Image", frame)
# cv2.waitKey(0)
cv2.destroyAllWindows()
