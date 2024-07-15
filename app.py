import gradio as gr

from const import DEMO_IMG_DICT
from utils import get_demo_img_by_id
from backend import update_demo_img

def create_interface():
    '''
    define the user interface
    '''        
    with gr.Blocks() as user_interface:
      # Tab 1: demo in Cantonese
      # Fixed scene images/sample questions/audio inputs
      with gr.Tab("Cantonese Demo"):
        # Layout: (1) Raw Scene Image (2) Scene Image processed by Yolo (3) Chatbot 
        with gr.Row():
          # select demo image
          with gr.Column():
            # default image
            demo_img = gr.Image(get_demo_img_by_id('default'), interactive=False)
            demo_img_dropdown = gr.Dropdown(DEMO_IMG_DICT.keys(), value='view_1', label="select view")
          with gr.Column():
            demo_yolo_img = gr.Image(interactive=False)
          with gr.Column():
            chatbot = gr.Chatbot()
            voice_input = gr.Audio(sources=["microphone"])

      # Add Event Listener
      demo_img_dropdown.input(update_demo_img, demo_img_dropdown, [demo_img, demo_yolo_img])

      with gr.Tab("Interactive English Demo"):
         pass
    
    return user_interface


if __name__ == "__main__":
    '''
    launch interface
    '''
    demo = create_interface().queue()
    demo.launch()
