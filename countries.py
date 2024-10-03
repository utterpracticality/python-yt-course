from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():
    url = "https://restcountries.com/v3.1/all"
    response = requests.get(url)
    countries = response.json()

    country_info = []
    for country in countries:
        try:
            name = country["name"]["common"]
            population = format(country["population"], ",")
            flag = country["flags"]["png"]
            language = list(country["languages"].values())
        except KeyError as e:
            print(f"Country {country['name']['common']} had a key error: ", e)

        country_info.append({"name": name, "population": population, "flag": flag, "language": language})
        num_countries = len(countries)

    return render_template("index.html", countries=country_info, num_countries=num_countries)

if __name__ == "__main__":
    app.run()


