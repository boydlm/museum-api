from api.services.museums.harvard_museum_service import HarvardMuseumService
from api.services.museum_service import MuseumService
from api.services.museums.chicago_museum_service import ChicagoMuseumService
import os
from api.constants.museum_types import MuseumTypes
from api.services.museums.sample_museum_service import SampleMuseumService


class MuseumFactory:
    def __init__(self, harvard_apikey: str, harvard_url: str, chicago_url: str) -> None:
        self._harvard_apikey = harvard_apikey
        self._harvard_url = harvard_url
        self._chicago_url = chicago_url

    def create_museum(self, museum_type: str) -> MuseumService:
        if museum_type == MuseumTypes.Harvard.value:
            url = f"{self._harvard_url}?apikey={self._harvard_apikey}&status=current"
            return HarvardMuseumService(url)
        elif museum_type == MuseumTypes.Test.value:
            return SampleMuseumService()
        elif museum_type == MuseumTypes.Chicago.value:
            return ChicagoMuseumService(self._chicago_url)

    

