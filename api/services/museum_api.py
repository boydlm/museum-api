import requests

class Museum:
    def __init__(self, url: str):
        self._url = url
    
    def get_exhibitions(self) -> tuple[dict, str]:
        try:
            response = requests.get(self._url)
        except Exception:
            return {}, "exception occurred fetching exhibitions"
        
        if response.status_code == 200:
            return response.text, ""
        
        return {}, "unable to fetching exhibitions"
    
    