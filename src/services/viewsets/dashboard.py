from datetime import datetime, timedelta
from rest_framework import (
        generics, viewsets, permissions)
from rest_framework.response import Response

from services.helpers.exchanger import ExchangeRates


class DashboardViewsets(generics.ListAPIView, viewsets.GenericViewSet):
    permission_classes = (permissions.AllowAny,)
    sample_response = None

    def list(self, request, *args, **kwargs):
        '''
        1. fetch date exchange latest one day
        2. convert to require response
        3. repeat process to other exchange
        '''
        params = {
                "gte": datetime.today().date() + timedelta(-1),
                "lte": datetime.today().date(),
                "scc": request.GET.get('scc') or "IDR"
            }
        target = ["USD", "JPY"]
        responses = []
        for exch in target:
            exchange = ExchangeRates()
            exchange.fetch_date_range_histories(**{**params, "bcc": exch})
            item = self.response_builder(exchange.data, exch)
            responses.append(item)
        return Response(responses)

    def response_builder(self, data, bcc):
        return {
                "updated_at": data[1][0],
                "bcc": bcc,
                "scc": "IDR",
                "exchange": self.get_exchange_rates(data[0][1], data[1][1])
            }

    def get_exchange_rates(self, a, b):
        return  {
                "value": round(b, 4),
                "one_day_before": round(a, 4),
                "distance": round(b-a, 4),
                "percentage": 0 if b-a ==0 else round((b-a)/a, 4) * 100
            }

