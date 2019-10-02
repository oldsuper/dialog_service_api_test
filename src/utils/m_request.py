import requests


def send_request(method, body, api_url):
    '''

    :param method:
    :param body:
    :param api_url:
    :return:
    '''
    response = requests.request(method, url=api_url, params=body)
    return response
