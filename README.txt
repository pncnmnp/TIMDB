TIMDB - The Indian Movie Database
An initiative to curate a well structured database for Indian movies

Current status: movies from 1950-2019 
               (can be used in both: content-based and collaborative filtering approaches)

The project is divided into five directories based on the year of release and type of approach:
    >> "collaborative"
    >> "1950-2019"
    >> "1950-1989"
    >> "1990-2009"
    >> "2010-2019"

Attributes present:
    IN ALL THE DATABASE PROVIDES 35 UNIQUE ATTRIBUTES TO TINKER WITH!

    In "1950-1989", "1990-2009" and "2010-2019":
        './x/bollywood.csv': title, imdb_id, poster_path,wiki_link
        './x/bollywood_meta.csv': imdb_id, title, original_title, is_adult, year_of_release, runtime, genres
        './x/bollywood_ratings.csv': imdb_id, imdb_rating, imdb_votes
        './x/bollywood_text.csv': imdb_id, story, summary, tagline, actors, wins_nominations, release_date

        where x = ["1990-2009", "2010-2019"]

        UNIQUE (18 attributes):
            title(wiki), imdb_id, poster_path, wiki_link, original_title,
            title(imdb), is_adult, year_of_release, runtime, genres,
            imdb_rating, imdb_votes, story, summary, tagline,
            actors, wins_nominations, release_date

    In "1950-2019":
        './x/bollywood_crew.csv': imdb_id, directors, writers
        For Director(s) info:
            './x/bollywood_crew_data.csv': crew_id, name, born_year, death_year, profession, known_for
        For Writer(s) info:
            './x/bollywood_writers_data.csv': crew_id, name, born_year, death_year, profession, known_for

        UNIQUE (7 attributes):
            crew_id ('directors' and 'writers' column in bollywood_crew.csv contains their respective crew_id),
            imdb_id, name, born_year, death_year, profession, known_for

    In "collaborative":
        './x/genome_scores.csv': movie_id, tag_id, relevance
        './x/genome_tags.csv': tag_id, tag
        './x/links.csv': movie_id, imdb_id
        './x/ratings.csv': user_id, movie_id, rating, timestamp
        './x/tags.csv': user_id, movie_id, tag, timestamp
        './x/titles.csv': movie_id, title

        UNIQUE (10 attributes):
            movie_id, tag (from genome_tags.csv), tag (from tags.csv), tag_id,
            relevance, imdb_id, user_id, rating, timestamp, title

NOTE: 
From MovieLens database:
    The leading zeros are removed for imdb_id, which are not removed for the rest of the database(i.e for "1950-1989", "1990-2009", "2010-2019" and "1950-2019").
    Example: in links.csv if imdb_id is 123456,
             it can be tt0123456 in imdb_id col in the datasets in "1950-1989", "1990-2009" and "2010-2019".

    The ratings(MovieLens) for collaborative filtering were from "Full" dataset available at http://files.grouplens.org/datasets/movielens/ml-latest.zip

    The genome-scores were available for very few movies (64 in total) from "Full" MovieLens dataset.

In 'bollywood_ratings.csv' if:
    value is NaN -> it means the film is yet to be released
    value is 0 -> No rating was given to the film

In 'bollywood_meta.csv' if:
    A title is missing, chances are the title had no info in the imdb dump
    Or the title is yet to be released
    (indicated by \N)

    As of this commit, all the is_adult values are 0.

In 'bollywood_text.csv':
    Some inconsistencies are removed, as of this commit some inconsistencies are left to find!

    To separate multiple actors: '|' is used
    
    'text delimiter' has to be 'None' to view the dataset in LibreOffice Calc
        as the attributes like story and summary contain "" and '' in them

In bollywood_crew.csv, bollywood_crew_data.csv and bollywood_writers_data.csv:
    To separate multiple directors, writers and known_for titles and professions: '|' is used

In 'src' directory:
    The paths mentioned in the script are relative, see ./src/PATHS.py

Future Scope:
    Plans on curating movies for other languages, like 'Gujarati', 'Tamil', 'Telugu', etc.

Attribution:
> F. Maxwell Harper and Joseph A. Konstan. 2015. The MovieLens Datasets: History and Context. ACM Transactions on Interactive Intelligent Systems (TiiS) 5, 4: 19:1–19:19. <https://doi.org/10.1145/2827872>
> IMDB  https://datasets.imdbws.com/
> Wikipedia https://wikimediafoundation.org/support/

License:
All the scripts are licensed under MIT License
For database licensing see the Attribution section