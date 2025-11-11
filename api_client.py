"""
API client module that uses vulnerable packages.
"""
import requests
from urllib3 import PoolManager
import json


class APIClient:
    """Client for making API requests"""
    
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()
        self.pool = PoolManager(num_pools=10)
    
    def get(self, endpoint, params=None):
        """Make GET request"""
        url = f"{self.base_url}/{endpoint}"
        response = self.session.get(url, params=params)
        return response.json()
    
    def post(self, endpoint, data=None):
        """Make POST request"""
        url = f"{self.base_url}/{endpoint}"
        response = self.session.post(url, json=data)
        return response.json()
    
    def download_resource(self, resource_id):
        """Download resource using urllib3"""
        url = f"{self.base_url}/resources/{resource_id}"
        response = self.pool.request('GET', url)
        return response.data


def fetch_github_repo(owner, repo):
    """Fetch GitHub repo info using requests"""
    url = f"https://api.github.com/repos/{owner}/{repo}"
    response = requests.get(url)
    return response.json()

