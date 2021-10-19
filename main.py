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

def get_film_info(title,year):
        film_info=''
        return film_info+title+'('+str(year)+')'

def get_series_info(title,season,episode):
        series_info=''
        return series_info+title+' '+'S'+str(season)+'E'+str(episode)

def get_movies(film_series):
        storage3=[]
        for v in range (0,9):
            if isinstance(v,Film):
                 film1=film_series[v]
                 storage3.append(film1)
        
        by_title = sorted(storage3, key=lambda Series: Series.title)
        return by_title


def get_series(film_series):
        storage4=[]
        for w in range (0,9):
            if isinstance(w,Series):
                 series1=film_series[w]
                 storage4.append(series1)
        by_title = sorted(storage4, key=lambda Film: Film.title)
        return by_title

def play(play_number):
       play_number+=1
       return play_number

def search(film_series,title):
    ver=2<1
    for k in range(1,10):
        if film_series[k].title==title:
            print('Film jest w bibliotece')
            ver=2>1
            return film_series[k]
    if not ver:
        print('Filmu nie ma w bibliotece')
  
          
def generate_views(film_series):
    u=0
    z=randint(1,10)
    film_series[z].play_number=randint(1,100)
    u=film_series[z].play_number
    return u

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
    if isinstance(i, Film):
      print(get_film_info(i.title,i.year))
    if isinstance(i, Series):
      print(get_series_info(i.title,i.season,i.episode))
print(generate_views(movie))
search(movie,'Kill Bill')
for x in get_movies(movie):
    print(x.title)
    print(x.type)
    print(x.year)
    print(x.play_number)
for y in get_series(movie):
    print(y.title)
    print(y.type)
    print(y.year)
    print(y.play_number)






#movie_top=top_titles(movie)
#for j in movie_top:
    #print(j.title)
    #print(j.type)
    #print(j.year)
    #print(j.play_number)   
    #print(play(j.play_number))
    #print(get_film(j.title,j.year))
    #print(get_series(j.title,j.season,j.episode))


 

    


