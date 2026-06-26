"""
Cyber Tool Box v6.0 - Mr Robot Edition
fsociety inspired design
"""

import requests


def search_exploit(service, html_render=False):
    """
    Recherche des CVE liees a un service via l'API officielle NVD (NIST).
    Endpoint : https://services.nvd.nist.gov/rest/json/cves/2.0/
    Aucune cle requise (mais ~6s de delai sans cle a cause du rate-limit).
    Garde la meme signature que la version precedente.
    """
    spacing = "<br>" if html_render else "\n"
    display_info = ""

    if not html_render:
        display_info += "\n\n===================================\n"
        display_info += " CVE related to " + service
        display_info += "\n===================================\n\n"

    try:
        url = "https://services.nvd.nist.gov/rest/json/cves/2.0/"
        params = {"keywordSearch": service, "resultsPerPage": 10}
        response = requests.get(url, params=params, timeout=30)
        response.raise_for_status()
        data = response.json()

        vulnerabilities = data.get("vulnerabilities", [])

        if not vulnerabilities:
            display_info += f"No CVE found for '{service}'.{spacing}"
            return display_info

        for item in vulnerabilities:
            cve = item.get("cve", {})
            cve_id = cve.get("id", "N/A")

            # Description en anglais
            summary = "No description available."
            for desc in cve.get("descriptions", []):
                if desc.get("lang") == "en":
                    summary = desc.get("value", summary)
                    break
            if len(summary) > 200:
                summary = summary[:200] + "..."

            # Score CVSS (on prend v3.1 si dispo, sinon v2)
            score = "N/A"
            metrics = cve.get("metrics", {})
            if "cvssMetricV31" in metrics:
                score = metrics["cvssMetricV31"][0]["cvssData"]["baseScore"]
            elif "cvssMetricV2" in metrics:
                score = metrics["cvssMetricV2"][0]["cvssData"]["baseScore"]

            display_info += f"[{cve_id}] (CVSS: {score}){spacing}{summary}{spacing}{spacing}"

    except requests.exceptions.RequestException as e:
        display_info += f"Error contacting NVD database: {e}{spacing}"

    return display_info