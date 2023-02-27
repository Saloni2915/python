#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install qrcode


# In[2]:


import qrcode as qr
img=qr.make("hello world")
img.save("hello.png")


# In[ ]



