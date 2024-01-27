from api.services.museum_service import MuseumService
from api.services.util import create_exhibition_dict
import random


class SampleMuseumService(MuseumService):

    def get_exhibitions(self) -> tuple[list[dict], str]:
        exhibitions = []
        for i in range(10):
            exhibition = create_exhibition_dict(
                f"test {i}",
                f"description {i}",
                "start",
                "end",
                "http://google.com",
                f"https://picsum.photos/seed/{random.random()}/200/300",
            )
            exhibitions.append(exhibition)
        return exhibitions, ""
