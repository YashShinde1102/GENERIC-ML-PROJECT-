from setuptools import find_packages,setup
from typing import List


HYPEN_E_DOT='-e.'
def get_requirements(file_path:str)->List[str]:

    """
    this function returs the list of requirements and setup.py helps to build packages and is 
    triggered by -e. in requirements.txt 
    """
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n", " ") for req in requirements]
    
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
  
    return requirements



setup(
name="ML project",
version="0.0.1",
author="Yash",
author_email="116yash@gmail.com",
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)