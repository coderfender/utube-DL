from django.shortcuts import render,HttpResponse
from DL_Logic import dow
from django.http import Http404
# Create your views here.

def home(request):
		return render(request,"home.html")

def res(request):

	if request.method == "POST" and request.POST['ylink'] != "":
		url = request.POST['ylink']
		res = dow(url)
		# print res
		best_video_url = res[0]
		streams_1= res[1]
		best_audio_url=res[2]
		title = res[3]
		author = res[4]
		resp = render(request,"res.html",{"best_video_url":best_video_url,"streams_1":streams_1,
										"best_audio_url":best_audio_url,"title":title,"author":author})
		return resp
	else:
		return HttpResponse("<h1 align=center>Are you kidding me?? Give me a link to Download!</h1>")

		# response['Content-Disposition'] = 'attachment; filename=myfile.m4a'
		
