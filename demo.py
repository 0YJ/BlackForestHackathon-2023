
import time
from picamera2 import Picamera2
from keras.models import load_model
import zmq  # TensorFlow is required for Keras to work

def load_model_from_file():
    path_to_model = './resources/smoke_model/keras_model.h5'
    path_to_labels = './resources/smoke_model/labels.txt'

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


FAN1 = 18
FAN2 = 23
def setup_gpio():
    GPIO.setmode(GPIO.BCM)   
    GPIO.setup(FAN1, GPIO.OUT)
    GPIO.setup(FAN2, GPIO.OUT)


def main():
    model, class_names = load_model_from_file()
    print('Model loaded.')
    picam2 = Picamera2()
    picam2.start()
    print('Model startet.')
    time.sleep(2)
    
    while True:
        time.sleep(1)
        image = picam2.capture_array()
        image = cv2.cvtColor(im,cv2.COLOR_BGR2RGB)
        print('image recived')
        imshow('Test', image)
        cv2.waitKey(1)

        class_name, confidence_score = predict(model=model,class_names=class_names, image=image)
        print(f'Class: {class_name}')
        print(f'Confidence {confidence_score}')
        
        if class_name > 'no_smoke':
            GPIO.output(FAN1,False)
            GPIO.output(FAN2,False)
        elif class_name > 'middel_smoke':
            GPIO.output(FAN1,True)
            GPIO.output(FAN2,False)
        elif class_name > 'full_smoke':
            GPIO.output(FAN1,True)
            GPIO.output(FAN2,True)
        else: 
            GPIO.output(FAN1,True)
            GPIO.output(FAN2,True)
        # 27 is the ASCII for the esc key on your keyboard.
        if keyboard_input == 27:
         break

    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
 
