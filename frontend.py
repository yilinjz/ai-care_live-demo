import PIL.Image
import gradio as gr

from utils import get_demo_img_by_id, get_demo_question_list_by_id
from backend import get_yolo_img, get_llm_response, get_tts_result


####################   Image   #################### 
def update_demo_img(new_img_id):
    '''
    Update displayed image when user select a scene from dropdown
    Also changes the list of demo questions to match the new image
    '''
    new_demo_img = PIL.Image.open(get_demo_img_by_id(new_img_id))
    new_yolo_img, context_json = get_yolo_img(new_demo_img)
    # TODO: save context_json for inference
    new_demo_question_dropdown = gr.Dropdown(
        label="Select Question To Ask",
        choices=get_demo_question_list_by_id(new_img_id),
        interactive=True
    )

    return new_demo_img, new_yolo_img, new_demo_question_dropdown

def update_live_img(new_live_img):
    '''
    Update displayed image when user uploads their own image
    Also changes the list of demo questions to match the new image
    '''
    new_yolo_img, context_json = get_yolo_img(new_live_img)
    # TODO: save context_json for inference

    return new_live_img, new_yolo_img

####################   Chatbot   ####################
def update_demo_chatbot(message, chat_history):
        '''
        Generate a response from the demo chatbot
        Also convert the response text to speech and return it
        '''
        ### placeholder for now ###
        context = ""
        response = get_llm_response(message=message, context=context)
        ### placeholder for now ###
        chat_history.append((message, response))

        audio_output = get_tts_result(response)
        return chat_history, audio_output

def update_live_chatbot(message, chat_history):
        '''
        Generate a response from the demo chatbot
        Also convert the response text to speech and return it
        '''
        ### placeholder for now ###
        context = ""
        response = get_llm_response(message=message, context=context)
        ### placeholder for now ###
        chat_history.append((message, response))

        audio_output = get_tts_result(response)
        # return empty string to Textbox to clear input
        return "", chat_history, audio_output
