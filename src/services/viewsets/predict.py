from rest_framework import (
    generics, status, viewsets
)
from rest_framework.response import Response
import random

class PredictViewsets(generics.CreateAPIView, viewsets.GenericViewSet):

    def create(self, request, *args, **kwargs):
        try:
            validate = self.validate(request.data)
        except BaseException as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        predicted = []
        for i in range(int(request.data['range'])):
            predicted.append({"time": i+1, "value": random.randint(800, 3000)})
        
        return Response(predicted, status=status.HTTP_200_OK)

    def validate(self, data):
        if 'histories' not in data:
            raise BaseException("Histories is required.")
            if type(data['histories']) is not type([]):
                raise BaseException("Histories only list data.")
        
        elif 'model' not in data:
            raise BaseException("Model is required.")

        elif 'range' not in data:
            raise BaseException("Range is required.")
            if type(int(data['range'])) is not type(int()):
                raise BaseException("Range must be integer.")

        return data
