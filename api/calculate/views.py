import json
from django.http import JsonResponse, HttpResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import ensure_csrf_cookie


@ensure_csrf_cookie
def get_token_view(request, *args, **kwargs):
    if request.method == 'GET':
        return HttpResponse()
    return HttpResponseNotAllowed(['GET'])

def add(request):
    if request.method == "POST":
        data = json.loads(request.body)
        if 'A' in data and 'B' in data:
            try:
                result = int(data['A']) + int(data['B'])
                return JsonResponse({'result': result})
            except:
                return JsonResponse({'error': 'Invalid input'}, status=400)
        else:
            return JsonResponse({'error': 'No data provided'}, status=400)


def subtract(request):
    if request.method == "POST":
        data = json.loads(request.body)
        if 'A' in data and 'B' in data:
            try:
                result = int(data['A']) - int(data['B'])
                return JsonResponse({'result': result})
            except:
                return JsonResponse({'error': 'Invalid input'}, status=400)
        else:
            return JsonResponse({'error': 'No data provided'}, status=400)


def multiply(request):
    if request.method == "POST":
        data = json.loads(request.body)
        if 'A' in data and 'B' in data:
            try:
                result = int(data['A']) * int(data['B'])
                return JsonResponse({'result': result})
            except:
                return JsonResponse({'error': 'Invalid input'}, status=400)
        else:
            return JsonResponse({'error': 'No data provided'}, status=400)


def divide(request):
    if request.method == "POST":
        data = json.loads(request.body)
        if 'A' in data and 'B' in data:
            try:
                result = int(data['A']) / int(data['B'])
                return JsonResponse({'result': result})
            except:
                return JsonResponse({'error': 'Invalid input'}, status=400)
        else:
            return JsonResponse({'error': 'No data provided'}, status=400)
