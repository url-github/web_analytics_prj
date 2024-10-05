import json
from datetime import date, timedelta
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import DateRange, Dimension, Metric, RunReportRequest
from google.cloud import bigquery

PROPERTY_ID = 'properties/347684205'
DATASET_ID = 'analytics_907689214'
TABLE_ID = '1cfdcbed2215436eb910901138e1ea84'

def ga4_api_gads(request):
    try:
        # Obliczanie daty przedwczoraj
        przedwczoraj = date.today() - timedelta(days=2)
        przedwczoraj_str = przedwczoraj.strftime('%Y-%m-%d')

        # Inicjalizacja klientów
        client = BetaAnalyticsDataClient()
        bq_client = bigquery.Client()

        # Konfiguracja zapytania do Google Analytics
        request = RunReportRequest(
            property=PROPERTY_ID,
            dimensions=[
                Dimension(name='date'),
                Dimension(name='googleAdsCampaignName'),
                Dimension(name='googleAdsCampaignId'),
            ],
            metrics=[
                Metric(name='keyEvents'),
                Metric(name='advertiserAdCost'),
                Metric(name='advertiserAdCostPerKeyEvent'),
                Metric(name='advertiserAdImpressions'),
                Metric(name='advertiserAdClicks'),
                Metric(name='advertiserAdCostPerClick'),
                Metric(name='purchaseRevenue'),
                Metric(name='returnOnAdSpend')
            ],
            date_ranges=[DateRange(start_date=przedwczoraj_str, end_date=przedwczoraj_str)]
        )

        # Pobranie raportu z Google Analytics
        response = client.run_report(request)

        # Przygotowanie danych do załadowania do BigQuery
        rows_to_insert = [
            {
                "date": row.dimension_values[0].value,
                "googleAdsCampaignName": row.dimension_values[1].value,
                "googleAdsCampaignId": row.dimension_values[2].value,
                "keyEvents": float(row.metric_values[0].value),
                "advertiserAdCost": float(row.metric_values[1].value),
                "advertiserAdCostPerKeyEvent": float(row.metric_values[2].value),
                "advertiserAdImpressions": int(float(row.metric_values[3].value)),
                "advertiserAdClicks": int(float(row.metric_values[4].value)),
                "advertiserAdCostPerClick": float(row.metric_values[5].value),
                "purchaseRevenue": float(row.metric_values[6].value),
                "returnOnAdSpend": float(row.metric_values[7].value)
            }
            for row in response.rows
        ]

        # Wstawianie danych do BigQuery
        table_ref = bq_client.dataset(DATASET_ID).table(TABLE_ID)
        errors = bq_client.insert_rows_json(table_ref, rows_to_insert)

        if not errors:
            return json.dumps({"message": "Dane zostały pomyślnie zapisane."}), 200
        else:
            return json.dumps({"error": f"Wystąpiły błędy: {errors}"}), 500

    except Exception as e:
        return json.dumps({"error": str(e)}), 500