from DbConnection import PostgresDbConnection
import selenium


postgres_db = PostgresDbConnection()
cursor = postgres_db.cursor()

cursor.execute("""CREATE TABLE git_repo(
       repo_id SERIAL PRIMARY KEY,
       repo_name VARCHAR(255), 
       files_list VARCHAR(255)
       )""")


cursor.close()
postgres_db.commit()