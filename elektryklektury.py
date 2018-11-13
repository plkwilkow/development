from selenium import webdriver
import xlwt

driver = webdriver.Firefox()
driver.get("http://zse.bialystok.pl/biblioteka/lektury/")


book = xlwt.Workbook(encoding="utf-8")
sheet1 = book.add_sheet("Wykaz lektur")

elem = driver.find_element_by_xpath('//*[@id="post-680"]/div/div/div/ul[1]')
n = (elem.text.count("\n"))

for i in range(1, n+2):
        link = '//*[@id="post-680"]/div/div/div/ul[1]/li[' + str(i) + ']'
        elem = driver.find_element_by_xpath(link)
        print(elem.text)
        myslnik = elem.text.find("-")
        long_myslnik = elem.text.find("–")
        if myslnik != -1:
            sheet1.write(i - 1, 0, elem.text[0:myslnik])
            sheet1.write(i - 1, 1, elem.text[myslnik+1:len(elem.text)])
        elif long_myslnik != -1:
            sheet1.write(i - 1, 0, elem.text[0:long_myslnik])
            sheet1.write(i - 1, 1, elem.text[long_myslnik + 1:len(elem.text)])
        else:
            spacja = elem.text.find(" ")
            spacja = elem.text.find(" ", spacja+1)
            sheet1.write(i - 1, 0, elem.text[0:spacja])
            sheet1.write(i - 1, 1, elem.text[spacja + 1:len(elem.text)])


book.save("raport1.xls")
driver.close()
