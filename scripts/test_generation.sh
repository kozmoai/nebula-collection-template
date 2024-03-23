#!/bin/bash

cookiecutter --no-input --overwrite-if-exists .

cd nebula-collection

conda create -n "nebula-collection" python=3.9 -y

eval "$(conda shell.bash hook)"

conda activate nebula-collection

pip install -e ".[dev]"