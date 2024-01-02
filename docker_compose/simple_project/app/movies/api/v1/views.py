# from django.http import HttpResponse


# def api(request):
#     return HttpResponse("My best API")

from django.http import JsonResponse
from django.views import View

class MoviesListApi(View):
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        # Получение и обработка данных
        return JsonResponse({}) 