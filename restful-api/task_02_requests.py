#!/usr/bin/python3
"""Consuming and processing data from an API using Python"""
import requests
import csv

response = requests.get('https://jsonplaceholder.typicode.com/posts')
status_code = response.status_code
posts = response.json()


def fetch_and_print_posts():
    """Function that fetches all post from JSONPlaceHolder"""
    print("Status Code: {}".format(status_code))
    if status_code == 200:
        for post in posts:
            print(post["title"])


def fetch_and_save_posts():
    """Function that fetches all post from JSONPlaceholder"""
    if status_code == 200:
        with open("posts.csv", "w", encoding='utf-8', newline='') as csvFile:
            fieldnames = ["id", "title", "body"]
            csvWriter = csv.DictWriter(csvFile, fieldnames=fieldnames)
            csvWriter.writeheader()
            for post in posts:
                csvWriter.writerows([{key: post[key] for key in fieldnames}])
