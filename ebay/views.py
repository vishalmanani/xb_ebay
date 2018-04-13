import json

from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
import requests
import base64


class Index(View):
    template = 'index.html'

    def get(self, request):
        url = """
        https://auth.sandbox.ebay.com/oauth2/authorize?client_id=vishalma-xbtest-SBX-b786e1828-de038b36&response_type=code&redirect_uri=vishal_manani-vishalma-xbtest-kvjqakom&scope=https://api.ebay.com/oauth/api_scope https://api.ebay.com/oauth/api_scope/buy.order.readonly https://api.ebay.com/oauth/api_scope/buy.guest.order https://api.ebay.com/oauth/api_scope/sell.marketing.readonly https://api.ebay.com/oauth/api_scope/sell.marketing https://api.ebay.com/oauth/api_scope/sell.inventory.readonly https://api.ebay.com/oauth/api_scope/sell.inventory https://api.ebay.com/oauth/api_scope/sell.account.readonly https://api.ebay.com/oauth/api_scope/sell.account https://api.ebay.com/oauth/api_scope/sell.fulfillment.readonly https://api.ebay.com/oauth/api_scope/sell.fulfillment https://api.ebay.com/oauth/api_scope/sell.analytics.readonly https://api.ebay.com/oauth/api_scope/sell.marketplace.insights.readonly https://api.ebay.com/oauth/api_scope/commerce.catalog.readonly
        """
        return render(request, self.template, locals())


class AcceptURL(View):
    template = 'accept_url.html'

    def get(self, request):
        print("accept url")

        code = request.GET.get('code')
        expires_in = request.GET.get('expires_in')

        print("expires======>", expires_in)
        print("code=====>", code)

        url = 'https://api.sandbox.ebay.com/identity/v1/oauth2/token'

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': 'Basic dmlzaGFsbWEteGJ0ZXN0LVNCWC1iNzg2ZTE4MjgtZGUwMzhiMzY6U0JYLTc4NmUxODI4ZDhjZC1mMGFhLTQ2MzItYTdiMi1iNmM2'
        }

        payload = {
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': 'vishal_manani-vishalma-xbtest-kvjqakom'

        }
        eb = requests.post(url, data=payload, headers=headers)
        print("eb_status===>", eb.status_code)
        print("eb_text=====>", eb.text)

        access_token_json = json.loads(eb.text)

        access_token = access_token_json.get('access_token')
        expires_in = access_token_json.get('expires_in')
        refresh_token = access_token_json.get('refresh_token')
        refresh_token_expires_in = access_token_json.get('refresh_token_expires_in')
        token_type = access_token_json.get('token_type')

        print("access_token====>", access_token)
        print("expires_in======>", expires_in)
        print("refresh_token=====>", refresh_token)
        print("refresh_token_expires_in====>", refresh_token_expires_in)
        print("token_type====>", token_type)

        re_payload = {
            'grant_type': 'refresh_token',
            'refresh_token': refresh_token,
            'scope': 'https://api.ebay.com/oauth/api_scope https://api.ebay.com/oauth/api_scope/buy.order.readonly https://api.ebay.com/oauth/api_scope/buy.guest.order https://api.ebay.com/oauth/api_scope/sell.marketing.readonly https://api.ebay.com/oauth/api_scope/sell.marketing https://api.ebay.com/oauth/api_scope/sell.inventory.readonly https://api.ebay.com/oauth/api_scope/sell.inventory https://api.ebay.com/oauth/api_scope/sell.account.readonly https://api.ebay.com/oauth/api_scope/sell.account https://api.ebay.com/oauth/api_scope/sell.fulfillment.readonly https://api.ebay.com/oauth/api_scope/sell.fulfillment https://api.ebay.com/oauth/api_scope/sell.analytics.readonly https://api.ebay.com/oauth/api_scope/sell.marketplace.insights.readonly https://api.ebay.com/oauth/api_scope/commerce.catalog.readonly'
        }

        refresh_eb = requests.post(url, data=re_payload, headers=headers)
        print("refresh_eb_status===>", refresh_eb.status_code)
        print("refresh_eb_text=====>", refresh_eb.text)

        r_access_token_json = json.loads(refresh_eb.text)

        r_access_token = r_access_token_json.get('access_token')
        r_expires_in = r_access_token_json.get('expires_in')
        r_token_type = r_access_token_json.get('token_type')

        print("r_access_token===>", r_access_token)
        print("r_expires_in====>", r_expires_in)
        print("r_token_type====>", r_token_type)

        return render(request, self.template, locals())

