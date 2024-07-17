#!/usr/bin/env python3
# -*-coding:UTF-8 -*

import os, sys
from PIL import Image

EXTS = {"png", "jpg"}
GOOD_FORMAT = f"python [path to conv_img_form.py] to [{' or '.join(EXTS)}] [path to image 1] ... [path to image n]"


if sys.argv[1] != "to":
    print(f"!'to' didn't appear in your command. The good format is: '{GOOD_FORMAT}'!")
    exit(1)
    
if sys.argv[2] not in EXTS:
    print(f"!The destination format must be in {EXTS}!")
    exit(2)
    
if len(sys.argv) == 3:
    print(f"!No given image for format conversion!")
    exit(3)
    
dest_ext = sys.argv[2]

    
for infile in sys.argv[3:]:
    file, ext = os.path.splitext(infile)
    
    if dest_ext != ext:
        try:
            with Image.open(infile) as im:
                if im.mode != 'RGB':
                    im = im.convert('RGB')
                im.save(f"{file}.{dest_ext}")
                
            print(f"The image'{infile}' has been successfully converted to the format '{dest_ext}'!")
        except FileNotFoundError as e:
            print(f"!The image '{infile}' hasn't been found in the given location!")
    

input(f"Press 'Enter' to quit.")