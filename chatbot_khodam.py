
"""chatbot khodam.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1VTZdfVeGkgmiztPkymBs0B6hMbj6T3vY
"""

import requests

out = requests.get("https://google.com")

print(out)

import requests as req

soal=input("soal:")

out = req.get("http://5.161.91.18/chat?text="+soal)

print(out.json())