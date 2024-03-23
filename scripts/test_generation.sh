#!/bin/bash

cookiecutter --no-input --overwrite-if-exists .

cd nebulaplugins-collection

conda create -n "nebulaplugins-collection" python=3.9 -y

eval "$(conda shell.bash hook)"

conda activate nebulaplugins-collection

pip install -e ".[dev]"