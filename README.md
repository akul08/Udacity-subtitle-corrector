# Udacity-subtitle-corrector
A python script to correctly modify the udacity courses subtitle.

## How to use

### First copy the subtitle_correct.py into all the folders
`ls -d Lesson\ * > directory.txt`

`cp subtitle_correct.py Lesson\ ` + each line from directory.txt

### Then go into folder having srt file and write the name in subtitles_name.txt

`ls *.srt >subtitles_name.txt`

### Then run python script `python subtitle_correct.py`