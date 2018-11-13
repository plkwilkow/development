from selenium import webdriver


def linki(i):
    linczek = '//*[@id="articleBody"]/div[1]/div[2]/div/form/div[1]/table/tbody/tr[' + str(i) + ']/td[2]/a'
    return linczek


tytul = input()
driver = webdriver.Chrome()
driver.get("https://www.filmweb.pl/" + tytul + "/cast/actors")

strona1 = list()
strona2 = list()

driver.find_element_by_xpath('//*[@id="goToLink"]').click()
driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[3]/button').click()

for i in range(1, 11):
    elem = driver.find_element_by_xpath(linki(i))
    strona1.append(elem.text)

tytul = input()
driver.get("https://www.filmweb.pl/" + tytul + "/cast/actors")

for i in range(1, 11):
    elem = driver.find_element_by_xpath(linki(i))
    strona2.append(elem.text)

for i in range(0, 10):
    for j in range(0, 10):
        if strona1[i] == strona2[j]:
            print(strona2[j])

print(strona1)
print(strona2)

driver.get("https://www.filmweb.pl/")
link = "https://www.filmweb.pl/search?q=" + "peaky"
driver.get(link)
cos = driver.find_element_by_class_name("filmPreview__link").get_attribute('href')
print(cos)
driver.get(cos)

driver.close()
