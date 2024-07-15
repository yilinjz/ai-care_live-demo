from const import DEMO_IMG_DICT

def get_demo_img_by_id(img_id):
    if img_id == 'default':
        return 'images\demo_scene_view_1.jpg'
    else:
        return DEMO_IMG_DICT[img_id]
    