# Handwritten Number Predictor!

A small neural network that can predict and recognize handwritten digits between 0 and 9.

The model is trained using the MNIST dataset. The model is then saved and integrated into a Gradio application, making it easier to actually test the model.

It is the first model I have ever built, so it might not predict well every time :P

#### Video Demo:
https://youtu.be/OvuiIfAz_6A?si=BCtbVZaXZbs0uUkD 

#### Installation

1. Clone the repository:

```sh
git clone https://github.com/XecilA/apa.git
cd apa/predictnumbers
```

2. Install the dependencies:

```sh
pip install gradio torch torchvision numpy scikit-learn matplotlib
```

3. Run the Gradio application:

```sh
python app.py
```

4. After running the code, Gradio will start a local server:

* Open `http://127.0.0.1:7860` to access the local web page.
* If `share=True`, you can instead open the public Gradio link.

#### How It Works

1. The user uploads a picture of a handwritten digit between 0 and 9.
2. The image is resized to 28×28 pixels and then flattened to match the training data.
3. The trained model predicts the digit.
4. The predicted number is displayed.

#### Process

I started by training a very small model on the small scikit-learn digits dataset. When evaluating that model with test data from the same dataset, the accuracy remained high. I therefore integrated it into a simple Gradio application to make the model easier to use. However, despite reshaping the pictures to the same size as the training data (8×8), the model almost never predicted the correct numbers.

I therefore retrained the model using the MNIST dataset instead. This dataset had larger pictures (28×28) and a larger number and variety of handwritten digits, which proved to work better. While it still does not predict every number correctly, most of the uploaded pictures are predicted correctly.

To train the model on the MNIST dataset, each 28×28 picture was flattened into a vector, with its pixel values rescaled to an interval between 0 and 1 instead of 0 and 255. I then split the MNIST dataset so that 80% of the images formed the training set and 20% formed the test set. After training, the model achieved high accuracy on the test images, so I saved it and then integrated it into Gradio.

My initial idea for the Gradio application was that the user would be able to draw a number on a sketchpad, which the model would then predict. However, I had some issues with Gradio’s built-in sketchpad and the version of Gradio I had installed. I eventually switched to the simpler option of having the user upload a picture instead, which worked much better!

#### Programming Language

Python is the only programming language used in this project!

#### AI Disclaimer

AI was used to help debug the project, especially when I was integrating the model into a Gradio application. I encountered errors because I had an incompatible version of Gradio installed, and AI helped me resolve these issues. It also helped me understand the Gradio functions better, as it was my first time using Gradio :)

#### Project files

##### `predictnumbers/app.py`

This file loads the trained model and creates the Gradio interface. It also
preprocesses uploaded images by cropping, resizing, flattening and normalizing
them before passing them to the model.

##### `predictnumbers/training.ipynb`

This file downloads and prepares the MNIST dataset, defines and trains the
neural network, evaluates its accuracy and saves the trained model.

##### `predictnumbers/realmodel.pth`

This file contains the trained PyTorch model used by the Gradio application.

##### `.gitignore`

This file tells Git to exclude automatically generated or local files, such
as the virtual environment, Python cache files and temporary Gradio files.