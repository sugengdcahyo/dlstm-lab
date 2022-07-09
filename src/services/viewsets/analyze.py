

from rest_framework import (
        status, permissions, generics, viewsets)
from rest_framework.response import Response
from random import randrange

class AnalyzeViewsets(generics.CreateAPIView, viewsets.GenericViewSet):
    serializer_class = None
    permission_classes = (permissions.AllowAny,)

    def create(self, request, *args, **kwargs):
        fields = ["model", "type", "timestep"]
        try:
            validate = self.validate(request, fields)
        except BaseException as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
        predict_histories = [
                ["Date", "Rate"],
                ["2021-1-1", 12000],
                ["2021-1-2", 12034],
                ["2021-1-3", 11099],
                ["2021-1-4", 11200],
                ["2021-1-5", 12400]
            ]
        predict_buckets=[]

        for idx, histo in enumerate(predict_histories):
            if idx == 0:
                histo.append("Predicted")
            else:
                histo.append(None)
            predict_buckets.append(histo)


        for idx in range(validate['timestep']):
            randomize = [f"2021-1-{idx+5}", None, randrange(10000, 15000)]
            predict_buckets.append(
                randomize
            )

        return Response(predict_buckets)

    def validate(self, request, fields=[]):
        for field in fields:
            if field not in request.data:
                raise BaseException(f"{field} is required.")

            if request.data[field] == None or request.data[field] == 0 or request.data[field] == "":
                raise BaseException(f"{field} not empty value.")
        return request.data
