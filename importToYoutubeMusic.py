from ytmusicapi import YTMusic

ytmusic = YTMusic('headers_auth.json')
playlistId = ytmusic.create_playlist("Yandex Music", "Imported from Yandex Music")

fp = open('yandexTracks.txt', 'r')
fSkipped = open('youtubeSkippedDuringImport.txt', 'a')

for track in fp:
    print(track)
    search_results = ytmusic.search(track.strip())

    if ('videoId' not in search_results[0]):
        fSkipped.writelines([track.strip(), '\n'])
        continue

    ytmusic.add_playlist_items(playlistId, [search_results[0]['videoId']])
    ytmusic.rate_song(search_results[0]['videoId'], 'LIKE')

fp.close()
fSkipped.close()
