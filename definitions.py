import requests
from bs4 import BeautifulSoup
import re
from collections import defaultdict


def get_html_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.content
    else:
        raise Exception(f"Failed to fetch the HTML content. Status code: {response.status_code}")


def extract_dictionary_definitions(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    definitions = defaultdict(list)
    for entry in soup.find_all("p"):
        text = entry.get_text().strip()
        if len(re.split(r"\(.*\)", text)) > 1:
            word, definition = re.split(r"\(.*\)", text)
            definitions[word.strip()].append(definition.strip())
    return definitions


def get_definition(word, dictionary):
    return dictionary.get(word, f"Definition not found for '{word}'.")


def print_definitions(word, definitions):
    if len(definitions) == 1:
        print(f"Definition of '{word}': {definitions[0]}")
    elif len(definitions) >= 1:
        print(f"Definitions of '{word}':")
        for i in range(len(definitions)):
            print("\t", definitions[i])
    else:
        print(f"No definition found for {word}. Please check your spelling and try again")


def define_word(word):
    url = f"https://www.mso.anu.edu.au/~ralph/OPTED/v003/wb1913_{word[0].lower()}.html"
    try:
        word = word[0].upper() + word[1:].lower()
        html_content = get_html_content(url)
        dictionary = extract_dictionary_definitions(html_content)
        definition = get_definition(word, dictionary)
        print_definitions(word, definition)
    except Exception as e:
        print(f"Error: {e}")
