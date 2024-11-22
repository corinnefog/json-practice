
import json

with open("/Users/corinnefogarty/json-practice/data/schacon.repos.json", 'r') as file:
    data = json.load(file)

with open('chacon.csv', 'w') as csv_file:
    csv_file.write('name,html_url,updated_at,visibility\n')
    
    for repo in data[:5]:
        name = repo.get('name', '')
        html_url = repo.get('html_url', '')
        updated_at = repo.get('updated_at', '')
        visibility = repo.get('visibility', '')
        
        line = f"{name},{html_url},{updated_at},{visibility}\n"
         
        csv_file.write(line)

print("CSV file was created.")
