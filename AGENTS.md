# LLM Agent: Japanese Subtitle Colorizer

## Current task

* TODO `Higurashi no Naku Koro ni/Season 01/TODO.md`
* Subtitles `Higurashi no Naku Koro ni/Season 01/*.ass`

## Overview

This agent parses TODO.md for unchecked `.ass` subtitle files, processes exactly **one** file per run, highlights matching Japanese ↔ English word pairs in unique inline colors, saves the modified subtitle file, then marks that item as done.

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
* The scoped TODO.md is always placed to the folder with the conenten to process. Always consult the TODO file in the current
  task folder to see what was done and what needs to be done. 

## Chunk-Processing Rules

* Work in mini-tasks of 2 – 4 lines when words are dense, or up to 10 lines when structure is simple
* Never process beyond the current chunk until it is fully colorized and saved in memory
* Continue chunk by chunk until the file ends
* Abort the run if an unexpected format error is detected and log the problem instead of guessing

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

## End of agents.md
