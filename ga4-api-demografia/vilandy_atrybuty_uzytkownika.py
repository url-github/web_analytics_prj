import csv
from google.oauth2 import service_account
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import DateRange, Dimension, Metric, RunReportRequest

credentials_path = "/Users/p/Documents/SA/sa-ga4-data.json"
credentials = service_account.Credentials.from_service_account_file(credentials_path)
client = BetaAnalyticsDataClient(credentials=credentials)

request = RunReportRequest(
   property='properties/347684205',  
   dimensions=[
       Dimension(name='date'),
       Dimension(name='userAgeBracket'), 
    #    Dimension(name='userGender'), 
    ],
   metrics=[
       Metric(name='activeUsers'),
   ],
   date_ranges=[DateRange(start_date='2024-07-01', end_date='2024-07-01')]
)

# Wykonaj żądanie
response = client.run_report(request)

# Ścieżka do pliku CSV
csv_file_path = "/Users/p/Documents/VSC/ga4-api-demografia/output_report_atrybuty_uzytkownika.csv"

# Zapisz wyniki do pliku CSV
with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    # Napisz nagłówki
    writer.writerow(['date',
                     'userAgeBracket',
                     'activeUsers'])

    # Napisz dane
    for row in response.rows:
        writer.writerow([
            row.dimension_values[0].value,
            row.dimension_values[1].value,
            row.metric_values[0].value

        ])

print(f"Wyniki zapisane do {csv_file_path}")