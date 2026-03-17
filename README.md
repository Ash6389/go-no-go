# go-no-go

## Overview
This project is a PsychoPy-based **Go/No-Go task** adapted from Price et al. (2016), originally designed to study **food-specific response inhibition**. In this version, participants see food images and must either press a key quickly during **Go trials** or withhold their response during **No-Go trials**.

The current script appears to be modified for a possible **anorexia nervosa intervention context**, where food categories are used to define Go versus No-Go trials.

## Task Design
Each trial includes three stages:

1. **Fixation cross** for 500 ms  
2. **Food image presentation** for 750 ms  
3. **Blank screen** for 500 ms  

Participants respond using the **space bar**:
- **Go trial**: press the space bar as quickly as possible
- **No-Go trial**: do not press any key

The **Escape** key can be used to quit the experiment early.

## Stimuli
The task uses food images listed in a CSV file. The script reads a food list and separates items into two groups based on the `fat` column:

- `fat == 0`: treated as **Go** stimuli
- `fat == 1`: treated as **No-Go** stimuli

The script currently samples and combines these items to create the trial sequence.

## Input Files
The script expects:

- A CSV file containing food stimulus information  
  Example in the script:  
  `HF_LF_60.csv`

- A folder containing food image files  
  Example in the script:  
  `stimuli/`

The CSV file should include at least:
- `food`: image filename
- `fat`: trial category code

## Software Requirements
- Python 3
- PsychoPy
- pandas

Possible imports used in the script:
- `pandas`
- `psychopy.gui`
- `psychopy.visual`
- `psychopy.core`
- `psychopy.event`
- `psychopy.hardware.keyboard`
- `psychopy.data`

## Procedure
When the script starts:

1. A dialog box asks for participant information.
2. A PsychoPy window opens.
3. Food stimuli are loaded from the CSV file.
4. Trials are generated and randomized.
5. On each trial:
   - a fixation cross is shown
   - a food image is displayed
   - keyboard response is recorded
6. Accuracy is classified as:
   - **correct Go response**
   - **omission error** on Go trials
   - **correct No-Go withholding**
   - **commission error** on No-Go trials

## Output
The intended output is a participant-level CSV file:

`[participant_id]_gonogo.csv`

The saved data are intended to include:
- trial type
- response
- reaction time
- accuracy
- error type

## Citation
This task is adapted from:

Price, M., Lee, M., & Higgs, S. (2016). *Food-specific response inhibition, dietary restraint and snack intake in lean and overweight/obese adults.*
