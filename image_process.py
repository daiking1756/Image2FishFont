import cv2

def image2fish_font(img):
    
    result_text = ""

    for img_x in img:
        for img_xy in img_x:
            result_text += pixel2fish_font(img_xy)
        result_text += '\n'
    print(result_text)

def pixel2fish_font(pixel):
    # Blue
    if pixel[0] > pixel[1] and pixel[0] > pixel[2]:
        result_text = "🐟"
    # Green
    elif pixel[1] > pixel[0] and pixel[1] > pixel[2]:
        result_text = "🐠"
    # Red
    elif pixel[2] > pixel[0] and pixel[2] > pixel[1]:
        result_text = "🐡"
    else:
        result_text = "魚"

    return result_text