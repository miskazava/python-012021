from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

class MujPrvniPohled(View):
    def get(self, request):
        return HttpResponse("Vítej na webu Czechitas!")

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('kurzy/', include("kurzy.urls"))
]
