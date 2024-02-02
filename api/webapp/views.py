from django.shortcuts import render
from django.views import View


class Index(View):
    def get(self, request):
        return render(self.request, 'index.html')
