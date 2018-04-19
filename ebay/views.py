import json
from xml.etree import ElementTree as ET
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.http import JsonResponse, HttpResponse
import requests
import base64

from django.views.decorators.csrf import csrf_exempt


class Index(View):
    template = 'index.html'

    def get(self, request):
        # sandbox
        # url = """
        # https://auth.sandbox.ebay.com/oauth2/authorize?client_id=vishalma-xbtest-SBX-b786e1828-de038b36&response_type=code&redirect_uri=vishal_manani-vishalma-xbtest-kvjqakom&scope=https://api.ebay.com/oauth/api_scope https://api.ebay.com/oauth/api_scope/buy.order.readonly https://api.ebay.com/oauth/api_scope/buy.guest.order https://api.ebay.com/oauth/api_scope/sell.marketing.readonly https://api.ebay.com/oauth/api_scope/sell.marketing https://api.ebay.com/oauth/api_scope/sell.inventory.readonly https://api.ebay.com/oauth/api_scope/sell.inventory https://api.ebay.com/oauth/api_scope/sell.account.readonly https://api.ebay.com/oauth/api_scope/sell.account https://api.ebay.com/oauth/api_scope/sell.fulfillment.readonly https://api.ebay.com/oauth/api_scope/sell.fulfillment https://api.ebay.com/oauth/api_scope/sell.analytics.readonly https://api.ebay.com/oauth/api_scope/sell.marketplace.insights.readonly https://api.ebay.com/oauth/api_scope/commerce.catalog.readonly
        # """

        # production

        url = """
        https://auth.ebay.com/oauth2/authorize?client_id=vishalma-xbtest-PRD-b786e1828-0e7d9ead&response_type=code&redirect_uri=vishal_manani-vishalma-xbtest-xaqkp&scope=https://api.ebay.com/oauth/api_scope https://api.ebay.com/oauth/api_scope/sell.marketing.readonly https://api.ebay.com/oauth/api_scope/sell.marketing https://api.ebay.com/oauth/api_scope/sell.inventory.readonly https://api.ebay.com/oauth/api_scope/sell.inventory https://api.ebay.com/oauth/api_scope/sell.account.readonly https://api.ebay.com/oauth/api_scope/sell.account https://api.ebay.com/oauth/api_scope/sell.fulfillment.readonly https://api.ebay.com/oauth/api_scope/sell.fulfillment https://api.ebay.com/oauth/api_scope/sell.analytics.readonly
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

        # sandbox
        # url = 'https://api.sandbox.ebay.com/identity/v1/oauth2/token'

        # headers = {
        #     'Content-Type': 'application/x-www-form-urlencoded',
        #     'Authorization': 'Basic dmlzaGFsbWEteGJ0ZXN0LVNCWC1iNzg2ZTE4MjgtZGUwMzhiMzY6U0JYLTc4NmUxODI4ZDhjZC1mMGFhLTQ2MzItYTdiMi1iNmM2'
        # }

        # payload = {
        #     'grant_type': 'authorization_code',
        #     'code': code,
        #     'redirect_uri': 'vishal_manani-vishalma-xbtest-kvjqakom'
        # }

        # production
        url = 'https://api.ebay.com/identity/v1/oauth2/token'

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': 'Basic dmlzaGFsbWEteGJ0ZXN0LVBSRC1iNzg2ZTE4MjgtMGU3ZDllYWQ6UFJELTc4NmUxODI4YjQ0ZS02MGZmLTQ5NDgtYTU5Ny0xYTdh'
        }

        payload = {
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': 'vishal_manani-vishalma-xbtest-xaqkp'

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

        # sandbox
        # re_payload = {
        #     'grant_type': 'refresh_token',
        #     'refresh_token': refresh_token,
        #     'scope': 'https://api.ebay.com/oauth/api_scope https://api.ebay.com/oauth/api_scope/buy.order.readonly https://api.ebay.com/oauth/api_scope/buy.guest.order https://api.ebay.com/oauth/api_scope/sell.marketing.readonly https://api.ebay.com/oauth/api_scope/sell.marketing https://api.ebay.com/oauth/api_scope/sell.inventory.readonly https://api.ebay.com/oauth/api_scope/sell.inventory https://api.ebay.com/oauth/api_scope/sell.account.readonly https://api.ebay.com/oauth/api_scope/sell.account https://api.ebay.com/oauth/api_scope/sell.fulfillment.readonly https://api.ebay.com/oauth/api_scope/sell.fulfillment https://api.ebay.com/oauth/api_scope/sell.analytics.readonly https://api.ebay.com/oauth/api_scope/sell.marketplace.insights.readonly https://api.ebay.com/oauth/api_scope/commerce.catalog.readonly'
        # }

        # production
        re_payload = {
            'grant_type': 'refresh_token',
            'refresh_token': refresh_token,
            'scope': 'https://api.ebay.com/oauth/api_scope https://api.ebay.com/oauth/api_scope/sell.marketing.readonly https://api.ebay.com/oauth/api_scope/sell.marketing https://api.ebay.com/oauth/api_scope/sell.inventory.readonly https://api.ebay.com/oauth/api_scope/sell.inventory https://api.ebay.com/oauth/api_scope/sell.account.readonly https://api.ebay.com/oauth/api_scope/sell.account https://api.ebay.com/oauth/api_scope/sell.fulfillment.readonly https://api.ebay.com/oauth/api_scope/sell.fulfillment https://api.ebay.com/oauth/api_scope/sell.analytics.readonly'
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

        # sandbox
        # r_access_token = "v^1.1#i^1#r^0#f^0#I^3#p^3#t^H4sIAAAAAAAAAOVXeWwUVRjv9jK1B8QYMJzLAFUss/tmZ3Znd2RXt7TYCr3YQmhR8c3Mm3ZkdmaZN7PtNqK1JkgIJiaImJhADRKNGCIRjAeCiv4hJsTEmIhKRMUjQhU8QlRE3+z22NYAPYhp4vwzee995+/7fe8A3YVFt26q2XSh1HVdbm836M51uZhiUFRYUFGWlzujIAdkCbh6uxd05/fkfb8Ew7iWEFYinDB0jNydcU3HQnoyTNmmLhgQq1jQYRxhwZKEWLRuheDzACFhGpYhGRrlrq0KUxzLsqLCyRzkWd7HQTKrD9hsNsJUCEhKKODzMSDEhQI8IOsY26hWxxbUrTDlA0yQBhzNsM0gIPh5gfN7WJ5ppdyrkYlVQyciHkBF0uEKaV0zK9YrhwoxRqZFjFCR2uiyWEO0tqq6vnmJN8tWpB+HmAUtGw8fLTVk5F4NNRtd2Q1OSwsxW5IQxpQ3kvEw3KgQHQhmHOGnoZb9rE+U/YoSZP2KeI2gXGaYcWhdOQ5nRpVpJS0qIN1SrdTVECVoiPcjyeof1RMTtVVu59dkQ01VVGSGqerKaMuqWPVKyh1rbDSNpCoj2cmUYdkgy3J+lopYCBMIkbkuqeJ2qAEA+p1lLPZDPcLbUkOXVQc47K43rEpEIkcj8eGy8CFCDXqDGVUsJ6psueAAjgGu1SlsppK21a47tUVxAoY7Pbx6FQZoMUSEa0YMn0/yI6D4QozII3E4MZxeHyc5Ik59oo2NXicWJMIUHYfmemQlNCghWiLw2nFkqrJA+Ohjgwqi5UBIobmQotCiXw7QjIIQQEgUpVDw/8YRyzJV0bbQIE9GLqQTDVMxyUigRkNTpRQ1UiS99/SzohOHqXbLSgheb0dHh6eD9Rhmm9cHAONdU7ciJrWjONl8B2TVqwvTapofEiJaWBWsVIJE00noR5zrbVSENeVGaFqpSjtFxjGkaeQ3QOFhEUZGzl4mVeykOrmSdPQxMQATqsdhuEcy4l4Dko52ptalI3aPRsgr2iniX0amx0RQNnQtNXq9NpswOKM9OiVMquHJNCNJY9Cj0+vjMTAGHVVPEi4bZmqMaQ5XHoMOlCTD1q3xuOtXHYOGYmuKqmlOu47HYZb6WMLUoZayVAmPx2XWjkzgxWpbuzVWO2SObONEX4IW1IwhOk2o2aOJRK08uZo9czwQuU7ROTLoWOUaWuSDAcQEfUFaRoANimxgQllXoeR/lHV+T+6Do84c+DmZlyWOlv2BEM2JPKShLHM0kMhZzQOWgMBPKO+lmkpI35yabPt7jYEtJE8sNXLVmlxJObwdoK0clMjNHEBIcwHWR0Ne9NFiQBo1i72Xva3867LqHf5ijOSkP6bH9Sbocb1GHp2ABzRTARYV5q3KzyuhsGohD4a6LBqdHhUqHrI76eRBZCLPepRKQNXMLXStnfnD7Rez3qq994CbBl+rRXlMcdbTFcwaWilgpkwvZYKAY1gQ8POcvxXMH1rNZ6bl33imqWXnIea++E83NL2zo+/knm8LWveB0kEhl6sgJ7/HlfNIXa1d9kLvjI+fX3huI5rp3fDkkXP7c+9037Lo5z3RxzZP3bLi1M6XK3oPsZ3zTr3/Lrfs5Fd/blsOjz3asIv6q+XsvuLCHevZt4vLbl55x4HZm1sX0nu9F2eXNv728O853EO/LK7xh6Kf9amL5+x96lJ5ydbAM29U1Rw//fjhzsVnXznSNffTlrK7Pz97F19SEjpfOf/ol/vbl1/qemDe9m2t5d/s+nH3d/ThX5MV9dXn/ph1b/O+5/zSh1O+bnpp3RN95XbvhqLkJx91hWdNL9897cSF5MGmje99cP0Xz5Z3Hd9+dM6ZBa9umfr3WwfZmXUHnz5zOu9YW/3rJ4yTqbl9C48LL56/7WK46Mhu3vSsPYAzZfwHL6en90UQAAA="
        # inventory_url = 'https://api.sandbox.ebay.com/sell/inventory/v1/inventory_item?limit=2&offset=0'

        # production
        r_access_token = "v^1.1#i^1#p^3#f^0#r^0#I^3#t^H4sIAAAAAAAAAOVXa2wURRzv9aXIQ6kIQgCPrYpA9m72bm93b+1dPNoiNZQeXEGk4TG7O9tbu7d77uy1dwpynrGCMSYaEwnGWAUVRHwAfhCNAeIjKhIJgQRFhYQEIxrhAyohorPXB9cqLW350MRLNpeZ+T9//99/HiBbPmp2+/z2P8a6rivuyIJsscvFjAajysvmjCspnlJWBAoEXB3Z27OluZKfqjBM6ElxMcJJ08DInU7oBhbzkyEqZRmiCbGGRQMmEBZtWYxF6heIPg8Qk5Zpm7KpU+66mhDFCozAKDKr+HheYpQAmTW6bTaaIYrjWJaTOAn4A7ICZZmsY5xCdQa2oWGHKB9gBBqwNCM0gqDI+MSAzxNkwHLKvRRZWDMNIuIBVDgfrpjXtQpi7T9UiDGybGKECtdF5sUaInU1tQsbq7wFtsJdOMRsaKdw71G1qSD3UqinUP9ucF5ajKVkGWFMecOdHnobFSPdwQwh/DzUKMCziGd8KqdAQQbwmkA5z7QS0O4/DmdGU2g1Lyoiw9bszECIEjSkB5Fsd40WEhN1NW7nb1EK6pqqIStE1c6NPLAkVruYcseiUcts1RSkOJkyPMezQY4PclS4VcMJaKxihS4nnZa6IO7jpdo0FM0BDLsXmvZcRCJGfXEBBbgQoQajwYqothNNgRzDdOMH+OVOQTsrmLLjhlNTlCAguPPDgdHvpsNlAlwrQgh+JcCDIMsysqQEOOU/CeH0+iBJEXbqEolGvU4sSIIZOgGtFmQndSgjWibwphLI0hTRH1B9fkFFtMIFVZoNqiotBRSOZlSEAEKSJAeF/ws3bNvSpJSNevjRdyGfYIiKyWYSRU1dkzNUX5H8XtPFhjQOUXHbTopeb1tbm6fN7zGtZq8PAMa7rH5BTI6jBNkBumW1gYVpLc8LGREtrIl2JkmiSRPaEedGMxX2W0oUWnYmhnSdTHSTtlds4b6zV0gSO0mOrPQcfUwMwKTmcTjtkc2E14Skh52pVfmI3Vcj5MUEIE9nRxDLHgtBxTT0zFCUB6GjGa2EVKaV6ceh0+sDGxiEU3JgmynDHkqOXaqD0FBTuqrputM7Q3FYoD6YMA2oZ2xNxj0uh0X8SDJZp4ws4pNNMg51IpeWbIRtOrq4hpZ4gUOM4CN7GuKVIMl8WFnXN2sjLGnGx/l4EBBYHgBuWLnVoNaRVlEQYBW+NFccJfdumhz8QZqVeEhDRWFpIJNTmAd+UmB+WHlX6xrppMbMSNvH55vYRsOjazW5RI2spJye7G5JiWURzQHVuVCxAg0DQZ5mIA+vNmXvFe8j/7qGenu/AcNF+R+Tc70Pcq73yDMSeMEdTCWYUV6ypLRkzBSs2cijQdWDtWaDPG0s5GlBmSTUrOJyV9PUd7etKnh1dqwAt/a8O0eVMKMLHqFg6uWVMubGSWMZAbDkCzK+gG85qLy8WspMLJ0wbXTVvgXjMn9FxFw6Gz03KxQNtoKxPUIuV1lRac5VtHv9MmUHdWb14YMz5894fp9VU3HXz1Nfnqg033D2681b75v5baY1XtKePGWfvvlM1bpPlmVXrj38w6vsyScPrTywwXXy4oHzv5/4Ebw4/rPaD5Obmi6t2ZyteHrv7reOTJc/2MSlm5ibXrn30/r0s3eax164/+G1vHU+N7vylzNj1m30u88+d/H6r2459PmK2XuWTH+qJTGn5VHvnIMb1nrXf3Nw72sn5LZtjzy25vvSS2+fn/DM34vmNm75bv/pc4/HX4r+9kSZtGXantdPlVUKoY/Ss8YfXX3bke0VKy/cs7X+i+Pq9p3h/X+yH0+O7Xzz7kh7x8zQO2/s2hg/uvVYw4VFlZOaKnb45h2v/PLXyWeXPrRL7SzfP9VM+CcPEAAA"
        # inventory_url = 'https://api.ebay.com/sell/inventory/v1/inventory_item?limit=2&offset=0'

        # inventory_header = {
        #     'Authorization': 'Bearer %s' % r_access_token
        # }

        # print(inventory_header)
        # inventory = requests.get(inventory_url, headers=inventory_header)
        #
        # print("inventory_status===>", inventory.status_code)
        # print("inventory_text=====>", inventory.text)

        bulk_migrate_listing_url = 'https://api.ebay.com/sell/inventory/v1/bulk_migrate_listing'

        bulk_migrate_listing_header = {
            'Authorization': 'Bearer %s' % r_access_token
        }

        bulk_migrate_listing_payload = {
            "requests": [
                {
                    "listingId": "222929471807"
                }
            ]
        }

        print(json.dumps(bulk_migrate_listing_payload))

        bulk_migrate_listing = requests.post(bulk_migrate_listing_url, headers=bulk_migrate_listing_header, data=bulk_migrate_listing_payload)

        print("bulk_migrate_listing_status===>", bulk_migrate_listing.status_code)
        print("bulk_migrate_listing_text=====>", bulk_migrate_listing.text)

        return render(request, self.template, locals())


class GetNotification(View):
    template = 'notification.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(GetNotification, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        print("====GET=====")
        print(request)
        print(request.body)
        response = request
        return render(request, self.template, locals())

    def post(self, request):
        print("====POST=====")
        print(request)
        # print(request.body)
        data = request.body
        # value = ET.fromstring(data).find('AddDisputeRequest')
        print("====Start data====")
        print(data)
        print("====end data====")
        response = {
            'status': 200,
            'type': 'OK'
        }
        return JsonResponse(response, safe=False)
