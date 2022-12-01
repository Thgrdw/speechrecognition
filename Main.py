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
    print("Silahkan Berbicara!!")
    rekaman = engine.listen(source)
    print("Maaf Waktu Habis")
    
    try:
        hasil = engine.recognize_google(rekaman, language = "id.ID")
        print(hasil)
    except engine.UnknownValueError:
        print("Mohon maaf tidak terdeteksi, silahkan ulangi")
    except Exception as e:
        print(e)


# In[ ]:




