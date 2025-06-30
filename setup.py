from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements if req.strip()]
    return requirements

setup(
    name='mygenericproject',
    version='0.0.1',
    author='Risha',
    author_email='rishagupta2263@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
