from setuptools import setup, find_packages

setup(
    name='my_package',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'holehe==1.61',
        'toutatis==1.24',
        'ignorant==1.2',
        'undetected-chromedriver==3.4.6',
        'tor==1.0.0',
        'stem==1.8.1',
        'tqdm==4.65.0',
        'selenium==4.8.3',
        'bs4==0.0.1',
        'termcolor==2.2.0',
        'geopy==2.3.0',
    ],
)