import requests

# Ersetzen Sie 'your_api_key_here' durch Ihren OpenWeatherMap API-Schlüssel
API_KEY = 'your_api_key_here'  # Der API-Schlüssel zur Authentifizierung bei der OpenWeatherMap API
CITY = 'your_city_here'  # Name der Stadt, für die die Wetterdaten abgerufen werden sollen
COUNTRY = 'your_country_code_here'  # Ländercode (z. B. 'DE' für Deutschland)
UNIT = 'metric'  # Verwenden Sie 'imperial' für Fahrenheit

def get_weather(api_key, city, country):
    """
    Diese Funktion ruft Wetterdaten von der OpenWeatherMap API ab.

    :param api_key: Der API-Schlüssel für den Zugriff auf die Wetterdaten.
    :param city: Der Name der Stadt, für die die Wetterdaten abgerufen werden sollen.
    :param country: Der Ländercode der Stadt.
    :return: Ein Dictionary mit den Wetterdaten, falls erfolgreich; andernfalls None.
    """
    # Die URL zur Abfrage der Wetterdaten wird erstellt.
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={api_key}&units={UNIT}'
    response = requests.get(url)  # Eine GET-Anfrage an die API wird gesendet.
    
    if response.status_code == 200:  # Überprüfung, ob die Anfrage erfolgreich war.
        return response.json()  # Die Wetterdaten werden im JSON-Format zurückgegeben.
    else:
        print("Error fetching weather data.")  # Fehlermeldung, falls die Anfrage fehlschlägt.
        return None  # Gibt None zurück, wenn die Daten nicht abgerufen werden konnten.

def suggest_outfit(temperature, weather_description):
    """
    Diese Funktion schlägt basierend auf der Temperatur und Wetterbeschreibung ein Outfit vor.

    :param temperature: Die aktuelle Temperatur in Grad Celsius.
    :param weather_description: Eine Beschreibung des aktuellen Wetters.
    :return: Ein String mit Outfit-Empfehlungen.
    """
    # Bestimmung des Outfits anhand der Temperatur
    if temperature >= 25:
        outfit = "It's hot! Wear light clothing like shorts and a t-shirt."
    elif 15 <= temperature < 25:
        outfit = "The weather is mild. You can wear jeans and a light shirt."
    elif 5 <= temperature < 15:
        outfit = "It's a bit chilly. Wear a jacket or a sweater."
    elif -5 <= temperature < 5:
        outfit = "It's cold! Wear a winter coat, hat, and gloves."
    else:
        outfit = "It's freezing! Dress warmly with a heavy coat, scarf, and gloves."

    # Zusätzliche Empfehlungen basierend auf der Wetterbeschreibung
    if 'rain' in weather_description or 'drizzle' in weather_description:
        outfit += " Don't forget an umbrella or a raincoat!"  # Empfehlung für Regen
    elif 'snow' in weather_description:
        outfit += " It's snowing, so make sure to wear waterproof boots and a warm hat."  # Empfehlung für Schnee
    
    return outfit  # Rückgabe der Outfit-Empfehlung

# Hauptfunktion
def main():
    """
    Die Hauptfunktion des Programms, die die Wetterdaten abruft und das Outfit vorschlägt.
    """
    weather_data = get_weather(API_KEY, CITY, COUNTRY)  # Abrufen der Wetterdaten
    
    if weather_data:  # Überprüfung, ob Wetterdaten erfolgreich abgerufen wurden.
        temp = weather_data['main']['temp']  # Aktuelle Temperatur aus den Wetterdaten extrahieren.
        description = weather_data['weather'][0]['description']  # Wetterbeschreibung extrahieren.
        print(f"The current temperature is {temp}°C with {description}.")  # Ausgabe der Temperatur und Wetterbeschreibung.
        outfit = suggest_outfit(temp, description)  # Outfit-Empfehlung basierend auf Temperatur und Beschreibung.
        print(outfit)  # Ausgabe der Outfit-Empfehlung.

# Ausführung der Hauptfunktion
if __name__ == "__main__":
    main()
