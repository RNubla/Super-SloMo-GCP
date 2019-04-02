# from django.shortcuts import render, redirect
# from django.conf import settings
# from django.http import HttpResponse
# from django.core.files.storage import FileSystemStorage

# from .models import Video
# from .forms import VideoForm

# # Create your views here.
# def index(request):
#     return render(request, "index.html")

# #def videoUpload(request):
# #    if request.method == 'POST':
# #        form = VideoForm(request.POST, request.FILES)

# #        if form.is_valid():
# #            form.save()
# #            return redirect('success')
# #    else:
# #        form = VideoForm()
# #    return render(request, 'video.html', {'form' : form})

# def success(request):
#     return HttpResponse('successfully upload video')

# #def watchVideo(request):
# #    if request.method == 'GET':
# #        Video = Video.objects.all()
# #        return render((request, 'video.html', {'Video': Video}))


# def showVideo(request):

#      lastvideo= Video.objects.last()

#      videoFile= lastvideo.videofile


#      form= VideoForm(request.POST or None, request.FILES or None)
#      if form.is_valid():
#          form.save()
    
#      context= {'videoFile': videoFile,
#                'form': form
#                }
    
#      return render(request, 'video.html', context)

from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage


# Create your views here.
def index(request):
    return render(request, "index.html")

def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'core/simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return index