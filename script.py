import torch
import urllib.request
from bs4 import BeautifulSoup

def getHtml(url)
    # Fetch the html file
    response = urllib.request.urlopen('file:///D:/GrAIphon/sito/main.html')
    html_doc = response.read()

    # Parse the html file
    soup = BeautifulSoup(html_doc, 'html.parser')

    # Format the parsed html file
    strhtm = soup.prettify()

    # Print the first few characters
    print (strhtm[:225])    


def html_grid_to_tensor(html):
    # Analizza la griglia HTML utilizzando BeautifulSoup
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

    return tensor