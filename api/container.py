from dependency_injector import containers, providers
from api.services.museum_factory import MuseumFactory

class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=["api.routes.exhibitions"])
    config = providers.Configuration(yaml_files=["config.yml"])

    museum_factory = providers.Factory(
        MuseumFactory, 
        harvard_apikey = config.harvard_apikey,
        harvard_url = config.harvard_api_url,
        chicago_url = config.chicago_api_url

    )
