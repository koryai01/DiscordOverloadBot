import phonenumbers
import requests

phone_number = input("Entrez un numéro de téléphone : ")

# Vérifiez si le numéro de téléphone est valide
try:
    parsed_number = phonenumbers.parse(phone_number)
    if not phonenumbers.is_valid_number(parsed_number):
        raise ValueError("Le numéro de téléphone n'est pas valide.")
except phonenumbers.phonenumberutil.NumberParseException:
    raise ValueError("Le numéro de téléphone n'est pas valide.")

# Recherchez le numéro de téléphone sur différents sites Web
url = f"https://www.truecaller.com/search/in/{phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)}"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    print(f"Résultats pour le numéro de téléphone {phone_number}:")
    print(response.text)
else:
    print(f"Erreur lors de la recherche du numéro de téléphone {phone_number} sur le site Truecaller.")
