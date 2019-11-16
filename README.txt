TIMDB - The Indian Movie Database
An initiative to curate a well structured database for Indian movies

Current status: movies from 1990-2019

The project is divided into two directories based on the year of release:
    >> "1990-2009"
    >> "2010-2019"

Attributes present:
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

Note: 
In MovieLens database:
    The leading zeroes are removed for imdbId, which are not removed for the rest of the database (i.e for "1950-1989", "1990-2009" and "2010-2019")
    Example: in MovieLens database: 123456
             can be tt0123456 in imdb_id col

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

    To separate actors '|' is used
    
    'text delimiter' has to be 'None' to view the dataset in LibreOffice Calc
        as the attributes like story and summary contain "" and '' in them

Future Scope:
    Plans on expanding this dataset from 1990 to 2019
                                      to 1950 to 1989
    Director and Writer information left to be added