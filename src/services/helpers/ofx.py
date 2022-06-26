import requests

class OFX:

    def __init__(self, gte, lte, currency_from, currency_to, *args, **kwargs):
        # self.url = "https://api.ofx.com/PublicSite.ApiService//SpotRateHistory/10year/JPY/IDR"
        self.gte = gte,
        self.lte = lte, 
        self.currency_from = currency_from,
        self.currency_to = currency_to,
        self.base_url = "https://api.ofx.com/PublicSite.ApiService//SpotRateHistory/"
        self.querystring = {
                "DecimalPlaces":"2",
                "ReportingInterval":"daily",
                "format":"json"
            }
        self.payload = ""
        self.headers = {
            "cookie": "AWSALB=KQnhdIBF1N9yF80SK9BvJfFbNkgU0WbiefsOgZ2%2BJTt6x9VcMr4XiHa7QPPazWaWL6Smu50fSI8Tig6P1rzfs0fK1ATCwbYwJAWSoU5LeDrewY3nHKuZnNdYTx1g; AWSALBCORS=KQnhdIBF1N9yF80SK9BvJfFbNkgU0WbiefsOgZ2%2BJTt6x9VcMr4XiHa7QPPazWaWL6Smu50fSI8Tig6P1rzfs0fK1ATCwbYwJAWSoU5LeDrewY3nHKuZnNdYTx1g",
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:101.0) Gecko/20100101 Firefox/101.0",
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br",
            "Referer": "https://www.ofx.com/",
            "Origin": "https://www.ofx.com",
            "Connection": "keep-alive",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-site",
            "Sec-GPC": "1",
            "TE": "trailers"
        }

    def fetch(self, *args, **kwargs):
        url = f"{self.base_url}{self.currency_from[0]}/{self.currency_to[0]}/{self.gte[0]}/{self.lte[0]}"
        print(url)
        response = requests.request("GET", url, data=self.payload, headers=self.headers, params=self.querystring)
        if response.status_code >= 200 and response.status_code < 300:
            return response
        else:
            raise BaseException("OFX service has been error!")
