import requests

class MatomoConnector:
    def __init__(self, url, token):
        self.url = url.rstrip('/')
        self.token = token

    def get_live_data(self, site_id):
        """Fetch live visitor data from Matomo"""
        endpoint = f"{self.url}/?module=API&method=Live.getLastVisitsDetails&idSite={site_id}&format=JSON&token_auth={self.token}"
        response = requests.get(endpoint)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Failed to fetch data. Code: {response.status_code}"}
