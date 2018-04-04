from django.views import View
from django.http import JsonResponse
import requests
import base64


class Index(View):

    def get(self, request):
        response = {"status": 200}
        url = 'https://api.sandbox.ebay.com/identity/v1/oauth2/token'

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': 'Basic %s' % base64.b64encode(bytes('vishalma-mytestap-SBX-75d7504c4-daa11ec3:SBX-5d7504c4347b-14d7-47db-90e1-1fdc', 'utf-8')),
        }
        print(headers)
        payload = dict(
            grant_type="vishalma-mytestap-SBX-75d7504c4-daa11ec3:SBX-5d7504c4347b-14d7-47db-90e1-1fdc &",
            redirect_uri="https://xb-ebay.herokuapp.com/callback/ &",
            scope="https://api.ebay.com/oauth/api_scope",
        )
        eb = requests.post(url, data=payload, headers=headers)

        print(eb.status_code)
        print(eb.text)
        return JsonResponse(response, safe=False)


class CallBackUrl(View):
    def get(self, request):
        print("callback url")
        print(request)
        response = {"status": 200}
        return JsonResponse(response, safe=False)
