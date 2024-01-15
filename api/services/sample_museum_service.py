from api.services.museum_service import MuseumService
from api.services.util import create_exhibition_dict

class SampleMuseumService(MuseumService):
    
    def get_exhibitions(self) -> tuple[list[dict], str]:
        exhibitions = []
        exhibitions1 = create_exhibition_dict("test", "description", "start", "end", "http://google.com")
        exhibitions.append(exhibitions1)
        return exhibitions, ""
    
 