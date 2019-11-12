TIMDB - The Indian Movie Database

Attributes present:
    './bollywood.csv': title, imdb_id, poster_path,wiki_link
    './bollywood_meta.csv': imdb_id, title, original_title, is_adult, year_of_release, runtime, genres
    './bollywood_ratings.csv': imdb_id, imdb_rating, imdb_votes
    './bollywood_text.csv': imdb_id, story, summary, tagline, actors, wins_nominations, release_date

    UNIQUE (18 attributes):
        title(wiki), imdb_id, poster_path, wiki_link, original_title,
        title(imdb), is_adult, year_of_release, runtime, genres,
        imdb_rating, imdb_votes, story, summary, tagline,
        actors, wins_nominations, release_date

Note: 
In './bollywood_ratings.csv' if:
    value is NaN -> it means the film is yet to be released
    value is 0 -> No rating was given to the film

In './bollywood_meta.csv' if:
    A title is missing, chances are the title had no info in the imdb dump
    Or the title is yet to be released
    (indicated by \N)

    As of this commit, all the is_adult values are 0.

In './bollywood_text.csv':
    Some inconsistencies are removed, as of this commit some inconsistencies are left to find!

    To separate actors '|' is used
    
    'text delimiter' has to be 'None' to view the dataset in LibreOffice Calc
        as the attributes like story and summary contain "" and '' in them

Future Scope:
    Plans on expanding this dataset from 2010 to 2019
                                      to 1950 to 2019
    Director and Writer information left to be added