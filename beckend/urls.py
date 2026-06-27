from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.http import FileResponse, Http404
from django.shortcuts import render
import os


def media_serve(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path) and os.path.isfile(file_path):
        return FileResponse(open(file_path, 'rb'))
    raise Http404("Media file not found")

# 404 sahifa
def custom_404(request, exception):
    return render(request, '404.html', status=404)

handler404 = custom_404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('fronend.urls')),  # asosiy app
    path('auth/', include('authentication.urls')),  # auth app
]

# Media fayllarni serving qilish
urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', media_serve),
]

