import requests
import matplotlib.pyplot as plt

def get_covid_data(country):
    url = f"https://disease.sh/v3/covid-19/countries/{country}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        print(f"\nCOVID-19 Statistics for {data['country']}:")
        print(f"Cases: {data['cases']}")
        print(f"Today's Cases: {data['todayCases']}")
        print(f"Deaths: {data['deaths']}")
        print(f"Recovered: {data['recovered']}")
        print(f"Active: {data['active']}")

        # Draw bar chart
        labels = ['Total Cases', 'Deaths', 'Recovered', 'Active']
        values = [data['cases'], data['deaths'], data['recovered'], data['active']]

        plt.figure(figsize=(8, 5))
        plt.bar(labels, values, color=['blue', 'red', 'green', 'orange'])
        plt.title(f"COVID-19 Summary: {data['country']}")
        plt.xlabel('Category')
        plt.ylabel('Number of People')
        plt.tight_layout()
        plt.show()

    else:
        print("⚠️ Could not retrieve data. Check the country name.")

def main():
    print("🌍 Welcome to the COVID-19 Tracker with Graphs")
    while True:
        country = input("\nEnter country name (or 'exit'): ")
        if country.lower() == 'exit':
            break
        get_covid_data(country)

if __name__ == "__main__":
    main()
