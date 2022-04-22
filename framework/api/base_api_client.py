import requests
from requests import Response

from framework.logger.logger import Logger


class BaseApiClient:
    """
    A class to represent a base API client. Can be inherited by specific API clients.

    Args:
        base_url (str): Base URL for API service
    """

    def __init__(self, base_url: str):
        self.__base_url = base_url

    def _send_request(self, endpoint: str, request_method, headers=None, data=None) -> Response:
        """
        Sends a parametrized request.

        Args:
            endpoint (str): Endpoint
            request_method: Request method to call (eg get, post)
            data: Request body

        Returns:
            Response object of requests module
        """
        Logger.info(f'Send {request_method.__name__.upper()} request to {self.__base_url}/{endpoint}')
        Logger.info(f'Data: {data}')
        response = request_method(f'{self.__base_url}/{endpoint}', headers=headers, data=data)
        Logger.info(f'Response status code: {response.status_code}')
        Logger.debug(f'Response content: {response.text}')
        response.raise_for_status()
        return response

    def get(self, endpoint: str) -> Response:
        """
        Sends a GET request.

        Args:
            endpoint (str): Endpoint

        Returns:
            Response object of requests module
        """
        return self._send_request(endpoint, requests.get)

    def post(self, endpoint: str, data=None, headers=None) -> Response:
        """
        Sends a POST request.

        Args:
            endpoint (str): Endpoint
            data: Request body
            headers: Request headers

        Returns:
            Response object of requests module
        """
        return self._send_request(endpoint, requests.post, headers=headers, data=data)

    def put(self, endpoint: str, data=None) -> Response:
        """
        Sends a PUT request.

        Args:
            endpoint (str): Endpoint
            data: Request body

        Returns:
            Response object of requests module
        """
        return self._send_request(endpoint, requests.put, data=data)

    def delete(self, endpoint: str) -> Response:
        """
        Sends a DELETE request.

        Args:
            endpoint (str): Endpoint

        Returns:
            Response object of requests module
        """
        return self._send_request(endpoint, requests.delete)
