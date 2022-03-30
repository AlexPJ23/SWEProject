from auth import get_auth
import requests

def get_data():
    access_token = get_auth()
    headers = {
        'Authorization': 'Bearer {TOKEN}'.format(TOKEN=access_token)

    }
    URL =	'https://api.spotify.com/v1/artists/{id}/top-tracks'.format(id='2hlmm7s2ICUX0LVIhVFlZQ')
    data = requests.get(URL + "?market=US", headers= headers)
    data = data.json()
    print(data)

if __name__ == '__main__':
    get_data()