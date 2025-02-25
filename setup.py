from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

with open ('README.md','r', encoding ='utf-8') as f:
    long_description = f.read()

setup(
    Repo_name= 'MongoDBpckg',
    Pkg_name='MongoConnection',
    version='0.0.1',
    author_name='KirollosMagdy',
    author_email='kirolloskhella8@gmail.com',
    url ='https://github.com/KirollosMessak',
    pkg_dir = {'':'src'},
    install_requires=["scikit-learn","pandas","numpy"],
    packages=find_packages(where='src'),
    
)