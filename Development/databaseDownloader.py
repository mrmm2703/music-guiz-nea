import csv
import unirest

token_response = unirest.post("https://accounts.spotify.com/api/token", headers={"Authorization": "Basic myApplicationKey"}, params={"grant_type": "client_credentials"})
token = token_response.body['access_token']
token = token.encode("utf-8")
print("Access Token: " + token)

playlistID = "4ILMkgvpV7YFJX62MKQPfm"
song_response = unirest.get("https://api.spotify.com/v1/playlists/4ILMkgvpV7YFJX62MKQPfm/tracks?limit=100&offset=200", headers={"Authorization": "Bearer " + token})
print(song_response.body['items'][0])

with open("database.csv", mode="a") as csvFile:
    writer = csv.writer(csvFile, delimiter=",", quotechar='"', quoting=csv.QUOTE_ALL)
    for item in song_response.body['items']:
        print item['track']['name']
        print "By:"
        print item['track']['artists'][0]['name']
        print ""
        try:
            writer.writerow([item['track']['artists'][0]['name'], item['track']['name']])
        except:
            pass
