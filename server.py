from cv2 import VideoCapture, imshow
import cv2 # Install opencv-python
import numpy as np
 
from keras.models import load_model
import zmq  # TensorFlow is required for Keras to work

def load_model_from_file():
    path_to_model = './resources/fire_model/keras_model.h5'
    path_to_labels = './resources/fire_model/labels.txt'

    # Disable scientific notation for clarity
    np.set_printoptions(suppress=True)

    # Load the model
    model = load_model(path_to_model, compile=False)

    # Load the labels
    class_names = open(path_to_labels, "r").readlines()
    return model, class_names







def predict(model,class_names,image):
        # Resize the raw image into (224-height,224-width) pixels
        image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)

         # Make the image a numpy array and reshape it to the models input shape.
        image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)

        # Normalize the image array
        image = (image / 127.5) - 1

        # Predicts the model
        prediction = model.predict(image)
        index = np.argmax(prediction)
        class_name = class_names[index]
        confidence_score = prediction[0][index]
            # Print prediction and confidence score
        print("Class:", class_name[2:], end="")
        print("Confidence Score:", str(np.round(confidence_score * 100))[:-2], "%")
        return class_name[2:], str(np.round(confidence_score * 100))[:-2]

def set_fan_speed(socket,speed:int):
    socket.send(speed)
    print(f'set_fan_speed {speed}')


def create_zmq_reciver():
    context = zmq.Context()
    socket = context.socket(zmq.PAIR)
    socket.bind("tcp://192.168.178.21:6666")
    print('bind')
    return socket

def create_fan_sender():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.connect("tcp://192.168.178.21:5555")
    return socket

def recive_image(socket):  
    # Grab the webcamera's image.
    #ret, image = camera.read()
    image = socket.recv()
    return image

def main():
    model, class_names = load_model_from_file()
    socket = create_zmq_reciver()
    fan_socket = create_fan_sender()
    print('Model loaded')
    # CAMERA can be 0 or 1 based on default camera of your computer
    #camera = cv2.VideoCapture(0)

    print('Cam conencted')

    while True:
        image = recive_image(socket)
        print('image recived')
        imshow('Test', image)

        cv2.waitKey(1)

        class_name, confidence_score = predict(model=model,class_names=class_names, image=image)

        if class_name > 'no_smoke':
             set_fan_speed(fan_socket,0)
        elif class_name > 'middel_smoke':
            set_fan_speed(fan_socket,50)
        elif class_name > 'full_smoke':
            set_fan_speed(fan_socket,100)
        else: 
            set_fan_speed(fan_socket,100)
            # Listen to the keyboard for presses.
        keyboard_input = cv2.waitKey(1)

        # 27 is the ASCII for the esc key on your keyboard.
        if keyboard_input == 27:
         break
    #camera.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
 
