import cv2
import os

def capture_images():
    video = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    name = input("Enter your name: ").lower()
    path = f'../../images/{name}'
    image_quantity = 1000

    if os.path.exists(path):
        print("Folder already exists")
        name = input("Enter your name: ").lower()
        path = f'../../images/{name}'

    else:
        print("Creating folder")
        os.makedirs(path)

    count = 0
    while True:
        ret, frame = video.read()
        H, W, _ = frame.shape
        print(frame.shape)
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray_frame, 1.3, 5)

        for (x, y, w, h) in faces:
            count += 1
            img_name = f"{path}/{count}.jpg"
            print("Creating image:", img_name)
            cv2.imwrite(img_name, cv2.resize(frame[y:y+h, x:x+w], (1024, 1024)))

        cv2.imshow('Face', frame)
        cv2.waitKey(15)

        if count == image_quantity:
            break

    video.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    capture_images()
