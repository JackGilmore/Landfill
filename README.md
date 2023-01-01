# Landfill

An archive of the Trash Compactor/Fantastic Beats playlist.

## Description

A Spotify playlist archiver with Python back-end and Jekyll front-end. Ran on a weekly basis on Friday at 17:00 UTC using GitHub Actions.

## Getting Started

### Dependencies

* Back-end
  * Python 3.9
  * Python PIP
  * A Spotify developer app with client ID and secret: [Guide](https://developer.spotify.com/documentation/general/guides/authorization/app-settings/)
  
* Front-end
  * Ruby 3.1.2
  * RubyGems

### Executing program

* Back-end
  * Set up the following environment variables from your Spotify 
  ```
  SPOTIPY_CLIENT_ID
  SPOTIPY_CLIENT_SECRET
  ```
  * If running for one of your own playlists, substitute out the `PLAYLIST_ID` variable value
  * Run `pip install -m requirements.txt` to install packages
  * Run `python main.py`
* Front-end
  * Run `bundle install` to install packages
  * Run `bundle exec jekyll serve` to start the web server
  * Access site at (http://localhost:4000)[http://localhost:4000]

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.
