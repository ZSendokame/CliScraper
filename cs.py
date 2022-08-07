import requests
import arguing
from bs4 import BeautifulSoup


def main():
    url = arguing.set('--url', mandatory=True, help_message='URL to scrape.')
    tag = arguing.set('--tag', help_message='Tags to filter.')
    selector = arguing.set('--selector', help_message='Selector to use.')
    attributes = arguing.set('--attributes', help_message='HTML Node attributes.')
    output = arguing.set('--output', help_message='Output type (BS4).',
                        default='attrs')

    # Error
    response = requests.get(url)

    if arguing.check('-h'):
        exit(arguing.documentation())

    # Main
    tags = tag.split(',')
    attribute_dict = {}
    soup = BeautifulSoup(response.text, 'lxml')
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


    if arguing.check('--tag'):
        nodes = soup.find_all(tags, attrs=attribute_dict)

    elif arguing.check('--selector'):
        nodes = soup.select(selector)

    for node in nodes:
        print(getattr(node, output))


if __name__ == '__main__':
    main()
