# Fetches a random joke from the Official Joke API.
# API URL: https://official-joke-api.appspot.com/random_joke

import requests

def fetch_random_joke():
    
    url = "https://official-joke-api.appspot.com/random_joke"
    
    try:
        response = requests.get(url)  # Send GET request
        response.raise_for_status()   # Raise error if request failed
        
        # Parse JSON response
        joke = response.json()
        print("Here's a random joke for you:")
        print(f"{joke['setup']} - {joke['punchline']}")
    
    except requests.exceptions.HTTPError as errh:
        print("HTTP Error:", errh)
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:", errc)
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:", errt)
    except requests.exceptions.RequestException as err:
        print("Something went wrong:", err)

# Run the program
fetch_random_joke()
