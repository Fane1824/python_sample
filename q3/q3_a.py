from bs4 import BeautifulSoup
import requests
import re
import matplotlib.pyplot as plt
from collections import Counter
import mysql.connector
import matplotlib.pyplot as plt

url = 'https://www.imdb.com/chart/toptv/'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
response = requests.get(url, headers=headers)
html_content = response.content
soup = BeautifulSoup(html_content, "html.parser")
response.status_code

movies = soup.find_all(class_='ipc-title__text')
ratings = soup.find_all(class_='ipc-rating-star')
movie_list = []
for i in movies[2:-12]:
    movie_list.append(i.get_text())
ratings_list = []
for i in ratings[::2]:
    ratings_list.append(i.get_text())
rating_list = []
for rating in ratings_list:
    rating_list.append(rating.split("\xa0")[0])
num_ratings = []
for rating in ratings_list:
    num_ratings.append(rating.split('\xa0')[1][1:-1])

eps = []
for i in soup.find_all(class_="sc-b189961a-8 kLaxqf cli-title-metadata-item"):
    eps.append(i.get_text())
ep = []
for episode in eps:
    parts = episode.split(' ')
    if len(parts) == 2 and parts[1] == 'eps':
        ep.append(int(parts[0]))

genre = str(soup.select('body'))
pattern = r'"titleGenres":{"genres":\[(.*?)\]'
matches = re.findall(pattern, genre, re.DOTALL)
genres = []
for i in matches:
    temp = re.findall(r'"text":"([^"]+)"', i)
    genres.append(temp)

data_list = []

for i in range(len(movie_list)):
    data = {
        "film_title": movie_list[i].split('.')[1][:50],
        "film_rating": rating_list[i],
        "number_of_ratings": num_ratings[i],
        "number_of_episodes": ep[i],
        "film_genre": genres[i]
    }
    data_list.append(data)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Toor123",
    port = "3306",
    database="top-250-shows"
)
user_db = db.cursor()

sql = "DELETE FROM shows"
user_db.execute(sql)
db.commit()

for data in data_list:
    title = str(data["film_title"])
    rating = str(data["film_rating"].strip())
    num_ratings = str(data["number_of_ratings"]).strip()
    num_episodes = str(data["number_of_episodes"]).strip()
    command = "SELECT COUNT(id) FROM shows;"
    user_db.execute(command)
    count = str(user_db.fetchone()[0] + 1)
    genre = ','.join(data["film_genre"]) 
    sql = "INSERT INTO shows (id, title, rating, num_episodes, num_ratings, genres) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (count, title, rating, num_episodes, num_ratings, genre)
    user_db.execute(sql, val)

db.commit()
user_db.execute("SELECT genres FROM shows")
genre_data = user_db.fetchall()
individual_genres = []
for genres_str in genre_data:
    genres_list = [genre.strip() for genre in genres_str[0].split(',')]
    individual_genres.extend(genres_list)
genre_counts = Counter(individual_genres)
genres = list(genre_counts.keys())
counts = list(genre_counts.values())
plt.figure(figsize=(10, 6))
plt.bar(genres, counts, color='skyblue')
plt.xlabel('Genres')
plt.ylabel('Number of TV Shows')
plt.title('Number of TV Shows by Genre')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

user_db.execute("SELECT num_episodes FROM shows")
episode_data = user_db.fetchall()

episodes_counts = Counter([int(episode[0]) for episode in episode_data])
num_episodes = sorted(episodes_counts.keys())
frequency = [episodes_counts[num] for num in num_episodes]
plt.figure(figsize=(10, 6))
plt.plot(num_episodes, frequency, marker='o', color='orange', linestyle='-')
plt.xlabel('Number of Episodes')
plt.ylabel('Frequency Count')
plt.title('Frequency Count of TV Shows by Number of Episodes')
plt.grid(True)
plt.tight_layout()
plt.show()



