# Helper functions for Blackfoot project
# CMPT 120 
# Nov. 12, 2020

import pygame
import random
import cmpt120image
import wave
import time

pygame.mixer.init()

def concat(infiles,outfile):
  """
  Input: 
  - infiles: a list containing the filenames of .wav files to concatenate,
    e.g. ["hello.wav","there.wav"]
  - outfile: name of the file to write the concatenated .wav file to,
    e.g. "hellothere.wav"
  Output: None
  """
  data= []
  for infile in infiles:
      w = wave.open(infile, 'rb')
      data.append( [w.getparams(), w.readframes(w.getnframes())] )
      w.close()    
  output = wave.open(outfile, 'wb')
  output.setparams(data[0][0])
  for i in range(len(data)):
      output.writeframes(data[i][1])
  output.close()

def learn_words():
  blackfoot_dic = {}
  blackfoot_worddoc = open("blackfoot_modified.txt")
  for line in blackfoot_worddoc:
    line_list = line.strip().split(",")
    blackfoot_dic[line_list[1]] = line_list[0]  #The 'learn_words' function creates a dictionary from a .txt file and gives blackfoot translation to the user input
  blackfoot_worddoc = open("blackfoot_speech.txt")
  blackfoot_speech_dic = {}
  for line in blackfoot_worddoc:
      line_list = line.strip().split(",")
      blackfoot_speech_dic[line_list[0]] = line_list[1]

  islearn = True
  while islearn:
    try:
      learn_word = input("\nWhat Blackfoot word do you want to learn? Type it in English, or type done to finish: ").lower()
      learn_word_audio = blackfoot_speech_dic.get(learn_word)
      print(blackfoot_dic[learn_word])
      pygame.mixer.Sound("sounds/"+str(learn_word_audio)+".wav").play()
    
    except:
      if learn_word == "done":
        islearn = False
      else:
        print("I cannot translate that...try again.")
      
def test_words(lst):
  blackfoot_worddoc = open("blackfoot_modified.txt")
  blackfoot_dic = {}
  for line in blackfoot_worddoc:
      line_list = line.strip().split(",")
      blackfoot_dic[line_list[0]] = line_list[1]  #'test_words(x)' is a function to that tests user by asking them to translate blackfoot words to english

  blackfoot_audio_worddoc = open("blackfoot_audio_modified.txt")  #This function also returns a 'correct_counter' value keeping track of the users progress
  blackfoot_audio_dic = {}
  for line in blackfoot_audio_worddoc:
      line_list = line.strip().split(",")
      blackfoot_audio_dic[line_list[0]] = line_list[1]
      
      
  correct_counter = 0
  
  for i in range(10):
    random_word = random.choice(lst)
    pygame.mixer.Sound("sounds/"+str(blackfoot_audio_dic.get(random_word))+".wav").play()
    test_prompt = input("\nwhat is " + random_word + ": ").lower()
    if test_prompt == blackfoot_dic.get(random_word):
        print("Correct!")
        correct_counter +=1
    else:
        print("\nSorry the correct answer was " + blackfoot_dic.get(random_word))
  scene_score = input("\nYour score is " + str(correct_counter) + "/10. Press 'Enter' to continue...")
  return correct_counter

def test_words_custom(lst,lst2):
  blackfoot_worddoc = open("blackfoot_modified.txt")
  blackfoot_dic = {}
  for line in blackfoot_worddoc:
      line_list = line.strip().split(",")
      blackfoot_dic[line_list[0]] = line_list[1]

  blackfoot_audio_worddoc = open("blackfoot_audio_modified.txt")
  blackfoot_audio_dic = {}
  for line in blackfoot_audio_worddoc:
      line_list = line.strip().split(",")
      blackfoot_audio_dic[line_list[0]] = line_list[1]  #This function gives user 2 black foot words and 1 english words and asks them to make the correct pair
  
  correct_counter = 0
  
  for i in range(10):
    random_word = random.choice(lst)
    random_word2 = random.choice(lst2)
    switch_list = [random_word,random_word2]
    switch_list_sort_num = random.randint(0,1)
    if switch_list_sort_num == 1:
      switch_temp = switch_list[0]
      switch_list[0] = switch_list[1]
      switch_list[1] = switch_temp
    concated_sound = concat(["sounds/"+str(blackfoot_audio_dic.get(switch_list[0]))+".wav","sounds/"+str(blackfoot_audio_dic.get(switch_list[1]))+".wav"],"sounds/custom_test_concated_sound.wav")
    pygame.mixer.Sound("sounds/custom_test_concated_sound.wav").play()
  
    test_prompt = input("\nIn Blackfoot, does " + blackfoot_dic.get(random_word) + " translate to " + switch_list[0] + " or " + switch_list[1] + ": ").lower()
    
    if test_prompt == random_word.lower():
        print("Correct!")
        correct_counter +=1
    else:
        print("\nSorry the correct answer was " + random_word)
        pygame.mixer.Sound("sounds/"+str(blackfoot_audio_dic.get(random_word))+".wav").play()
        input("Press ENTER to continue with the test...")
    
  scene_score = input("\nYour score is " + str(correct_counter) + "/10. This custom test has no weight. Press 'Enter' to continue...")

def speech_synthesis():
  blackfoot_worddoc = open("blackfoot_speech.txt")
  blackfoot_speech_dic = {}
  for line in blackfoot_worddoc:
      line_list = line.strip().split(",")
      blackfoot_speech_dic[line_list[0]] = line_list[1] #This function allows user to make structurally limited sentences

  blackfoot_worddoc = open("blackfoot_modified.txt")  #This functio also uses 'concat()' to create sentences that the user desires
  blackfoot_dic = {}
  for line in blackfoot_worddoc:
      line_list = line.strip().split(",")
      blackfoot_dic[line_list[1]] = line_list[0]

  make_speech = True
  while make_speech:
      time = input("\nWhat time setting will your statement take place ('Today','This morning','Tomorrow'): ").lower()
      verb = input("\nWhat verb would you like to use ('I will go','I will eat'): ").lower()
      noun = input("\nInput any of the previously learnt nouns: ").lower()
      
      try:
        concated_speech = concat(["sounds/"+str(blackfoot_speech_dic.get(time))+".wav","sounds/"+str(blackfoot_speech_dic.get(verb))+".wav","sounds/"+str(blackfoot_speech_dic.get(noun))+".wav"],"sounds/speech_synthesis_concated_sound.wav")
        print("\n"+blackfoot_dic.get(time)+" "+blackfoot_dic.get(verb).lower()+" "+blackfoot_dic.get(noun).lower()+".")
        pygame.mixer.Sound("sounds/speech_synthesis_concated_sound.wav").play()
      except:
        print("\nSorry your sentence was not recognizable...")

      play_again_confirmed = False

      while not play_again_confirmed:
        again = input("\nType 'Again' to synthesize another sentence\nType 'Done' to stop: ").lower()
        if again == "again":
            play_again_confirmed = True
        elif again == "done":
            play_again_confirmed = True
            make_speech = False
  

  
  


