#!/usr/bin/env python3
"""Fetch posts from JSONPlaceholder and demonstrate requests + csv usage."""
import csv
import requests

BASE_URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts():
    """Fetch all posts and print the status code followed by each title."""
    response = requests.get(BASE_URL)
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post["title"])


def fetch_and_save_posts():
    """Fetch all posts and save id, title, and body to posts.csv."""
    response = requests.get(BASE_URL)

    if response.status_code == 200:
        posts = response.json()
        data = [
            {"id": post["id"], "title": post["title"], "body": post["body"]}
            for post in posts
        ]

        with open("posts.csv", "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(data)
