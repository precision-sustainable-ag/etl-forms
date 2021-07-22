#!/bin/sh

cd /home/azureuser/etl-forms
git checkout master 
git pull > ../tempfile
python3 parse_forms.py >> ../tempfile
echo '\n' >> ../tempfile
cat ~/cron.log >> ../tempfile
cp ../tempfile ~/cron.log

