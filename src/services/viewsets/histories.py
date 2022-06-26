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
            "bcc": request.GET.get('bcc'),
            "scc": request.GET.get('scc')
        }
        exchange.fetch_date_range_histories(**params)
        histories = history_standarization(exchange.data)
        return Response({**params, "data":histories})
