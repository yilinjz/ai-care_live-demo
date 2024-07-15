import gradio as gr

def create_interface():
    '''
    define the user interface with gradio
    '''        
    with gr.Blocks() as user_interface:
      with gr.Row():
        with gr.Column():
          im = gr.Image()
          dd = gr.Dropdown(["far", "medium", "close"], label="select")
        with gr.Column():
          il = gr.Image()
        with gr.Column():
          cb = gr.Chatbot()
          voice = gr.Audio(sources=["microphone"])
    

    return user_interface

if __name__ == "__main__":
    '''
    launch interface
    '''
    demo = create_interface().queue()
    demo.launch()
