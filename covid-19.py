import requests


def get_covid_data(country):
    url = f"https://disease.sh/v3/covid-19/countries/{country}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(f"\nCOVID-19 Statistics for {data['country']}:")
        print(f"  - Cases: {data['cases']}")
        print(f"  - Today's Cases: {data['todayCases']}")
        print(f"  - Deaths: {data['deaths']}")
        print(f"  - Today's Deaths: {data['todayDeaths']}")
        print(f"  - Recovered: {data['recovered']}")
        print(f"  - Active: {data['active']}")
        print(f"  - Critical: {data['critical']}")
        print(f"  - Total Tests: {data['tests']}")
    else:
        print("⚠️ Could not retrieve data. Please check the country name.")


# Main function
def main():
    print("🌍 Welcome to the COVID-19 Global Data Tracker")
    while True:
        country = input("\nEnter a country name (or 'exit' to quit): ").strip()
        if country.lower() == 'exit':
            print("Goodbye 👋")
            break
        get_covid_data(country)


if __name__ == "__main__":
    main()
