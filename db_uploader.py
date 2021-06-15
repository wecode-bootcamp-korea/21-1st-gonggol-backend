import os, django, csv, sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gonggol.settings")

django.setup()

from products.models import MainCategory, SubCategory, Product

CSV_PATH_PRODUCTS = './gonggol_db.csv'

with open(CSV_PATH_PRODUCTS) as in_file:
    data_reader = csv.reader(in_file)

    for fow in data_reader:
        print(fow)