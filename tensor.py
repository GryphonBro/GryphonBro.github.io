import libs.torch
import libs.urllib
from libs.bs4 import BeautifulSoup

def gridToTensor():
    with urllib.request.urlopen('https://gryphonbro.github.io/') as response:
        html = response.read()

    soup = BeautifulSoup(html, 'html.parser')

    # Trova tutti gli elementi div con classe "grid-item"
    grid_items = soup.find_all('div', class_='grid-item')

    # Inizializza una lista per contenere i dati
    data = []

    # Scansiona tutti gli elementi grid-item
    for grid_item in grid_items:
        # Trova il bottone e l'immagine all'interno di ciascun grid-item
        button = grid_item.find('button')
        img = grid_item.find('img')

        # Estrai i dati dal bottone e dall'immagine
        button_text = button.get_text()
        img_title = img['title']

        # Assegna un valore in base al titolo
        if img_title == 'empty':
            value = 0
        elif img_title == 'blue':
            value = 1
        elif img_title == 'red':
            value = 2
        else:
            # Assegnare un valore predefinito nel caso in cui il titolo non sia riconosciuto
            value = -1

        # Aggiungi il valore alla lista
        data.append(value)

    # Converte la lista dei dati in un tensore PyTorch
    tensor = torch.tensor(data).view(1, 13, 13)

    tensor
