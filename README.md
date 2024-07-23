# IP Score 🥇

## 🎉 Description

Bienvenue dans IP Score ! Ce script Python vous permet de vérifier les scores de malveillance des adresses IP en utilisant l'API AbuseIPDB. Que vous soyez un développeur, un administrateur réseau, ou simplement curieux, ce script vous offre une manière rapide et simple de surveiller les adresses IP.

Il vous suffit d'ajouter les IPs au fichiers list.txt ou d'importer votre fichier avec l'option -i.

```java
Conseil : Utiliser VScode et son terminal pour manipuler le projet
```
## 🌟 Fonctionnalités 

- **Lecture des adresses IP** depuis un fichier (par defaut list.txt).
- **Filtrage des adresses IP privées** pour se concentrer uniquement sur les adresses IP publiques.
- **Affichage des résultats** dans le terminal ou sauvegarde dans un fichier Excel ou CSV (Le résultat se trouvera dans le dossier : "Excel").
- **Option de filtrage** pour afficher uniquement les adresses IP ayant un score de malveillance supérieur ou égal à une valeur spécifiée.

## 🚀 Installation

**Clonez le dépôt ou téléchargez le script :**

   ```bash
   git clone https://github.com/amaz974/IP-Score.git
   ```
Ou téléchargez simplement le fichier ipscore.py.

Installez les dépendances requises :
```bash
python -m venv venv
source venv/bin/activate  # Sur Windows utilisez `venv\Scripts\activate`
pip install -r requirements.txt
```
## 📜 Utilisation
Exécutez le script avec Python et choisissez vos options préférées :

```bash
python ipscore.py [OPTIONS]
Options
-h, --help : Afficher une aide avec les options disponibles.
-i, --input : Chemin vers le fichier contenant les adresses IP (par défaut : list.txt).
-e, --excel : Sauvegarder les résultats au format Excel.
-t, --terminal : Afficher les résultats dans le terminal.
-c, --csv : Sauvegarder les résultats au format CSV.
-s, --score : Afficher uniquement les IPs ayant un score de malveillance supérieur ou égal à cette valeur.
```
## 🛠️ Exemples
Pour exécuter le script avec un fichier d'entrée personnalisé et sauvegarder les résultats en CSV :

```
python ipscore.py -i mon_fichier_ips.txt -c
```
Pour afficher les résultats directement dans le terminal :

```
python ipscore.py -t
```
Pour obtenir de l'aide sur les options disponibles :

```
python ipscore.py -h
```
Pour filtrer les IPs avec un score de malveillance supérieur ou égal à une valeur spécifiée (par exemple 10) :

```
python ipscore.py -s 10
```

## 🔑 Clé API
Le script utilise une clé API pour accéder à l'API AbuseIPDB. La clé API est incluse dans le script à titre d'exemple. Pour une utilisation sécurisée, remplacez-la par votre propre clé API obtenue depuis AbuseIPDB. 

## ⚠️ Notes
Assurez-vous que le fichier list.txt ou le fichier spécifié existe et contient des adresses IP valides, une par ligne.
Utilisez votre propre clé API pour éviter les restrictions.

## 👤 Auteur
Auteur : amaz974

Version : 1.0 - Date : 2024-07-19

## 📜 Licence
Ce script est fourni sous la licence MIT. Utilisez, modifiez et redistribuez le code comme bon vous semble, en incluant un avis de licence approprié.

Merci d'utiliser le script IP Score ! Si vous avez des questions ou des suggestions, n'hésitez pas à me contacter. 😊







