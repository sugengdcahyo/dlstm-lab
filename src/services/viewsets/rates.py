from services.helpers.exchanger import (
        ExchengeRateLabel
    )

from rest_framework import (
        generics, viewsets, status, permissions)
from rest_framework.response import Response


class RatesViewsets(generics.ListAPIView, viewsets.GenericViewSet):
    permission_classes = (permissions.AllowAny,)

    def list(self, request, *args, **kwargs):
        exchange = ExchengeRateLabel()
        exchange.fetch_exchage_rate()
        return Response(exchange.rates)
