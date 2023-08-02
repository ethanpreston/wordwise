import requests


def get_synonyms(word, all_flag):
    api_url = 'https://api.api-ninjas.com/v1/thesaurus?word={}'.format(word)
    response = requests.get(api_url, headers={'X-Api-Key': 'RzWgMmKU0LbGr4zxkgoF2Q==mgZOsW8E0lUyB6l3'})
    if response.status_code == requests.codes.ok:
        if len(response.json()['synonyms']) == 1:
            print(f"Synonym for {word}: {response.json()['synonyms'][0]}")
        elif len(response.json()['synonyms']) == 0:
            print(f"No synonyms found for {word}")
        elif len(response.json()['synonyms']) > 10 and not all_flag:
            print(f"Synonyms for {word}:")
            for synonym in response.json()['synonyms'][:10]:
                print(f"\t {synonym}")
        else:
            print(f"Synonyms for {word}:")
            for synonym in response.json()['synonyms']:
                print(f"\t {synonym}")
    else:
        print("Error:", response.status_code, response.text)
