import cv2 as cv
import numpy as np
import os


def read_video():
    file_path = 1
    capture = cv.VideoCapture(file_path)

    target_width = 1280
    target_height = 720

    
    w,l = 0,0
    recorded = True
    #Team preview image
    target_image = os.getcwd() + r'\photos\team_preview.jpg'
    template = cv.imread(target_image,0)
    #load the indicators for battle start and WIN or LOSE
    win_image = os.getcwd() + r'\photos\win_image.png'
    win_template = cv.imread(win_image,0)
    
    win_lose(w,l)
    saved_team = cv.imread('Opponent_team.png')
    while (capture.isOpened()):
        ret, frame = capture.read()
        frame = cv.resize(frame, (target_width, target_height))
        cv.imshow("See this", frame)
        
        
            
        gray_scale = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        width,height = gray_scale.shape[::-1]

        #cv.imshow("Gray", gray_scale)
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
        print(f'{max_val1= } {max_val2=}')
        threshold = .8
        result_threshold = .755
        _,max_val,_,_ = cv.minMaxLoc(result)
        print(f'{max_val}')
        if max_val >= threshold:
            
            cropped_team = frame[152:555, 821:895]
            if saved_team is None or not np.array_equal(cropped_team, saved_team):
                cv.imwrite("Opponent_team.png", cropped_team)
                saved_team = cropped_team.copy()
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
    read_video()