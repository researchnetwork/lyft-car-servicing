from setuptools import setup, find_packages


setup(
    author='Henry Nwaogu',
    author_email= 'onlineinfomaticgroup@gmail.com',
    description= 'A package template for car servicing condtions based on battery and engine',
    long_description= 'File: README.md ',
    name= 'Lyftservices',
    url= 'www.aigeotech.com',
    version='1.1.0',
    
    packages=find_packages(include=['car_service'])


)

