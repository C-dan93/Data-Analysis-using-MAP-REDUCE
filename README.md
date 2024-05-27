# Data-Analysis-using-MAP-REDUCE
Project Description

This MapReduce project analyzes a large dataset of movie ratings (ratings.txt) to determine the highest-rated film(s) for each year within a specified range. The analysis considers multiple genres per film and excludes films not released in the years listed in years.txt.

Key Features:

MapReduce Paradigm: Leverages the power of Hadoop's MapReduce framework for distributed processing of large-scale data.

Python Implementation: Utilizes Python for mapper, combiner, and reducer functions.

Genre Handling: Properly attributes ratings to multiple genres associated with a film.

Year Filtering: Selectively analyzes movies based on the provided list of years.

Rating Threshold: Only considers movies with at least 10 ratings to ensure statistical significance.

Technical Details:

Data Source: ratings.txt (100,000+ ratings), years.txt (list of years), and smaller test files (r5.txt, r100.txt).

Environment: Designed to run on hadoop.cs.stir.ac.uk using the provided runhadoop.sh script.

Output Format: Tab-separated values (TSV) with year, movie title(s), and average rating.

Project Goals:
Demonstrate proficiency in MapReduce design and implementation.

Efficiently process large datasets in a distributed environment.

Extract meaningful insights from movie rating data.


