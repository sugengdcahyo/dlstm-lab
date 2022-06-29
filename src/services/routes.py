from rest_framework import routers

from services.viewsets.rates import RatesViewsets
from services.viewsets.currency import CurrencyViewsets
from services.viewsets.dashboard import DashboardViewsets
from services.viewsets.histories import HistoriesViewsets, HistoryOneDayViewsets
from .viewsets.models import ModelViewsets
from .viewsets.predict import PredictViewsets

router = routers.DefaultRouter()

router.register('currency', CurrencyViewsets, basename='currency-histories')
router.register('dashboard', DashboardViewsets, basename='dashboard-viewsets')
router.register('dashboard/charts', DashboardViewsets, basename='dashboard-viewsets')
router.register('histories', HistoriesViewsets, basename='histories-viewsets')
router.register('latest-day', HistoryOneDayViewsets, basename='latest-day-histories-viewsets')
router.register('predict', PredictViewsets, basename='predict-viewsets')
router.register('rates', RatesViewsets, basename='get-range-exchange')
router.register('models', ModelViewsets, basename='models-viewsets')

service_urls = router.urls
