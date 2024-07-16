import PIL
import gradio as gr

from const import DEMO_IMG_DICT
from utils import get_demo_img_by_id
from backend import get_yolo_img, update_demo_img


def create_interface():
    '''
    define the user interface
    '''        
    with gr.Blocks() as user_interface:
      # Tab 1: Pre-Build Demo (Cantonese)
      with gr.Tab("Pre-Build"):
        # Layout: (1) Raw Scene Image (2) Yolo-Processed Scene Image (3) Chatbot 
        with gr.Row():
          with gr.Column():
            # default image 
            # e.g. "images\demo_scene_view_1.jpg"
            default_img = get_demo_img_by_id('view_1')
            demo_img = gr.Image(default_img, interactive=False)
            # select demo image from dropdown
            demo_img_dropdown = gr.Dropdown(DEMO_IMG_DICT.keys(), value='view_1', label="select view")
          with gr.Column():
            demo_yolo_img = gr.Image(get_yolo_img(PIL.Image.open(default_img)), interactive=False)
          with gr.Column():
            chatbot = gr.Chatbot()
            voice_input = gr.Audio(sources=["microphone"])

      # Add Event Listener
      demo_img_dropdown.input(update_demo_img, demo_img_dropdown, [demo_img, demo_yolo_img])

      # Tab 2: Interactive Demo (English)
      with gr.Tab("Interactive Demo"):
         pass
    
    return user_interface


if __name__ == "__main__":
    '''
    launch interface
    '''
    demo = create_interface().queue()
    demo.launch()
