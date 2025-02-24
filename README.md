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