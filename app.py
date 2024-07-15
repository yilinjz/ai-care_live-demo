import gradio as gr

from const import DEMO_IMG_DICT


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
            demo_img = gr.Image("images\demo_scene_view_1.jpg")
            demo_img_dropdown = gr.Dropdown(DEMO_IMG_DICT.keys(), label="select view")
          with gr.Column():
            demo_yolo_result = gr.Image()
          with gr.Column():
            chatbot = gr.Chatbot()
            voice_input = gr.Audio(sources=["microphone"])

      with gr.Tab("Interactive English Demo"):
         pass
    
    return user_interface


if __name__ == "__main__":
    '''
    launch interface
    '''
    demo = create_interface().queue()
    demo.launch()
