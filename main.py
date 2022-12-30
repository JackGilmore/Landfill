import os
import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from datetime import datetime


__author__ = "Jack Gilmore"
__version__ = "0.1.0"

PLAYLIST_ID = "0o5ML957b0fHG4BjaH6Wfo?si=b527e8203cbd4672"


def init_client():
    return spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())


def main():
    """Main entry point of the app"""
    print("Starting playlist archive...")
    spotify_client = init_client()

    results = spotify_client.playlist(PLAYLIST_ID)

    print(f"Found {len(results['tracks']['items'])} songs in playlist")

    current_date = datetime.today().strftime("%Y-%m-%d")

    file_name = current_date + "_playlist" + ".json"
    file_path = "_playlists/" + file_name

    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    with open(file_path, "w") as f:
        f.write(json.dumps(results["tracks"]["items"]))
        f.close()

    print("Playlist archive complete!")


if __name__ == "__main__":
    """This is executed when run from the command line"""
    main()
