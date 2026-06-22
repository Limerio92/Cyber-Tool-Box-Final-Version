# Cyber Tool Box v6.0

### Projet Fin d'Année MSI-1 - Cybersécurité

**Auteur :** Peligrosa (Salma Chirah)  
**Date :** Juin 2026  
**Statut :** ✅ Fonctionnel

---

## 📋 Objectif

Développement d'une boîte à outils interactive et automatisée conçue pour simplifier et automatiser les processus de tests d'intrusion, notamment les Pentests. Cette toolbox intègre des fonctionnalités de reconnaissance réseau, détection de vulnérabilités, analyse de sécurité et exploitation.

---

## 📁 Structure du Projet

```
cyber-tool-box-v6/
├── cyber-tool-box.py              # Fichier principal
├── affichage_menu.py              # Gestion des menus
├── preflight_check.py             # Vérification des pré-requis
├── requirements.txt               # Dépendances Python
├── install.bat                    # Installation automatique
├── Read_Me.md                     # Documentation
│
└── modules/
    ├── scan_ip_os.py              # Scan réseau et OS
    ├── portscan.py                # Scan de ports (Nmap)
    ├── searchsploit.py            # Recherche d'exploits
    ├── scan_vulnerable_proto.py   # Analyse de protocoles
    ├── scan_vulnerable_os.py      # Analyse d'OS
    ├── eval_password.py           # Évaluation de mots de passe
    ├── Connection.py              # Connexions SSH/HTTP
    ├── keys_certif.py             # Scan de clés et certificats
    ├── extract_ad.py              # Extraction Active Directory
    ├── gen_pdf.py                 # Génération de rapports PDF
    ├── words_keys.csv             # Liste de mots de passe (test)
    └── logins_authen.csv          # Identifiants d'authentification (test)
```

---

## 🔧 Installation des Pré-requis

### 1. Python 3.12+

- Télécharge Python depuis : https://www.python.org/ftp/python/3.12.3/python-3.12.3-amd64.exe
- **Important :** Coche la case `Add Python to PATH` lors de l'installation
- Vérifie l'installation : `python --version`

### 2. Nmap (obligatoire)

- Télécharge Nmap depuis : https://nmap.org/download.html
- Windows Installer recommandé
- Installe avec les options par défaut
- Vérifie l'installation : `nmap --version`

### 3. Bibliothèques Python

Deux options :

**Option A - Installation automatique (recommandée) :**

```
Double-clique sur install.bat
```

**Option B - Installation manuelle :**

```
pip install -r requirements.txt
```

Ou directement :

```
pip install colorama googlesearch-python python-nmap requests paramiko scapy fpdf2
```

---

## 🚀 Utilisation de la Toolbox

### Démarrage

1. Ouvre un terminal (PowerShell ou CMD)
2. Navigue vers le dossier du projet :
   ```
   cd chemin/vers/cyber-tool-box-v6
   ```
3. Lance la toolbox :
   ```
   python cyber-tool-box.py
   ```

### Navigation

- Le menu principal s'affiche automatiquement
- Sélectionne une option en entrant le numéro correspondant
- Les sous-menus permettent de choisir des fonctionnalités spécifiques
- Tape `z` pour revenir au menu précédent
- Tape `99` pour quitter

---

## 🛠️ Fonctionnalités Disponibles

### 1️⃣ Scanning (Reconnaissance)

- **Network / OS Scan** : Scan ARP et détection d'OS sur un réseau
- **Port Scan (21-433)** : Scan de ports standard avec Nmap
- **Custom Port Scan** : Scan personnalisé sur une plage de ports

### 2️⃣ Detection Vulnerabilities (Détection)

- **Search Exploits on Service** : Recherche d'exploits pour un service
- **Search Vulnerabilities on Protocol** : Analyse de protocoles vulnérables
- **Search Vulnerabilities on OS** : Détection de vulnérabilités d'OS

### 3️⃣ Security Analysis (Analyse de Sécurité)

- **Test Password** : Évalue la force d'un mot de passe individuel
- **CSV Password List** : Analyse une liste de mots de passe depuis un fichier CSV
- **Add Line to CSV** : Ajoute un nouveau mot de passe à la liste

### 4️⃣ Authentication Analysis (Authentification)

- **Simple SSH Auth** : Teste une connexion SSH unique
- **Multi-Factor SSH** : Teste plusieurs identifiants SSH (brute-force)
- **Simple HTTP Auth** : Teste une authentification HTTP
- **Multi-Factor HTTP** : Teste plusieurs identifiants HTTP
- **Add Credentials** : Ajoute des identifiants à la liste de test

### 5️⃣ Exploitation (Exploitation)

- **Retrieve SSH Keys** : Extrait les clés SSH d'une machine cible
- **Retrieve Certificates** : Extrait les certificats d'une machine cible

### 6️⃣ Post Exploitation (Post-Exploitation)

- **Active Directory Extraction** : Détecte et extrait l'arborescence Active Directory

### 7️⃣ Report Creation (Génération de Rapport)

- Génère un rapport PDF de sécurité basé sur un scan réseau

---

## 🐛 Corrections Appliquées (v6.0)

### Bugs Critiques Fixés ✅

1. **Chemins de fichiers Windows** → Remplacés par `os.path.join()` (compatibilité cross-platform)
2. **Option 3c (Add Password)** → Corrigée pour demander username ET password
3. **Gestion d'erreurs** → Ajouté try/except sur toutes les options principales
4. **Fichier logins manquant** → Créé et documenté

### Améliorations ✅

- Tous les fichiers CSV ont la bonne structure (login, password)
- Gestion robuste des fichiers manquants
- Messages d'erreur plus clairs

---

## ⚙️ Configuration

### Chemins Important

- Les fichiers CSV doivent être dans `modules/` :
  - `words_keys.csv` : Liste de mots de passe à tester
  - `logins_authen.csv` : Identifiants pour authentification

### Variables d'Environnement

Aucune configuration requise. La toolbox utilise les chemins relatifs.

---

## 🔍 Tests Vérifiés

| Fonctionnalité            | Statut | Notes                             |
| ------------------------- | ------ | --------------------------------- |
| Option 1a - Network Scan  | ✅ OK  | Fonctionne sur réseau local       |
| Option 3a - Test Password | ✅ OK  | Évalue correctement la force      |
| Option 3b - CSV List      | ✅ OK  | Lit et affiche tous les passwords |
| Option 3c - Add Password  | ✅ OK  | Ajoute username + password        |
| Option 7 - Report PDF     | ✅ OK  | Génère PDF (contenu selon scan)   |

---

## ❓ Troubleshooting

### Erreur : "CSV file not found: modules\words_keys.csv"

**Solution :**

- Vérifie que tu es dans le **bon dossier** (`cyber-tool-box-v6`)
- Commande : `cd cyber-tool-box-v6` puis `python cyber-tool-box.py`

### Erreur : "nmap not found"

**Solution :**

- Installe Nmap depuis https://nmap.org/download.html
- Redémarre le terminal après l'installation
- Vérifie : `nmap --version`

### Erreur : "ModuleNotFoundError: No module named 'paramiko'"

**Solution :**

```
pip install -r requirements.txt
```

### Le scan réseau ne trouve rien

**Normal si :**

- Tu as peu d'appareils connectés au réseau
- Tu es en environnement de développement isolé
- C'est un réseau sans autres appareils actifs

### Option 7 crée un PDF vide

**Normal si :**

- Le réseau scanné n'a pas d'appareils actifs
- Tu as scanné `127.0.0.1` (localhost)

---

## 📝 Notes Techniques

### Langues

- **Code** : Français (commentaires) + Anglais (code)
- **Interface** : Anglais (normes industrielles)
- **Documentation** : Français

### Architecture

- Modularisée avec dossier `modules/`
- Menu hiérarchique (menu principal → sous-menus)
- Gestion d'erreurs complète sur les opérations critiques

### Dépendances Principales

```
colorama         → Coloration du terminal
python-nmap      → Scan de ports
paramiko         → Connexions SSH
requests         → Requêtes HTTP
scapy            → Manipulation de paquets réseau
fpdf2            → Génération PDF
googlesearch-python → Recherche d'exploits
```

---

## 📚 Exemples d'Utilisation

### Test d'un mot de passe

```
Menu principal → 3 → a
Enter password: MyPassword123
Output: Password difficulty: Average
```

### Scan réseau

```
Menu principal → 1 → a
Enter IP: 192.168.1.0/24
Output: Appareils trouvés avec OS détecté
```

### Ajout d'identifiants

```
Menu principal → 3 → c
Enter username: admin
Enter password: SecurePass2024
Output: [+] Password added to CSV
```

---

## 📄 License & Credits

Projet académique MSI-1 Cybersécurité - Sup de Vinci

---

## 📧 Support

En cas de problème ou question, vérifies d'abord la section **Troubleshooting**.

**Dernière mise à jour :** Juin 2026
