# CAPTCHA Solver

This project involves developing a CAPTCHA solver using a Convolutional Neural Network (CNN) and deploying it using a Flask web application.

## Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Training the Model](#training-the-model)
- [Deploying with Flask](#deploying-with-flask)

## Overview

This project trains a CAPTCHA solver using a CNN. The model is trained on a dataset of CAPTCHA images containing 6-digit numbers. The trained model is then deployed using Flask to provide a web interface for users to upload CAPTCHA images and receive predictions.

## Prerequisites

- Python 3.x
- TensorFlow
- Flask
- NumPy
- OpenCV
- tqdm

You can install the required packages using pip:

```bash
pip install -r requirements.txt
```

## Training The Model
used CNN model with layers as follows

    - first convolutional layer
        32 filters, with max pooling of 2x2
        and dropout of 0.25 to avoid overfitting

    - second convolutional layer
        64 filters, with max pooling of 2x2
        and dropout of 0.25 to avoid overfitting
        
    - third convolutional layer
        128 filters, with max pooling of 2x2
        and dropout of 0.25 to avoid overfitting

    - fourth convolutional layer
        256 filters, with max pooling of 2x2
        and dropout of 0.25 to avoid overfitting

    used ReLU activation function in the convolution hidden layers

    - flatten dense layer with 512 nodes
    used softmax activation function for the output layer

    used the adam optimizer for compiling with categorical_crossentropy loss function


## Deploying with Flask
deployed on localhost on default port of 5000
    - index.html will allow you to select the file and forward the file to our
    model for prediction and then show the result on the result.html file


ENJOY!!!