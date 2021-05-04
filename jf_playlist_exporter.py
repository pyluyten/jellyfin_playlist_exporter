import os
import locale
from xml.dom import minidom

# Playlist directory.
g_dir = "/var/lib/jellyfin/data/playlists"


# There are subfolders in the playlist directory.
for filename in os.listdir(g_dir):
    g_subdir = os.path.join(g_dir, filename)
    print(g_subdir)

    # In the subfolders there are xml files
    for xml_playlist in os.listdir(g_subdir):
        g_fullpath = os.path.join(g_subdir, xml_playlist)
        playlist_name = filename + '.m3u8'
        f_path = os.path.join(g_dir,playlist_name)
        print("Creating playlist")
        #print(playlist_name)

        # Start to write a file
        with open(f_path, 'w') as writer:
            writer.write("#EXTM3U")
            writer.write("\n")

            # Parse for each song in the playlist...
            mydoc = minidom.parse(g_fullpath)
            items = mydoc.getElementsByTagName('Path')
        
            # add it to the file
            for elem in items:
                writer.write(elem.firstChild.data.encode('utf8'))
                writer.write("\n")
        
print("Done!")
