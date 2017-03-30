# from bs4 import BeautifulSoup
#
# crontable = []
# outputs = []
# file_path = ''
#
#
# def process_message(data):
#     if data['channel'].startswith("D"):
#         if data['text'].startswith("DE") or data['text'].startswith("US"):
#             param = data['text'].split(' ')
#             if len(param) < 2:
#                 return
#
#             defect_name = param[0]
#             link = param[1]
#
#             outputs.append([data['channel'], 'Done! '+defect_name+' has completed'])
#
#             if defect_name == '' or link == '' or file_path == '':
#                 return
#
#             html_file = open(file_path)
#             html = html_file.read()
#             html_file.close()
#
#             soup = BeautifulSoup(html)
#             tbody = soup.body.table.tbody
#             entry = BeautifulSoup(
#                 '<tr><th>' + defect_name + '</th><th><p><a href="' + link + '">Link</a></p></th></tr>')
#             tbody.append(entry)
#
#             html_file = open(file_path, "w")
#             html_file.write(soup.prettify())
#             html_file.close()
