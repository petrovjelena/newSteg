#!/usr/bin/env python
# coding: utf-8

# In[12]:


from PIL import Image
import numpy as np


# In[17]:


def txt2bin(text): #converts text into 8 bit binary
    return ''.join(format(ord(i), '08b') for i in text)


# In[16]:


def int2bin(int):
    return "{0:08b}".format(int)


# In[22]:


def encode_text(cover_img, txt_msg, out_path):
    
    img = Image.open(cover_img)
    width, height = img.size

    txt_msg += "Stegovic" #add delimiter
    bin_msg = txt2bin(txt_msg)
    data_len = len(bin_msg)

    if len(bin_msg) > width * height * 3: #image must be 3 times larger than text
        raise ValueError("Image not large enough. Please choose another image or reduce length of text.")
    else:
        data_index=0
        
    for x in range(width):
        for y in range(height):
            r, g, b = img.getpixel((x,y))

            if data_index < data_len:
                r = r & ~1 | int(bin_msg[data_index])
                data_index += 1
            if data_index < data_len:
                g = g & ~1 | int(bin_msg[data_index])
                data_index += 1
            if data_index < data_len:
                b = b & ~1 | int(bin_msg[data_index])
                data_index += 1

            img.putpixel((x,y), (r,g,b))

            if data_index >= data_len:
                break
    
    img.save(out_path)
    print("Success- your encoded image has been saved.")
 


# In[23]:


def banner():
    banner = """
   ___________________________ _    ____________
  / ___/_  __/ ____/ ____/ __ \ |  / /  _/ ____/
  \__ \ / / / __/ / / __/ / / / | / // // /     
 ___/ // / / /___/ /_/ / /_/ /| |/ // // /___   
/____//_/ /_____/\____/\____/ |___/___/\____/   
                                                """
    print(banner)

if __name__ == "__main__":
    banner()
    print("Welcome to Stegovic- an image steganography tool.")
    print("\n")
    print("Please select one of the following options:")
    print("   1: Hide text in image")
    print("   2: Hide image in image")
    print("   3: Reveal hidden text in an image")
    print("   4: Reveal hidden image in an image")

    func = input()

    if func == '1':
        print("Type path for cover image:")
        cover_img = input()
        print("Type your secret message:")
        txt_msg = input()
        print("Type path of where you want the encoded image to be saved:")
        out_img = input()
        # progress bar
        encode_text(cover_img, txt_msg, out_img)


# In[ ]:




