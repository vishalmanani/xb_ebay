from django.views import View
from django.http import JsonResponse


class Index(View):

    def get(self, request):
        response = {"status": 200}
        return JsonResponse(response, safe=False)
