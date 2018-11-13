from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import xlrd
from xlutils.copy import copy


def linki(tytul):
	link = 'https://www.taniaksiazka.pl/Szukaj/q-' + str(tytul)
	return link


driver = webdriver.Firefox()
driver.get("https://www.taniaksiazka.pl/")

book = xlrd.open_workbook("raport1.xls")
rb = xlrd.open_workbook("raport1.xls")
wb = copy(rb)

arkusz = book.sheet_by_name("Wykaz lektur")

for i in range(0, 45):
	tytul = (arkusz.row_values(i)[0] + arkusz.row_values(i)[1])
	elem = driver.find_element_by_name("q")
	elem.clear()
	elem.send_keys(tytul)
	elem.send_keys(Keys.RETURN)
	driver.get(linki(tytul))
	cena = driver.find_element_by_class_name('product-price')
	print(cena.text)
	s = wb.get_sheet(0)
	s.write(i, 2, cena.text)

wb.save('raport2.xls')
driver.close()
