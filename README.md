# Food-Specific Go/No-Go Task

## Overview

This repository contains a PsychoPy adaptation of a Go/No-Go protocol initially based on Price et al. (2016) regarding food-specific response inhibition. This specific version has been modified for use in an anorexia nervosa intervention context.

The task measures a participant's ability to inhibit their response to specific food images (High Fat vs. Low Fat).

## Task Protocol

The experimental flow is structured as follows:

* **Initialization:** The researcher enters the participant's number and age via a dialog box.
* **Instructions:** Participants are presented with an instruction screen explaining the cues.
* **Trial Sequence:**
1. **Fixation:** A fixation cross (`+`) appears for 500 ms.
2. **Stimulus:** A food image appears for up to 750 ms alongside a specific visual cue.
3. **Response:** * **Go Trial (Low Fat / `fat == 0`):** A green **"O"** is displayed. The participant must press the **SPACEBAR** as quickly as possible.
* **No-Go Trial (High Fat / `fat == 1`):** A red **"X"** is displayed. The participant must withhold their response (do not press anything).




* **Exit:** Participants can press the **ESCAPE** key at any time during the stimulus presentation to abort the task.

## Prerequisites & Dependencies

Ensure you have Python installed along with the following libraries:

* `psychopy`
* `pandas`

You can install the required packages using pip:

```bash
pip install psychopy pandas

```

## Setup & File Structure

**Important:** This script currently relies on absolute file paths. Before running the experiment on a new machine, you must update the following paths in the script to match your local directory structure:

1. **Stimulus List:** Update the `f_list` variable to point to your condition CSV file.
```python
f_list = "C:/path/to/your/HF_LF_60.csv"

```


2. **Image Directory:** Update the `path` variable within the trial loop to point to your image folder.
```python
path = "C:/path/to/your/stimuli_folder/" + trial.food

```



### Required CSV Format (`HF_LF_60.csv`)

The script expects a CSV file containing at least the following two columns:

* `food`: The exact filename of the image (e.g., `apple.jpg`).
* `fat`: A binary indicator where `0` represents Low Fat (Go) and `1` represents High Fat (No-Go).

## Output Data

Upon completion (or if the script successfully runs through the trial loop), the program will generate a CSV file named `<participant_nr>_gonogo.csv` in the current working directory.

The output file logs the original stimulus data alongside the participant's performance metrics:

* **`response`**: Whether the participant pressed the spacebar (`press`) or not (`no_press`).
* **`rt`**: Reaction time in seconds (recorded as `NA` if no response was made).
* **`trial_type`**: The condition of the trial (`go` or `nogo`).
* **`accuracy`**: Scored as `1` (correct) or `0` (incorrect).
* **`error_type`**:
* `none`: Correct response.
* `omission`: Failed to press the spacebar during a Go trial.
* `commission`: Incorrectly pressed the spacebar during a No-Go trial.
