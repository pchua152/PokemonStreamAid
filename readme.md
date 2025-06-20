<h1> Pokemon Stream Aid</h1>
A tool created using Python's opencv library to be used when streaming or recording gameplay of Pokemon Scarlet/Violet to update overlays tracking opponent's team and win/loss record

<h2> Inital setup </h2>
This program has been tested to work with both the Switch and Switch 2. In order to make it work on both, there is some inital setup that needs to be done. 
You must first verify that your console is outputting at a resolution of 720 x 1280p. This can be verified in the settings under Display. Below is a picture of the settings from a Switch 2:
![Image of Settings]![IMG_2748](https://github.com/user-attachments/assets/1c5e599d-92df-459a-9b70-af2c641e47bd)

Once that is setup on the Switch, there are some steps that need to be done on your computer.
- Install Python from [here](https://www.python.org/downloads/)
- Once installed, install opencv using the command `pip install opencv-python`
- In the file obsplugin.py, the default value for video path is set to `1`, if you do have a webcam attached to your computer this will work fine if your capture card is the only other device attached. If there is another device, change this value to `0` instead
- If you play the game in English or play in another language but do not care about the win/loss ratio, you are done and you can ignore this step
    - change line 16 to say `win_image = os.getcwd() + r'\photos\win_japan.png'` in order to have it track win/loss record correctly if you play in Japanese

Run the file as `python obsplugin.py` and it should be up and running.
