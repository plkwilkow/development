from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def linki(i):
    linczek = '//*[@id="articleBody"]/div[1]/div[2]/div/form/div[1]/table/tbody/tr[' + str(i) + ']/td[2]/a'
    return linczek


def otwieranie_strony(search):
    driver.find_element_by_xpath('//*[@id="searchOpener"]/i').click()
    elem = driver.find_element_by_name("q")
    elem.send_keys(search)
    elem.send_keys(Keys.RETURN)
    cos = driver.find_element_by_class_name("filmPreview__link").get_attribute('href')
    driver.get(cos)
    driver.find_element_by_xpath('//*[@id="articleBody"]/div[1]/a[2]').click()


print("Podaj pierwszy film: ")
search1 = input()
print("Podaj drugi film: ")
search2 = input()

strona1 = list()
strona2 = list()

driver = webdriver.Chrome()
driver.get("https://www.filmweb.pl/")
driver.find_element_by_xpath('//*[@id="goToLink"]').click()
driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[3]/button').click()

otwieranie_strony(search1)
for i in range(1, 11):
    elem = driver.find_element_by_xpath(linki(i))
    strona1.append(elem.text)

driver.get("https://www.filmweb.pl/")

otwieranie_strony(search2)
for i in range(1, 11):
    elem = driver.find_element_by_xpath(linki(i))
    strona2.append(elem.text)

for i in range(0, 10):
    for j in range(0, 10):
        if strona1[i] == strona2[j]:
            print("Ten aktor się powtarza: " + strona2[j])

driver.close()
