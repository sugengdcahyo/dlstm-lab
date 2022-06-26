from ..helpers.ofx import OFX

import datetime, time
from datetime import timedelta

from rest_framework import (
        permissions, status, generics, viewsets)
from rest_framework.response import Response

def date_range(request):
    gte = request.GET.get('gte') or datetime.datetime.now() + timedelta(-10)
    lte = request.GET.get('lte') or datetime.datetime.now()
    return time.mktime(gte.timetuple())*1000, time.mktime(lte.timetuple()) * 1000

class CurrencyViewsets(generics.ListAPIView, viewsets.GenericViewSet):
    permission_classes = (permissions.AllowAny,)
    
    def list(self, request, *args, **kwargs):
        gte, lte = date_range(request)
        currency_x = request.GET.get('from') or "IDR"
        currency_y = request.GET.get('to') or "USD"
        histories = OFX(int(gte), int(lte), currency_x, currency_y).fetch()
        try:
            histories = OFX(int(gte), int(lte), currency_x, currency_y).fetch()
            return Response({"histories": histories.json()}, status=status.HTTP_200_OK)
        except BaseException as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
