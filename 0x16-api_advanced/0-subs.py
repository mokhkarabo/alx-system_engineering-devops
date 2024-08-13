import requests

def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit.
    
    Args:
        subreddit (str): The name of the subreddit to query.
    
    Returns:
        int: The number of subscribers, or 0 if the subreddit is invalid.
    """
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {
        'User-Agent': 'python:subreddit_info:v1.0.0 (by /u/yourusername)'
    }
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check for successful response
        if response.status_code == 200:
            data = response.json()
            return data.get('data', {}).get('subscribers', 0)
        
        # If subreddit does not exist or other errors, return 0
        return 0

    except requests.RequestException:
        # Catch any request-related exceptions
        return 0
