#!/usr/bin/env python3

import requests
import csv


def fetch_and_print_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        datos = response.json()

        for dato in datos:
            print(dato["titulo"])

def fetch_and_save_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        datos = response.json()

        data = []

        for dato in datos:
            data.append = ({"id": dato["id"], "title": dato["title"], "body": dato["body"]})

        with open("posts.csv", 'w') as file:
            escribir = csv.DictWriter(file, fieldnames=["id", "title", "body"])
            escribir.writeheader()
            escribir.writerows(datos)

if __name__ == "__main__":
    fetch_and_print_posts()
    fetch_and_save_posts()