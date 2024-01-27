from api.constants.museum_types import MuseumTypes
from api.constants.museum_request_types import MuseumRequestTypes
from dependency_injector.wiring import inject, Provide
from api.services.museum_factory import MuseumFactory
from api.container import Container
from flask import make_response
import logging

logger = logging.getLogger(__name__)

@inject
def get_current_exhibitions(museum_name, museum_factory: MuseumFactory = Provide[Container.museum_factory]):
    logger.info(f"requesting museum: {museum_name}")
    
    if museum_name == MuseumRequestTypes.Harvard.value:
        service = museum_factory.create_museum(MuseumTypes.Harvard.value)
    elif museum_name == MuseumRequestTypes.Test.value:
        service = museum_factory.create_museum(MuseumTypes.Test.value)
    elif museum_name == MuseumRequestTypes.Chicago.value:
        service = museum_factory.create_museum(MuseumTypes.Chicago.value)

    exhibitions, errors = service.get_exhibitions()
    
    if errors:
        logger.error(f"failure to fetch exhibitions: {errors}")
        return make_response("internal server error", 500)
    return make_response(exhibitions, 200)
