import requests
from requests.structures import CaseInsensitiveDict
import pyautogui
import time
name=""
prog=0
is_playing=False
duration=0
def callme():
  global name
  global prog
  global is_playing
  global duration
  url = "https://api.spotify.com/v1/me/player"
  headers = CaseInsensitiveDict()
  headers["Accept"] = "application/json"
  key="" #Enter your api token here
  headers["Authorization"] = "Bearer "+key
  resp = requests.get(url, headers=headers)
  # print(resp.json())
  name=resp.json()['item'].get('name')
  is_playing=resp.json().get('is_playing')
  prog=int(resp.json().get('progress_ms'))//1000
  duration=int(resp.json()['item'].get('duration_ms'))//1000
callme()
time.sleep(5) #Focus on audacity window within 5 seconds
while(1):
  print(prog)
  print(duration)
  if prog>4 :
    print('ran')
    pyautogui.press('playpause')
    pyautogui.press('prevtrack')  
    pyautogui.press('playpause')
  pyautogui.press('r')
  pyautogui.press('playpause')
  time.sleep(duration)
  pyautogui.press('space')
  pyautogui.press('playpause')
  pyautogui.hotkey('ctrl','shift','m') #bind this to save as mp3 in audacity
  pyautogui.write(name)
  pyautogui.press('enter')
  pyautogui.press('enter')
  time.sleep(10)
  pyautogui.hotkey('ctrl','a')
  pyautogui.press('backspace')
  pyautogui.press('playpause')
  time.sleep(5)
  pyautogui.press('playpause')
  callme()
  