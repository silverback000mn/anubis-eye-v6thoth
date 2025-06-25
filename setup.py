from setuptools import setup, find_packages

setup(
    name="anubis_eye",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "fastapi",
        "uvicorn",
        "pytz"
    ]
)
