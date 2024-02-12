import tensorflow as tf
import numpy as np
import csv

class_name_to_breed = {}
with open('data/dog_breed_names.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        class_name_to_breed[row['class_name']] = row['dog_breed']


def format_predictions(predictions, class_names, min_probability=0.01):
    print('Formatting 🐩')
    # Convert the predicted probabilities to percentages
    predicted_probabilities = predictions * 100

    # Sort the predictions by probability in descending order
    sorted_indices = np.argsort(-predicted_probabilities[0])

    # Filter out indices with probabilities higher than min_probability
    filtered_indices = [i for i in sorted_indices if predicted_probabilities[0][i] >= min_probability]

    # Take top 5 predictions
    top_5_indices = filtered_indices[:5]

    # Calculate total sum of these top 5 predictions
    #top_5_sum = sum(predicted_probabilities[0][i] for i in top_5_indices)

    # Construct the formatted output string
    formatted_output = ""
    cumulative_sum = 0
    for i in top_5_indices:
        prob = predicted_probabilities[0][i]
        class_name_key = class_names[i]
        dog_breed = class_name_to_breed.get(class_name_key, "Unknown")
        formatted_output += f"{prob:.2f}%\t {dog_breed}\n"
        cumulative_sum += prob

    if len(filtered_indices) > 5:
        other_prob = 100 - cumulative_sum
        formatted_output += f"{other_prob:.2f}%\t Others\n"

    return formatted_output


def preprocess_image(image_path):
    print('Preprocessing 🐕')
    img = tf.keras.preprocessing.image.load_img(image_path, target_size=(256, 256))
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)

    return img_array
