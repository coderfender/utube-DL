import pafy
from pytube import YouTube
def dow(url):
	video = pafy.new(url)
	streams = video.streams
	best = video.getbest()
	bestaudio = video.getbestaudio()
	# dowlo(url)
	# print [best.url,streams,bestaudio]
	return [best.url,streams,bestaudio.url,video.title,video.author]

# def dowlo(url):
# 	try:

# 		yt = YouTube()
# 		yt.url = url
# 		vid=yt.get('mp4','720p')
# 		vid.download()
# 		print "Done!"
# 	except:
# 		print "MoFo"


