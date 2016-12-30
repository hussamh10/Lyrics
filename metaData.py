import spotipy

def getArtistInfo(artist):
    spotify = spotipy.Spotify()
    results = spotify.search(q='artist:' + artist, type='artist')
    items = results['artists']['items']
    if len(items) > 0:
        artist = items[0]
    data = {'name': artist['name'], 'image': artist['images'][0]['url'], 'genre': artist['genres'][0]}
    return data
