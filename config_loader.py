"""
Configuration loader using vulnerable YAML parsing.
"""
import yaml
import os


def load_app_config(config_path):
    """Load application configuration from YAML file"""
    if not os.path.exists(config_path):
        return get_default_config()
    
    with open(config_path, 'r') as f:
        # Vulnerable: using yaml.load without Loader
        config = yaml.load(f)
    
    return config


def get_default_config():
    """Return default configuration"""
    return {
        'app_name': 'wellarchitect-test',
        'version': '1.0.0',
        'debug': True,
        'database': {
            'host': 'localhost',
            'port': 5432,
            'name': 'testdb'
        }
    }


def parse_yaml_string(yaml_str):
    """Parse YAML from string (vulnerable)"""
    return yaml.load(yaml_str)


def save_config(config, config_path):
    """Save configuration to YAML file"""
    with open(config_path, 'w') as f:
        yaml.dump(config, f, default_flow_style=False)

