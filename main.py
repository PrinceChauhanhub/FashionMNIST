import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np
import os

os.environ['PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION'] = 'python'


working_dir = os.path.dirname(os.path.abspath(__file__))
model_path = f"{working_dir}/trained_fashion_mnist_model.h5"

# Loading the pre-trained model
model = tf.keras.models.load_model(model_path)

## defining class labels
class_names = ['T-shirt/top','Trouser','Pullover','Dress','Coat','Sandal','Shirt','Sneaker','Bag','Ankle boot']

## preprocess the uploaded image

def preprocess_image(image):
    img = Image.open(image)
    img = img.resize((28, 28))
    img = img.convert('L')
    img_array = np.array(img) / 255.0
    img_array = img_array.reshape((1, 28, 28, 1))
    return img_array

## Streamlit app
st.title("Fashion Item Classification")

uploaded_image = st.file_uploader("upload an image...", type=["jpg","jpeg","png"])

if uploaded_image is not None:
    image = Image.open(uploaded_image)
    col1, col2 = st.columns(2)
    
    with col1:
        resized_img = image.resize((100,100))
        st.image(resized_img)
        
    with col2:
        if st.button('classify'):
            img_array = preprocess_image(uploaded_image)
            
            result = model.predict(img_array)
            
            predicted_class = np.argmax(result)
            prediction = class_names[predicted_class]
            
            st.success(f"Prediction: {prediction}")