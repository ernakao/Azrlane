#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pyautogui as gui
import numpy as np
import pandas as pd
import os

confidence_imagem = 0.8
gui.PAUSE = 0.1
df_image = pd.read_csv(os.path.join(os.getcwd(),r"CSVs\data_images.csv"),index_col = 'Unnamed: 0')


def bool_img(imagem,region_imagem = None):
    return (0 if gui.locateCenterOnScreen(imagem,confidence = confidence_imagem,region = region_imagem) is None else 1)

#Locates image coordinates on screen
def locate_image(imagem,nome_imagem):
    while(gui.locateOnScreen(imagem,confidence = confidence_imagem) is None):
        continue
    [x,y,w,h] = gui.locateOnScreen(imagem,confidence = confidence_imagem)
    [x,y,w,h] = [0 if i < 0 else i for i in [x-10,y-10,w+10,h+10]]
    df_image.at[nome_imagem,'Region'] = (x,y,w,h)
    df_image.to_csv(os.path.join(os.getcwd(),r"CSVs\data_images.csv"))
    return [x,y,w,h]
    
#Funcao Auxiliar - Click(str nome_imagem)
def click_region(imagem,nome_imagem):
    region_imagem = df_image['Region'][nome_imagem] 
    while((gui.locateCenterOnScreen(imagem,confidence = confidence_imagem,region = region_imagem) is None)):
          pass
    x,y = gui.locateCenterOnScreen(imagem,confidence = confidence_imagem,region = region_imagem)
    gui.click(x,y,button = 'left')
    
    return None

def wait(imagem):
    while(gui.locateOnScreen(imagem,confidence=confidence_imagem) is None):
        pass

