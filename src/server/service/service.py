
import requests
import json

class Service:
    base_url = None

    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, endpoint: str = '', params: dict[str, any] = None) -> any:
        """Fetches response with get request from url endpoint as JSON"""
        url = self.base_url + endpoint
        try:
            response = requests.get(url, params=params)
            response.raise_for_status() 
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error getting data: {e}")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")

    def post(self, endpoint: str = '', data: dict[str, any] = None, params: dict[str, any] = None) -> any:
        """Fetches response with post request from url endpoint as JSON"""
        url = self.base_url + endpoint
        try:
            response = requests.post(url, data=data, params=params)
            response.raise_for_status() 
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error posting data: {e}")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")