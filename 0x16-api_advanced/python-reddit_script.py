import requests

def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit."""
    headers = {'User-Agent': 'my-app/0.0.1'}
    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data.get('data', {}).get('subscribers', 0)
        else:
            print(f"Error fetching subscribers: HTTP {response.status_code}")
            return 0
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return 0

def top_ten(subreddit):
    """Prints the titles of the top ten hot posts for a given subreddit."""
    headers = {'User-Agent': 'my-app/0.0.1'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'

    try:
        response = requests.get(url, headers=headers, params={'limit': 10}, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data.get('data', {}).get('children', [])
            if not posts:
                print("No posts found.")
                return

            for post in posts:
                print(post.get('data', {}).get('title', "No Title"))
        else:
            print(f"Error fetching top ten posts: HTTP {response.status_code}")
    except requests.RequestException as e:
        print(f"An error occurred: {e}")

def recurse(subreddit, hot_list=[], after=None):
    """Recursively gets all hot post titles for a given subreddit."""
    headers = {'User-Agent': 'my-app/0.0.1'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    params = {'after': after}

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data.get('data', {}).get('children', [])
            for post in posts:
                hot_list.append(post.get('data', {}).get('title', "No Title"))

            after = data.get('data', {}).get('after')
            if after:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        else:
            print(f"Error fetching posts: HTTP {response.status_code}")
            return hot_list
    except requests.RequestException as e:
        print(f"An error occurred while fetching data: {e}")
        return hot_list

def count_words(subreddit, word_list):
    """Counts the occurrences of each word in word_list in the hot posts of a subreddit."""
    hot_titles = recurse(subreddit)
    if not hot_titles:
        return

    word_count = {word.lower(): 0 for word in word_list}

    for title in hot_titles:
        words = title.lower().split()
        for word in word_count:
            word_count[word] += words.count(word)

    sorted_word_count = sorted(word_count.items(), key=lambda item: (-item[1], item[0]))

    for word, count in sorted_word_count:
        if count > 0:
            print(f"{word}: {count}")

# Example usage
if __name__ == "__main__":
    subreddit = 'learnpython'  # Example subreddit

    # Number of subscribers
    print(f'The number of subscribers for {subreddit}:', number_of_subscribers(subreddit))

    # Top ten hot posts
    print(f'\nTop ten hot posts in {subreddit}:')
    top_ten(subreddit)

    # Recursively get hot post titles
    print(f'\nHot post titles in {subreddit}:')
    hot_list = recurse(subreddit)
    print(hot_list)

    # Count words in hot posts
    word_list = ['python', 'learning', 'tutorial']
    print(f'\nWord counts in hot posts in {subreddit}:')
    count_words(subreddit, word_list)
