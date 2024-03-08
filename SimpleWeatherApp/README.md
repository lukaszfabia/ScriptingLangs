# Prezentacja modulów Flask i Requests

**Flask** to mini *framework* służący do tworzenia aplikacji webowych od strony serwera. 

Raczej do nauki backendu, albo do malutkich projektów.

Przykład użycia w kodzie mini aplikacja pogodowa.

**Requests** to modul umożliwiający wykonywanie żądań *http*. 

Gdzie mogę użyć:
- web scraping, requests i BeautifulSoup idą ze sobą w parze bo wykonujemy żądanie GET i dostajemy stronę, z której będziemy pobierać dane przy użyciu tego drugiego

- pobieranie API

Przykłady w kodzie, z dokumentacji modulu **requests**

```python
import requests
r = requests.get('https://api.github.com/events')
r = requests.post('https://httpbin.org/post', data={'key': 'value'})
r = requests.put('https://httpbin.org/put', data={'key': 'value'})
r = requests.delete('https://httpbin.org/delete')
r = requests.head('https://httpbin.org/get')
r = requests.options('https://httpbin.org/get')

```



