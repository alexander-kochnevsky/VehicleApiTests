from json.decoder import JSONDecodeError

from framework.api.base_api_client import BaseApiClient
from project.models.signal import Signal
from project.models.signals import Signals


class SignalsTestClient(BaseApiClient):
    """
    A class to represent a Signals API.

    Args:
        base_url (str): URL for vehicle service
    """

    endpoint: str = 'api/signals'
    """str: Signals api endpoint."""

    def __init__(self, base_url: str):
        super().__init__(base_url)

    def get_all_signals(self) -> Signals:
        """
        Sends a GET request to the /signals endpoint to retrieve all signal values.

        Returns:
            Signals
        """
        response = self.get(self.endpoint)
        return Signals(response.json(object_hook=Signal.decode_signal))

    def get_signal(self, signal_id: int) -> Signal:
        """
        Sends a GET request to the /signals/{id} endpoint to retrieve a specific signal.

        Args:
            signal_id (int): An integer signal id

        Returns:
            Signal
        """
        response = self.get(f'{self.endpoint}/{signal_id}')
        signal = None
        try:
            signal = response.json(object_hook=Signal.decode_signal)
        except JSONDecodeError:
            pass
        return signal
