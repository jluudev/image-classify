# Image Classification App

This is a simple Flask application that uses a pre-trained ResNet50 model to classify images. Users can upload an image through a POST request to the application, and it will return the top 3 predictions with their corresponding probabilities.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software and how to install them:

- Docker
- Python 3.9 or later
- Pip

### Installing

Here's how to test this app:

1. Clone this repository to your local machine:

    ```
    git clone https://github.com/jluudev/image-classify.git
    cd image-classify
    ```

2. Build the Docker image:

    ```
    docker build -t image-classify-app .
    ```

3. Run the application:

    ```
    docker run -p 5000:5000 image-classify-app
    ```

   After running this command, the application should be accessible at `http://localhost:5000`.

### Running the tests

test_app.py contains some simple tests to ensure basic working of the app. To us test_app.py:

    ```
    python -m unittest test_app.py
    ```
    

## Usage

To use the app with your own images, send a POST request to `http://localhost:5000/predict` with a form-data body including an 'image' field with the image file you wish to classify.

### Example with `curl`:

```sh
curl -X POST -F "image=@path_to_your_image.jpg" http://localhost:5000/predict
```

### Example with Python:

Provided in the repo is the post_image.py. It sends a POST request provided a path to an image as an argument.

    ```
    python3 post_image.py /path_to_your_image.jpg
    ```