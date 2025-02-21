#!/usr/bin/env python3

import requests
import csv


def fetch_and_print_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    print(f"Estados de Codigo: {response.status_code}")

    if response.status_code == 200:
        dato = response.json()

        for post in dato:
            print(post["titulo"])
    else:
        print("Error al obtener los datos")

def fetch_and_save_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        dato = response.json()
        posts = [{"id": post["id"], "title": post["title"], "body": post["body"]} for post in dato]

        with open("posts.csv", 'w') as file:
            escribir = csv.DictWriter(file, fieldnames=["id", "title", "body"])
            escribir.writeheader()
            escribir.writerows(posts)
        
        print("Datos guardados en posts.csv")
    else:
        print("Error al obtener los datos")
