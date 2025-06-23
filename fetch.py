#!/usr/bin/env python3
"""
Script to fetch Hacker News (news.ycombinator.com) and obtain the linked pages.
"""

from concurrent.futures import ThreadPoolExecutor, as_completed

import requests

URL_BASE = 'https://hacker-news.firebaseio.com/v0/'
STORIES_URL = f'{URL_BASE}topstories.json'
INFO_URL = f'{URL_BASE}item/'
HEADERS = {
    'User-Agent': (
        'Mozilla/5.0 (compatible; HNLinkScraper/1.0; '
        '+https://github.com/brandonlmorris)'
    )
}


def top_story_ids(limit=10):
    """Retrieve the story identifiers for the top stories on Hacker News."""
    resp = requests.get(STORIES_URL, headers=HEADERS, timeout=10)
    resp.raise_for_status()
    return resp.json()[:limit]


def story_info(story_id):
    """Retrieve the details object for a given HN story id."""
    resp = requests.get(f'{INFO_URL}{story_id}.json')
    resp.raise_for_status()
    return resp.json()


def top_stories():
    """Get details objects for the top Hacker News stories."""
    ids = top_story_ids()
    results = []
    with ThreadPoolExecutor(max_workers=10) as executor:
        future_to_id = {executor.submit(story_info, id_): id_ for id_ in ids}
        for future in as_completed(future_to_id):
            try:
                data = future.result()
                results.append(data)
            except Exception as e:
                print(f'Failed to fetch {future_to_id[future]}: {e}')
    return results


def main():
    stories = top_stories()
    for story in stories:
        print(f'{story['title']} ({story['url']})')


if __name__ == '__main__':
    main()

