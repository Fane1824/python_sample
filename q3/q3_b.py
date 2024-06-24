import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Toor123",
    port = "3306",
    database="top-250-shows"
)
user_db = db.cursor()

genres_input = input("Enter genres to search for: ")
g = []
for genre in genres_input.split():
    g.append(genre.title())
rating_input = input("Enter rating limits: ")
r = []
for item in rating_input.split():
    r.append(float(item))
episode_input = input("Enter episode count limits: ")
e = []
for item in episode_input.split():
    e.append(int(item))

ge=''
for i in g:
    ge+=f'genres LIKE "%{i}%" OR '
ge = ge[:-4]
query = f'SELECt * FROM shows WHERE {ge} and rating>={r[0]} and rating<={r[1]} and num_episodes>={e[0]} and num_episodes<={e[1]};'
user_db.execute(query)
results = user_db.fetchall()
dic = {}
for row in results:
    print(row)
    dic[row[1]]=float(row[2])