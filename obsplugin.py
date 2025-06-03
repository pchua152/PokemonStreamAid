import cv2 as cv
import numpy as np

import os
def take_screenshot():
    
    test_image = os.getcwd() + r'\photos\preview_eng.jpg'
    img = cv.imread(test_image)
    img2 = cv.imread(test_image,0)
   
    target_image = os.getcwd() + r'\photos\IMG_2543.jpg'
    template = cv.imread(target_image,0)
    
    width,height = template.shape[::-1]

    result = cv.matchTemplate(img2,template, cv.TM_CCOEFF_NORMED)
    
    threshold = .8
    
    locations = np.where(result >= threshold)
    if locations:
        cv.imwrite("Opponent_team.png", img[152:555, 821:895])
    cv.waitKey(0)
    cv.destroyAllWindows()
    
    
    

def video_attempt():
    file_path = 0
    capture = cv.VideoCapture(file_path)
    
    target_image = os.getcwd() + r'\photos\IMG_2543.jpg'
    template = cv.imread(target_image,0)
    cv.imshow("test", template)
    width,height= template.shape[::-1]

    while (capture.isOpened()):
        ret, frame = capture.read()
        #used to multiple of the same photo from being taken, causing the image to glitch out
        photo_taken = False
        cv.imshow("See this", frame)
        gray_scale = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        #Team check
        result = cv.matchTemplate(gray_scale,template, cv.TM_CCOEFF_NORMED)
        threshold = .8
        _,max_val,_,max_aloc = cv.minMaxLoc(result)
        if max_val >= threshold and not photo_taken:
            cv.imwrite("Opponent_team.png", frame[152:555, 821:895])
            photo_taken = True
        
        if cv.waitKey(1) == ord('z'):
            #Temporary solution, will be replaced with the win/lose screen
            photo_taken = False
        #Start timer and record win/loss
        if cv.waitKey(1) == ord('x'):
            break
        
    capture.release()
    cv.destroyAllWindows()
        
    
    
    
    
if __name__ == "__main__":
    take_screenshot()