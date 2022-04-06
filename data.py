from auth import get_auth
import requests
import random

def get_data():
    access_token = get_auth()
    headers = {
        'Authorization': 'Bearer {TOKEN}'.format(TOKEN=access_token)

    }
    URL =	'https://api.spotify.com/v1/artists/{id}/top-tracks'.format(id='3hcs9uc56yIGFCSy9leWe7')
    data = requests.get(URL + "?market=US", headers= headers)
    data = data.json()

    #rand=random.randint(0,len(data['tracks'])-1)
    rand = 2
    print(data)

    x =data["tracks"][rand]["external_urls"]["spotify"]
    song_name=data["tracks"][rand]["name"]
    artist_names = []

    for i in data["tracks"][rand]["name"]:
        artist_names.append(i["name"])
    
    artist_names = data["tracks"][rand]["name"]
    album_image = data["tracks"][rand]["album"]["images"][0]["url"]
    song_preview = data["tracks"][rand]["preview_url"] #can be null
    spotify_link = data["tracks"][rand]["external_urls"]["spotify"]

    info = [song_name,artist_names,album_image,song_preview,spotify_link]

    return info

if __name__ == '__main__':
    get_data()