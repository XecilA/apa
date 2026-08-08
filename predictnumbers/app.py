import gradio as gr
from PIL import Image
import numpy as np
import torch
import torch.nn as nn

import torch.nn as nn
class numbers(nn.Module):
    def __init__(self):
        super().__init__()

        self.linear1=nn.Linear(784, 128)
        self.relu1 = nn.ReLU()
        self.linear2 = nn.Linear(128,64)
        self.relu2 = nn.ReLU()
        self.linear3 = nn.Linear(64, 19)
    def forward(self, x):
        x = self.linear1(x)
        x=self.relu1(x)
        x=self.linear2(x)
        x=self.relu2(x)
        x=self.linear3(x)
        return  x
    
 #download the model
model = torch.load("realmodel.pth", weights_only=False)
model.eval()


#cropping the picture so that the drawn figure is in the center
def crop(image_crop, padding = 2):
    no_background = np.where(image_crop>10)

    #checks so that the image is not empty, becuase if it is, this returns the original and doesnt change anything
    if len(no_background[0]) == 0:
        return image_crop

    y_min, y_max = no_background[0].min(), no_background[0].max()
    x_min, x_max = no_background[1].min(), no_background[1].max()
    cropped = image_crop[y_min:y_max+1, x_min:x_max+1]

    padded = np.pad(cropped, padding, mode = "constant", constant_values=0)

    return padded


def predict(image_from_sketchpad):
    #taking the cropped picture
    cropped_image = crop(image_from_sketchpad, padding = 2)
      
    #convert user's drawing to PIL image
    image = Image.fromarray(cropped_image.astype("uint8"))
    image = image.resize((28,28))

    #flatten the image
    flattened = np.array(image).reshape(1, -1)

    flattened = flattened / 255.0

    tensor_image = torch.from_numpy(flattened).float()

    with torch.no_grad():
        output = model(tensor_image)
        prediction = torch.argmax(output)
        return_this = prediction.item()

    return return_this

with gr.Blocks() as demo:
    gr.Markdown("# Digits predictor:)")
    gr.Markdown("##Upload a photo of a digit below!")

    with gr.Row():
        with gr.Column():
            sketchpad = gr.Image(
                type = "numpy",
                image_mode="L",
                label = "draw here"
            )
        with gr.Column():
            predict_button= gr.Button("Predict!!")
            clear = gr.Button("Clear")
        with gr.Column():
            output = gr.Textbox(label = "Prediciton", lines = 3)

    predict_button.click(predict, sketchpad, output)

    clear.click(fn=lambda:(None, ""), inputs = None, outputs=[sketchpad, output])
    

print("helloo")
demo.launch(share = True)


