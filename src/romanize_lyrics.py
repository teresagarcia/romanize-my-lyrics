# -*- coding: utf-8 -*-

import sys

from mykoreanromanizer import Romanizer

input_file = sys.argv[1]
r = Romanizer()
output_file = "data/romanized/romanization.txt"
final_text = ""

with open(input_file, 'r', encoding="utf-8") as reader:
    for line in reader.readlines():
        final_text += line + r.romanize(line) + "\n"

with open(output_file, 'w', encoding="utf-8") as writer:
    writer.writelines(final_text)

print(frase)