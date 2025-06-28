#!/usr/bin/env python3
import re
import sys
from pathlib import Path
import pysubs2
from fugashi import Tagger
import unidic_lite

palette = [
    "&HFFFFFF&",
    "&HCCFFFF&",
    "&HCCFFCC&",
    "&HFFFFCC&",
    "&HFFCCCC&",
    "&HFFCCFF&",
    "&HCCE5FF&",
    "&HCCFFFF&",
    "&HFFD8B1&",
    "&HCCE0FF&",
    "&HFFFFE0&",
    "&HFFF0F5&",
    "&HFFE4E1&",
    "&HFAFAD2&",
    "&HFFFACD&",
    "&HFFEFD5&",
    "&HFFFFF0&",
    "&HFFF5EE&",
    "&HFAEBD7&",
    "&HFFFAFA&",
]

special_tokens = {"\\N", "\\n", "\\h"}

re_token = re.compile(r"{[^}]*}|\\\w|\s+|\w+|[^\w\s]")

def tokenize_en(text: str):
    return re_token.findall(text)

tagger = Tagger(f'-d {unidic_lite.DICDIR}')

# Japanese tokenization preserving ASS control and newlines

def tokenize_ja(text: str):
    tokens = []
    i = 0
    while i < len(text):
        if text[i] == "{" :
            j = text.find("}", i)
            if j != -1:
                tokens.append(text[i:j+1])
                i = j + 1
                continue
        if text.startswith("\\N", i) or text.startswith("\\n", i) or text.startswith("\\h", i):
            tokens.append(text[i:i+2])
            i += 2
            continue
        j = i
        while j < len(text) and not text[j] in "{" and not text.startswith("\\N", j) and not text.startswith("\\n", j) and not text.startswith("\\h", j):
            j += 1
        segment = text[i:j]
        for t in tagger(segment):
            tokens.append(t.surface)
        i = j
    return tokens


def is_special(tok: str) -> bool:
    return tok.strip() == "" or tok in special_tokens or (tok.startswith("{") and tok.endswith("}"))


def apply_colors(en_tokens, ja_tokens):
    idx = 0
    i = j = 0
    while i < len(en_tokens) or j < len(ja_tokens):
        while i < len(en_tokens) and is_special(en_tokens[i]):
            i += 1
        while j < len(ja_tokens) and is_special(ja_tokens[j]):
            j += 1
        if i >= len(en_tokens) and j >= len(ja_tokens):
            break
        color = palette[idx % len(palette)]
        if i < len(en_tokens):
            en_tokens[i] = f"{{\\c{color}}}" + en_tokens[i] + f"{{\\c{color}}}"
            i += 1
        if j < len(ja_tokens):
            ja_tokens[j] = f"{{\\c{color}}}" + ja_tokens[j] + f"{{\\c{color}}}"
            j += 1
        idx += 1


def main(path):
    subs = pysubs2.load(str(path))
    events = subs.events
    i = 0
    while i < len(events) - 1:
        ev1 = events[i]
        ev2 = events[i+1]
        if ev1.style == "Default" and ev2.style == "Default-ja":
            en_tokens = tokenize_en(ev1.text)
            ja_tokens = tokenize_ja(ev2.text)
            apply_colors(en_tokens, ja_tokens)
            ev1.text = "".join(en_tokens)
            ev2.text = "".join(ja_tokens)
            i += 2
        elif ev1.style == "Default-ja" and ev2.style == "Default":
            ja_tokens = tokenize_ja(ev1.text)
            en_tokens = tokenize_en(ev2.text)
            apply_colors(en_tokens, ja_tokens)
            ev1.text = "".join(ja_tokens)
            ev2.text = "".join(en_tokens)
            i += 2
        else:
            i += 1
    subs.save(str(path))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: colorize.py path_to_ass", file=sys.stderr)
        sys.exit(1)
    main(Path(sys.argv[1]))
