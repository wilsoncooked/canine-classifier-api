from snoop_dog.predict import format_predictions
from snoop_dog.class_names import class_names
from snoop_dog.registry import load_image, dogimg_process, gradcam
import base64

    

# put it all together for the api
def predict_breeds(model, img):
    image = load_image(img)
    image_processed = dogimg_process(image)
    model = model
    predictions = model.predict(image_processed)
    output = format_predictions(predictions, class_names)
    grad_img = gradcam(model, image_processed)
    output[0]['ai_view'] = base64.b64encode(grad_img) # Check if not a dog
    return output
