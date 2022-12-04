from datetime import datetime, timedelta
from services.utils.reshaping_responses import history_standarization
from services.helpers.exchanger import (
        ExchangeRates
    )

from rest_framework import (
        generics, viewsets, status, permissions)
from rest_framework.response import Response


class HistoriesViewsets(generics.ListAPIView, viewsets.GenericViewSet):
    permission_classes = (permissions.AllowAny,)

    def list(self, request, *args, **kwargs):
        exchange = ExchangeRates()
        params = {
            "gte": request.GET.get('gte') or str(datetime.today().date() + timedelta(-7)),
            "lte": request.GET.get('lte') or str(datetime.today().date()),
            "bcc": request.GET.get('bcc') or "USD",
            "scc": request.GET.get('scc') or "IDR"
        }
        exchange.fetch_date_range_histories(**params)
        histories = history_standarization(data=exchange.data)
        return Response({**params, "data":histories})

class HistoryOneDayViewsets(generics.ListAPIView, viewsets.GenericViewSet):
    permission_classes = (permissions.AllowAny,)

    def get_change_rate(self, current, last_one):
        return current - last_one
    
    def get_percentage_change_rate(self, last_one, change_rate):
        return change_rate / last_one
    
    sample_response = [{
            "bcc": "USD",
            "scc": "IDR",
            "gte": 223480234,
            "lte": 129389012,
            "data": {
                "today": {
                    "value": 12312,
                    "timestamp": 129813,
                },
                "one_day_before": {
                    "value": 1231,
                    "timestamp": 1928312
                },
                "exchange": {
                    "rate": -0.12,
                    "percentage": -0.001
                }
            }
        }]
    def list(self, request, *args, **kwargs):
        exchange = ExchangeRates()
        params = {
                "gte": datetime.today().date() + timedelta(-30),
                "lte": datetime.today().date(),
                "bcc": request.GET.get('bcc') or "USD",
                "scc": request.GET.get('scc') or "IDR"
            }
        exchange.fetch_date_range_histories(**params)
        change_rate = exchange.data[1][1] - exchange.data[0][1]
        change_rate_percentage = change_rate / exchange.data[0][1]
        return Response({
            **params, 
            "histories": exchange.data,
            "data": {
                "value": round(exchange.data[1][1], 2),
                "change": round(change_rate, 2),
                "percentage": round(change_rate_percentage * 100, 2)
            }
        })
