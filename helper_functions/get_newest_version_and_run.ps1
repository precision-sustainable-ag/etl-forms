# run and log parse_forms.py
Set-Location C:\Users\mikah\Documents\etl-forms
git checkout master 
# git pull > logs\tempfile.txt
python parse_forms\parse_forms.py
# Write-Output "`n" >> logs\tempfile.txt

# run and log push_to_prod.py
python push_to_prod\push_to_prod.py
# Write-Output "`n" >> logs\tempfile.txt
# Get-Content logs\logs.txt >> logs\tempfile.txt
# Copy-Item logs\tempfile.txt logs\logs.txt
