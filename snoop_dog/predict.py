import tensorflow as tf
import numpy as np


def format_predictions(predictions, class_names, min_probability=0.01):
    # Convert the predicted probabilities to percentages
    predicted_probabilities = predictions * 100

    # Sort the predictions by probability in descending order
    sorted_indices = np.argsort(-predicted_probabilities[0])

    # Filter out indices with probabilities higher than min_probability
    filtered_indices = [i for i in sorted_indices if predicted_probabilities[0][i] >= min_probability]

    # Construct the formatted output string
    formatted_output = ""
    for i in filtered_indices:
        prob = predicted_probabilities[0][i]
        class_name = class_names[i].split('-')[1].replace('_', ' ').title()
        formatted_output += f"{prob:.2f}%\t {class_name}\n"

    return formatted_output

def preprocess_image(image_path):
    img = tf.keras.preprocessing.image.load_img(image_path, target_size=(256, 256))
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)

    return img_array
