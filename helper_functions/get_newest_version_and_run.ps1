Set-Location C:\Users\mikah\Documents\etl-forms
git checkout master 
git pull > logs\tempfile.txt
python parse_forms.py >> logs\tempfile.txt
Write-Output '\n' >> logs\tempfile.txt
Get-Content logs\logs.txt >> logs\tempfile.txt
Copy-Item logs\tempfile.txt logs\logs.txt