#!/usr/bin/env python3

# Student ID: okc00008

import sys

with open('years.txt', 'r') as f:
    included_years = f.read().split()

years = set(included_years) if included_years else None

print('included_years = %s' % included_years, file=sys.stderr)

for line in sys.stdin:
    data = line.strip().split('\t')
  #Checks if the length of the data list is not equal to 5 and skips any entry/feature that has 'attributes' less than or greater than 5 
    if len(data) != 5:
        continue

    year = data[3]
    #this ensures that text file will be processed even though years.txt is empty
    if years is None or year in years:
        movie_title, genres, rating = data[1], data[2], float(data[4])
       
        if genres:
            genres = genres.split('|')
            for genre in genres:
                print('%s\t%s\t%s\t%s' % (year, movie_title,rating,1))
               
                
                