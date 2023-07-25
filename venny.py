import spotipy
import json
import webbrowser

  

def main():
    USERNAME = 'Your Spotify User name'
    CLIENT_ID = ''
    CLIENT_SECRET = ''
    REDIRECT_URL = '' 
    
    # Doing Authorization
    oauth = spotipy.SpotifyOAuth(CLIENT_ID, CLIENT_SECRET, REDIRECT_URL)

    # Generating Token
    token_dict = oauth.get_access_token()
    #print(token_dict)
    token = token_dict['access_token']

    spotifyObject = spotipy.Spotify(auth=token)
    user_name = spotifyObject.current_user()
    #print(user_name[])

    #CLI
    while True:
        print("0 - Exit the console")
        print("1 - Search for a Song")
        choice = int(input("Enter Your Choice: "))
    # If user chooses 1 then user is prompted for song name, and song is searched and played on spotify
    # If user chooses 0, break out of loop
    # If invalid input is entered then user is prompted to enter either 1 or 0
        if choice == 1:
            search_song = input("Enter the name of a song: ")
            results = spotifyObject.search(search_song, 1, 0, "track")
            songs_dict = results['tracks']
            song_items = songs_dict['items']
            song = song_items[0]['external_urls']['spotify']
            webbrowser.open(song)
            print('Song has opened in your browser.')
        elif choice == 0:
            print("GoodBye")
            break
        else:
            print("Invalid Choice")

if __name__ == "__main__":
    main()