import os
import django
import csv
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gonggol.settings")

django.setup()

from products.models import MainCategory, SubCategory, Product, Image, Size, Stock, Tag, ProductTag, Like
CSV_PATH_PRODUCTS = './products.csv'
with open(CSV_PATH_PRODUCTS) as in_file:
    data_reader = csv.reader(in_file)
    for row in data_reader:
        print(row)