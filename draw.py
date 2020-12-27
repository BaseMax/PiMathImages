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
