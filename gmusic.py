from gmusicapi import Musicmanager, Webclient, Mobileclient

mc = Mobileclient()
mc.oauth_login(Mobileclient.FROM_MAC_ADDRESS)
# pl = mc.get_all_playlists()
# print(pl)

# Mobileclient.add_songs_to_playlist(playlist_id, song_ids)
# Mobileclient.add_store_tracks(store_song_ids)
als = mc.get_all_songs()
print(als)