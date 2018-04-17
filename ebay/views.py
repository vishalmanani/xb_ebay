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
        # r_access_token = "v^1.1#i^1#p^3#f^0#r^0#I^3#t^H4sIAAAAAAAAAOVXbWwURRju9Qva8mUEBALJsUggkL2bvd29vVt7F68thJoWzl4BqdYytzvbruztnjtzbc9oUhotJoJRAzH1IzR+gGgQCBFiSAjGoCEaixpQiWkQhRikJuoPEkR09vrBtUpLW340sX+anXk/nvd5n3duBrQVFq3oWNNxdbprSm5XG2jLdbm4ElBUWLByRl7ugoIckGXg6mq7ty2/Pe/nUgwTRlKuQThpmRi5WxOGieXMYohJ2aZsQaxj2YQJhGWiyLFIdZXs8wA5aVvEUiyDcVdWhBhRUwKi5FMEwAuCpiC6ag7ErLXofjwARcUv8ZLiR5Km0n2MU6jSxASaJMT4ABdggcByQi2QZJ8oc7xHCEh1jHsDsrFumdTEA5hwBq6c8bWzsI4MFWKMbEKDMOHKyOrYukhlxaq1taXerFjhfh5iBJIUHvpVbqnIvQEaKTRyGpyxlmMpRUEYM95wX4ahQeXIAJhxwM9Q7Vd9SEAaFDjKp0+R7giVqy07AcnIOJwVXWW1jKmMTKKT9GiMUjbijyGF9H+tpSEqK9zOvwdT0NA1HdkhZlVZZNP62Koaxh2LRm2rWVeR6lTKSX5JCPqloJ8JN+s4Ac0GIdCfpC9SP8XDspRbpqo7hGH3WouUIYoYDeeFy+KFGq0z19kRjThosu2Cg/wJdU5D+zqYIk2m01OUoCS4M5+jsz8gh5sCuFOC0IIaElVJjEs80vx84D8F4cz6GEURdvoSiUa9DhYUh2k2Ae0tiCQNqCBWofSmEsjWVZkXNR8f0BCr+oMaKwQ1jY2Lqp/lNIQAQvG4Egz8X7RBiK3HUwQN6mP4RqbAEBNTrCSKWoaupJnhJpmzpl8NrTjENBGSlL3elpYWTwvvsexGrw8AzvtQdVVMaUIJyAza6qMbs3pGF84RTe1lkk5SNK1UdjS52ciEeVuNQpukY8gw6MKAaIdgCw9fvUWR2ClycpXn+GMaACZ1j6Npj2IlvBakM+wsNWQQu2/HyIspQZ6+iaCRPTaCqmUa6fE4j8FHN5upqCw7PUJCZ9ZHDzCGpFBRrJRJxlNjv+sYPLSUoemG4czOeBJmuY8FpgmNNNEVPJhyQsKPJJOV6uQSPj0km6BB7VrjBGHCRmsq2LgU8CMu4KNnGpLUIK18QlVXN+qTrGjOJ3ICH+ABD4B/QrVVoObJ1lEgCqqU354bVRWBVUV/kBXiEmShqgosUOivsAR42mBpQnWXGzqdpNr0ZDvH11iYoInJtZxeoiZXUc5MDoxkXBAQ6weac6ESAiwUgxLLQQnebsneW95H/nUN9Q59A4ZzMn9cu+sD0O46RJ+RwAuWckvA4sK89fl50xZgnSCPDjUP1htN+rSxkWcLSiehbucWuh5eeHBfQ9ars6sezBt8dxblcSVZj1Cw8OZOATfznulcAAicACQ6tnwdWHJzN5+bmz87V9za0HP68jevnus+3f3c4XC6a9sOMH3QyOUqyMlvd+XI7ZFHz+9webw1G+PHWi+eeW/OVweuvX/1rR+erVzUE5z2yPeLS+dvfLP3emJFxzvber7ePevF8/OrrnTtvFI29cLvnXsObPuyaPPn3UfOLd+1/8Pq4l3Pnzql4k115rJjvXb9a8Kfyt3F5Z13Vc1bdPGzo29f2+T9+7i75IGT962xH7dDl17YPHu965M39voOzvy2t3jK3sudPyYjS3t//fiM+PpPM47HL5QyX5S9/Ol2PrWEPH20+MLcV3qqru/bv3PPb+JLO9J6w/GpzSsPHV6+r377u6H6LV1K+Oylhr+eefKjX+bc+OPkiUio42xL6dEDnd/1Hjm7ddZTT8SW1e7ZLZ7aVeE+Mf9gd8mc+695am/0te8fJlHcow8QAAA="
        inventory_url = 'https://api.ebay.com/sell/inventory/v1/inventory_item?limit=2&offset=0'

        inventory_header = {
            'Authorization': 'Bearer %s' % r_access_token
        }

        print(inventory_header)
        inventory = requests.get(inventory_url, headers=inventory_header)

        print("inventory_status===>", inventory.status_code)
        print("inventory_text=====>", inventory.text)

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
        print(request.body)
        data = request.body
        # value = ET.fromstring(data).find('AddDisputeRequest')
        print(data)
        return HttpResponse(data)
