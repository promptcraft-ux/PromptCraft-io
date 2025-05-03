import os

BASE_DIR = os.path.expanduser("~/Documents/PromptCraft")

# Liste des fichiers à supprimer s'ils existent
UNUSED_OR_WRONG_FILES = [
    "Prompt Templates Library.md",
    "AI Concepts Glossarv.ison",
    "PromptCraft Verification Script.pv",
    "Prompt Examples By Objectives.csv"
]

# Dossiers obsolètes ou doublons potentiels
UNUSED_FOLDERS = [
    "Examples Prompts",
    "Exemples Prompts",
    "Actions_Externes",
    "External_Actions",
    "Scripts",  # à supprimer uniquement si vide
    "Ressources IA NLP"
]

def safe_remove_file(file_name):
    path = os.path.join(BASE_DIR, file_name)
    if os.path.isfile(path):
        os.remove(path)
        print(f"🗑️ Supprimé : {file_name}")
    else:
        print(f"✅ Ignoré (inexistant ou déjà supprimé) : {file_name}")

def safe_remove_folder(folder_name):
    path = os.path.join(BASE_DIR, folder_name)
    if os.path.isdir(path):
        if not os.listdir(path):
            os.rmdir(path)
            print(f"📁 Supprimé (dossier vide) : {folder_name}")
        else:
            print(f"⚠ Non supprimé (dossier non vide) : {folder_name}")
    else:
        print(f"✅ Ignoré (dossier inexistant) : {folder_name}")

def main():
    print("Nettoyage sécurisé de PromptCraft...")
    for f in UNUSED_OR_WRONG_FILES:
        safe_remove_file(f)
    for d in UNUSED_FOLDERS:
        safe_remove_folder(d)
    print("✔ Nettoyage terminé.")

if __name__ == "__main__":
    main()