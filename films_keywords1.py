# This program works faster then previous on 27%
import time
def film_analysis():
    """
    1. Function print intro
    2. Recieve name_file from user, open it
    3. Create keywords and film_keywords generators
    4. Find freq_keywords
    5. Find number of films with these keywords
    6 Close file
    """
    print_intro()
    f = open(my_file(), 'r')
    keywords = generator_keywords(f)
    film_keywords = generator_film_keywords(f)
    keyw1, keyw2 = freq_keywords(keywords)
    number_films = len(find_films(film_keywords, keyw1, keyw2))
    print_report(number_films, keyw1, keyw2)
    f.close()

def my_file():
    return input('Please type the file name and path to file if need: ')

def print_intro():
    print("This program find number of films")
    print("that use two keywords with maximal frequency.")
    print("This program use data from imdb database file keywords.list.")

def print_report(number_films, keyw1, keyw2):
    """
    Print a report on the number of films
    """
    print("\nFilms analysis result")
    print("Keywords {0} and {1} are using".format(keyw1, keyw2))
    print("in {0} films".format(number_films))

def generator_keywords(f):
    """
    (file) -> generator
    Return tuples of keywords one by one
    Also read all needed lines
    """
    for line in iter(f.readline, '   keywords in use:\n'):
        pass
    for line in iter(f.readline, '5: Submission Rules\n'):
        line = line.strip().split("\t")
        line = filter(lambda w: w != '', line)
        line = map(lambda w: (int(w.split()[1][1:-1]), w.split()[0]), line)
        for w in line:
            yield w

def generator_film_keywords(f):
    """
    (file) -> generator
    Return tuples of film_keywords one by one
    where first value is name of film and the second one is word
    Also read all needed lines
    """
    for line in iter(f.readline, '8: THE KEYWORDS LIST\n'):
        pass
    for line in f:
        film, keyword = line.strip().split("\t")[0], \
        line.strip().split("\t")[-1]
        yield (film, keyword)
        
def freq_keywords(keywords):
    """
    (generator) -> tuple
    Find to freq keywords
    """
    m1 = 0
    keyw1 = 0
    for i in keywords:
        if i[0] > m1:
            m2, m1 = m1, i[0]
            keyw2, keyw1 = keyw1, i[1]
        elif i[0] > m2:
            m2, keyw2 = i[0], i[1]

    return keyw1, keyw2
    
def find_films(film_keywords, keyw1, keyw2):
    """
    (generator, str, str) -> set
    Return set which include all films
    which have keyw1 and keyw2
    """
    s = set()
    for w in film_keywords:
        if (w[1] == keyw1) or (w[1] == keyw2):
            s.add(w[0])
    return s

film_analysis()

