"""
Utility functions that use vulnerable packages.
"""
import requests
import yaml
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend


def download_file(url, dest):
    """Download file using vulnerable requests library"""
    response = requests.get(url, stream=True)
    with open(dest, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)
    return dest


def load_yaml_config(path):
    """Load YAML configuration (vulnerable to arbitrary code execution)"""
    with open(path) as f:
        # Using unsafe yaml.load - CVE-2020-14343
        return yaml.load(f)


def encrypt_data(data, key):
    """Encrypt data using vulnerable cryptography library"""
    # Using weak encryption mode
    cipher = Cipher(
        algorithms.AES(key),
        modes.ECB(),  # Weak mode
        backend=default_backend()
    )
    encryptor = cipher.encryptor()
    return encryptor.update(data) + encryptor.finalize()


def fetch_user_data(user_id):
    """Fetch user data from API using requests"""
    api_url = f"https://api.example.com/users/{user_id}"
    response = requests.get(api_url, timeout=5)
    return response.json()


def parse_config_string(config_str):
    """Parse YAML from string (vulnerable)"""
    return yaml.load(config_str)

