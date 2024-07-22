import requests
import pandas as pd
import ipaddress
import os
import argparse
from tqdm import tqdm  # Importer tqdm pour la barre de progression

def print_ascii_art():
    """ Affiche l'ASCII art en couleur. """
    ascii_art = """
\033[91m

._____________    _________                            
|   \______   \  /   _____/ ____  ___________   ____   
|   ||     ___/  \_____  \_/ ___\/  _ \_  __ \_/ __ \  
|   ||    |      /        \  \__(  <_> )  | \/\  ___/  
|___||____|     /_______  /\___  >____/|__|    \_____ 
                              
\033[0m
\033[94m
=============================================
            IP SCORE SCRIPT
             Author: amaz974
    Version: 1.0 - Date: 2024-07-19
=============================================

\033[0m
"""
    print(ascii_art)

def read_ip_list(file_path):
    """ Lire les adresses IP depuis un fichier. """
    try:
        with open(file_path, 'r') as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"Erreur : Le fichier {file_path} est introuvable.")
        return []
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier : {e}")
        return []

def fetch_ip_info(ip, api_key):
    """ Rechercher les informations IP via l'API AbuseIPDB. """
    url = 'https://api.abuseipdb.com/api/v2/check'
    querystring = {'ipAddress': ip, 'maxAgeInDays': '90'}
    headers = {'Accept': 'application/json', 'Key': api_key}

    try:
        response = requests.get(url, headers=headers, params=querystring)
        response.raise_for_status()
        data = response.json()
        return {
            'IP Address': ip,
            'Pays': data['data'].get('countryCode', 'N/A'),
            'Hostname': data['data']['hostnames'][0] if data['data'].get('hostnames') else 'N/A',
            'Domaine': data['data'].get('domain', 'N/A'),
            'Usage Type': data['data'].get('usageType', 'N/A'),
            'Score de malveillance': data['data'].get('abuseConfidenceScore', 'N/A')
        }
    except requests.RequestException as e:
        print(f"Erreur lors de la requête pour l'IP {ip} : {e}")
        return None

def save_to_excel(df):
    """ Sauvegarde le DataFrame au format Excel. """
    excel_dir = os.path.join(os.path.dirname(__file__), 'excel')
    os.makedirs(excel_dir, exist_ok=True)
    file_name = input("Entrez le nom du fichier de sortie (sans extension): ").strip()
    file_path = os.path.join(excel_dir, f"{file_name}.xlsx")
    df.to_excel(file_path, index=False)
    print(f"Fichier Excel généré : {file_path}")

def save_to_csv(df):
    """ Sauvegarde le DataFrame au format CSV. """
    file_name = input("Entrez le nom du fichier de sortie (sans extension): ").strip()
    file_path = f"{file_name}.csv"
    df.to_csv(file_path, index=False)
    print(f"Fichier CSV généré : {file_path}")

def main():
    parser = argparse.ArgumentParser(description="Script pour obtenir les scores de malveillance des adresses IP via AbuseIPDB.")
    parser.add_argument('-i', '--input', type=str, default='list.txt', help="Chemin vers le fichier contenant les adresses IP (par défaut: 'list.txt').")
    parser.add_argument('-e', '--excel', action='store_true', help="Sauvegarder le résultat au format Excel.")
    parser.add_argument('-t', '--terminal', action='store_true', help="Afficher le résultat dans le terminal.")
    parser.add_argument('-c', '--csv', action='store_true', help="Sauvegarder le résultat au format CSV.")
    args = parser.parse_args()

    # Clé API par défaut
    api_key = 'f7cfa0682722afb355dc0e37c07cf75508bfcd10834affab42772af971968dd914dd05dedffd92eb'

    print_ascii_art()

    list_file_path = args.input

    ip_list = read_ip_list(list_file_path)
    if not ip_list:
        return

    public_ip_list = [ip for ip in ip_list if not ipaddress.ip_address(ip).is_private]

    # Créer une barre de progression avec tqdm
    results = []
    print("Traitement des adresses IP...")
    for ip in tqdm(public_ip_list, desc="Chargement des IPs", unit="IP"):
        result = fetch_ip_info(ip, api_key)
        if result:
            results.append(result)

    df = pd.DataFrame(results)

    if args.excel:
        save_to_excel(df)
    elif args.csv:
        save_to_csv(df)
    elif args.terminal:
        print(df.to_string(index=False))
    else:
        output_format = input("Voulez-vous le fichier en format Excel, CSV, ou afficher dans le terminal? (tapez 'excel', 'csv', ou 'terminal'): ").strip().lower()
        if output_format == 'excel':
            save_to_excel(df)
        elif output_format == 'csv':
            save_to_csv(df)
        elif output_format == 'terminal':
            print(df.to_string(index=False))
        else:
            print("Format non reconnu. Veuillez choisir entre 'excel', 'csv', ou 'terminal'.")

if __name__ == "__main__":
    main()