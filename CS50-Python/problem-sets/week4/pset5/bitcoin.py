import requests
from sys import argv, exit

API_url = "https://rest.coincap.io/v3/assets/bitcoin?apiKey=YOURAPIKEYHERE" # PLACE YOUR API KEY HERE


def main():
    try:
        if len(argv) <= 2:
            btc_amount = argv[1]
            btc_amount = float(btc_amount)
    except ValueError:
        exit("Command-line argument is not a number")
    except IndexError:
        exit("Missing command-line argument")

    data = api_response(API_url)

    btc_price = float(data["data"]["priceUsd"])
    total = btc_price * btc_amount
    print(f"${total:,.4f}")


def api_response(api_url):
    respone = requests.get(API_url)
    return respone.json()


if __name__ == "__main__":
    main()
