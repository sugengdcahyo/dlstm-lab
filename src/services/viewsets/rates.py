from services.helpers.exchanger import (
        ExchengeRateLabel
    )

from rest_framework import (
        generics, viewsets, status, permissions)
from rest_framework.response import Response


class RatesViewsets(generics.ListAPIView, viewsets.GenericViewSet):
    permission_classes = (permissions.AllowAny,)

    def list(self, request, *args, **kwargs):
        q = request.GET.get('q', None)
        exchange = ExchengeRateLabel()
        exchange.fetch_exchage_rate()

        response = []

        if q == 'currency' or not q:
            print("disini")
            for resp in exchange.rates:
                if resp['issuer'] != 'Cryptocurrency':
                    response.append(resp)

        elif q == 'crypto' or q == 'cryptocurrency':
            for resp in exchange.rates:
                if resp['issuer'] == 'Cryptocurrency':
                    response.append(resp)

        return Response(response, 200)