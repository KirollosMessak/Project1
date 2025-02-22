import os
# interact with operating system
from pathlib import Path 
# handle file and directory path and forward and backslach for windows and linux
print(Path('a/b/c.txt'))
import logging
list_of_files =[
    '.github/workflows/.gitkeep',
    'src/__init__.py',# to make it a python package
    'src/components/__init__.py',#components of pipeline stages
    'src/components/data_ingestion.py',
    'src/components/data_transformation.py',
    'src/components/model_trainer.py',
    'src/components/model_evaluation.py',
    'src/pipeline/__init__.py',
    'src/pipeline/training_pipeline.py',
    'src/pipeline/prediction_pipeline.py',
    'src/utils/__init__.py',
    'src/utils/utils.py',#store helper functions that are reused 
                  #across different parts of your MLOps
    'src/logger/logging.py',
    'src/exeption/exception.py', 
    'test/unit_testing/__init__.py',#for single unit testing
    'test/integration_testing/__init__.py',#for intire system testing
    'init_setup.sh',#to automate initial setup install dependencies and create VE 
    'requirements.txt',
    'requirements_dev.txt',
    'setup.py',
    'setup.cfg',
    'pyproject.toml',
    'tox.ini',#to test code in a local environment
    'experiment/experiments.ipynb'# to do experiments
]

for file_path in list_of_files:
    file_path = Path(file_path)
    filedir, filename = os.path.split(file_path)
    if filedir != '':
        os.makedirs(filedir, exist_ok=True)
        logging.info(f'creating directory : {filedir} for file:{filename}')

    if (not os.path.exists(file_path)) or (os.path.getsize(file_path)==0):
        with open(file_path, 'w') as f:
            pass #create an empty file