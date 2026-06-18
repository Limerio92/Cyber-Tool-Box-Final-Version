#!/usr/bin/env python3
"""
preflight_check.py - Verification de l'environnement avant lancement de Cyber Tool Box.

A lancer depuis le dossier RACINE du projet (a cote de cyber-tool-box.py) :
    python preflight_check.py          (Linux : sudo python3 preflight_check.py)

Ce script ne lance AUCUN scan reseau : il verifie seulement que tout est en place
(dependances, nmap, privileges, structure des fichiers, imports des modules).
"""

import importlib
import os
import shutil
import sys

GREEN = "\033[92m"; RED = "\033[91m"; YELLOW = "\033[93m"; RESET = "\033[0m"

errors = 0
warnings = 0


def ok(msg):
    print(f"{GREEN}[OK]{RESET}  {msg}")


def check(cond, ok_msg, ko_msg, fatal=True):
    """Affiche OK si cond est vraie, sinon KO (bloquant) ou ! (avertissement)."""
    global errors, warnings
    if cond:
        ok(ok_msg)
    elif fatal:
        print(f"{RED}[KO]{RESET}  {ko_msg}")
        errors += 1
    else:
        print(f"{YELLOW}[!]{RESET}   {ko_msg}")
        warnings += 1
    return cond


print("=" * 60)
print(" Cyber Tool Box - preflight check")
print("=" * 60)

# 1. Version de Python
print("\n-- Python --")
check(sys.version_info >= (3, 9),
      f"Python {sys.version.split()[0]}",
      f"Python {sys.version.split()[0]} (3.9+ recommande)", fatal=False)

# 2. Dependances pip  (cle = nom d'import, valeur = nom du paquet pip)
print("\n-- Dependances Python --")
deps = {
    "colorama": "colorama",
    "nmap": "python-nmap",
    "requests": "requests",
    "paramiko": "paramiko",
    "scapy": "scapy",
    "fpdf": "fpdf2",
    "googlesearch": "googlesearch-python",
}
for module, pkg in deps.items():
    try:
        importlib.import_module(module)
        ok(f"{module} (pip: {pkg})")
    except Exception:
        print(f"{RED}[KO]{RESET}  {module} manquant  ->  pip install {pkg}")
        errors += 1

# 3. Binaire nmap (necessaire pour python-nmap)
print("\n-- Outils systeme --")
check(shutil.which("nmap") is not None,
      "nmap installe et dans le PATH",
      "nmap introuvable  ->  https://nmap.org/download.html")

# 4. Privileges admin / root (requis pour scan ARP et nmap -O)
print("\n-- Privileges --")
is_admin = False
try:
    if os.name == "nt":
        import ctypes
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    else:
        is_admin = os.geteuid() == 0
except Exception:
    pass
check(is_admin,
      "Execute avec privileges admin/root",
      "Pas de privileges admin : le scan ARP et 'nmap -O' echoueront", fatal=False)

# 5. Structure du projet
print("\n-- Structure du projet --")
for f in ["cyber-tool-box.py", "affichage_menu.py"]:
    check(os.path.isfile(f), f"{f} present", f"{f} manquant a la racine")

module_files = [
    "scan_ip_os.py", "portscan.py", "searchsploit.py",
    "scan_vulnerable_proto.py", "scan_vulnerable_os.py", "eval_password.py",
    "Connection.py", "keys_certif.py", "extract_ad.py", "gen_pdf.py",
]
check(os.path.isdir("modules"), "dossier modules/ present", "dossier modules/ manquant")
for f in module_files:
    p = os.path.join("modules", f)
    check(os.path.isfile(p), f"modules/{f}", f"modules/{f} manquant", fatal=False)

# 6. Fichiers de donnees
print("\n-- Fichiers de donnees --")
for f in ["words_keys.csv", "logins_authen.csv"]:
    p = os.path.join("modules", f)
    check(os.path.isfile(p), f"modules/{f}", f"modules/{f} manquant", fatal=False)

# fichier 'logins' reference par eval_password.py (chemin 'modules/logins')
check(os.path.isfile(os.path.join("modules", "logins")),
      "modules/logins (mots de passe communs) present",
      "modules/logins introuvable -> option 3a (test password) plantera. "
      "Cree le fichier ou corrige le chemin dans eval_password.py", fatal=False)

# 7. Import reel des modules du projet
print("\n-- Import des modules du projet --")
sys.path.insert(0, os.getcwd())
try:
    import affichage_menu  # noqa: F401
    ok("affichage_menu importe")
except Exception as e:
    print(f"{RED}[KO]{RESET}  affichage_menu : {e}")
    errors += 1

for f in module_files:
    name = "modules." + f[:-3]
    try:
        importlib.import_module(name)
        ok(f"{name} importe")
    except Exception as e:
        print(f"{YELLOW}[!]{RESET}   {name} : {e}")
        warnings += 1

# Bilan
print("\n" + "=" * 60)
if errors == 0:
    print(f"{GREEN}Pret a lancer{RESET}  -  {warnings} avertissement(s).")
else:
    print(f"{RED}{errors} bloquant(s){RESET} et {warnings} avertissement(s) a corriger.")
print("=" * 60)

sys.exit(1 if errors else 0)
