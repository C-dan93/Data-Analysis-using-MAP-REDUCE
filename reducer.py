#!/usr/bin/env python3

# Student ID: okc00008

import sys
from collections import defaultdict

# Dictionary to store movies and their corresponding ratings for each year
movies_by_year = defaultdict(list)

minimum_votes = 10

# Initialize dictionaries to store the sum of ratings and counts for each unique key
rating_sum_dict = defaultdict(float)
count_sum_dict = defaultdict(int)

# Read each line of input
for line in sys.stdin:
    # Split the line into different pieces of information
    year, movie_title, rating, count = line.strip().split('\t')

    # Convert rating and count to numbers (float and int respectively)
    rating = float(rating)
    count = int(count)
    
    # Combine year and movie title as a key
    key = (year, movie_title)
    
    # Add the rating and count to the respective dictionaries
    rating_sum_dict[key] += rating
    count_sum_dict[key] += count

# Find the highest rated movies for each year
for key, rating_sum in rating_sum_dict.items():
    year, movie_title = key
    count_sum = count_sum_dict[key]
    
    # Calculate average rating
    average_rating = rating_sum / count_sum
    
    # Check if enough votes were received
    if count_sum >= minimum_votes:
        # Add movie and its average rating to the dictionary of movies by year
        movies_by_year[year].append((movie_title, average_rating))

# Print the highest rated movies for each year
for year, movies in movies_by_year.items():
    # Find the maximum rating for each year
    max_rating = max(movies, key=lambda x: x[1])[1]
    
    # Filter movies with the maximum rating
    highest_rated_movies = [(movie, rating) for movie, rating in movies if rating == max_rating]
    
    # Print each highest rated movie with its year and rating
    for movie_info in highest_rated_movies:
        movie_title, average_rating = movie_info
        print('%s\t%s\t%s' % (year, movie_title, round(average_rating, 1)))
