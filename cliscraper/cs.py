import arguing
import requests
from bs4 import BeautifulSoup


def main():
    url = arguing.set('--url', mandatory=True, help_message='URL to scrape.')
    tag = arguing.set('--tag', help_message='Tags to filter.')
    selector = arguing.set('--selector', help_message='Selector to use.')
    filter = arguing.set('--filter', help_message='Filter to use.')

    response = requests.get(url)
    tags = tag.split(',')
    soup = BeautifulSoup(response.text, 'lxml')

    if arguing.check('--tag'):
        nodes = soup.find_all(tags)

    elif arguing.check('--selector'):
        nodes = soup.select(selector)

    else:
        exit('- No selector nor tag used.')

    for node in nodes:
        if arguing.check('--filter'):
            print(eval(filter, {'node': node}))

        else:
            print(node)


if __name__ == '__main__':
    main()
