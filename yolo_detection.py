# import required packages
import cv2
import argparse
import numpy as np




# # read input image
# image = cv2.imread('1.jpg')
#
# Width = image.shape[1]
# Height = image.shape[0]
# scale = 0.00392

# read class names from text file
classes = None
with open('yolov3.txt', 'r') as f:
    classes = [line.strip() for line in f.readlines()]

# generate different colors for different classes
COLORS = np.random.uniform(0, 255, size=(len(classes), 3))

modelConfiguration = "yolov3.cfg";
modelWeights = "yolov3.weights";
# read pre-trained model and config file
net = cv2.dnn.readNet(modelConfiguration, modelWeights)
# net = cv2.dnn.readNetFromDarknet(modelConfiguration, modelWeights)





# function to get the output layer names
# in the architecture
def get_output_layers(net):
    layer_names = net.getLayerNames()

    output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]

    return output_layers


# function to draw bounding box on the detected object with class name

def draw_bounding_box(img, class_id, confidence, x, y, x_plus_w, y_plus_h):
    label = str(classes[class_id])
    # if label== 'person':
    #     no_of_person.append('person')
    #
    # print(str(len(no_of_person)))
    color = COLORS[class_id]

    # cv2.rectangle(img, (x, y), (x_plus_w, y_plus_h), color, 2)
    #
    # cv2.putText(img, label, (x - 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    font = cv2.FONT_HERSHEY_SIMPLEX
    bottomLeftCornerOfText = (10, 50)
    fontScale = 1
    fontColor = (200, 255, 155)
    lineType = 2


    cv2.putText(img, 'Person :' + str(len(no_of_person)),
               bottomLeftCornerOfText,
               font,
               fontScale,
               fontColor,
               lineType)





# display output image
video = cv2.VideoCapture(0)
ret = video.set(3, 640)  # set frame width
ret = video.set(4, 480)  # set frame height
ret = video.set(cv2.CAP_PROP_FPS, 1)  # adjusting fps to 5


while (True):

    ret, frame = video.read()
    Width = frame.shape[1]
    Height = frame.shape[0]
    scale = 0.00392

    blob = cv2.dnn.blobFromImage(frame, scale, (416, 416), (0, 0, 0), True, crop=False)
    net.setInput(blob)
    # run inference through the network
    # and gather predictions from output layers
    outs = net.forward(get_output_layers(net))
    # initialization
    class_ids = []
    confidences = []
    boxes = []
    conf_threshold = 0.5
    nms_threshold = 0.4

    # for each detetion from each output layer
    # get the confidence, class id, bounding box params
    # and ignore weak detections (confidence < 0.5)
    no_of_person = []
    for out in outs:

        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:
                center_x = int(detection[0] * Width)
                center_y = int(detection[1] * Height)
                w = int(detection[2] * Width)
                h = int(detection[3] * Height)
                x = center_x - w / 2
                y = center_y - h / 2
                class_ids.append(class_id)
                confidences.append(float(confidence))
                boxes.append([x, y, w, h])
                label = str(classes[class_id])
                if label == 'person':
                 no_of_person.append('person')

        print(str(len(no_of_person)))
    # apply non-max suppression
    indices = cv2.dnn.NMSBoxes(boxes, confidences, conf_threshold, nms_threshold)

    # go through the detections remaining
    # after nms and draw bounding box
    for i in indices:
        i = i[0]
        box = boxes[i]
        x = box[0]
        y = box[1]
        w = box[2]
        h = box[3]

        draw_bounding_box(frame, class_ids[i], confidences[i], round(x), round(y), round(x + w), round(y + h))

    cv2.imshow('Window', frame)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    if cv2.waitKey(1) == ord('q'):
         break

# Clean up
video.release()
cv2.destroyAllWindows()

#
# cv2.imshow("object detection", image)
#
# # wait until any key is pressed
# cv2.waitKey()
#
# # save output image to disk
# cv2.imwrite("object-detection.jpg", image)
#
# # release resources
# cv2.destroyAllWindows()
