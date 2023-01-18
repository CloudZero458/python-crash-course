def display_message():
    print('\nI\'m learning about functions in this chapter')
display_message()

def favorite_book(title):
    print(f'\nMy favorite book is {title.title()}.')

favorite_book('harry potter and the goblet of fire')

def make_shirt(size, text):
    print(f't-shirt size is {size} with the text "{text}".')

make_shirt('xl', 'killer')
make_shirt(text = 'killer',size='xl')

def make_shirt(text, size='large'):
    print(f't-shirt size is {size} with the text "{text}".')

make_shirt('python is my favorite language')

def make_shirt(size, text='python is my favorite language'):
    print(f't-shirt size is {size} with the text "{text}".')

make_shirt('xxl')

def describe_city(city, country='America'):
    print(f'{city.title()} is in {country.title()}')

describe_city('baltimore')
describe_city('barcelona', 'spain')

def city_country(city, country):
    return f'{city}, {country}'

location = city_country('baltimore', 'maryland').title()
print(location)

def make_album(artist, title, year):
    album = {'artist': artist.title(),'title': title.upper(), 'year': year}

    return album

album = make_album('joyner lucas','adhd', 2020)
print(album)

def user_album(artist, title, year,song_count = None):
    album = {'artist': artist.title(),'title': title.upper(), 'year': year, 'song_count': song_count}

    return album

while True:
    print('\nenter the artist, title, year, and song count(optional) for an album \n(enter "x" to quit)')

    artist = input('\nartist: ')

    if artist == 'x':
        break

    title = input('\ntitle: ')

    if title == 'x':
        break
    year = input('\nyear: ')
    if year == 'x':
        break
    song_count = input('\nsong count: ')

    if song_count== 'x':
        break
    album = user_album(artist, title, year, song_count)
    print(f'\n{album}')
