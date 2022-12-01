#!/usr/bin/env python
# coding: utf-8

# In[1]:


import speech_recognition as sr


# In[6]:


engine = sr.Recognizer()
mic = sr.Microphone()
hasil = " "
engine.pause_treshold = 4

with mic as source:
    print("Ngomong")
    rekaman = engine.listen(source)
    print("Tetot")
    
    try:
        hasil = engine.recognize_google(rekaman, language = "id.ID")
        print(hasil)
    except engine.UnknownValueError:
        print("Tidak dengar, ulang")
    except Exception as e:
        print(e)


# In[ ]:




