import requests
import json 

#date = f'{year}-{month}-{day}' 
api_key = 'Iqm1fbLQqhc7w6UgQqs8fX5plM758BFoBdtNE0Qs'
url = 'https://api.nasa.gov/planetary/apod'

def get_data(date, url=url, api_key=api_key):
    params = {'date': date, 'api_key':api_key}
    api = requests.get(url, params=params)
    datos = json.loads(api.text)
    
    return datos

class SpaceImage:
    
    def __init__(self, date):
        self.datos = get_data(date)
        self.description = self.datos['explanation']
        try:
            self.image_url = self.datos['hdurl']
        except:
            self.image_url = self.datos['url']
        
        self.title = self.datos['title']


image = SpaceImage('2020-05-17')
print(image.datos)   