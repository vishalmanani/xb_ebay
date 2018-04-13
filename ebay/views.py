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
        is_auth_successful = request.GET.get('isAuthSuccessful')
        expires_in = request.GET.get('expires_in')

        print("auth=====>", is_auth_successful)
        print("expires======>", expires_in)
        print("code=====>", code)

        url = 'https://api.sandbox.ebay.com/identity/v1/oauth2/token'
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': 'Basic %s' % base64.b64encode(bytes('vishalma-xbtest-SBX-b786e1828-de038b36:SBX-786e1828d8cd-f0aa-4632-a7b2-b6c6', 'utf-8')),
        }

        payload = dict(
            grant_type='authorization_code',
            code=code,
            redirect_uri='vishal_manani-vishalma-xbtest-kvjqakom',

        )
        eb = requests.post(url, data=payload, headers=headers)

        print("eb_status===>", eb.status_code)
        print("eb_text=====>", eb.text)

        return render(request, self.template, locals())

