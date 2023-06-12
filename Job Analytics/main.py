import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver_service = Service(executable_path='C:/Users/rahul/Downloads/chromedriver.exe')
website = 'https://www.instahyre.com/search-jobs'
driver = webdriver.Chrome(options=options, service=driver_service)
driver.get(website)

limit = 200
start = 0
Title = []
company_name = []
locations = []
employee = []
Date_of_establishment = []
hr= []
Descriptions = []
Skill = []
while start < limit:
    new = 0
    start += 1
    time.sleep(2)
    new = driver. find_elements(By.XPATH, '//div[contains(@class,"imageblock profile-image col-md-3 col-sm-2 col-xs-2")]/a')
    try:
        for i in new:
            a = (i.get_attribute('href'))
            driver.get(a)
            time.sleep(2)
            heading = driver.find_element(By.XPATH, '//*[@id="floating-header"]/div[1]/h1')
            company = driver.find_element(By.XPATH, '//*[@id="floating-header"]/div[1]/h2')
            year = driver.find_element(By.XPATH, '//*[@id="employer-profile"]/div[2]/div/div/div[1]/div[2]/div[1]')
            Emp = driver.find_element(By.XPATH, '//*[@id="employer-profile"]/div[2]/div/div/div[1]/div[2]/div[2]')
            loc = driver.find_element(By.XPATH, '//*[@id="floating-header"]/div[1]/div/span[1]')
            HR = driver.find_element(By.XPATH, '//*[@id="employer-profile"]/div[2]/div/div/div[3]/div[1]/div/span/span[1]')
            Description = driver.find_element(By.XPATH, '//*[@id="job-description"]/div/div/p')
            Skills = driver.find_element(By.XPATH, '//*[@id="job-skills-description"]')
            find = Skills.find_elements(By.TAG_NAME, 'li')
            a=[]
            for i in find:
                a.append(i.text)
            my_list = list(Skills.text)
            Title.append(heading.text)
            company_name.append(company.text)
            Date_of_establishment.append(year.text[11:])
            employee.append(Emp.text)
            hr.append(HR.text)
            locations.append(loc.text)
            Descriptions.append(Description.text[10:])
            Skill.append(a)
            driver.back()
        pagination = driver.find_element(By.XPATH, "//div[contains(@class,'pagination ng-scope')]")
        page = pagination.find_elements(By.TAG_NAME, 'li')
        a = page[-1]
        a.click()
    except StaleElementReferenceException:
        if start == limit:
            raise
        else:
            driver.back()
    except NoSuchElementException:
        driver.back()

data = {'Title': Title, 'Company Name': company_name, 'Locations': locations,
        'Number of Employees': employee, 'Date of Establishment': Date_of_establishment,
        'HR': hr, 'Descriptions': Descriptions, 'Skills': Skill}
df = pd.DataFrame(data)
df.to_csv('scraped_new_final.csv', index=False)
# print(df)
# print(Title)
# print(company_name)
# print(locations)
# print(employee)
# print(hr)
# print(Descriptions)
# print(Skill)
# print(Date_of_establishment)



