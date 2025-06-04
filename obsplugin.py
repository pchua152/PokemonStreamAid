import cv2 as cv
import numpy as np
import time
import os
def take_screenshot():
    
    test_image = os.getcwd() + 'insert your path here'
    img = cv.imread(test_image)
    img2 = cv.imread(test_image,0)
    
    w,h = img2.shape[::-1]
    your_side = img2[0:h, 0:w//2]
    show_this = img[0:h, 0:w//2:]
   
    target_image = os.getcwd() + r'\photos\lose_image.png'
    template = cv.imread(target_image,0)
    cv.imshow("Template", template)

    result = cv.matchTemplate(your_side,template, cv.TM_CCOEFF_NORMED)
    _,max_val1, _, _ = cv.minMaxLoc(result)
    threshold = .75
    print(max_val1)
    print(max_val1 >= threshold)
    locations = np.where(result >= threshold)
    print(locations)
    for pt in zip(*locations[::-1]):
        cv.rectangle(show_this,  pt, (pt[0] + w, pt[1] + h), (0, 255, 255), 2)
        win_lose(0,0)
    cv.imshow("Half",show_this)
    cv.waitKey(0)
    cv.destroyAllWindows()
    
    
    

def video_attempt():
    file_path = 1
    capture = cv.VideoCapture(file_path)
    
    w,l = 0,0
    recorded = True
    #Team preview image
    target_image = os.getcwd() + r'\photos\team_preview.jpg'
    template = cv.imread(target_image,0)
    #load the indicators for battle start and WIN or LOSE
    win_image = os.getcwd() + r'\photos\win_image.png'
    win_template = cv.imread(win_image,0)
    
    win_lose(w,l)
    while (capture.isOpened()):
        ret, frame = capture.read()
        cv.imshow("See this", frame)
        gray_scale = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        width,height = gray_scale.shape[::-1]
        #Team check
        result = cv.matchTemplate(gray_scale,template, cv.TM_CCOEFF_NORMED)
        
        #Win/Lose check
        your_side = gray_scale[0:height, 0:width//2]
        opponent_side = gray_scale[0:height, width//2:]
        
        #Due to low threshold on lose image, find where the win is located and change win/loss off of that
        win_result = cv.matchTemplate(your_side, win_template, cv.TM_CCOEFF_NORMED)
        lose_result = cv.matchTemplate(opponent_side, win_template, cv.TM_CCOEFF_NORMED)
        _,max_val1, _, _ = cv.minMaxLoc(win_result)
        _,max_val2, _, _ = cv.minMaxLoc(lose_result)
        threshold = .8
        result_threshold = .75
        _,max_val,_,_ = cv.minMaxLoc(result)
        if max_val >= threshold:
            saved_team = cv.imread('Opponent_team.png')
            if saved_team is not None:
                #Check to see if its the same as the picture
                if not (saved_team == frame[152:555, 821:895]).all():
                    cv.imwrite("Opponent_team.png", frame[152:555, 821:895])
            else:
                 cv.imwrite("Opponent_team.png", frame[152:555, 821:895])
            recorded = False

        
        elif max_val1 >= result_threshold and not recorded:
            w += 1
            win_lose(w,l)
            recorded = True
        
        
        elif max_val2 >= result_threshold:
            l+= 1
            win_lose(w,l)
            recorded = True
        if cv.waitKey(1) == ord('x'):
            print('Closing')
            break
        
    capture.release()
    cv.destroyAllWindows()


def win_lose(w,l):
    file_path = os.getcwd() + r'\record.txt'   
    
    file = open(file_path, 'w')
    file.write(f'{w} - {l}')
    file.close()
    
if __name__ == "__main__":
    video_attempt()