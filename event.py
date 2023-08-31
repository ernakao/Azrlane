import util_gui
from PIL import Image
import glob
import os
import time
import cv2
import numpy as np
import pandas as pd

#Codigo para o evento atual
#Falta o caso em que acabam os 15 daily tries -> Precisa pegar o "ticket bonus"
path_imgs = os.getcwd()
img_retry = Image.open(os.path.join(path_imgs,'retry.png'))
img_tap_to_continue = Image.open(os.path.join(path_imgs,'tap_to_continue.png'))
img_touch_to_continue = Image.open(os.path.join(path_imgs,'touch_to_continue.png'))
img_affinity = Image.open(os.path.join(path_imgs,'affinity.png'))

oil_base_cost = 41
oil_spent = 1000
iterations_run = oil_spent//oil_base_cost
contador = time.time()

while(iterations_run):
    time.sleep(48)
    while(not util_gui.bool_img(img_affinity)):
        bool_touch = util_gui.bool_img(img_touch_to_continue)
        time.sleep(1)
        if(bool_touch):
            iterations_run -= 1
            print("Tempo decorrido: {}s \n".format(time.time() - contador))
            contador = time.time()
            util_gui.click(img_touch_to_continue)
            util_gui.click(img_tap_to_continue)
            util_gui.click(img_retry)
            break