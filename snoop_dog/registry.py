from tensorflow import keras
import numpy as np
from PIL import Image
import os

def load_image(img):
    img = Image.open(img).convert("RGB")
    print("dog is loaded")
    img = img.resize((256,256))
    print("dog is resized")
    return img

def dogimg_process(img):
    img_array = keras.preprocessing.image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

def load_dogmodel():
    new_model = keras.models.load_model(f"{os.path.dirname(os.path.dirname(__file__))}/models/effnetv2l_finetuned_valsplit01.keras")
    return new_model
