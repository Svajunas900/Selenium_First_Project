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
git_repo = {}

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
      files_list = add_all_files()
      files = " ".join(files_list)
      git_repo[repo_name] = files_list
      driver.back()
   except Exception:
      print(f"Error with repo {counter}: {Exception}")
      repo = None
      print(repo)
   counter += 1


for key, value in git_repo.items():
   files = " ".join(value)
   cursor.execute("INSERT INTO git_repo (repo_name, files_list) VALUES (%s, %s)", (key, files))

cursor.close()
postgres_db.commit()
driver.quit()