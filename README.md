Cloud 6 MusicBox


********************************
Instructions
********************************
- after vagrant up, please go on http://127.0.0.1:8080/musicbox/ to see our project.
- for sample data, please check out the file named "sample_data.json" under the directory 'group-project/mysite' to see the list of sample data provided.


********************************
Possible functionalities to test
********************************
- signup: sign up an account 
- signin: sign in with an existing account or the newly created account.
- genres: click on the "genres" tab in the homepage to see the list of genres.
- mp3: click on "instrumental" genre to the sample mp3 in a detailed page.
- upload: click on "upload" tab to upload an mp3 of your choice. And go back to check it is in the genre you have chosen later. (Have not implemented the feature to check whether the file is mp3 format)
- rating: there are two tables in raing page, you can click on music name in each table to access music details and listen to the music.

********************************
Possible security holes
********************************
- do not need to actually log in in order to get to home page: just append "home/" to the end of "http://127.0.0.1:8080/musicbox/"
- some urls does not look professional and might subject to security issues. e.g. "musicbox/home/2/" when you click a song under a genre.


********************************
Preloaded Sample Data
********************************
- In the "sample_data.json" file, it contains sample data for user accounts, songs, and genres.
- There are 6 sample user accounts. For example:

	 "name_first": "Laura",
     "name_last": "Dern",
     "password": "123456789",
     "repassword": "123456789",
     "email": "ld@sfu.ca",
     "phone_number": "111-111-1111"
	  
is one of them.
- There are 2 sample mp3 files. For example:

	"title": "why so serious",
    "artist": "Wong",
    "genre": 7,
    "year": "1979",
    "publisher": "someone",
    "rating": "0",
	"overall_rating": "0",
    "total_rating": "0",
	"sumitted_count": "0",
    "play_count": "0",
	"added_date":"2009-10-25 14:30",
	"file": "music/Why_So_Serious.mp3"

is one of them.
- There are 10 sample genres. For example:

	"genre_name": "Blues"

is one of them.
