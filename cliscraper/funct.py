import requests
from bs4 import BeautifulSoup


def process_attributes(attributes):
    attributes = attributes.split(';')
    attribute_dict = {}

    for attribute in attributes:
        key = attribute.split('=')

        if len(key) > 1:
            if key[1] in ['True', 'true']:
                key[1] = True

            elif key[1] in ['False', 'false']:
                key[1] = False

            attribute_dict[key[0]] = key[1]

    return attribute_dict


def fetch(url, **kwargs):
    response = requests.get(url, **kwargs).text
    soup = BeautifulSoup(response, 'lxml')

    return soup
