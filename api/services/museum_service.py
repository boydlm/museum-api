from abc import ABC, abstractmethod


class MuseumService(ABC):

    @abstractmethod
    def get_exhibitions(self) -> tuple[list[dict], str]:
        pass
