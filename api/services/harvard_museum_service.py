import requests
from api.services.museum_service import MuseumService
import json
from api.services.util import create_exhibition_dict
import logging

logger = logging.getLogger(__name__)

class HarvardMuseumService(MuseumService):
    def __init__(self, url: str):
        self._url = url
    
    def get_exhibitions(self) -> tuple[list[dict], str]:
        try:
            response = requests.get(self._url)
        except Exception as e:
            logger.error(f"exception occurred fetching exhibitions: {str(e)}")
            return [], "exception occurred fetching exhibitions"
        
        if response.status_code == 200:
            exhibitions = self.make_exhibitions_from_api_response(response.text)
            return exhibitions, ""
        logger.error(f"unable to fetch exhibitions status code: {response.status_code}")
        return [], "unable to fetch exhibitions"
    
    def make_exhibitions_from_api_response(self, api_response: str ="") -> list[dict]:
        api_response = json.loads(api_response)
        exhibition_response = api_response["records"]
        exhibitions = []
        for exhibition in exhibition_response:
            new_exhibition = create_exhibition_dict(exhibition["title"],exhibition["description"], exhibition["begindate"], exhibition["enddate"], exhibition["url"], "")
            exhibitions.append(new_exhibition)
        return exhibitions
