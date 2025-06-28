# Command Reference

## colorize.py

Usage: `scripts/colorize.py <subtitle.ass>`

Applies sequential light color tags to paired English and Japanese subtitle lines.
Requires `pysubs2` and `fugashi`; the script automatically loads the `unidic-lite` dictionary.
Words are tokenized and wrapped with identical colors across each pair.
