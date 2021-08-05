#!/bin/sh

# run and log parse_forms.py
cd /home/azureuser/etl-forms
git checkout master 
git pull > logs/tempfile.log
python3 parse_forms/parse_forms.py >> logs/tempfile.log
echo '\n' >> logs/tempfile.log

# run and log push_to_prod.py
python3 push_to_prod/push_to_prod.py >> logs/tempfile.log
echo '\n' >> logs/tempfile.log
cat logs/logs.log >> logs/tempfile.log
cp logs/tempfile.log logs/logs.log

