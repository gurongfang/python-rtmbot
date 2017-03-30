from bs4 import BeautifulSoup
file_path = ''
defect_name = ''
link = ''

if defect_name == '' or link == '':
    exit(0)

html_file = open(file_path)
html = html_file.read()
html_file.close()

soup = BeautifulSoup(html)
tbody = soup.body.table.tbody
entry = BeautifulSoup('<tr><th>'+defect_name+'</th><th><p><a href="'+link+'">Link</a></p></th></tr>')
tbody.append(entry)

html_file = open(file_path, "w")
html_file.write(soup.prettify())
html_file.close()