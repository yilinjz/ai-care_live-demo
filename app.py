import PIL.Image
import gradio as gr

from utils import get_demo_img_id_list, get_demo_img_by_id, get_demo_question_list_by_id
from frontend import update_demo_img, update_live_img, update_demo_chatbot, update_live_chatbot
from backend import get_yolo_img


def create_interface():
    '''
    Define the user interface

    Tab 1: Pre-Build Demo (Cantonese)
    Layout: (1) Raw Scene Image (2) Yolo-Processed Scene Image (3) Chatbot & Audio

    Tab 2: Interactive Live Demo (English)
    Layout: (1) Raw Scene Image (2) Yolo-Processed Scene Image (3) Chatbot & Audio
    '''        
    with gr.Blocks() as user_interface:
      ### Tab 1: Pre-Build Demo (Cantonese) ###
      with gr.Tab("Pre-Build Demo"):
        default_img_id = 'view_1' 
        with gr.Row():
          ## (1) Raw Scene Image ##
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
               label="select view", 
               choices=get_demo_img_id_list(), 
               value=default_img_id,
               interactive=True
              )
          ## (2) Yolo-Processed Scene Image ##
          with gr.Column(): 
            default_yolo_img, default_context_json = get_yolo_img(PIL.Image.open(default_img))
            demo_yolo_img = gr.Image(
               label="Object Detection Result", 
               value=default_yolo_img, 
               interactive=False
              )
          ## (3) Chatbot & Audio ##
          with gr.Column():
            demo_chatbot = gr.Chatbot(
              label="AI-Care"
              )
            demo_question_dropdown = gr.Dropdown(
               label="select question to ask",
               choices=get_demo_question_list_by_id(default_img_id),
               interactive=True
              )
            demo_audio_output = gr.Audio(
               label="listen to audio response",
               interactive=False
              )

      ##  Add Event Listener  ##
      demo_img_dropdown.input(update_demo_img, demo_img_dropdown, [demo_img, demo_yolo_img, demo_question_dropdown])
      demo_question_dropdown.input(update_demo_chatbot, [demo_question_dropdown, demo_chatbot], [demo_chatbot, demo_audio_output])

      ###   Tab 2: Interactive Live Demo (English)   ###
      with gr.Tab("Interactive Demo"):
        with gr.Row():
          ## (1) Raw Scene Image ##
          with gr.Column():
            live_img = gr.Image(
              label="Scene Image", 
              interactive=True
            )
          ## (2) Yolo-Processed Scene Image ##
          with gr.Column():
            live_yolo_img = gr.Image(
               label="Object Detection Result", 
               interactive=False
              )
          ## (3) Chatbot & Audio ##
          with gr.Column():
            live_chatbot = gr.Chatbot(
              label="Chat"
            )
            live_text_input = gr.Textbox(
              label="send a message",
               interactive=True
            )
            live_audio_output = gr.Audio(
               label="listen to speech audio",
               interactive=False
              )
        
        ##  Add Event Listener  ##
        live_img.upload(update_live_img, live_img, [live_img, live_yolo_img])
        live_text_input.submit(update_live_chatbot, [live_text_input, live_chatbot], [live_text_input, live_chatbot, live_audio_output])
    
    return user_interface


if __name__ == "__main__":
    '''
    launch interface
    '''
    demo = create_interface().queue()
    demo.launch()
