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
   date_ranges=[DateRange(start_date='2024-06-01', end_date='2024-06-01')]
)

response = client.run_report(request)

csv_file_path = "/Users/p/Documents/VSC/ga4-api-gads/report.csv"

with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['date',
                     'googleAdsCampaignName',
                     'googleAdsCampaignId',
                     'keyEvents',
                     'advertiserAdCost',
                     'advertiserAdCostPerKeyEvent',
                     'advertiserAdImpressions',
                     'advertiserAdClicks',
                     'advertiserAdCostPerClick',
                     'purchaseRevenue',
                     'returnOnAdSpend'])

    for row in response.rows:
        writer.writerow([
            row.dimension_values[0].value,
            row.dimension_values[1].value,
            row.dimension_values[2].value,
            row.metric_values[0].value,
            row.metric_values[1].value,
            row.metric_values[2].value,
            row.metric_values[3].value,
            row.metric_values[4].value,
            row.metric_values[5].value,
            row.metric_values[6].value,
            row.metric_values[7].value

        ])

print(f"Wyniki zapisane do {csv_file_path}")