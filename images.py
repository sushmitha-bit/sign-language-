import os
import cv2

DATA_DIR = './data'
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

alphabet_classes = [chr(65 + i) for i in range(26)]
dataset_size = 100

cap = cv2.VideoCapture(0)

for class_label in alphabet_classes:
    class_dir = os.path.join(DATA_DIR, class_label)
    if not os.path.exists(class_dir):
        os.makedirs(class_dir)

    print('Collecting data for class {}'.format(class_label))

    while True:
        ret, frame = cap.read()
        cv2.putText(frame, f'Get ready for {class_label}. Press "Q" to start!', (50, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    counter = 0
    while counter < dataset_size:
        ret, frame = cap.read()
        cv2.putText(frame, f'Capturing {class_label}: {counter}/{dataset_size}', (50, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
        cv2.imshow('frame', frame)
        cv2.imwrite(os.path.join(class_dir, f'{counter}.jpg'), frame)
        counter += 1
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
