# Dealabs-Discord-Notifier

Ce bot Discord surveille les offres de Dealabs et les partage automatiquement dans votre serveur Discord.

## Fonctionnalités

- Surveillance continue des offres de Dealabs
- Notifications automatiques sur Discord
- Pas de doublons grâce à la mémoire des offres déjà envoyées
- Mise à jour toutes les 60 secondes

## Configuration

1. Copiez le fichier [deal.py](cci:7://file:///c:/Users/maxim/Desktop/Bot%20discord/deal.py:0:0-0:0) dans votre projet
2. Éditez le fichier pour configurer :
   - `rss_url` : L'URL du flux RSS de Dealabs
   - `webhook_url` : L'URL de votre webhook Discord

## Prérequis

- Python 3.x
- Les bibliothèques suivantes :
  - requests
  - xml.etree.ElementTree

## Installation

1. Installez les dépendances :
```bash
pip install requests
