#!/bin/sh
CODE_PATH=./src/app

echo "Black stuff"
black --check --line-length=79 $CODE_PATH || exit 1

echo " "
echo "Isort stuff"
isort --check --profile black $CODE_PATH || exit 1

echo " "
echo "Mypy stuff"
mypy --explicit-package-bases --ignore-missing-imports $CODE_PATH || exit 1