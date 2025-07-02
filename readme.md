<h1> Pokemon Stream Aid</h1>
A tool created using Python's opencv library to be used when streaming or recording gameplay of Pokemon Scarlet/Violet to update overlays tracking opponent's team and win/loss record

<h2>Setup </h2>
This program has been tested to work with both the Switch and Switch 2. In order to make it work on both, there is some inital setup that needs to be done. 

- Install Python from [here](https://www.python.org/downloads/)
- Once installed, install opencv using the command `pip install opencv-python`
- If you play the game in English or play in another language but do not care about the win/loss ratio, you are done and you can ignore this step
    - change line 16 to say `win_image = os.getcwd() + r'\photos\win_japan.png'` in order to have it track win/loss record correctly if you play in Japanese

<h3> OBS Setup </h3>
This setup has only been tested on OBS Studio, which you can download <a href = "https://obsproject.com/download"> here </a>

- Once downloaded, setup a scene that is just your capture card and fit to screen
    - For most capture cards, click Add Source and it will be under Video Capture Device
    - If this doesn't work, refer to the manual of your capture card
- Set up a virtual camera that captures this scene.
- Create another scene that has the `opponent_team.png` and the `record.txt` if you want to display these during a recording/livestream

  

Run the file as `python obsplugin.py` and it should be up and running.

<h2> Troubleshooting </h2>

**A video isnt appearing/ the wrong video is appearing  on my feed**  
If you are experiencing this issue, this is normal behavior. In order to fix this, change `file_path = 1` to a different value until the video appears.  
For example, if you have one webcam attached, the value will be `2` because 0 is your default webcam, 1 will be the capture card itself which will not work due to both programs attempting to access the same camera, 2 will be the virtual camera. Most of the time, the values correspond with the order they were plugged into your computer.  
I am currently looking into ways to make this easier than manually changing the value.
