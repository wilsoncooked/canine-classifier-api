import os
from snoop_dog.predict import preprocess_image, format_predictions
from snoop_dog.class_names import class_names
from tensorflow import keras
from snoop_dog.registry import load_dogmodel, load_image, dogimg_process


#def who_am_i():
#    print("Hello my name is Grumpy")

#if __name__ == '__main__':
#    who_am_i()

# initialize the model

#new_model = keras.models.load_model(f"{os.path.dirname(os.path.dirname(__file__))}/models/effnetv2s_finetuned_valsplit01.keras")
#new_model = load_dogmodel()

# Show the model architecture
#new_model.summary()


# load an image
#dog_1 = f"{os.path.dirname(os.path.dirname(__file__))}/dogs/corgie.jpeg"


# predict an image
#predictions = new_model.predict(preprocess_image(dog_1))
#output = format_predictions(predictions, class_names)
#print(output)



# put it all together for the api
def predict_breeds(model, img):
    image = load_image(img)
    image_processed = dogimg_process(image)
    model = model
    predictions = model.predict(image_processed)
    output = format_predictions(predictions, class_names)
    return output
