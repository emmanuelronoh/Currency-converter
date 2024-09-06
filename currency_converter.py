import requests

def get_exchange_rate(api_key, base_currency, target_currency):
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{base_currency}"
    response = requests.get(url)
    data = response.json()

    if response.status_code != 200:
        raise Exception(f"Error fetching data: {data.get('error-type', 'Unknown error')}")

    rates = data.get("conversion_rates", {})
    rate = rates.get(target_currency)

    if rate is None:
        raise Exception(f"Currency code {target_currency} not found.")

    return rate

def convert_currency(api_key, amount, base_currency, target_currency):
    rate = get_exchange_rate(api_key, base_currency, target_currency)
    return amount * rate

def main():
    api_key = 'aedf9fc2be73bb65d9edd16a'  # Your API key
    base_currency = input("Enter base currency (e.g., USD): ").upper()
    target_currency = input("Enter target currency (e.g., EUR): ").upper()
    amount = float(input(f"Enter amount in {base_currency}: "))

    try:
        converted_amount = convert_currency(api_key, amount, base_currency, target_currency)
        print(f"{amount} {base_currency} is equal to {converted_amount:.2f} {target_currency}")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
