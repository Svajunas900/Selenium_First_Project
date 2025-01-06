from DbConnection import PostgresDbConnection
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

postgres_db = PostgresDbConnection()
cursor = postgres_db.cursor()

url = "https://github.com/Svajunas900?tab=repositories"

driver = webdriver.Chrome()

driver.get(url)

title = driver.title

print(title)
counter = 1
repo = driver.find_element(by=By.XPATH, value='//*[@id="user-repositories-list"]/ul/li[1]/div[1]/div[1]/h3/a')

def add_all_files():
   row = 0
   file = driver.find_element(by=By.XPATH, value=f'//*[@id="folder-row-{row}"]/td[2]/div/div/div/div/a')
   empty_list = []
   while True:
      try:
         empty_list.append(file.text)
         row += 1
         file = driver.find_element(by=By.XPATH, value=f'//*[@id="folder-row-{row}"]/td[2]/div/div/div/div/a')
      except:
         print("No Such file")
         break
   return empty_list

while repo:
   try:
      repo = driver.find_element(by=By.XPATH, value=f'//*[@id="user-repositories-list"]/ul/li[{counter}]/div[1]/div[1]/h3/a')
      repo_name = repo.text
      repo.click()
      WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="folder-row-0"]/td[2]/div/div/div/div/a'))
            )
      file_list = add_all_files()
      print(repo_name, file_list)
      driver.back()
   except Exception:
      print(f"Error with repo {counter}: {Exception}")
      repo = None
      print(repo)
   counter += 1
   print(counter)


driver.quit()