#!/usr/bin/python3
"""
Script to print hot posts on a given Reddit subreddit.
"""

import requests


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""
    # Construct the URL for the subreddit's hot posts in JSON format
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)

    # Define headers for the HTTP request, including User-Agent
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }

    # Define parameters for the request, limiting the number of posts to 10
    params = {
        "limit": 10
    }

    try:
        # Send a GET request to the subreddit's hot posts page
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)

        # Check the response status code
        if response.status_code != 200:
            print("None")
            return

        # Parse the JSON response and extract the 'data' section
        results = response.json().get("data", {})

        # Check if 'children' key exists in the response
        children = results.get("children", [])
        if not children:
            print("None")
            return

        # Print the titles of the top 10 hottest posts
        for c in children:
            print(c.get("data", {}).get("title", "No Title"))

    except requests.exceptions.RequestException as e:
        print("An error occurred while fetching the subreddit data:", e)
    except ValueError as e:
        print("An error occurred while parsing the response:", e)

# Example usage
top_ten('python')
