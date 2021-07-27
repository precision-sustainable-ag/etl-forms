#!/bin/sh

# run and log parse_forms.py
cd /home/azureuser/etl-forms
git checkout master 
git pull > logs/tempfile.txt
python3 parse_forms/parse_forms.py >> logs/tempfile.txt
echo '\n' >> logs/tempfile.txt

# run and log push_to_prod.py
python3 push_to_prod/push_to_prod.py >> logs/tempfile.txt
echo '\n' >> logs/tempfile.txt
cat logs/logs.txt >> logs/tempfile.txt
cp logs/tempfile.txt logs/logs.txt

