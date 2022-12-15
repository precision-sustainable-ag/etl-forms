#!/bin/sh

# run and log parse_forms.py
cd /home/azureuser/etl-forms
git checkout main 
git pull # > logs/tempfile.log
python3 run_live.py # >> logs/tempfile.log
# echo '\n' >> logs/tempfile.log

# # prepend to main.log
# cat logs/main.log >> logs/tempfile.log
# cp logs/tempfile.log logs/main.log

