import PIL.Image
import gradio as gr

from utils import get_demo_img_id_list, get_demo_img_by_id, get_question_list_by_id
from backend import get_yolo_img, update_demo_img, get_llm_response


def create_interface():
    '''
    define the user interface
    '''        
    with gr.Blocks() as user_interface:
      # Tab 1: Pre-Build Demo (Cantonese)
      with gr.Tab("Pre-Build Demo"):
        default_img_id = 'view_1'
        # Layout: (1) Raw Scene Image (2) Yolo-Processed Scene Image (3) Chatbot 
        with gr.Row():
          with gr.Column():
            # default demo image
            default_img = get_demo_img_by_id(default_img_id)
            demo_img = gr.Image(
              label="Scene Image", 
              value=default_img, 
              interactive=False
            )
            # select demo image from dropdown
            demo_img_dropdown = gr.Dropdown(
               label="Select View", 
               choices=get_demo_img_id_list(), 
               value=default_img_id,
               interactive=True
              )
          with gr.Column():
            demo_yolo_img = gr.Image(
               label="Object Detection Result", 
               value=get_yolo_img(PIL.Image.open(default_img)), 
               interactive=False
              )
          with gr.Column():
            demo_chatbot = gr.Chatbot(label="Chat")
            demo_question_dropdown = gr.Dropdown(
               label="Select Question To Ask",
               choices=get_question_list_by_id(default_img_id),
               interactive=True
              )
            demo_voice_output = gr.Audio(label="Listen To AI-Care's Response")

      # Add Event Listener
      demo_img_dropdown.input(update_demo_img, demo_img_dropdown, [demo_img, demo_yolo_img, demo_question_dropdown])
      demo_question_dropdown.input(get_llm_response, [demo_question_dropdown, demo_chatbot], demo_chatbot)

      # Tab 2: Interactive Demo (English)
      with gr.Tab("Interactive Demo"):
         # text_input.submit(get_llm_response, [text_input, chatbot], [text_input, chatbot])
         pass
    
    return user_interface


if __name__ == "__main__":
    '''
    launch interface
    '''
    demo = create_interface().queue()
    demo.launch()
