
from rest_framework import (
        generics, viewsets, permissions)
from rest_framework.response import Response


class DashboardViewsets(generics.ListAPIView, viewsets.GenericViewSet):
    permission_classes = (permissions.AllowAny,)

    def list(self, request, *args, **kwargs):
        response = {
                "currency_latest": {
                    "value": 0, 
                    "keyword": "Japan Yen",
                    "code": "JPY"
                }
            }
        return Response(response)
        
