# Simple Python script to download subtitles of movies
# https://github.com/prashantsengar/SubtitlesDL
# prashantsengar5@gmail.com

import requests
from pythonopensubtitles.utils import File
from pythonopensubtitles.opensubtitles import OpenSubtitles
ost = OpenSubtitles()
from zipfile import ZipFile
import os
import time

EMAIL = "YOUR OpenSubtitles email"
PASSW = "YOUR OpenSubtitles password"

token = ost.login(EMAIL, PASSW)

filename=input("Enter path to file: ")
sub_path = os.path.dirname(filename)
name = '.'.join(filename.split('.')[0:-1])

sname = name+'.srt'
zname = name+'.zip'

f = File(filename)
hashh = f.get_hash()
size = f.size
print(hashh)
print(size)
data = ost.search_subtitles([{'sublanguageid': 'all', 'moviehash': hashh, 'moviebytesize': size}])
assert type(data)!=None

link = data[0]['ZipDownloadLink']
print(link)

file = open(os.path.join(sub_path,zname),'wb')
s = requests.get(link)
for chunk in s.iter_content(100000):
	if chunk:
		file.write(chunk)

file.close()


with ZipFile(os.path.join(sub_path,zname), 'r') as zip: 
    # printing all the contents of the zip file 
    files = zip.namelist()
    for fi in files:
    	if fi.lower().endswith('.srt'):
    		print(fi)
    		selected = fi

    time.sleep(5)
    # extracting all the files 
    print('Extracting all the files now...')
    
    zip.extract(selected, path=sub_path)
    time.sleep(5)
    os.rename(os.path.join(sub_path,selected),os.path.join(sub_path, sname))
    print('Done!')
    print(sname)

