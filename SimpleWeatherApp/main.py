import requests

if __name__ == '__main__':
    r = requests.get('https://api.github.com/events')
    print(r.json()[0]) # first element of the json list 
    r = requests.post('https://httpbin.org/post', data={'python': 'requests'})
    print(r.text)
    r = requests.put('https://httpbin.org/put', data={'python': 'requests'})
    print(r.text)
    r = requests.delete('https://httpbin.org/delete')
    print(r.text)
    r = requests.head('https://httpbin.org/get')
    print(r.text)
    r = requests.options('https://httpbin.org/get')
    print(r.text)
