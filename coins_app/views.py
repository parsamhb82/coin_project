from django.shortcuts import render
import requests 
import json
from django.http import JsonResponse

def get_coins_price(request,src_currency, dst_currency ):
    if request.method == 'GET':
        url = f"https://api.nobitex.ir/market/stats?srcCurrency={src_currency}&dstCurrency={dst_currency}"
        response = requests.get(url)
        data = json.loads(response.content)
        if data['status'] == "ok":
            return JsonResponse({'latest-price' : data['stats'][f"{src_currency}-{dst_currency}"]['latest']}, safe=False)
        return JsonResponse({'status': 'error'}, safe=False)
    return JsonResponse({'status': 'error'}, safe=False)
    
def get_coins_latest_change(request, src_currency):
    if request.method == 'GET':
        url = f"https://api.nobitex.ir/market/stats?srcCurrency={src_currency}&dstCurrency=rls"
        response = requests.get(url)
        data = json.loads(response.content)
        if data['status'] == "ok":
            return JsonResponse({'day-change' : data['stats'][f"{src_currency}-rls"]['dayChange']}, safe=False)
        return JsonResponse({'status': 'error'}, safe=False)
    return JsonResponse({'status': 'error'}, safe=False)


