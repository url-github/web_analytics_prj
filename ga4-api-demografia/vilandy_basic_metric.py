import csv
from google.oauth2 import service_account
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import DateRange, Dimension, Metric, RunReportRequest

# Ścieżka do pliku JSON z poświadczeniami konta serwisowego
credentials_path = "/Users/p/Documents/SA/sa-ga4-data.json"

# Wczytaj poświadczenia
credentials = service_account.Credentials.from_service_account_file(credentials_path)

# Utwórz klienta
client = BetaAnalyticsDataClient(credentials=credentials)

# Konfiguracja żądania
request = RunReportRequest(
   property='properties/347684205',  
   dimensions=[
       Dimension(name='date'),
    #    Dimension(name='customItem:offer'), # Wymiar niestandardowy na poziomie produktu.
       Dimension(name='googleAdsCampaignName'), # Nazwa kampanii Google Ads przypisanej do kluczowego zdarzenia.
       Dimension(name='googleAdsCampaignId'), # Identyfikator kampanii Google Ads przypisanej do kluczowego zdarzenia.
    #    Dimension(none='googleAdsAdGroupName'), # Nazwa grupy reklam przypisana do kluczowego zdarzenia. [Unknown field for Dimension: none]

    ],
   metrics=[
       Metric(name='keyEvents'), # Liczba kluczowych zdarzeń.
       Metric(name='advertiserAdCost'), # Łączny koszt reklam. Obejmuje koszty z połączonych integracji, takich jak połączone konta Google Ads.
       Metric(name='advertiserAdCostPerKeyEvent'), # Koszt kluczowego zdarzenia to koszt reklamy podzielony przez kluczowe zdarzenia.
       Metric(name='advertiserAdImpressions'), # Łączna liczba wyświetleń. Obejmuje wyświetlenia z połączonych integracji, takich jak połączeni reklamodawcy DV360.
       Metric(name='advertiserAdClicks'), # Łączna liczba kliknięć reklamy, które doprowadziły użytkowników do danej usługi. Obejmuje kliknięcia z połączonych integracji, takich jak połączeni reklamodawcy SA360.
       Metric(name='advertiserAdCostPerClick'), # Koszt kliknięcia reklamy to koszt reklamy podzielony przez liczbę kliknięć reklamy. Często jest to skrót od CPC.
       Metric(name='purchaseRevenue'), # Suma przychodów z zakupów pomniejszona o zwrócone przychody z transakcji dokonanych w Twojej aplikacji lub witrynie. Przychody z zakupów sumują przychody z tych zdarzeń: purchase.
       Metric(name='returnOnAdSpend') # Zwrot z nakładów na reklamę (ROAS) to łączne przychody podzielone przez koszt reklamy reklamodawcy.

   ],
   date_ranges=[DateRange(start_date='2024-06-01', end_date='2024-06-01')]
)

# Wykonaj żądanie
response = client.run_report(request)

# Ścieżka do pliku CSV
csv_file_path = "/Users/p/Documents/VSC/ga4-api-demografia/output_report.csv"

# Zapisz wyniki do pliku CSV
with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    # Napisz nagłówki
    writer.writerow(['date',
                     'googleAdsCampaignName',
                     'googleAdsCampaignId',
                    #  'googleAdsAdGroupName',
                     'keyEvents',
                     'advertiserAdCost',
                     'advertiserAdCostPerKeyEvent',
                     'advertiserAdImpressions',
                     'advertiserAdClicks',
                     'advertiserAdCostPerClick',
                     'purchaseRevenue',
                     'returnOnAdSpend'])

    # Napisz dane
    for row in response.rows:
        writer.writerow([
            row.dimension_values[0].value,
            row.dimension_values[1].value,
            row.dimension_values[2].value,
            # row.dimension_values[3].value,
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