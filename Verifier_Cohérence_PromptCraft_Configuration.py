import os

# Chemin cible après synchronisation
TARGET_DIR = r"C:\GPT_PromptCraft_Configuration"

# Fichiers et dossiers attendus pour un PromptCraft cohérent
EXPECTED_STRUCTURE = {
    "documents": [".md"],
    "examples": [],
    "manuels": [],
    "resources": [".json", ".csv", ".yaml"],
    "README_master.md": None
}

def check_structure():
    problems = []

    for key, extensions in EXPECTED_STRUCTURE.items():
        path = os.path.join(TARGET_DIR, key)
        if extensions is None:
            # C'est un fichier
            if not os.path.isfile(path):
                problems.append(f"❌ Fichier manquant : {key}")
        else:
            # C'est un dossier
            if not os.path.isdir(path):
                problems.append(f"❌ Dossier manquant : {key}")
            else:
                # Vérifier les extensions si précisé
                if extensions:
                    for file in os.listdir(path):
                        if not any(file.endswith(ext) for ext in extensions):
                            problems.append(f"⚠ Fichier inattendu dans {key}: {file}")

    if problems:
        print("\n🔴 Problèmes détectés :")
        for p in problems:
            print("-", p)
    else:
        print("\n🟢 Structure et cohérence validées ✅")

if __name__ == "__main__":
    print("[Vérification de la performance et de la cohérence de PromptCraft Configuration]")
    check_structure()