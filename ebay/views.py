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
        print(request)
        return render(request, self.template, locals())

