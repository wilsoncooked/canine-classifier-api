from tensorflow import keras
import numpy as np
from PIL import Image
import os
import tensorflow as tf
import cv2
import matplotlib.pyplot as plt
import io

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
    new_model = keras.models.load_model(f"{os.path.dirname(os.path.dirname(__file__))}/models/effnetv2s_finetuned_valsplit01.keras")
    return new_model

def gradcam(model, img_array):
    last_conv_layer = model.get_layer('efficientnetv2-s').get_layer('top_activation')
    last_conv_layer_model = tf.keras.Model(model.get_layer('efficientnetv2-s').inputs, last_conv_layer.output)
    
    classifier_input = tf.keras.Input(shape=last_conv_layer.output.shape[1:])
    x = classifier_input
    for layer_name in ["global_average_pooling2d", "dense"]:
        x = model.get_layer(layer_name)(x)
    classifier_model = tf.keras.Model(classifier_input, x)
    
    with tf.GradientTape() as tape:
        inputs = img_array
        last_conv_layer_output = last_conv_layer_model(inputs)
        tape.watch(last_conv_layer_output)
        preds = classifier_model(last_conv_layer_output)
        top_pred_index = tf.argmax(preds[0])
        top_class_channel = preds[:, top_pred_index]
    
    grads = tape.gradient(top_class_channel, last_conv_layer_output)
    pooled_grads = tf.reduce_mean(grads, axis=(0, 1, 2))
    last_conv_layer_output = last_conv_layer_output.numpy()[0]
    pooled_grads = pooled_grads.numpy()
    for i in range(pooled_grads.shape[-1]):
        last_conv_layer_output[:, :, i] *= pooled_grads[i]
    np.shape(last_conv_layer_output)
    gradcam = np.mean(last_conv_layer_output, axis=-1)
    gradcam = np.clip(gradcam, 0, np.max(gradcam)) / np.max(gradcam)
    gradcam = cv2.resize(gradcam, (256, 256)) # Can be probably also be done with PIL
    fig = plt.figure(visible=False)
    canvas = fig.canvas
    ax = fig.gca()
    fig = plt.imshow(np.squeeze(img_array))
    fig = plt.imshow(gradcam, alpha=0.5)
    ax.axis('off')
    canvas.draw()
    image_flat = np.frombuffer(canvas.tostring_rgb(), dtype='uint8')
    img_arr = image_flat.reshape(*reversed(canvas.get_width_height()), 3)
    return img_arr