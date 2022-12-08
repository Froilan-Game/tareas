import os
import time
import sys
import re


def lengthConsole():
    return os.get_terminal_size().columns


def load_animation(message):
    character = message

    for i in range(1, int(lengthConsole())+1):
        
        if(i == 1):
          sys.stdout.write(character)
        else:
          time.sleep(0.1)
          os.system("clear")
          character = re.sub(message, " ", character)
          character+=message
          sys.stdout.write(character)
        

    os.system("clear")


if __name__ == "__main__":
  print(lengthConsole())
  
  while True:
    
    char = input("enter a character: ")
    

    if(len(char) == 1):
      break

  load_animation(char)
