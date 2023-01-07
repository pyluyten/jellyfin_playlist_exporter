import os
import locale
from glob import glob
from xml.dom import minidom

# Playlist directory.
input_xml_playlist_directory = input("Input path to Jellyfin's XML playlist directory:")
output_m3u8_playlist_directory = input("Input path to your output directory for the .m3u playlist files:")

# There are subfolders in the playlist directory.
for playlist_name in os.listdir(input_xml_playlist_directory):
    xml_playlist_subdir = os.path.join(input_xml_playlist_directory, playlist_name)

    # In the subfolders there are xml files
    for xml_playlist in glob(os.path.join(xml_playlist_subdir, "*.xml")):
        xml_playlist_fullpath = os.path.join(xml_playlist_subdir, xml_playlist)
        m3u8_playlist_name = playlist_name + '.m3u8'
        m3u8_playlist_path = os.path.join(output_m3u8_playlist_directory, m3u8_playlist_name)
        print("Creating playlist: " + playlist_name)

        # Start to write a file
        with open(m3u8_playlist_path, 'w') as writer:
            writer.write("#EXTM3U")
            writer.write("\n")

            # Parse for each song in the playlist...
            mydoc = minidom.parse(xml_playlist_fullpath)
            items = mydoc.getElementsByTagName('Path')

            # add it to the file
            for elem in items:
                writer.write(elem.firstChild.data)
                writer.write("\n")

print("Done!")

