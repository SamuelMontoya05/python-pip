import requests

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    print(r.status_code) # codigo de como funciona toda la pagina
    print(r.text) #imprime como str lo que devuelve el link
    print(type(r.text)) #str
    categories = r.json() # transforma en una lista
    print(type(categories)) # list
    for category in categories:
        print(category['name'])
    