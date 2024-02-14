import tensorflow as tf
import numpy as np
import csv


csv_data = []
with open('data/dog_breed_names.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        csv_data.append(row)


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

    # Construct the formatted output string
    formatted_output = ""
    cumulative_sum = 0
    breeds = []
    for i in top_5_indices:
        prob = predicted_probabilities[0][i]
        if prob > 1: # check if the probabilty is more than 1%
            class_name_key = class_names[i]
            dog = next((item for item in csv_data if item['class_name'] == class_name_key), None)
            breeds.append({
                    "breedNames":dog['dog_breed'],
                    "prob":round(float(prob),2),
                    "referenceImageId": dog['reference_image_id']
                    })
            cumulative_sum += prob
            other_prob = 100 - cumulative_sum

    if len(filtered_indices) > 5: # more than 5 predictions would be summed as others
        formatted_output += f"{other_prob:.2f}%\t Others\n"
        breeds.append({
            "breedNames":"Others",
            "prob":round(float(other_prob),2),
            "referenceImageId": None
            })

   # Check if the cumulative probability in "Others" category is more than 75%
        if other_prob > 75:
            breeds = [{
                "breedNames":"It doesn't look like a dog!",
                "prob":round(float(other_prob),2),
                "referenceImageId": None
                }]

    return breeds


def preprocess_image(image_path):
    print('Preprocessing 🐕')
    img = tf.keras.preprocessing.image.load_img(image_path, target_size=(256, 256))
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)

    return img_array
