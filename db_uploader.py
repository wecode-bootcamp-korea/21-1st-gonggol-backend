import os
import django
import csv
import sys
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gonggol.settings")
django.setup()
from products.models import MainCategory, SubCategory, Product, Image, Size, Stock, Tag, ProductTag, Like
CSV_PATH_MAINCATEGORY = './GONGGOL - maincategory.csv'
CSV_PATH_SUBCATEGORY = './GONGGOL - subcategory.csv'
CSV_PATH_PRODUCT = './GONGGOL - products.csv'
CSV_PATH_IMAGE = './GONGGOL - image.csv'
# CSV_PATH_SIZE =
# CSV_PATH_STOCK =
# CSV_PATH_TAG =
# CSV_PATH_PRODUCTTAG =
#CSV_PATH_LIKE =
MainCategory.objects.all().delete()
SubCategory.objects.all().delete()
Product.objects.all().delete()
Image.objects.all().delete()
# Size.objects.all().delete()
# Stock.objects.all().delete()
# Tag.objects.all().delete()
# ProductTag.objects.all().delete()
# Like.objects.all().delete()
with open(CSV_PATH_MAINCATEGORY, newline='') as in_file:
    data_reader = csv.DictReader(in_file)
    for row in data_reader:
        MainCategory.objects.create(**row)
with open(CSV_PATH_SUBCATEGORY, newline='') as in_file:
    data_reader = csv.DictReader(in_file)
    for row in data_reader:
        SubCategory.objects.create(**row)
with open(CSV_PATH_PRODUCT, newline='') as in_file:
    data_reader = csv.DictReader(in_file)
    for row in data_reader:
        Product.objects.create(**row)
with open(CSV_PATH_IMAGE, newline='') as in_file:
    data_reader = csv.DictReader(in_file)
    for row in data_reader:
        Image.objects.create(**row)
# with open(CSV_PATH_SIZE) as in_file:
#     data_reader = csv.reader(in_file)
#     for row in data_reader:
#         Size.objects.create(**row)
# with open(CSV_PATH_STOCK) as in_file:
#     data_reader = csv.reader(in_file)
#     for row in data_reader:
#         Stock.objects.create(**row)
# with open(CSV_PATH_TAG) as in_file:
#     data_reader = csv.reader(in_file)
#     for row in data_reader:
#         Tag.objects.create(**row)
# with open(CSV_PATH_PRODUCTTAG) as in_file:
#     data_reader = csv.reader(in_file)
#     for row in data_reader:
#         ProductTag.objects.create(**row)
# with open(CSV_PATH_LIKE) as in_file:
#     data_reader = csv.reader(in_file)
#     for row in data_reader:
#         Like.objects.create(**row)