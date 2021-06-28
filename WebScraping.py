import sys
# from PyQt4.QtGui import QApplication

from bs4 import BeautifulSoup
from requests import get


#URL = "https://app.studiuje.it/user"
URL = 'https://edu.dokodu.dev/pystart-pl-dwoch-prowadzacych-i-python/'
# URL = 'https://docs.python.org/3/library/stdtypes.html'
page = get(URL)
bs = BeautifulSoup(page.content, 'html.parser')

result = bs.find_all('div', id='html')
#result = bs.find('div', class_='list-group-item active')
print(result)

# for modul in bs.find_all('div', class_='menu_glowne'):
#     print(modul)
#     break


