# Import the 'requests' library to make HTTP requests
import requests

# Define the target website
target = "http://example.com"  # Change to your target URL

# Define the path of the word list file
wordList = "/exp/exp/exp.txt"   # Change to the correct path of your word list file

# Open and read the word list file
with open(wordList, 'r') as f:
    words = f.read().split('\n')

    # Iterate through each word in the word list
    for word in words:
        # Construct the full URL by appending the current word to the target URL
        url = f"{target}/{word}"
        # Send a GET request to the constructed URL
        r = requests.get(url)
        # Get the status code from the response
        status_code = r.status_code
        # Check if the status code is not 404 (page not found)
        if status_code != 404:
            # Print a message indicating a discovered web directory
            print(f"Found Web Directory: {url}")

            # If the status code is 404, do nothing (continue to the next word)

            # Thanks For Watching, You Can Find This Script And More in https://github.com/ThCyberMaster

