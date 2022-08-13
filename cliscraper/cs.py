import arguing
import requests
from bs4 import BeautifulSoup

import cliscraper.funct as funct


def main():
    url = arguing.set('--url', mandatory=True, help_message='URL to scrape.')
    tag = arguing.set('--tag', help_message='Tags to filter.')
    selector = arguing.set('--selector', help_message='Selector to use.')
    attributes = arguing.set('--attributes',
                             help_message='HTML Node attributes.')
    output = arguing.set('--output', help_message='Output type (BS4).',
                         default='attrs')

    # Error
    response = requests.get(url)
    if arguing.check('-h'):
        exit(arguing.documentation())

    # Main
    tags = tag.split(',')
    attribute_dict = funct.process_attributes(attributes)
    soup = BeautifulSoup(response.text, 'lxml')

    if arguing.check('--tag'):
        nodes = soup.find_all(tags, attrs=attribute_dict)

    elif arguing.check('--selector'):
        nodes = soup.select(selector)

    else:
        exit('- No selector nor tag used.')

    for node in nodes:
        print(getattr(node, output))


if __name__ == '__main__':
    main()
