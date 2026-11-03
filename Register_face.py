import cv2
import os

person_name = "Princy"

save_path = os.path.join("faces", person_name)

os.makedirs(save_path, exist_ok=True)

camera = cv2.VideoCapture(0)

count = 0

print("Press SPACE to capture image")
print("Press ESC to exit")

while True:

    ret, frame = camera.read()

    if not ret:
        break

    cv2.putText(
        frame,
        f"Images : {count}/20",
        (20,40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0,255,0),
        2
    )

    cv2.imshow("Register Face", frame)

    key = cv2.waitKey(1)

    if key == 32:

        count += 1

        filename = os.path.join(
            save_path,
            f"{count}.jpg"
        )

        cv2.imwrite(filename, frame)

        print("Saved :", filename)

    elif key == 27:
        break

    if count == 20:
        break

camera.release()

cv2.destroyAllWindows()

print("Registration Completed")