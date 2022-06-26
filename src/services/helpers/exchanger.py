import requests
import datetime, time

EX_BAD_REQUEST_ERROR = "Any problem in exchange rate server target."

"""
services from https://exchangerate.guru
"""
class BaseExchange:

    def __init__(self, *args, **kwargs):
        self.url = "https://exchangerate.guru/system"
        self.querystring = {}

        self.payload = ""
        self.headers = {
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:101.0) Gecko/20100101 Firefox/101.0",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br",
            "X-Requested-With": "XMLHttpRequest",
            "Connection": "keep-alive",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "Sec-GPC": "1",
            "TE": "trailers"
        }


class ExchangeRates(BaseExchange):

    def fetch_date_range_histories(self, bcc, scc, gte, lte):
        url = f"{self.url}/exchange-rate-chart"

        querystring = {
                "amount":"1",
                "bcc": bcc,
                "scc": scc,
                "dateFrom": gte,
                "dateTo": lte
            }
        response = requests.request("GET", url, data=self.payload, headers=self.headers, params=querystring)
        
        if response.status_code == 200 and response.status_code < 400:
            self.data = response.json()
        else:
            raise BaseException(EX_BAD_REQUEST_ERROR)

class ExchengeRateLabel(BaseExchange):

    # fetch global exchange rates
    def fetch_exchage_rate(self, *args, **kwargs):
        url = f"{self.url}/get-rates"
        self.querystring = {
                "date": str(datetime.datetime.today().date())}
        response = requests.request("GET", url, data=self.payload, headers=self.headers, params=self.querystring)
        if response.status_code >= 200 and response.status_code < 400:
            self.rates = response.json()
        else:
            raise BaseException(EX_BAD_REQUEST_ERROR)
