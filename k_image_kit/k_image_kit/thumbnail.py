#!/usr/bin/env python3
# -*-coding:UTF-8 -*

import os, sys
from PIL import Image

THUM_SIZE = (128, 128)
THUM_EXT = "jpeg"

if len(sys.argv) == 1:
    print("No file to transform to thumbnail:")
    exit(1)
    
for infile in sys.argv[1:]:
    outfile = os.path.splitext(infile)[0] + ".thumbnail"
    
    try:
        with Image.open(infile) as im:
            im.thumbnail(THUM_SIZE)
            im.save(outfile, THUM_EXT)
            
        print(f"The image'{infile}' has been successfully transformed to a thumbnail!")
    except FileNotFoundError as e:
        print(f"!The image '{infile}' hasn't been found in the given location!")
    

input("Press 'Enter' to quit.")