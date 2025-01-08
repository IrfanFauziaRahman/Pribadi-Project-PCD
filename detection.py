from ultralytics import YOLO
import cv2
import matplotlib.pyplot as plt

def detect_faces_yolov8(image_path, model_path="model.pt"):

    model = YOLO(model_path)


    image = cv2.imread(image_path)


    results = model(image)

 
    for result in results[0].boxes.xyxy:  
        x1, y1, x2, y2 = map(int, result)
        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 5)

    return image

image_path = "dataset/IMG_2186.JPG"  


result_image = detect_faces_yolov8(image_path)


plt.imshow(cv2.cvtColor(result_image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.show()
