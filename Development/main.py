import getpass
import re
import random
import csv

# Initialise variables
points = 0
password = "ele"

def clean(song):
	cleaned = song.lower()
	cleaned = cleaned.strip()
	cleaned = re.sub(" +", " ", cleaned)
	return str(cleaned)

def songNameFormat(song):
	finalString = ""
	words = song.split()
	for word in words:
		ind = 1
		for letter in word:
			if(ind == 1):
				finalString = finalString + letter
			else:
				finalString = finalString + "_"
			ind = ind + 1
		finalString = finalString + " "
	return finalString

# Ask for password until correct
while(True):
	password_attempt = getpass.getpass()
	if(password_attempt == password):
		break # Break out of loop
	else:
		print("Incorrect password. Try again.")

# Open CSV file and load into list 'songDB'
SongFile = open("database.csv", "rt")
fileReader = csv.reader(SongFile)
songDB = []

# Put records from database into list
for row in fileReader:
	songDB.append(row)

while(True):
	# Select random song and put into list
	song = []
	randInd = random.randint(0, len(songDB)-1)
	song.append(songDB[randInd][0])
	song.append(songDB[randInd][1])
	songDB.pop(randInd)
	tries = 1
	print(songNameFormat(song[1]))
	print("By: " + str(song[0]))
	while(True):
		songAttempt = raw_input("Enter the full song name: ")
		songAttempt = clean(songAttempt)
		while(songAttempt == ""):
			print("You entered nothing. Try again: ")
			songAttempt = raw_input("Enter the full song name: ")
			songAttempt = clean(songAttempt)
		if(songAttempt == clean(song[1])):
			if(tries == 1):
				points = points + 3
				print("Points: " + str(points))
				break
			elif(tries == 2):
				points = points + 1
				print("Points: " + str(points))
				break
		else:
			print("Incorrect answer.")
			tries = tries + 1
			if(tries > 2):
				endGame()
			else:
				pass
