import requests
from api.services.museum_service import MuseumService
import json
from api.services.util import create_exhibition_dict


class ChicagoMuseumService(MuseumService):
    def __init__(self, url: str):
        self._url = url

    def get_exhibitions(self) -> tuple[list[dict], str]:
        try:
            response = requests.get(self._url)
        except Exception:
            return [], "exception occurred fetching exhibitions"

        if response.status_code != 200:
            return [], "unable to fetch exhibitions"

        exhibitions = self.make_exhibitions_from_api_response(response.text)

        return exhibitions, ""

    def make_exhibitions_from_api_response(self, api_response: str = "") -> list[dict]:
        api_response = json.loads(api_response)
        exhibition_response = api_response["data"]
        exhibitions = []
        for exhibition in exhibition_response:
            new_exhibition = create_exhibition_dict(
                exhibition["title"],
                exhibition["short_description"],
                exhibition["aic_start_at"],
                exhibition["aic_end_at"],
                exhibition["web_url"],
                exhibition["image_url"],
            )
            exhibitions.append(new_exhibition)
        return exhibitions
