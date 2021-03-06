# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class SalePropertyItem(Item):
    id = Field()
    price = Field()
    number_of_beds = Field()
    number_of_baths = Field()
    area = Field()
    price_unit = Field()
    project_type = Field()
    project_id = Field()
    project_name = Field()
    district_id = Field()
    sub_district_id = Field()
    top = Field()
    tenure = Field()
    address = Field()
    postal_code = Field()
    #description = Field()
    #indoor_features = Field()
    #outdoor_features = Field()
    #special_features = Field()
    scraped_date = Field()
    last_updated_date = Field()
    latitude = Field()
    longitude = Field()
    mrts = Field()
    agent = Field()
    url = Field()