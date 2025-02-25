tox.ini local env to  test code  for developper tox.ini or CI/CD pipeline for running automated tests and linting in an MLOps or Python project
1️⃣ [gh-actions] → Defines Python versions for GitHub Actions
2️⃣ [testenv] → Defines a test environment with dependencies and commands
# Stop build if critical Python syntax errors exist
flake8 src --count --select=E9,F63,F7,F82 --show-source --statistics
# Allows all errors as warnings but enforces complexity ≤ 10 and max line length 127 chars.
flake8 src --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
# Ensures type correctness
mypy src/
# Runs unit tests (tests/unit/) and integration tests (tests/integration/) using pytest
setup.cfg: pkg metadata
# requirements_dev.txt we use for the testing
It makes it easier to install and manage dependencies for development and testing, separate from the dependencies required for production.

# difference between requirements_dev.txt and requirements.txt

requirements.txt is used to specify the dependencies required to run the production code of a Python project, while requirements_dev.txt is used to specify the dependencies required for development and testing purposes.

# tox.ini
We use if for the testing in the python package testing against different version of the python 

## how tox works tox enviornment creation
1. Install depedencies and packages 
2. Run commands
3. Its a combination of the (virtualenvwrapper and makefile)
4. It creates a .tox


# pyproject.toml
it is being used for configuration the python project it is a alternative of the setup.cfg file. its containts configuration related to the build system
such as the build tool used package name version author license and dependencies

# setup.cfg
In summary, setup.cfg is used by setuptools to configure the packaging and installation of a Python projec

# Testing python application
*types of testing*
1. Automated testing 
2. Manual testing

*Mode of testing*
1. Unit testing
2. Integration tests

*Testing frameworks*

1. pytest
2. unittest
3. robotframework
4. selenium
5. behave
6. doctest

# check with the code style formatting and syntax(coding standard)

1. pylint
2. flake8(it is best because it containt 3 library pylint pycodestyle mccabe)
3. pycodestyle

