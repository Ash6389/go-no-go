import pandas as pd
from psychopy.gui import DlgFromDict
from psychopy.visual import Window, TextStim, ImageStim, Rect, TextBox, DotStim
from psychopy.core import Clock, quit, wait
from psychopy.event import Mouse
from psychopy.hardware.keyboard import Keyboard
from psychopy import event, data
import random

exp_info = {'participant_nr': '', 'age': '21'}
dlg = DlgFromDict(exp_info)

p_name= exp_info['participant_nr']

# Initialize a fullscreen window with my monitor (HD format) size
# and my monitor specification called "samsung" from the monitor center
win = Window(size=(1200, 800), fullscr=False)

# ----------------------------------------------------------------------
# 1. ADDED INSTRUCTIONS HERE
# ----------------------------------------------------------------------
instr_text = (
    "Welcome to the task!\n\n"
    "On each trial, you will see an image of food.\n"
    "If you see a green 'O' (GO), press the SPACEBAR as fast as possible.\n"
    "If you see a red 'X' (NO-GO), DO NOT press any key.\n\n"
    "Press the SPACEBAR to begin."
)
instructions = TextStim(win, text=instr_text, wrapWidth=1.5, height=0.08)
instructions.draw()
win.flip()
event.waitKeys(keyList=['space'])
# ----------------------------------------------------------------------

# Also initialize a mouse, although we're not going to use it
mouse = Mouse(visible=False)

# Initialize a (global) clock
clock = Clock()
f_list = f"C:/Users/cl157/OneDrive/Desktop/coding/lecture 7/HF_LF_60.csv"
foods = pd.read_csv(f_list)
hf = foods[foods['fat']==1]
lf = foods[foods['fat']==0]
lf = lf.sample(frac=0.4)
hf = hf.sample(frac=0.4)
trial_foods=pd.concat([lf,lf,lf,lf,hf])
trial_foods = trial_foods.sample(frac=1)
kb=Keyboard()

for i in range(0,len(trial_foods)):
    trial=trial_foods.iloc[i]
    print(trial)
    t=TextStim(win,"+")
    t.draw()
    win.flip()
    wait(0.5)
    path = "C:/Users/cl157/OneDrive/Desktop/coding/lecture 7/Food-Choice-Task-main/Food-Choice-Task-main/stimuli/" + trial.food
    print(trial.fat)
    
    # ------------------------------------------------------------------
    # 2. ADDED GO/NO-GO CUES HERE
    # ------------------------------------------------------------------
    if trial.fat==1:
        trial_type = "nogo"
        cue = TextStim(win, text="X", color="red", pos=(0, 0.4), height=0.2)
    else: 
        trial_type = "go" # Fixed 'rtial_type' typo
        cue = TextStim(win, text="O", color="green", pos=(0, 0.4), height=0.2)
    # ------------------------------------------------------------------
        
    im=ImageStim(win, path)
    
    t_clock=Clock()
    response = "no_press"
    rt="NA"
    while t_clock.getTime() < .75:
        im.draw()
        cue.draw() # <-- Draw the cue alongside the image
        win.flip()
        keys = kb.getKeys(['space','escape'], waitRelease=False)
        if keys:
            resp = keys[0].name
            rt = keys[0].rt
            if resp == 'escape':
                win.close()
                quit()
            elif resp == 'space':
                response = "press"
                rt = t_clock.getTime()
                break
                
    # ------------------------------------------------------------------
    # NOTE: Indentation fixed below so scoring & saving occurs PER trial
    # ------------------------------------------------------------------
    # score go/nogo performance
    if trial_type == "go" and response == "press":
        accuracy = 1
        error_type = "none"
    elif trial_type == "go" and response == "no_press":
        accuracy = 0
        error_type = "omission"
    elif trial_type == "nogo" and response == "no_press":
        accuracy = 1
        error_type = "none"
    elif trial_type == "nogo" and response == "press":
        accuracy = 0
        error_type = "commission"
            
    win.flip()
    wait(.5)
    
    # save current trial data (Fixed rtial_foods typo)
    trial_foods.loc[i, 'response'] = response
    trial_foods.loc[i, 'rt'] = rt
    trial_foods.loc[i, 'trial_type'] = trial_type
    trial_foods.loc[i, 'accuracy'] = accuracy
    trial_foods.loc[i, 'error_type'] = error_type
    
# Fixed save method from trials.save() to trial_foods.to_csv()
trial_foods.to_csv(f"{p_name}_gonogo.csv")
