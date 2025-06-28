# LLM Agent: Japanese Subtitle Colorizer

## Current task

* TODO `Higurashi no Naku Koro ni/Season 01/TODO.md`
* Subtitles `Higurashi no Naku Koro ni/Season 01/*.ass`

## Overview

This agent parses TODO.md for unchecked `.ass` subtitle files, processes exactly **one** file per run, highlights matching Japanese ↔ English word pairs in unique inline colors, saves the modified subtitle file, then marks that item as done.

## AGENT: use your japanese knowledge to create content
Use your best judgment and japanese knowledge that you have to complete the task.
if necessary, download dictionaries or other tools. The result may not be precise.



## .ASS Special Tokens

For your information:

Here is a list of special tokens in the Advanced SubStation Alpha (ASS) subtitle format, specifically focusing on `\N` and similar text formatting tokens:

- `\N` — Hard line break (new line). It forces a new line within the same subtitle event.
- `\n` — Soft line break. Its effect depends on the subtitle renderer but usually treated similarly to `\N` in most cases.
- `\h` — Non-breaking space (prevents line wrapping at that space).

These tokens must be processed as special tokens, no need to highlight them. 



## Use previous examples

Use TODO.md for the current task. I you are unsure how to implement the task, consult with the already completed work. There is always room for improvement, and you can always make the work better than it was done before, do not limit yourself, and check what was done before and what was already approved to continue with your current task. 



## Responsibilities

* Read TODO.md and locate the first line that starts with `- [ ]`
* Load that subtitle file from the repository path
* Work through the file in chunks of up to ten dialogue lines
* Within each chunk identify Japanese words and their English translations that appear in the same relative position
* Apply identical inline color tags to each matching pair using the style palettes in **Styles Reference**
* Ensure every dialogue line in the file uses a distinct color not reused elsewhere in that file
* Keep all original text, timing, and formatting; add only color and optional style tags
* After the final chunk write the updated file back to disk
* Update TODO.md by replacing the box with `- [x]` for that filename
* End the run; do not touch additional files

## TODOs
* The scoped TODO.md is always placed to the folder with the content to process. Always consult the TODO file in the current
  task folder to see what was done and what needs to be done. 

## Chunk-Processing Rules

* Work in mini-tasks of 2 – 4 lines when words are dense, or up to 10 lines when structure is simple
* Never process beyond the current chunk until it is fully colorized and saved in memory
* Continue chunk by chunk until the file ends
* Abort the run if an unexpected format error is detected and log the problem instead of guessing
* Avoid highlighting solo punctuation symbols, like ".", quotes, commas, "!". Make sure group punctuation with neighbor word.  
* Make sure if  the words logically needs to be grouped together -- group them together and highlight with same color. 

## Styles Reference

### 20 high-contrast light colors (primary palette)

```
{\c&HFFFFFF&}White
{\c&HCCFFFF&}Pale Cyan
{\c&HCCFFCC&}Pale Green
{\c&HFFFFCC&}Pale Yellow
{\c&HFFCCCC&}Pale Pink
{\c&HFFCCFF&}Pale Magenta
{\c&HCCE5FF&}Light Sky Blue
{\c&HCCFFFF&}Light Aqua
{\c&HFFD8B1&}Peach
{\c&HCCE0FF&}Light Lavender Blue
{\c&HFFFFE0&}Light Light Yellow
{\c&HFFF0F5&}Lavender Blush
{\c&HFFE4E1&}Misty Rose
{\c&HFAFAD2&}Light Goldenrod Yellow
{\c&HFFFACD&}Lemon Chiffon
{\c&HFFEFD5&}Papaya Whip
{\c&HFFFFF0&}Ivory
{\c&HFFF5EE&}Seashell
{\c&HFAEBD7&}Antique White
{\c&HFFFAFA&}Snow
```

### 15 preset combinations (weight + outline + color)

```
{\b1\bord2\c&HFFFFFF&}Bold white outline
{\b0\bord2\c&HCCFFFF&}Cyan outline
{\b1\bord1\c&HCCFFCC&}Bold green thin
{\b0\bord3\c&HFFFFCC&}Yellow thick
{\b1\bord2\c&HFFCCCC&}Bold pink medium
{\b0\bord1\c&HFFCCFF&}Magenta thin
{\b1\bord2\c&HCCE5FF&}Bold sky medium
{\b0\bord1\c&HFFD8B1&}Peach thin
{\b1\bord3\c&HCCE0FF&}Bold lavender thick
{\b0\bord2\c&HFFF0F5&}Blush medium
{\b1\bord1\c&HFFE4E1&}Bold misty thin
{\b0\bord2\c&HFAFAD2&}Goldenrod medium
{\b1\bord3\c&HFFFACD&}Bold lemon thick
{\b0\bord1\c&HFFEFD5&}Papaya thin
{\b1\bord2\c&HFFFFF0&}Bold ivory medium
```

## Workflow

* Step 1 Read `TODO.md`
* Step 2 Select the first unchecked subtitle file
* Step 3 Load the file content into memory
* Step 4 Iterate through the dialogue events in chunks (≤ 10 lines)
* Step 5 For each chunk highlight matching Japanese-English word pairs with a unique color from the palette
* Step 6 Write the modified chunk back to the in-memory file text
* Step 7 After final chunk save the updated `.ass` file, preserving original encoding and line order
* Step 8 Replace `- [ ]` with `- [x]` for that file in TODO.md
* Step 9 Exit

## Failure Handling

* If a file cannot be opened log the filename and skip processing
* If a line does not conform to expected `Dialogue:` format keep the line unchanged and continue
* If insufficient unique colors remain in the palette raise an error and abort gracefully

## Update Tracking

* Every successful run commits two changes only: the updated subtitle file and TODO.md
* Never modify any other repository files automatically

## Notes on User Instructions

* Obey the flat bullet structure; do not create nested lists
* Preserve personal directives: professional tone, ASCII punctuation, no extraneous comments
* Do not close code fences inside subtitle output sessions when the user explicitly instructs not to

## Example output in file
```
Dialogue: 0,0:00:00.50,0:00:03.46,Default,,0,0,0,,You {\c&H33CCFF&}heard{\c&H33CCFF&} that {\c&H66FF66&}already{\c&H66FF66&}?
Dialogue: 0,0:00:00.52,0:00:03.59,Default-ja,,0,0,0,,（大石）しかし {\c&H33CCFF&}耳{\c&H33CCFF&}が {\c&H66FF66&}早い{\c&H66FF66&}なぁ

Dialogue: 0,0:00:05.66,0:00:09.47,Default-ja,,0,0,0,,（大石） 私は {\c&HFF99CC&}悟史(さとし)君{\c&HFF99CC&}が {\c&HFF6666&}犯人{\c&HFF6666&}の一点読みでしたからね
Dialogue: 0,0:00:05.70,0:00:09.30,Default,,0,0,0,,I was quite sure that {\c&HFF99CC&}Satoshi-kun{\c&HFF99CC&} was the {\c&HFF6666&}suspect{\c&HFF6666&}.

Dialogue: 0,0:00:09.80,0:00:13.87,Default-ja,,0,0,0,,（詩音）{\c&H99FFFF&}聞かせてください{\c&H99FFFF&} {\c&H33FFFF&}真犯人{\c&H33FFFF&}って {\c&HFFCC66&}一体{\c&HFFCC66&}{\c&HFFCC99&}何者{\c&HFFCC99&}です？
Dialogue: 0,0:00:09.87,0:00:14.04,Default,,0,0,0,,{\c&H99FFFF&}Please tell me{\c&H99FFFF&}. {\c&HFFCC99&}Who{\c&HFFCC99&} {\c&HFFCC66&}exactly{\c&HFFCC66&} is the {\c&H33FFFF&}true suspect{\c&H33FFFF&}?

Dialogue: 0,0:00:14.67,0:00:16.64,Default-ja,,0,0,0,,{\c&H66FFFF&}異常者{\c&H66FFFF&}とか聞きましたけど
Dialogue: 0,0:00:14.68,0:00:16.54,Default,,0,0,0,,I heard he’s {\c&H66FFFF&}abnormal{\c&H66FFFF&}.

```
## The Goal

I edit the subtitle file so the Japanese line and the English line appear together, and I color-code each matching word pair. For example, the word 耳 and its translation “heard” both get the same blue tag. When I watch the episode, I can glance at the colors and instantly see which words match without stopping the video.
The `.ass` format lets me place those color tags directly inside the subtitle text, so the timing and layout stay unchanged. I work in small chunks of ten lines or fewer, add colors, save the file, and mark that episode as done in my to-do list.
By re-using a light, high-contrast palette across the whole episode, each color becomes a mini flashcard. Seeing the same hue pop up again reinforces the meaning, and over time I start recalling the Japanese word the moment I see its color. Watching anime turns into a live vocabulary drill that is fun and natural.
This is my design.



## The requirement to automate routine repetitive commands. Secondary objective

Read manual at:
- scripts/task_scoped_command_wrappers_manual_index.md
- scripts/task_scoped_bash_command_wrappers_manual.md
- scripts/task_scoped_powershell_command_wrappers_manual.md
- scripts/task_scoped_python_command_wrappers_manual.md

Use your best judgement when you see a need to create a new script for repetitive command that you use. 

Extend the existing scripts or create new scripts in the folder `scripts/`

For the quick reference, maintain the file `scripts/commands.md` which will have detailed description and purpose, good categorization of commands you have added. 

Use your best judgment when editing and managing these commands. Make sure to keep `scripts/commands.md` always up to date. 



when you see any issues, record and describe them briefly, but with all essential information in `scripts/commands_issues.md` this could be a misuse or intermittent issue. Maybe you don't have full context to fix it now, so just record your observations there, this will allow to fix the issue later. this is a backlog! when issue is fixed, make sure to update  `scripts/commands_issues.md` . add short note if existing issue is persistent and repeat. Again, this is your secondary objective, if you cannot fix the issue now, record  your observation for later. Feel free to edit or even remove or replace content in `scripts/`  folder. I grant you full ownership over the content there, please use your best judgement. 



Please note, this is very desired, but secondary and optional objective. 