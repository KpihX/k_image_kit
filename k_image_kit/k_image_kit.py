#!/usr/bin/env python3
# -*-coding:UTF-8 -*

import os, sys

from PIL import Image, ImageSequence
from k_general_kit.gen_func import bye

""" Constant(s)"""

FRAMES_FORMATS = ["GIF"]
  
""" Functions """

def conv_comp(src_path, dest_fold_path="", result_name="", format="JPEG", quality=80):
    if dest_fold_path == "":
        dest_fold_path = os.path.split(src_path)

    if result_name == "":
        result_name = os.path.splitext(os.path.basename(src_path))[0] + "_conv"
        if quality < 100:
            result_name += "_comp"
            
    with Image.open(src_path) as img:
        if img.mode != "RGB":
            img = img.convert("RGB")
        img.save(f"{dest_fold_path}/{result_name}.{format.lower()}", format.upper(), optimize=True, quality=quality)
  
def merge_x(img1:Image.Image, img2:Image.Image)-> Image.Image:
    w = img1.size[0] + img2.size[0]
    h = max(img1.size[1], img2.size[1])
    img = Image.new("RGBA", (w, h))
    
    img.paste(img1)
    img.paste(img2, (img1.size[0], 0))
    
    return img

def merge_y(img1:Image.Image, img2:Image.Image)-> Image.Image:
    w = max(img1.size[0], img2.size[0])
    h = img1.size[1] + img2.size[1]
    img = Image.new("RGBA", (w, h))
    
    img.paste(img1)
    img.paste(img2, (0, img1.size[1]))
    
    return img

def roll(img:Image.Image, delta)-> Image.Image:
    """Roll an image sideways"""
    xsize, ysize = img.size
    
    delta = delta % xsize
    img_result = img.copy()
    if delta == 0:
        return img_result
    
    part1 = img.crop((0, 0, delta, ysize))
    part2 = img.crop((delta, 0, xsize, ysize))
    img_result.paste(part1, (xsize-delta, 0, xsize, ysize))
    img_result.paste(part2, (0, 0, xsize-delta, ysize))
    
    return img_result

def split_frames(img:Image.Image):
    assert img.format() in FRAMES_FORMATS, f"!The image format must be in {FRAMES_FORMATS}!"

    return ImageSequence.Iterator(img)

def details(img:Image.Image):
    return f"Format: {img.format}, Size: {img.size}, Mode: {img.mode}",


OPERATIONS = {"h": "Help", "fc": "Format Conversion", "c":"Compression", "fcc":"Format Conversion & Compression", "hm": "Horizontal Merging", "vm":"Vertical Merging", "r":"Rolling", "caif":"Conversion Animated Image to Frames", "cfai":"Conversion Frames to Animated Image"} 

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("Choose an operation (Enter just the corresponding code before the operation): ")
        for code, operation in OPERATIONS.items():
            print(f"\t{code}: {operation}", file=sys.stderr)
        
        while True:
            code =input("\nYour choice (An empty input stop the program)! ")
            if code == "":
                bye()
            if code not in OPERATIONS.keys():
                print("\n!You didn't enter a valid code amongst the ones proposed!", file=sys.stderr)
                continue
            break
    else:
        if sys.argv[1] not in OPERATIONS.keys():
            print(f"!Yon didn't enter a valid operation code.\nThe codes are defined as follow: {OPERATIONS}!", file=sys.stderr)
            bye()
        code = sys.argv[1]
            
    if code == "h":
        import k_image_kit.k_image_kit as k_image_kit
        print(help(k_image_kit))
    
    