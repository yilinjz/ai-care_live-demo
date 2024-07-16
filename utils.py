from const import DEMO_IMG_LIST, DEMO_QUESTION_LIST

def get_demo_img_id_list():
        return DEMO_IMG_LIST.keys()

# image_id to image_path
# e.g. view_1 -> images\demo_scene_view_1.jpg
def get_demo_img_by_id(img_id):
        return DEMO_IMG_LIST[img_id]

# image_id to question_list
# e.g. view_1 -> ['question_1', 'question_2', 'question_3']
def get_question_list_by_id(img_id):
        return DEMO_QUESTION_LIST[img_id]
