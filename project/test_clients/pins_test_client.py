from json.decoder import JSONDecodeError
from typing import List

import allure

from framework.api.base_api_client import BaseApiClient
from project.models.pin import Pin
from project.models.pins import Pins


class PinsTestClient(BaseApiClient):
    """
    A class to represent a Pins API.

    Args:
        base_url (str): URL for Pins service
    """

    endpoint: str = 'api/pins'
    """str: Pins api endpoint."""

    def __init__(self, base_url: str):
        super().__init__(base_url)

    def get_all_pins(self) -> List[Pin]:
        """
        Sends a GET request to the /pins endpoint to retrieve all pins.

        Returns:
            list of pins
        """
        response = self.get(self.endpoint)
        return response.json(object_hook=Pin.decode_pin)

    def get_pin(self, pin_id: int) -> Pin:
        """
        Sends a GET request to the api/pins/{id} endpoint to retrieve a specific Pin.

        Args:
            pin_id (int): An integer pin id

        Returns:
            Pin
        """
        response = self.get(f'{self.endpoint}/{pin_id}')
        pin = None
        try:
            pin = response.json(object_hook=Pin.decode_pin)
        except JSONDecodeError:
            pass
        return pin

    @allure.step('Update "{pin_id}" pin with "{voltage}" voltage')
    def update_pin(self, pin_id: int, voltage: float) -> None:
        """
        Sends a POST request to the api/pins/{id}/update_pin endpoint to update a specific Pin.

        Args:
            pin_id (int): An integer pin id
            voltage (int): Voltage to set
        """
        data = {'Voltage': voltage}
        self.post(f'{self.endpoint}/{pin_id}/update_pin', data=data)

    @allure.step('Update pins: "{pins}"')
    def update_pins(self, *pins: Pin) -> None:
        """
        Sends a POST request to the api/pins/{id}/update_pin endpoint to update a specific Pin.

        Args:
            pins Tuple[Pin]: A tuple of Pin objects
        """
        headers = {
            'Content-Type': 'application/json'
        }
        json_body = Pins(list(pins)).to_json()
        self.post(f'{self.endpoint}/update_pins', headers=headers, data=json_body)
