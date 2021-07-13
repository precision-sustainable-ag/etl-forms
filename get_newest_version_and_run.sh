#!/bin/sh

cd /home/azureuser/etl-forms
git checkout master
git pull
python3 parse_forms.py