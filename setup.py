'''
Essential part of packaging and distributing python packages. used by setup tools
to define the configuration of your project, such as its dependencies and more
'''

from setuptools import find_packages,setup 
from typing import List 

def get_requirements()->List[str]:
    '''
    This function will return list of requirements
    '''
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()
                # ignore empty lines and -e
                if requirement and requirement!='-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print('Requirement.txt file not found')

    return requirement_lst

# print(get_requirements())

setup(
    name = 'NetworkSecurity',
    version='1.0.0.0',
    author='Dhanush Garrepalli',
    author_email='inform2dhanush@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements()
)