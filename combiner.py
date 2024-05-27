#!/usr/bin/env python3

# Student ID: okc00008

import sys
from collections import defaultdict

# Initialize defaultdicts to store the sum of ratings and counts for each unique key
rating_sum_dict = defaultdict(float)
count_sum_dict = defaultdict(int)

# Read input data line by line
for line in sys.stdin:
    # Split the line into parts: year, movie_title, rating, count
    year, movie_title, rating, count = line.strip().split('\t')
    
    # Convert rating and count to numbers (float and int respectively)
    rating = float(rating)
    count = int(count)
    
    # Form the key by concatenating year and movie_title
    key = (year, movie_title)
    
    # Update the dictionaries with rating and count for the current key
    rating_sum_dict[key] += rating
    count_sum_dict[key] += count

# Print the aggregated results for each key
for key in rating_sum_dict:
    # Extract the year and movie_title from the key
    year, movie_title = key
    
    # Print the result: year, movie_title, sum_of_ratings, sum_of_counts
    print('%s\t%s\t%s\t%s' % (year, movie_title, rating_sum_dict[key], count_sum_dict[key]))
