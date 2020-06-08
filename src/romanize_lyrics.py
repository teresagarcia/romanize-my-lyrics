# -*- coding: utf-8 -*-

import sys
import re

from mykoreanromanizer import Romanizer

input_file = sys.argv[1]
r = Romanizer()
output_file = input_file.replace("original", "romanized")
final_text = ""

with open(input_file, 'r', encoding="utf-8") as reader:
    for line in reader.readlines():
        clean_line = line.rstrip()
        rom_line = r.romanize(clean_line)
        rom_line = rom_line[:1].upper() + rom_line[1:]
        final_text += clean_line + "\n" + rom_line + "\n\n"

with open(output_file, 'w', encoding="utf-8") as writer:
    writer.writelines(final_text)