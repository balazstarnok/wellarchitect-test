from setuptools import setup, find_packages

setup(
    name="wellarchitect-test",
    version="1.0.0",
    description="Vulnerable Python application for security testing",
    author="Test",
    packages=find_packages(),
    install_requires=[
        "requests==2.25.0",
        "flask==1.1.1",
        "urllib3==1.25.8",
        "pyyaml==5.3.1",
        "jinja2==2.11.2",
        "cryptography==2.9",
    ],
    python_requires=">=3.8",
)

