from api.services.museum_api import Museum
import os
from api.constants.museum_types import MuseumTypes


class MuseumFactory:
    def __init__(self, harvard_apikey: str, harvard_url: str) -> None:
        self._harvard_apikey = harvard_apikey
        self._harvard_url = harvard_url

    def create_museum(self, museum_type: str):
        if museum_type == MuseumTypes.Harvard.value:
            url=self.harvard_url()
            return Museum(url)
    
    def harvard_url(self):
        url = f"{self._harvard_url}?apikey={self._harvard_apikey}&status=current"
        print(url)
        return url

