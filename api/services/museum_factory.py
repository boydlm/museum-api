from api.services.museum_api import Museum
import os
from api.constants.museum_types import MuseumTypes

def create_museum(museum_type: str):
    if museum_type == MuseumTypes.Harvard.value:
        url=harvard_url()
        return Museum(url)
    
def harvard_url():
    base_url = "https://api.harvardartmuseums.org"
    endpoint = "/exhibition"
    api_key = os.getenv("HARVARD_API_KEY")
    url = f"{base_url}{endpoint}?apikey={api_key}&status=current"
    print(url)
    return url

