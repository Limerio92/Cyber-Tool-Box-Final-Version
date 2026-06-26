# Cyber Tool Box v6.0 - fsociety Edition

### Projet Fin d'Annee MSI-1 - Cybersecurite

**Equipe :** Abdelkarim Moufid, Nadjim, Selma
**Date :** Juin 2026
**Statut :** Fonctionnel (16/16 options validees)
**Theme :** Mr Robot / fsociety

---

## Objectif

Developpement d'une boite a outils interactive et automatisee concue pour simplifier et automatiser les processus de tests d'intrusion (Pentests). Cette toolbox integre des fonctionnalites de reconnaissance reseau, detection de vulnerabilites, analyse de securite, exploitation, post-exploitation et generation automatique de rapports PDF.

---

## Structure du Projet

```
cyber-tool-box-v6 - 2026/
├── cyber-tool-box.py              # Fichier principal
├── affichage_menu.py              # Interface menu (theme Mr Robot)
├── preflight_check.py             # Verification des pre-requis
├── requirements.txt               # Dependances Python
├── install.bat                    # Installation automatique
├── Read_Me.md                     # Documentation
│
├── modules/
│   ├── scan_ip_os.py              # Scan reseau et OS (Scapy + Nmap)
│   ├── portscan.py                # Scan de ports (Nmap)
│   ├── searchsploit.py            # Recherche d'exploits (Google)
│   ├── scan_vulnerable_proto.py   # Analyse de protocoles
│   ├── scan_vulnerable_os.py      # Analyse d'OS
│   ├── eval_password.py           # Evaluation de mots de passe
│   ├── Connection.py              # Connexions SSH/HTTP (Paramiko)
│   ├── keys_certif.py             # Scan de cles SSH et certificats
│   ├── extract_ad.py              # Extraction Active Directory
│   ├── gen_pdf.py                 # Generation de rapports PDF
│   ├── words_keys.csv             # Liste de mots de passe (test)
│   ├── logins_authen.csv          # Identifiants d'authentification (test)
│   └── logins                     # Base de mots de passe courants
│
└── reports/                       # Rapports PDF generes automatiquement
```

---

## Installation des Pre-requis

### 1. Python 3.12+

Telecharger Python depuis : https://www.python.org/downloads/
Important : Cocher la case "Add Python to PATH" lors de l'installation.

Verifier l'installation :

```
python --version
```

### 2. Nmap (obligatoire)

Telecharger Nmap depuis : https://nmap.org/download.html

Verifier l'installation :

```
nmap --version
```

### 3. Docker (pour les tests Option 5)

Telecharger Docker Desktop : https://www.docker.com/products/docker-desktop/

Lancer le container de test SSH :

```
docker run -d -p 22:22 --name ssh-test rastasheep/ubuntu-sshd
```

### 4. Bibliotheques Python

Option A - Installation automatique (recommandee) :

```
Double-cliquer sur install.bat
```

Option B - Installation manuelle :

```
pip install -r requirements.txt
```

Ou directement :

```
pip install colorama googlesearch-python python-nmap requests paramiko scapy fpdf2
```

---

## Utilisation de la Toolbox

### Demarrage

1. Ouvrir un terminal (PowerShell ou CMD)
2. Naviguer vers le dossier du projet :

```
cd "chemin/vers/cyber-tool-box-v6 - 2026"
```

3. Lancer la toolbox :

```
python cyber-tool-box.py
```

### Navigation

Le menu principal s'affiche automatiquement avec le theme Mr Robot (fsociety). Selectionner une option en entrant le numero correspondant. Les sous-menus permettent de choisir des fonctionnalites specifiques. Taper "z" pour revenir au menu precedent et "99" pour quitter.

---

## Fonctionnalites Disponibles (16 options)

### Option 1 : Scanning (Reconnaissance)

- 1A - Network / OS Scan : Scan ARP (Scapy) + detection d'OS (Nmap) + resolution hostname
- 1B - Port Scan (21-443) : Scan de ports standard avec detection de versions (Nmap -sV)
- 1C - Custom Port Scan : Scan personnalise sur une plage de ports configurable

### Option 2 : Detection Vulnerabilities

- 2A - Search Exploits on Service : Recherche d'exploits publics via Google Search
- 2B - Search Vulnerabilities on Protocol : Analyse de protocoles vulnérables (comparaison versions securisees/insecurisees)
- 2C - Search Vulnerabilities on OS : Detection de systemes d'exploitation obsoletes

### Option 3 : Security Analysis (Mots de Passe)

- 3A - Test Password : Evalue la force d'un mot de passe individuel (longueur + complexite + base commune)
- 3B - CSV Password List : Analyse batch d'une liste de mots de passe depuis un fichier CSV
- 3C - Add Line to CSV : Ajoute un nouveau couple username/password a la liste

### Option 4 : Authentication Analysis

- 4A - Simple SSH Auth : Teste une connexion SSH unique via Paramiko
- 4B - Multi SSH Auth : Teste plusieurs identifiants SSH depuis un CSV (brute-force simulation)
- 4C - Simple HTTP Auth : Teste une authentification HTTP Basic
- 4D - Multi HTTP Auth : Teste plusieurs identifiants HTTP depuis un CSV
- 4E - Add Credentials : Ajoute des identifiants a la liste de test

### Option 5 : Exploitation

- 5A - Retrieve SSH Keys : Extrait les cles SSH d'une machine cible (Linux/Windows/macOS)
- 5B - Retrieve Certificates : Extrait les certificats SSL/TLS d'une machine cible

### Option 6 : Post Exploitation

- 6A - Active Directory Extraction : Detecte un service AD et extrait l'arborescence du domaine (utilisateurs, groupes, machines)

### Option 7 : Report Creation

- 7 - Generate PDF Report : Genere un rapport PDF de securite complet avec OS, ports, services et vulnerabilites. Le rapport est sauvegarde dans le dossier reports/.

---

## Tests Verifies

| Fonctionnalite               | Cible                      | Resultat               | Statut |
| ---------------------------- | -------------------------- | ---------------------- | ------ |
| Option 1a - Network Scan     | 192.168.56.0/24            | Devices detectes       | OK     |
| Option 1b - Port Scan        | 192.168.56.101             | 9 ports ouverts        | OK     |
| Option 1c - Custom Scan      | 192.168.56.101 (20-100)    | 6 ports ouverts        | OK     |
| Option 2a - Search Exploits  | apache 2.2                 | Exploits trouves       | OK     |
| Option 2b - Protocol Vulns   | 192.168.56.101             | Protocoles insecurises | OK     |
| Option 2c - OS Vulns         | 192.168.56.101             | OS detecte             | OK     |
| Option 3a - Test Password    | test123                    | Weak                   | OK     |
| Option 3b - CSV List         | words_keys.csv             | 10 passwords evalues   | OK     |
| Option 3c - Add Password     | demouser/DemoPass          | Password ajoute        | OK     |
| Option 4a - SSH Single       | 127.0.0.1 (Docker)         | Connection successful  | OK     |
| Option 4b - SSH Brute Force  | 127.0.0.1 (Docker)         | root/root trouve       | OK     |
| Option 4c - HTTP Single      | 192.168.56.101             | Connection successful  | OK     |
| Option 4d - HTTP Brute Force | 192.168.56.101             | admin/admin trouve     | OK     |
| Option 4e - Add Credentials  | testuser/TestPass          | Credentials ajoutees   | OK     |
| Option 5a - SSH Keys         | 127.0.0.1 (Docker)         | Keys extraites         | OK     |
| Option 5b - Certificates     | 127.0.0.1 (Docker)         | 55 certificats         | OK     |
| Option 6a - Active Directory | 192.168.56.102 (WinServer) | AD tree extrait        | OK     |
| Option 7 - Report PDF        | 192.168.56.101             | PDF 2 pages genere     | OK     |

---

## Environnement de Test

| Machine                               | IP             | Utilisation             |
| ------------------------------------- | -------------- | ----------------------- |
| Docker SSH (rastasheep/ubuntu-sshd)   | 127.0.0.1      | Options 4a, 4b, 5a, 5b  |
| Metasploitable (VirtualBox)           | 192.168.56.101 | Options 1, 2, 4c, 4d, 7 |
| Windows Server 2022 + AD (VirtualBox) | 192.168.56.102 | Option 6                |

### Identifiants de Test

Docker SSH : root / root
Metasploitable HTTP : admin / admin
WinServer-AD : Administrateur / P@ssw0rd123 (domain: test.local)

---

## Corrections Appliquees (v6.0)

### Bugs Critiques Fixes

1. Chemins de fichiers Windows : remplaces par os.path.join() (compatibilite cross-platform)
2. Option 3c (Add Password) : corrigee pour demander username ET password
3. Gestion d'erreurs : ajout try/except sur toutes les options principales
4. Fichier logins manquant : cree et documente
5. gen_pdf.py : correction encodage PDF (caracteres speciaux)
6. gen_pdf.py : rapports generes dans le dossier reports/ du projet
7. keys_certif.py : correction chemins CSV + commande certificats Linux
8. scan_ip_os.py : ajout resolution hostname dans le scan reseau
9. Connection.py : compatibilite SSH avec anciennes cles (disabled_algorithms)

### Ameliorations

- Interface Mr Robot / fsociety (theme vert sur noir)
- Tous les fichiers CSV ont la bonne structure (login, password)
- Gestion robuste des fichiers manquants
- Messages d'erreur clairs
- Resolution automatique du hostname lors du scan reseau
- Rapports PDF generes dans un dossier dedie (reports/)
- Support Docker pour les tests SSH

---

## Architecture Technique

### Stack Technologique

| Composant  | Technologie         | Utilisation              |
| ---------- | ------------------- | ------------------------ |
| Langage    | Python 3.12         | Code principal           |
| Scanning   | Nmap 7.99           | Scan ports, OS detection |
| Reseau     | Scapy               | ARP scanning             |
| SSH        | Paramiko            | Connexions SSH           |
| HTTP       | Requests            | Authentification HTTP    |
| PDF        | FPDF2               | Generation rapports      |
| Interface  | Colorama            | Menu CLI colore          |
| Exploits   | googlesearch-python | Recherche CVEs           |
| Versioning | Git + GitHub        | Collaboration            |

### Design Pattern

Architecture modulaire : chaque fonctionnalite est un module independant dans le dossier modules/. Cela permet d'ajouter de nouvelles fonctionnalites sans modifier le code existant.

### Interface

Theme Mr Robot (fsociety) : interface CLI avec fond noir et texte vert, inspiree de la serie Mr Robot. Bordures ASCII, noms de menus style hacker, citations de la serie.

---

## Troubleshooting

### Erreur : "CSV file not found"

Verifier qu'on est dans le bon dossier :

```
cd "chemin/vers/cyber-tool-box-v6 - 2026"
```

### Erreur : "nmap not found"

Installer Nmap depuis https://nmap.org/download.html et redemarrer le terminal.

### Erreur : "ModuleNotFoundError"

```
pip install -r requirements.txt
```

### Docker : container ssh-test n'existe plus

```
docker run -d -p 22:22 --name ssh-test rastasheep/ubuntu-sshd
```

### Docker : port 22 already in use

```
docker stop ssh-test
docker rm ssh-test
docker run -d -p 22:22 --name ssh-test rastasheep/ubuntu-sshd
```

### Le scan reseau ne trouve rien

Normal en environnement VM isole. Le scan ARP fonctionne mieux avec plusieurs machines sur le meme reseau (Metasploitable + WinServer-AD).

### Option 7 cree un PDF vide

Normal si le reseau scanne n'a pas d'appareils actifs. Utiliser l'IP directe (ex: 192.168.56.101) au lieu d'un range.

### WinServer-AD : connexion refusee

Verifier que SSH tourne dans la VM. Dans PowerShell de la VM :

```
Get-Service sshd
Start-Service sshd
```

---

## Exemples d'Utilisation

### Scan de ports

```
Menu principal → 1 → B
Target: 192.168.56.101
Resultat: 9 ports ouverts avec services et versions
```

### Test d'un mot de passe

```
Menu principal → 3 → A
Password: test123
Resultat: Weak
```

### Extraction SSH Keys

```
Menu principal → 5 → A
IP: 127.0.0.1 | Login: root | Password: root
Resultat: SSH keys saved in modules/ssh_keys_linux.csv
```

### Extraction Active Directory

```
Menu principal → 6 → A
IP: 192.168.56.102 | Login: Administrateur | Password: P@ssw0rd123
Domain: test.local
Resultat: AD tree exported to ad_tree.csv
```

### Generation de rapport

```
Menu principal → 7
IP: 192.168.56.101
Resultat: reports/Report_Security_Network_2026-06-22.pdf
```

---

## Dependances Principales

```
colorama              → Coloration du terminal (theme Mr Robot)
python-nmap           → Scan de ports et detection d'OS
paramiko              → Connexions SSH
requests              → Requetes HTTP
scapy                 → Manipulation de paquets reseau (ARP)
fpdf2                 → Generation de rapports PDF
googlesearch-python   → Recherche d'exploits publics
```

---

## Perspectives d'Evolution

Court terme : interface web Flask, base de donnees SQLite, multi-threading, export JSON/CSV.
Moyen terme : integration Metasploit, module forensique, SIEM integration, API REST.
Long terme : dashboard temps reel, machine learning, version SaaS, compliance reports.

---

## License & Credits

Projet academique MSI-1 Cybersecurite - Sup de Vinci / ESIEE IT
GitHub : https://github.com/Limerio92/Cyber-Tool-Box-Final-Version

Derniere mise a jour : Juin 2026
