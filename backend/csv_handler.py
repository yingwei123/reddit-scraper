import csv

def downloadAsCSV(data, name):
    name = f'{name}.csv'
    with open(name, mode='w', newline='', encoding='utf-8') as file:
        fieldnames = ['author', 'body', 'created_utc', 'id', 'parent_id']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for comments in data:
            for comment in comments:
                writer.writerow(comment)
