##go no go

#Hi, I’m trying to adapt a GO/NOGO protocol from Price et al., 2016. Food-specific response inhibition,
#dietary restraint and snack intake in lean and overweight/obese adults.
#The task consists in 50 trials (40 go and 10 no-go). During go trials the 
#subject should press a key as fast as possible. During no-go trials, no key should be pressed. 
#Each trial is composed by an image presented for 750ms and was separated by a blank screen for 500 ms 
#and preceded by a fixation cross for 500 ms. The sequence of go/nogo stimuli are predetermined. 
#Two set of images are used: 10 go images (each one is presented 4 times) and 10 no-go images 
#(each one is presented one time). Image order should be randomized across subjects.
# we are going to change for anorexia nervosa intervention

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
    if trial.fat==1:
        trial_type = "nogo"
    else: 
        rtial_type = "go"
    im=ImageStim(win, path)
    
    
    t_clock=Clock()
    response = "no_press"
    rt="NA"
    while t_clock.getTime() < .75:
        im.draw()
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
trial_foods['response']=response
trial_foods['rt']= rt
rtial_foods['correct_response'] = correct
    
 # save current trial data
trial_foods.loc[i, 'trial_type'] = trial_type
trial_foods.loc[i, 'response'] = response
trial_foods.loc[i, 'rt'] = rt
trial_foods.loc[i, 'accuracy'] = accuracy
trial_foods.loc[i, 'error_type'] = error_type
    
trials.save(f"{p_name}_gonogo.csv")

## tasks
# 1. figure out what is happening in the task & add instructions
# 2. we need to add go-nogo! How would we do that?

    
