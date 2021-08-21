import requests
from bs4 import BeautifulSoup

URL = 'https://www.timeout.com/newyork/movies/best-movies-of-all-time'

response = requests.get(URL)
response.raise_for_status()
website_data = response.text

soup = BeautifulSoup(website_data, 'html.parser')
all_movies = soup.find_all(name='a', class_='xs-text-charcoal decoration-none')

all_movies = [movie.getText().strip() for movie in all_movies]

numbers = []
names = []
for movie in all_movies:
    strip = movie.strip('.\xa0')
    print(strip)
    numbers.append(all_movies.index(movie) + 1)
    names.append(strip[strip.index(' '):])


with open('movies.txt', mode='a') as f:
    for i in range(len(names)-1):
        f.write(f"{numbers[i]}) {names[i]}\n")