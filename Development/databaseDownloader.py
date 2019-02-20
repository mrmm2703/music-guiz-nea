import math
import csv
import unirest
import os

# Delete if database alreay exists
if os.path.exists("database.csv"):
    os.remove("database.csv")

playlistID = "4ILMkgvpV7YFJX62MKQPfm"

# Get an authentication token
print("Requesting access token...")
token_response = unirest.post("https://accounts.spotify.com/api/token", headers={"Authorization": "Basic YTgyMTZjMDIwZjA0NGQ0MDk4M2YwN2RlODhlOWFkZjU6YzZkZGMxYTM1MGM3NGQ1NDliNWIzODc4OTFlOTRhOTM="}, params={"grant_type": "client_credentials"})
token = token_response.body['access_token']
token = token.encode("utf-8")
print("Access Token: " + token)
print("")

# Find number of songs to get around 100 song limit
print("Retrieveing songs...")
playlist_response = unirest.get("https://api.spotify.com/v1/playlists/" + str(playlistID), headers={"Authorization": "Bearer " + token})
songCount = playlist_response.body['tracks']['total']
print str(songCount) + " songs in total."
numberOfIterations = math.ceil(float(songCount) / 100)
print("")

# Open the database
print("Writing songs into database...")
with open("database.csv", mode="wb") as csvFile:
    writer = csv.writer(csvFile, delimiter=",", quotechar='"', quoting=csv.QUOTE_ALL)
    offset = 0
    while(True):
        if numberOfIterations == 0:
            break
        song_response = unirest.get("https://api.spotify.com/v1/playlists/4ILMkgvpV7YFJX62MKQPfm/tracks?limit=100&offset=" + str(offset), headers={"Authorization": "Bearer " + token})
        for item in song_response.body['items']:
            try:
                writer.writerow([item['track']['artists'][0]['name'], item['track']['name']])
            except:
                pass
        # Add 100 to the offset to get the next set of songs
        offset = offset + 100
        numberOfIterations = numberOfIterations - 1

print("Finished creating database of songs.")
print("")
print("Press enter key to continue...")
input("")
