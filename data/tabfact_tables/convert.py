import csv, json

f = open('name_list.txt','r')
titles = {}
with open('table_to_page.json') as title_map:
  titles = json.load(title_map)
print(len(titles))
for name in f:
    name = name.strip()
    title = titles[name][2]
    table_name = './all_csv/' + name
    d = {}
    d[str((0,0))] = title
    with open(table_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='#')
        row_no = 0
        for row in csv_reader:
            row_no = row_no+1
            col_no = 0
            for col in row :
                key = (row_no,col_no)
                d[str(key)] = col
                col_no = col_no + 1
    json_file = "./tabfact_jsons/" + str(name.replace('.html.csv','.json'))
    with open(json_file, 'w', encoding='utf-8') as file:
        json.dump(d, file, ensure_ascii=False, indent=2)