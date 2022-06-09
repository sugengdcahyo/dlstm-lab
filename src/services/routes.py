from rest_framework import routers
from .viewsets.models import ModelViewsets
from .viewsets.predict import PredictViewsets

router = routers.DefaultRouter()

router.register('predict', PredictViewsets, basename='predict-viewsets')
router.register('models', ModelViewsets, basename='models-viewsets')

service_urls = router.urls