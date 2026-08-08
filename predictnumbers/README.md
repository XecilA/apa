# apa
A small neural network that can predict and recognize handwritten digits between 0-9

The model is trained using the MNIST dataset. The model is then downloaded and nested into a Gradio website, to make it easier for actually testing the model. 

It is the first model I have ever built so it might not predict well every time :P

## live demo of the project:
Sorry I'm currently in China, and huggingface, through which to access the public link, is blocked

## How to run the project
### installation

1. Clone repository:
```sh
git clone link "Sorry im currently in China where github is blocked"

cd predictnumbers
```

3. Install dependencies:
```sh
pip install gradio torch torchvision numpy scikit-learn matplotlib 

4. Run the gradio app:
```sh
python app.py
```
5. After running the code, Gradio will start a local server
    -Open `http://127.0.0.1:7860` to access the local web page
    -Or if 'share=True', open the public Gradio link
## How it works
1. The user uploads a picture of a handwritten digit between 0 and 9
2. The image is resized to 8x8 and then flattened to match the training data
3. The trained model predicts the digit
4. The predicted number is displayed

## Process
I started by training a very small model on the small Sci-learn dataset. When evaluating that model with test-data from the same dataset, the accuracy remained high. I therefore integrated it into a simple Gradio website to more easily use the model. However, despite reshaping the pictures to the same size as the training data (8x8) the model almost never predicted the correct numbers. 

I therefore retrained the model using the MNIST dataset instead. This dataset had larger pictures (28x28) and also a larger variation of numbers, which proved to work better. While it still does not predict every number correct, most of the uploaded pictures are predicted correctly. 

## Programming languages
Until now, Python has been the only language used!

## Challenges 
At first, the model could not predict any number very well. Initially, it was trained on the scikit-learn dataset, but since those pictures were only 8x8 pixels, the model did not really work for real pictures, even when i transformed them to the same size. I therefore trained a new model on the MNIST dataset, which had more and larger pictures. This made the model more accurate (altough not every number is predicted correctly here either)

Getting the model to work through Gradio also took time. I first started with a sketchpad, instead of uploading a picture, but the sketchpad and the current Gradio version I had installed could not really work together. I therefore changed to the more simple version of uploading a pictures, which worked. 

## AI disclaimer
AI was used to debug the project, especially when integrating it into a Gradio application. I got errors because the wrong version of Gradio was installed etc, and AI helped me resolve these issues. It also helped me to understand the Gradio functions better as it was my first time using Gradio :)

## screenshots
1. ![alt text](<Skärmbild 2026-08-08 083737.png>)
