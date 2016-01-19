import time
import random

# variables
RV = random.randrange(1,20)
Class = "fish"
Species = "fish"
Class_Stats = 0
action = "meow"

"""location guide: 
0 = plains
1 = valley
2 = Forest
3 = desert
4 = lake
5 = village
6 = farm
"""

#base info
Location = 0
Farmfound = False
direction = "Central"
enemy = "nothing"

# Class data 
# buff to stats [attack, defence, magic, agility, health, gold, XP]
WarriorS = [3,2,0,0,5,0,0]
MageS = [1,3,5,2,2,0,0]
ThiefS = [1,2,2,5,4,0,0]
RougeS = [2,2,2,5,3,0,0]

# Species data
elfS = [0,2,1,2,2,0,0]
darklingS = [2,0,2,0,0,0,0]
dragonS = [2,1,2,0,3,0,5]
humanS = [1,1,1,1,1,0,0]
wolfS = [3,1,0,2,0,0,0]
goblinS = [1,0,0,1,3,5,0]
tigerS = [3,1,0,3,0,0,0]
foxS = [1,2,3,2,0,0,0]
demonS = [2,2,2,0,0,0,0]


def Print_Stats(lime):
	print "Your attack is: ", lime[0]
	print "Your defence is: ", lime[1]
	print "Your magic is: ", lime[2]
	print "Your agility is: ", lime[3]
	print "Your health is: ", lime[4]
	print "You have ", lime[5], " gold."

def Travel(Farmfound):
	global Location
	if Location == 0:
		print "you find yourself standing in the middle of a flat plane, in the distance you can see Mountains to the North, a Forest to the West, a Desert to the East, and a Lake to the South."
		print "You can also see a the smoke from the chimneys of a small village to the North East"
		print "which direction do you want to go?"
		Choose_Travel(Farmfound)
	elif Location == 1:
		print "you find yourself in a small valley surrounded by tall snow-capped mountains riddled with caves, you can either follow the river South to the plains, hike East to the village, or take the mountain pass to the South-West to go to the Forest"
		print "which direction do you want to go?"
		Choose_Travel(Farmfound)
	elif Location == 2:
		if Farmfound == True:
			print "you are standing in a small clearing in the forests, the clearing is surrounded by tall pines on all sides, you can go South to the farm, South-East to the lake, East to the planes, or North-East to the mountains"
		else:
			print "you are standing in a small clearing in the forests, the clearing is surrounded by tall pines on all sides, you can go South-East to the lake, East to the planes, or North-East to the mountains"
		print "which direction do you want to go?"
		Choose_Travel(Farmfound)
	elif Location == 3:
		print "you are ankle deep in sand in a desert, you can go North to the village, West to the plains, or South-West to the Lake"
		print "which direction do you want to go?"
		Choose_Travel(Farmfound)	
	elif Location == 4:
		if Farmfound == True:
			print "you are on the edge of a large flat lake, you can go West to the farm, North-West to the forest, North to the plains, or North-East to the desert"
		else:
			print "you are on the edge of a large flat lake, North-West to the forest, North to the plains, or North-East to the desert"
		print "which direction do you want to go?"
		Choose_Travel(Farmfound)			
	elif Location == 5:
		print "you are surrounded by buildings in the small village, you can go West to the mountains, South-West to the plains, or go South to the Desert"
		print "which direction do you want to go?"
		Choose_Travel(Farmfound)
	elif Location == 6:
		print "you are surrounded by buildings on the farm, you can go North to the forest, or East to the Lake"
		print "which direction do you want to go?"
		Choose_Travel(Farmfound)
	else:
		Location = 0
		print "somehow you're no longer on the map, please go light yourself on fire"
		print "which direction do you want to go?"
		Choose_Travel(Farmfound)
	return Location

def Choose_Travel(Farmfound):
	global Location
	ChoiceM = (raw_input(">>>").lower())
	if Location == 0:
		if ChoiceM == "n" or ChoiceM == "north":
			Location = 1
			Direction = "North"
		elif ChoiceM == "w" or ChoiceM == "west":
			Location = 2
			Direction = "West"
		elif ChoiceM == "e" or ChoiceM == "east":
			Location = 3
			Direction = "East"
		elif ChoiceM == "s" or ChoiceM == "south":
			Location = 4
			Direction = "South"
		elif ChoiceM == "ne" or ChoiceM == "north east":
			Location = 5
			Direction = "North East"
		else: 
			print "it's not that hard, there are only so many choices you can make, just pick one okay?"
			Location = 0
			Direction = "Nowhere"
	elif Location == 1:
		if ChoiceM == "sw" or ChoiceM == "South-West":
			Location = 2
			Direction = "South-West"
		elif ChoiceM == "e" or ChoiceM == "east":
			Location = 5
			Direction = "East"
		elif ChoiceM == "s" or ChoiceM == "south":
			Location = 0
			Direction = "South"
		else: 
			print "it's not that hard, there are only so many choices you can make, just pick one okay?"
			Location = 1
			Direction = "Nowhere"
	elif Location == 2:
		if ChoiceM == "ne" or ChoiceM == "north-east":
			Location = 1
			Direction = "North-East"
		elif ChoiceM == "e" or ChoiceM == "east":
			Location = 0
			Direction = "East"
		elif (ChoiceM == "s" or ChoiceM == "south") and Farmfound == True:
			Location = 6
			Direction = "South"
		else: 
			print "it's not that hard, there are only so many choices you can make, just pick one okay?"
			Location = 2
			Direction = "Nowhere"
	elif Location == 3:
		if ChoiceM == "n" or ChoiceM == "north":
			Location = 5
			Direction = "North"
		elif ChoiceM == "w" or ChoiceM == "west":
			Location = 0
			Direction = "West"
		elif ChoiceM == "sw" or ChoiceM == "south-east":
			Location = 4
			Direction = "South-East"
		else: 
			print "it's not that hard, there are only so many choices you can make, just pick one okay?"
			Location = 3
			Direction = "Nowhere"
	elif Location == 4:
		if ChoiceM == "n" or ChoiceM == "north":
			Location = 0
			Direction = "North"
		elif ChoiceM == "nw" or ChoiceM == "north-west":
			Location = 2
			Direction = "Norht-West"
		elif ChoiceM == "ne" or ChoiceM == "norht-east":
			Location = 3
			Direction = "North-East"
		elif (ChoiceM == "w" or ChoiceM == "west") and Farmfound == True:
			Location = 6
			Direction = "West"
		else: 
			print "it's not that hard, there are only so many choices you can make, just pick one okay?"
			Location = 4
			Direction = "Nowhere"

	elif Location == 5:
		if ChoiceM == "s" or ChoiceM == "south":
			Location = 3
			Direction = "South"
		elif ChoiceM == "w" or ChoiceM == "west":
			Location = 1
			Direction = "West"
		elif ChoiceM == "sw" or ChoiceM == "south-west":
			Location = 0
			Direction = "South-West"
		else: 
			print "it's not that hard, there are only so many choices you can make, just pick one okay?"
			Location = 5
			Direction = "Nowhere"
	elif Location == 6:
		if ChoiceM == "n" or ChoiceM == "north":
			Location = 2
			Direction = "North"
		elif ChoiceM == "e" or ChoiceM == "east":
			Location = 3
			Direction = "East"
		else: 
			print "it's not that hard, there are only so many choices you can make, just pick one okay?"
			Location = 6
			Direction = "Nowhere"
	else:
		Location = 0
	print "you decide to venture ", Direction 
	return Location

def Error_Message_General():
	#General error message generator 
	message_code = random.randrange(1,11)
	if message_code == 1:
		print "you had one job, was that so hard?"
	elif message_code == 2:
		print "That's not really... um.... yeah....."
	elif message_code == 3:
		print "Just try again okay?"
	elif message_code == 4:
		print "that's not a vaild choice, please try agian"
	elif message_code == 5:
		print "*sighs heavily* ....just.... no.... "
	elif message_code == 6:
		print "there are few words to describe how dissapointed I am with you right now...."
	elif message_code == 7:
		print "...w-what? how did you even.... ugh...."
	elif message_code == 8:
		print ".... you're not very bright are you....."
	elif message_code == 9:
		print "Could you take this seriously please?"
	elif message_code == 10:
		print "you took the short bus to school didn't you...."
	elif message_code == 11:
		print "I DIDN'T make that an option, try again...."
	else:
		print "IDK how but you made the error message generator generate an error message.... please just stop...."

def Explore(Class_Stats,Species,Name,Farmfound,Location):
	if Location == 0:
		Explore_plains(Species,Name)
	elif Location == 1:
		Explore_Valley(Class_Stats,Species,Name)
	elif Location == 2:
		Explore_Forest(Class_Stats,Species,Name,Farmfound)
	elif Location == 3:
		Explore_Desert(Class_Stats,Species,Name)
	elif Location == 4:
		Explore_Lake(Class_Stats,Species,Name,Farmfound)
	elif Location == 5:
		Explore_Village(Class_Stats,Species,Name)
	elif Location == 6:
		Explore_Farm(Class_Stats,Species,Name)
	else:
		print "please stop existing..."

def Explore_plains(Species,Name):
	global Class_Stats
	global enemy
	Event = random.randrange(0,5)
	if Event == 1:
		#encounter a snakemm
		print "you wanter for a while before coming accros a small stream, you follow it till you come to a small pool \n while examining the pond you almost step on a snake"
		enemy = "snake"
		Combat(enemy)

	elif Event == 2:
		#encounter a wolf
		"you explore for a while till you hear the howling of a wolf, you have no-where to hide and must fight the creature"
		enemy = "wolf"
		Combat(enemy)
	elif Event == 3:
		#find a coin
		print "you trudge over the rolling hills for a while finding nothing till something catches your eye. You rush over to it to find a single gold coin on the ground."
		print "you pocket the coin, happy with your good fortune"
		Class_Stats[5] = (Class_Stats[5] + 1)
	elif Event == 4:
		#trip and fall down a hill (loose some health)
		print "you march over the grass lands for a while and climb to the top of a small hill to get a better view of your surroundings"
		print "admiring the view you don't notice the small hole in your path and step into it, loosing your balance and rolling down the hill"
		print "you lost 1 HP from the fall"
		Class_Stats[4] = (Class_Stats[4] - 1)
	elif Event == 5:
		#get lost in the grass and loose time
		print "you wander for about an hour, slowing becoming more and more lost in the tall grass. \n You eventually find your way back to the path. "
	else:
		print "after about an hour you still haven't found anything so you return to where you started from"

def Explore_Valley(Class_Stats,Species,Name):
	pass

def Explore_Forest(Class_Stats,Species,Name,Farmfound):
	pass

def Explore_Desert(Class_Stats,Species,Name):
	pass

def Explore_Lake(Class_Stats,Species,Name,Farmfound):
	pass

def Explore_Village(Class_Stats,Species,Name):
	pass

def Explore_Farm(Class_Stats,Species,Name):
	pass

def Combat(monster):
	global Class_Stats
	print "you are fighting a ", monster, "!"
	Monster_Stats = []
	#[attack, defence, magic, agility, health, gold, XP]

# intro 
print "welcome to the universe!" 
print "what do you wanna be called?"
Name = raw_input(">>>")
print "Are you sure you wanna go by ", Name, "?"
time.sleep(.5)
print "Not my first choice, but it's up to you..."
time.sleep(.5)
while Class == "fish": 
	print "what kind of hero are you? Warrior, Mage, Thief, or Rouge?"
	while Class == "fish":
		Classalpha = (raw_input(">>>")).lower()
		Classalpha = Classalpha.replace(" ", "")
		if Classalpha == "warrior" or Classalpha == "w":
			Class = "Warrior"
			Class_Stats = WarriorS
		elif Classalpha == "mage" or Classalpha == "m":
			Class = "Mage"
			Class_Stats = MageS
		elif Classalpha == "thief" or Classalpha == "t":
			Class = "Thief"
			Class_Stats = ThiefS
		elif Classalpha == "rouge" or Classalpha == "r":
			Class = "Rouge"
			Class_Stats = RougeS
		else:
			print "Silly, that's not a hero class. try again!"
	print "So you're a", Class, "huh?"
	print "Are you sure?"
	bravo = (raw_input("y/n?\n").lower())
	if bravo == "y" or bravo == "yes":
		print Class, "it is then!"
	elif bravo == "n" or bravo == "no":
		Class = "fish" 
	else:
		Error_Message_General() 
		Class = "fish"

while Species == "fish":
	print "what species are you? Elf, Darkling, Dragon, Human, Wolf, Goblin, Tiger, Fox, or Demon?"
	while Species == "fish":
		Kite = (raw_input(">>>").lower())
		Kite = Kite.replace(" ", "")
		if Kite == "elf":
			Species = "Elf"
			SpeciesS = elfS
		elif Kite == "darkling":
			Species = "Darkling"
			SpeciesS = darklingS
		elif Kite == "dragon":
			Species = "Dragon"
			SpeciesS = dragonS
		elif Kite == "human":
			Species = "Human"
			SpeciesS = humanS
		elif Kite == "wolf":
			Species = "Wolf"
			SpeciesS = wolfS
		elif Kite == "goblin":
			Species = "Goblin"
			SpeciesS = goblinS
		elif Kite == "tiger":
			Species = "Tiger"
			SpeciesS = tigerS
		elif Kite == "fox":
			Species = "Fox"
			SpeciesS = foxS
		elif Kite == "demon":
			Species = "Demon"
			SpeciesS = demonS
		else: 
			Error_Message_General()
			Species = "fish"
	print "So you're a", Species, "huh? interesting..... I wasn't expecting the Champion to be from THAT family..... very interesting....."
	if Species == "Elf":
		print ""
	elif Species == "Darkling":
		print ""
	elif Species =="Dragon":
		print ""
	elif Species == "Human":
		print "You are a human, plain and simple."
	elif Species == "Wolf":
		print ""
	elif Species == "Goblin":
		print ""
	elif Species == "Tiger":
		print ""
	elif Species == "Fox":
		print "You are coated head to toe in a fine coat of short, red fur, save for your chest and inner thighs which are a light white instead. You stand on two powerful digitigrades legs ending in feral paws like those of a fox allowing you to run faster than a normal human. Your lean body gives you the speed you need to avoid dangers and your thick, fluffy tail aids in your balance. You lack fingernails though, in their place grow sharp little claws that allow you to scratch any enemy you may encounter. Your final feature is your face, which is slightly more pointed than a human but retains many of the normal human ones, two pointed fox ears top off your physique. Although your real power may not be physical, your mental abilities far surpass those of a normal human giving you far stronger magic than others. "
	elif Species == "Demon":
		print "You look quite similar to a regular run of the mill human except you have a shiny black skin as dark as the night showing off your demonic heritage. Sprouting from your back are two large and strong wings, similar to those of a very large bat. Although not feeling any different than normal skin to the touch, it is tougher and does not take damage as easily (preventing quite a few broken limbs in your rambunctious youth). The demon blood running through your veins gives you a better understanding of nature and the art of magic, making your magic more powerful than others. The final part of your blood heritage is the sharpness of your fingertips, making them a powerful weapon in a pinch. "
	print "are you sure about your heritage?"
	alpha = (raw_input("y/n\n").lower())
	alpha = alpha.replace(" ", "")
	if alpha == "y" or alpha == "yes":
		print "well... if you're sure then..."
	elif alpha == "n" or alpha == "no":
		print "I didn't think so"
		Species = "fish"
	else:
		print "really? how can you not be sure? it's your stupid family! try again"

time.sleep(.2)
print "well I guess we should see what you're made of huh?"
Class_Stats[0] = (random.randrange(7,20) + Class_Stats[0] + SpeciesS[0]) 
Class_Stats[1] = (random.randrange(7,20) + Class_Stats[1] + SpeciesS[1])
Class_Stats[2] = (random.randrange(3,15) + Class_Stats[2] + SpeciesS[2])
Class_Stats[3] = (random.randrange(3,10) + Class_Stats[3] + SpeciesS[3])
Class_Stats[4] = (random.randrange(10,20) + Class_Stats[4] + SpeciesS[4])

Print_Stats(Class_Stats)

while (Class_Stats[4]) >= 0:
	if action == "meow" :
		print "you can either EXPLORE, VIEW_STATS, or TRAVEL in a direction"
		print "what do you want to do?"
		feline = (raw_input(">>>").lower())
		feline = feline.replace(" ", "")
		if feline == "explore" or feline == "e":
			action = "E"
		elif feline == "travel" or feline == "t":
			action = "T"
		elif feline == "view_stats" or feline == "vs":
			action = "VS"
		else:
			Error_Message_General()
			action = "meow"
	if action == "T":
		print "which direction do you want to go?"
		Travel(Farmfound)
		action = "meow"
	if action == "E":
		print "you decide to explore the surrounding area to see what you can find"
		Explore(Class_Stats,Species,Name,Farmfound,Location)
		action = "meow"
	if action == "VS":
		Print_Stats(Class_Stats)
		action = "meow"
raw_input("end")