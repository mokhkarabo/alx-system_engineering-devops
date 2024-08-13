#!/usr/bin/python3
"""
1-top_ten
"""
import requests

def top_ten(subreddit):
    """Print the titles of the first 10 hot posts listed for a given subreddit."""
    # Construct the URL for the subreddit's hot posts in JSON format
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    
    # Define headers for the HTTP request, including User-Agent
    headers = {
        "User-Agent": "python:subreddit.topten:v1.0.0 (by /u/yourusername)"
    }
    
    # Define parameters for the request, limiting the number of posts to 10
    params = {
        "limit": 10
    }
    
    try:
        # Send a GET request to the subreddit's hot posts page
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        
        # Check if the response status code indicates success
        if response.status_code == 200:
            data = response.json()
            posts = data.get("data", {}).get("children", [])
            
            if not posts:
                print("None")
                return
            
            for post in posts:
                print(post.get("data", {}).get("title", "No Title"))
        
        else:
            # Print None for any non-successful status codes (e.g., 404 for invalid subreddit)
            print("None")
    
    except requests.RequestException:
        # Handle any request exceptions and print None
        print("None")
