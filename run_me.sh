#!/bin/bash

export ADOPAT="MyDefaultToken"

py3=$(which python3)



$py3 ~/repos/project-builder-python/parser.py --token $ADOPAT

