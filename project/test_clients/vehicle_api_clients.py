from project.test_clients.pins_test_client import PinsTestClient
from project.test_clients.singals_test_client import SignalsTestClient


class VehicleApi:
    def __init__(self, base_url: str):
        self.__base_url = base_url

    @property
    def pins(self) -> PinsTestClient:
        return PinsTestClient(self.__base_url)

    @property
    def signals(self) -> SignalsTestClient:
        return SignalsTestClient(self.__base_url)
