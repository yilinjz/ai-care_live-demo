from const import DEMO_IMG_LIST, DEMO_QUESTION_LIST


def get_demo_img_id_list():
        '''
        get list of demo image_ids
        e.g. view_1, view_2, view_3, ...
        '''
        return DEMO_IMG_LIST.keys()

def get_demo_img_by_id(img_id):
        '''
        image_id to image_path
        e.g. view_1 -> images\demo_scene_view_1.jpg
        '''
        return DEMO_IMG_LIST[img_id]

def get_demo_question_list_by_id(img_id):
        '''
        image_id to question_list
        e.g. view_1 -> ['question_1', 'question_2', 'question_3', ...]
        '''
        return DEMO_QUESTION_LIST[img_id]
