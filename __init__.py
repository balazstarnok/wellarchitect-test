"""
Wellarchitect Test - Vulnerable Python Application Package
"""

__version__ = "1.0.0"
__author__ = "Test"

# Import main components to make them available at package level
from .app import app, fetch_data
from .utils import download_file, load_yaml_config, encrypt_data
from .api_client import APIClient, fetch_github_repo
from .config_loader import load_app_config, parse_yaml_string

__all__ = [
    'app',
    'fetch_data',
    'download_file',
    'load_yaml_config',
    'encrypt_data',
    'APIClient',
    'fetch_github_repo',
    'load_app_config',
    'parse_yaml_string',
]

