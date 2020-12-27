# -*- coding: utf-8 -*-
import os 
import sys
import glob
import random
import subprocess
import numpy as np
from PIL import Image, ImageDraw, ImageFont

fontFile = 'Yas.ttf'
dir_path = os.path.dirname(os.path.realpath(__file__))
# im = Image.open("target.jpg")
im = None
draw = None

colors = [
    # "#05b4ff", # blue
    "#ffb22e",
    "#ef3c38",
    "#fbf018",
    "#f53b3c",
    # "#05b4ff", # blue
    "#cbf11f",
    "#1b3c9d",
    "#ff6117",
    "#93ce34",
    "#c6e420",
    "#fec337",
    "#fcc73d",
    "#05b4ff",
    "#23c244",
]
