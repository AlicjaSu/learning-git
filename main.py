class Film:
   def __init__(self, title, year, type, play_number):
       self.title = title
       self.year = year
       self.type = type
       self.play_number = play_number
    

class Series(Film):
    def __init__(self, episode , season, *args, **kwargs):
         super().__init__(*args, **kwargs)
         self.episode = episode
         self.season = season
   


from random import *

titlesF=['Pulp Fiction', 'Django', 'The Piano','Kill Bill','Bridget Jones'] 
titlesS=['Pacific', 'Tchernobyl','Queens Gambit','Friends','Stranger Things']

types=['Action','Thriller','Family','Romantic','Science_Fiction','Comedy', 'Adventure']


def create_film(quantity):
    storage = []
    for i in range(int(quantity)):
            film1 = Film(title=titlesF[i], year=randint(1900,2021), type=types[i], play_number=randint(0,1000))
            storage.append(film1)
    return storage

def create_series(quantity):
    storage = []
    for i in range(int(quantity)):
            series1 = Series(title=titlesS[i], year=randint(1900,2021), type=types[i] , play_number=randint(0,1000),episode=randint(0,250),season=randint(0,30))
            storage.append(series1)
    return storage

def create_movie (quantityF, quantityS):
    storage = []
    storage= create_film(quantityF)+create_series(quantityS)
    return storage

def get_film(title,year):
        film_info=''
        return film_info+title+'('+str(year)+')'

def get_series(title,season,episode):
        series_info=''
        return series_info+title+' '+'S'+str(season)+'E'+str(episode)

def play(play_number):
       play_number+=1
       return play_number
def get_film_t(title):
        film_info=''
        return film_info+title
def search_f(title):
       if get_film_t(title) == title:
          return title
def get_series_t(title):
        series_info=''
        return series_info+title 
def search_s(title):
    if get_series_t(title) == title:
        return title

def generate_views(film_series):
    random.shuffle(film_series)
    film_series.play_number[1]=randint(1,100)
def generate_views_10(film_series):
    for i in range(0,9):
     generate_views(film_series)
def top_titles (film_series):
    storage=[]
    storage=film_series.sort(key=lambda film_series: film_series.play_number)
    return storage     
print("Biblioteka filmów")
movie=create_movie(5,5)
for i in movie:
    print(i.title)
    print(i.type)
    print(i.year)
    print(i.play_number)   
    print(play(i.play_number))
    print(get_film(i.title,i.year))
    print(get_series(i.title,i.season,i.episode))
#movie_top=top_titles(movie)
#for j in movie_top:
    #print(j.title)
    #print(j.type)
    #print(j.year)
    #print(j.play_number)   
    #print(play(j.play_number))
    #print(get_film(j.title,j.year))
    #print(get_series(j.title,j.season,j.episode))







 

    


