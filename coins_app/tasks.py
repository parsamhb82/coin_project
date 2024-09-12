from celery import shared_task
from .models import LowerConditions, HigherConditions
import requests
import json
from django.core.mail import send_mail
@shared_task(bind= True, default_retry_delay=10)
def check_lowers(self):
    try:
        lowers = LowerConditions.objects.all()
        for lower in lowers:
            src_currency = lower.src_currency
            condition_price = lower.condition_price
            url = f"https://api.nobitex.ir/market/stats?srcCurrency={src_currency}&dstCurrency=rls"
            response = requests.get(url)
            data = json.loads(response.content)
            price = data['stats'][f"{src_currency}-rls"]['latest']
            if price <= condition_price:
                # print(f"Condition met for {src_currency} with price {price}")
                send_mail(
                    'subject',
                    f"Condition met for {src_currency} with price {price}",
                    'a06793342@gmail.com',
                    [f'{lower.email}'],
                    fail_silently=False
                )
    except Exception as e:
        return self.retry(exc=e,max_retries=10)



@shared_task(bind= True, default_retry_delay=10)
def check_highers(self):
    try:
        highers = HigherConditions.objects.all()
        for higher in highers:
            src_currency = higher.src
            condition_price = higher.condition_price
            url = f"https://api.nobitex.ir/market/stats?srcCurrency={src_currency}&dstCurrency=rls"
            response = requests.get(url)
            data = json.loads(response.content)
            price = data['stats'][f"{src_currency}-rls"]['latest']
            if price >= condition_price:
                # print(f"Condition met for {src_currency} with price {price}")
                send_mail(
                    'subject',
                    f"Condition met for {src_currency} with price {price}",
                    'a06793342@gmail.com',
                    [f'{higher.email}'],
                    fail_silently=False
                )
    except Exception as e:
        return self.retry(exc=e,max_retries=10)



