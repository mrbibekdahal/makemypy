import requests


def welcome():
    print("=" * 40)
    print("      Foreign Currency Converter")
    print("=" * 40)
    print("Uses live exchange rates.\n")


def get_rates():
    try:
        url = "https://open.er-api.com/v6/latest/USD"

        response = requests.get(url, timeout=10)

        response.raise_for_status()

        data = response.json()

        return data["rates"]

    except requests.exceptions.RequestException:
        print("\n❌ Unable to connect to the exchange rate server.")
        return None


def show_currencies(rates):
    print("\nAvailable currencies:\n")

    for currency in sorted(rates):
        print(currency, end="  ")

    print("\n")


def get_amount():
    while True:
        try:
            amount = float(input("Enter amount: "))

            if amount <= 0:
                print("Amount must be greater than zero.\n")
                continue

            return amount

        except ValueError:
            print("Please enter a valid number.\n")


def get_currency(message, rates):
    while True:

        currency = input(message).upper().strip()

        if currency in rates:
            return currency

        print("Invalid currency code. Try again.\n")


def convert(amount, from_currency, to_currency, rates):

    if from_currency == to_currency:
        return amount

    amount_in_usd = amount / rates[from_currency]

    converted_amount = amount_in_usd * rates[to_currency]

    return converted_amount


def main():

    welcome()

    rates = get_rates()

    if rates is None:
        return

    while True:

        show_currencies(rates)

        amount = get_amount()

        from_currency = get_currency("From Currency: ", rates)

        to_currency = get_currency("To Currency: ", rates)

        result = convert(amount, from_currency, to_currency, rates)

        print(f"\n✅ {amount:.2f} {from_currency} = {result:.2f} {to_currency}\n")

        choice = input("Do another conversion? (y/n): ").lower().strip()

        if choice != "y":
            print("\nThank you for using the converter!")
            break


if __name__ == "__main__":
    main()