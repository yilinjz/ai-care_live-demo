import PIL.Image
import numpy as np
import gradio as gr

from utils import get_demo_img_by_id, get_question_list_by_id


####################   Image Processing   #################### 
              
def get_yolo_img(input_img):
        '''
        get img with yolo class labels
        '''
        # placeholder for now #
        input_img = np.asarray(input_img)
        sepia_filter = np.array([
            [0.393, 0.769, 0.189], 
            [0.349, 0.686, 0.168], 
            [0.272, 0.534, 0.131]
        ])
        sepia_img = input_img.dot(sepia_filter.T)
        sepia_img /= sepia_img.max()
        return sepia_img
        # placeholder for now #

def update_demo_img(img_id):
    '''
    update displayed image when user select from dropdown
    
    also changes the list of demo questions to match the new image
    '''

    new_demo_img = PIL.Image.open(get_demo_img_by_id(img_id))
    new_yolo_img = get_yolo_img(new_demo_img)
    new_demo_question_dropdown = gr.Dropdown(
        label="Select Question To Ask",
        choices=get_question_list_by_id(img_id),
        interactive=True
    )

    return new_demo_img, new_yolo_img, new_demo_question_dropdown

####################   Chat   ####################

def get_demo_response(message, chat_history):
        '''
        get response from llm
        '''
        # placeholder for now #
        import random
        bot_message = random.choice(["How are you?", "I love you", "I'm very hungry"])
        chat_history.append((message, bot_message))
        # placeholder for now #
        return chat_history

def get_llm_response(message, chat_history):
        '''
        get response from llm
        '''
        # placeholder for now #
        import random
        bot_message = random.choice(["How are you?", "I love you", "I'm very hungry"])
        chat_history.append((message, bot_message))
        # placeholder for now #
        return "", chat_history

####################   Audio   ####################
