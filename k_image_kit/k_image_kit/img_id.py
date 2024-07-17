#!/usr/bin/env python3
# -*-coding:UTF-8 -*

import sys
from PIL import Image

if len(sys.argv) == 1:
    print("!No given image!")
    exit(1)
    
for infile in sys.argv[1:]:
    try:
        with Image.open(infile) as img:
            print(f"Image Information:",
                f"\tPath: {infile}",
                f"\tFormat: {img.format}",
                f"\tSize: {img.size}",
                f"\tMode: {img.mode}",
                sep="\n")
    except FileNotFoundError as e:
        print(f"!The image '{infile}' hasn't been found in the given location!")
    

input("Press 'Enter' to quit.")