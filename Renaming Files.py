import os

path = "/foldername"

lst = []

file = open("path/youtubePlaylist.txt", 'r')
for line in file:
    if line.strip():
        lst.append(line)

i = 0
for filename in os.listdir(path):
    final = lst[i] + ".mkv"
    initial = path + filename
    final = path + final
    os.rename(initial, final)
    i += 1
