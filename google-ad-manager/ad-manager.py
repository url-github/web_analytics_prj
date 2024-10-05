from googleads import ad_manager


def main(client):
  # Initialize appropriate service.
  network_service = client.GetService('NetworkService', version='v202402')

  current_network = network_service.getCurrentNetwork()

  print("Current network has network code '%s' and display name '%s'." %
        (current_network['networkCode'], current_network['displayName']))


if __name__ == '__main__':
  # Initialize client object.

  ad_manager_client = ad_manager.AdManagerClient.LoadFromStorage(r"C:\Users\pmackowka\OneDrive - Empik S.A\Dokumenty\Dokumenty\github\ad-manager\googleads.yaml")

  main(ad_manager_client)
