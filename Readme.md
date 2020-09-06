# Import from Yandex Music to Youtube Music

```
pip install -r requirements.txt
```

## Export list of tracks from Yandex Music

Set your Yandex Music credentials in `exportFromYandexMusic.py`

```
client = Client.from_credentials('username', 'password')
```

Run a script:

```
python exportFromYandexMusic.py
```

A list of tracks will be store in `yandexTracks.txt`

## Import list of tracks to Youtube Music

### Copy authentication headers

To run authenticated requests you need to set up you need to copy your request headers from a POST request in your browser. To do so, follow these steps:

    Open a new tab
    Open the developer tools (Ctrl-Shift-I) and select the “Network” tab
    Go to https://music.youtube.com and ensure you are logged in
    Find an authenticated POST request. The simplest way is to filter by /browse using the search bar

Headers should be pasted in `headers_auth.json` file

Run a script:

```
python importToYoutubeMusic.py
```

If the scipt fails to import any tracks, it will place their names to `youtubeSkippedDuringImport.txt` file.

## Thank you to authors of these libraries:

- https://github.com/MarshalX/yandex-music-api
- https://github.com/sigma67/ytmusicapi
