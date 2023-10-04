#Blackfoot game
#Jasmeen Brar, Jason Gill
#Nov 23,2020

import pygame
import cmpt120image
import helper
import random
import time

pygame.mixer.init()     #Initializing mixer for pygame audio

town_image_array = cmpt120image.getImage("places_images/"+"town.jpg")        #Showing the default 'town' image to start the game
scene_show = cmpt120image.showImage(town_image_array,"pygame")

#This next section are the words associated with each scene
town_words = ["Itoiyo'pii","Naapoiyiss","Itaohpomoapii","Aisaksittoo","Niitoiyiss"]
diner_words = ["Aohkii","Mamii","Aotahkoinammiksi","Aipasstaamiinammiksi","Paataakistsi(fries)","Paataakistsi(potatoes)","Pikkiaaksin","Pisatsoyiikan","Napayin","Siksikimmii","Iitapsiksikimmii"]
people_words = ["Ninaa","Aakii","Aakiikoan","Saahkomaapi","Iksisst","Inn"]
greetings_words = ["Oki","Oki napi","Tsa niita'piiwa?","Tsikohssokopii. Kistoo?","Matohkwiikii","Oki(Let's go)","Aa","Saa"]
home_words = ["Makapoiyiss","Itoiyo'soap","Aiksistomatomahka","Aisspaohpii","Ksisstsikomstan","Imitaa"]

in_town = True
in_diner = False
in_people = False   #These are boolean values to keep track of what image is being displayed 
in_greetings = False
in_home = False

town_words_test = 0
diner_words_test = 0
people_words_test = 0   #These are the top test marks for each scene (not custom test marks). These are defaulted to 0.
greetings_words_test = 0    
home_words_test = 0

print("\nOki (Hello)! Welcome to Brocket, Alberta! I can teach you some Blackfoot while you are here!")

want_play_game = True

while want_play_game:
    user_options = input("\nDo you want to learn some words around you (learn), \nhave me test you (test), \npractice with a custom test(custom test), \ngo somewhere else (move), \nsee your top test marks(marks), \ncreate blackfoot sentences (speech) \nor leave(exit)?: ").lower()
    if user_options == "learn":
        helper.learn_words()
        
    elif user_options == "test":
        if in_town:
            mark1 = helper.test_words(town_words)   #test option that allows user to test their blackfoot vocabulary taking into account what scene they're in.
            if town_words_test < mark1:             #the nested if statement are to update users top test score for each of the scenes
                town_words_test = mark1
                
        elif in_diner:
            mark2 = helper.test_words(diner_words)  #""
            if diner_words_test < mark2:
                diner_words_test = mark2
        elif in_people:
            mark3 = helper.test_words(people_words) #""
            if people_words_test < mark3:
                people_words_test = mark3
        elif in_greetings:
            mark4 = helper.test_words(greetings_words)  #""
            if greetings_words_test < mark4:
                greetings_words_test = mark4
        elif in_home:
            mark5 = helper.test_words(home_words)   #""
            if home_words_test < mark5:
                home_words_test = mark5

    elif user_options == "custom test":
        if in_town:
            helper.test_words_custom(town_words,home_words)
        elif in_diner:
            helper.test_words_custom(diner_words,town_words)    #Custom test (does not affect users top score for 'test' feature
        elif in_people:
            helper.test_words_custom(people_words,diner_words)  #Custom test uses the function 'test_words_custom(x,y)' defined in the helper file
        elif in_greetings:
            helper.test_words_custom(greetings_words,people_words)
        elif in_home:
            helper.test_words_custom(home_words,greetings_words)

    elif user_options == "move":
        move_confirmed = False
        while not move_confirmed:
            move_where = input("\nWhere would you like to move (Town/Restaurant/People/Greetings/Home)?: ").lower()
            try:
              scene_show = cmpt120image.showImage(cmpt120image.getImage("places_images/"+move_where+".jpg"),"pygame")
              if move_where == "town":
                in_town = True
                in_diner = False
                in_people = False
                in_greetings = False
                in_home = False
              elif move_where == "restaurant":
                in_town = False
                in_diner = True
                in_people = False
                in_greetings = False
                in_home = False
              elif move_where == "people":  #This algorithm is designed to chanbe the scene and update the boolean values to keep track of where the user is
                in_town = False
                in_diner = False
                in_people = True
                in_greetings = False
                in_home = False
              elif move_where == "greetings":
                in_town = False
                in_diner = False
                in_people = False
                in_greetings = True
                in_home = False
              elif move_where == "home":
                in_town = False
                in_diner = False
                in_people = False
                in_greetings = False
                in_home = True
              move_confirmed = True
            except:
              print("\nSorry I don't know where that is...")

    elif user_options == "marks":
        try:
            print("\n"+str(town_words_test)+"/10 for town scene, "+str(diner_words_test)+"/10 for restaurant scene, "+str(people_words_test)+"/10 for people scene, "+str(greetings_words_test)+"/10 for greetings scene, and "+str(home_words_test)+"/10 for home scene.")
        except:
            print("\nThere was some error retrieving your marks...")    #The 'marks' option allows the user to see their marks for each scene (marks initiazlized to 0)

    elif user_options == "speech":
        helper.speech_synthesis()   #speech synthesis feature that allows user to create blackfoot sentences. 'speech_synthesis()' is defined in the helper file
        
    elif user_options == "exit":
        print("\nThank you for playing the Blackfoot Audio-Visual learning app!")   #Allows user to stop playing the game
        want_play_game = False

    else:
        print("\nI didn't get that...Try again.")   #Response for if none of the options were chosen

    
    
        
    
