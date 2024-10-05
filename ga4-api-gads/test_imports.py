# test_imports.py
import csv
from google.oauth2 import service_account
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import DateRange, Dimension, Metric, RunReportRequest

print("Wszystkie biblioteki zostały zaimportowane poprawnie.")