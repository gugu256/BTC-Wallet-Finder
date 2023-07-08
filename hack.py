import os
import pyautogui as pgi
import checkfail
from winsound import Beep as b

flr = "FAILURE.png"
img = "image.png"

words = open("wurds.txt").read().replace("\n", " ").split(" ")

os.system('"C:/Program Files/WasabiWallet/wassabee.exe"')

sentences = open("sentences.txt").read().splitlines()



pgi.sleep(5)
for i in range(0, len(sentences)):
  pgi.write(sentences[i], 0.05)
  pgi.screenshot("image.png")
  if checkfail.fail(flr, img):
    print(f"{i+1} : FAIL")
    pgi.press("backspace", 12, 0.05)
  else:
    print(f"{i+1} : SUCCESS")
    b(440, 300)
    b(660, 300)
    b(880, 600)
    open("working.txt", "a").write(sentences[i] + "\n")
    pgi.press("backspace", 12, 0.05)
    #quit()
  pgi.sleep(0.1)



"""

# GENERATE SENTENCES

for i in range(0, 1):
  current_sent = ""

  for i in range(0, 12): 
    current_sent += random.choice(words) + " "
  
  if current_sent not in sentences:
    sentences.append(current_sent)
    open("sentences.txt", "a").write(current_sent + "\n")
  else:
    print("ALREADY IN")

"""