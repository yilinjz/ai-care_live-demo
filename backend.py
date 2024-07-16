import PIL
import numpy as np

from utils import get_demo_img_by_id


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
    '''

    new_demo_img = PIL.Image.open(get_demo_img_by_id(img_id))
    new_yolo_img = get_yolo_img(new_demo_img)

    return new_demo_img, new_yolo_img
