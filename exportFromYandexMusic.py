from yandex_music.client import Client

client = Client.from_credentials('username', 'password')


f = open("yandexTracks.txt", "a")

for item in client.users_likes_tracks():
    track = item.track
    trackLine = []

    for artist in track.artists:
        trackLine.append(artist.name)
        trackLine.append(' ')
    
    trackLine.append(track.title)
    trackLine.append('\n')
    
    print(trackLine)
    f.writelines(trackLine)


f.close()

