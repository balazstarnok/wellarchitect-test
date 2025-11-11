"""
Image processing module with vulnerable Pillow dependency.
Tests import detection and usage of critically vulnerable package.
"""
from PIL import Image
import io
import numpy as np
import pandas as pd


def process_image(image_path):
    """
    Process image using vulnerable Pillow library
    This should trigger reachable CVE detection because:
    1. Pillow 7.0.0 has critical CVEs
    2. This file imports PIL
    3. The function actively uses it
    """
    img = Image.open(image_path)
    
    # Convert to numpy array (tests numpy import)
    img_array = np.array(img)
    
    # Resize image - vulnerable operation
    resized = img.resize((800, 600))
    
    return resized


def load_image_from_bytes(data):
    """
    Load image from bytes - another vulnerable usage
    """
    img = Image.open(io.BytesIO(data))
    return img


def create_thumbnail(image_path, size=(128, 128)):
    """
    Create thumbnail using vulnerable Pillow
    """
    img = Image.open(image_path)
    img.thumbnail(size)
    return img


def analyze_image_data(image_path):
    """
    Analyze image using pandas (tests pandas import and usage)
    """
    img = Image.open(image_path)
    img_array = np.array(img)
    
    # Convert to pandas DataFrame
    df = pd.DataFrame(img_array.reshape(-1, 3), columns=['R', 'G', 'B'])
    
    stats = {
        'mean_red': df['R'].mean(),
        'mean_green': df['G'].mean(),
        'mean_blue': df['B'].mean(),
        'std_red': df['R'].std()
    }
    
    return stats

