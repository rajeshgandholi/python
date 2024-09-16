current_movies = {'RRR': '11:00am',
                  'Bahubali': '1:00pm',
                  'Pushpa': '3:00pm',
                  'SVSC': '5:00pm'
                  }

print('We are currently showing the following movies: ')
for movie_names in current_movies:
    print(movie_names)

movie = input("What movie would you like the showtime for? ")
showtime = current_movies.get(movie)

if showtime is None:
    print("Requested movie isn't playing !!")
else:
    print('Showtime for the movie ', movie, ' is: ', showtime)  # noqa
