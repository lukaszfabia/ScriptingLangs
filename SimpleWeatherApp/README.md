# Prezentacja modulów Requests i Flask

## [Requests](https://requests.readthedocs.io/en/latest/)

**Requests** to modul umożliwiający wykonywanie żądań *http*. 

Gdzie mogę użyć:
- web scraping, requests i BeautifulSoup idą ze sobą w parze bo wykonujemy żądanie GET i dostajemy stronę, z której będziemy wybierać insteresujące nas dane przy użyciu tego drugiego

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

## [Flask](https://flask.palletsprojects.com/en/3.0.x/)

**Flask** to mini *framework* służący do tworzenia aplikacji webowych od strony serwera, raczej do nauki backendu, albo do malutkich projektów.

Przykład użycia w kodzie z [dokumentacji](https://flask.palletsprojects.com/en/3.0.x/quickstart/#sessions) **flaska**.

``` python
from flask import session

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
    if 'username' in session:
        return f'Logged in as {session["username"]}'
    return 'You are not logged in'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))
```

W kodzie powyżej chodzi najogólnej o to, że pamiętamy logowanie usera w aplikacji webowej, **przydatne przy aplikacjach związanych z tworzeniem konta na stronie**.

Ostatni przykład do **flaska** jest jako aplikacja do pogody.




