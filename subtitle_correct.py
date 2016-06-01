import re

with open('subtitles_name.txt') as subtitles:
	filenames = subtitles.readlines()

for filename in filenames: 
	with open(filename[:-1]) as f:
		data = f.read()

	if not re.search('-->', data):
		with open(filename[:-1], 'w') as f:
			f.write(re.sub('\d,', '0 --> ', data))

