#!/bin/bash
GREEN="\e[32m"
RESET="\e[0m"
set -e
echo "Installing test dependencies..."
pip install -q -r requirements-test.txt || exit 1

echo "Running pytest (UnitTest)..."
set -e python -m pytest app.py || exit 1

echo "Running flake8(Linter)..."
python -m flake8 app.py || exit 1

echo "Running isort(Organizing import)..."
python -m isort app.py || exit 1

echo "Running mypy(Static type checking)..."
python -m mypy app.py || exit 1

echo "Running bandit(vulnerability test)..."
python -m bandit -r app.py || exit 1

echo -e "${GREEN}============= All checks passed! ===============${RESET}"
echo "Removing test Dependencies"
pip uninstall -r requirements-test.txt -y || exit 1