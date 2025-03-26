import requests
import xml.etree.ElementTree as ET
import time  

rss_url = ""
webhook_url = ""

# Pour mémoriser les alertes déjà envoyées
sent_alerts = set()

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
}

while True:
    try:
        response = requests.get(rss_url, headers=headers, timeout=10)
        response.raise_for_status()  # Lève une exception pour les erreurs HTTP

        # Analyse du flux RSS
        root = ET.fromstring(response.content)

        new_alerts = []
        for item in root.findall('.//item'):
            title = item.find('title').text
            link = item.find('link').text
            alert_id = link  # Utiliser le lien comme identifiant unique

            if alert_id not in sent_alerts:
                sent_alerts.add(alert_id)
                new_alerts.append({'title': title, 'link': link})

        # Envoyer les nouvelles alertes sur Discord
        for alert in new_alerts:
            message = {
                "content": f"🔔 **Nouvelle alerte :** {alert['title']}\n🔗 {alert['link']}"
            }
            response = requests.post(webhook_url, json=message)
            
            if response.status_code == 204:
                print(f"[INFO] Alerte envoyée : {alert['title']}")
            else:
                print(f"[ERREUR] Échec de l'envoi : {response.status_code} - {response.text}")

    except requests.exceptions.HTTPError as e:
        print(f"[ERREUR HTTP] {e.response.status_code} - {e.response.reason}")
    except requests.exceptions.RequestException as e:
        print(f"[ERREUR] Problème de connexion : {e}")
    except ET.ParseError:
        print("[ERREUR] Impossible d'analyser le flux RSS, le contenu peut être mal formé.")
    
    # Attendre 60 secondes avant la prochaine vérification
    time.sleep(60)
