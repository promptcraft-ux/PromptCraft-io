import os
import shutil

# Répertoire source enrichi
SOURCE_DIR = r"C:\Users\attc2\Documents\PromptCraft"

# Répertoire cible fictif représentant l’environnement de configuration GPT
# (À adapter à votre cas : dossier assistant OpenAI local ou environnement de test)
TARGET_DIR = r"C:\GPT_PromptCraft_Configuration"  # Exemple de cible de synchronisation

# Extensions valides à transférer dans l'environnement GPT
ALLOWED_EXTENSIONS = [".md", ".json", ".csv", ".yaml", ".py"]

# Étape 1 : suppression du contenu existant
def clean_target(target_path):
    if os.path.exists(target_path):
        for root, dirs, files in os.walk(target_path, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                shutil.rmtree(os.path.join(root, name))
        print("🗑 Ancien contenu supprimé.")
    else:
        os.makedirs(target_path)
        print("📁 Répertoire cible créé.")

# Étape 2 : copie enrichie depuis PromptCraft
def sync_promptcraft():
    clean_target(TARGET_DIR)
    for root, _, files in os.walk(SOURCE_DIR):
        for file in files:
            if any(file.endswith(ext) for ext in ALLOWED_EXTENSIONS):
                rel_path = os.path.relpath(root, SOURCE_DIR)
                target_subdir = os.path.join(TARGET_DIR, rel_path)
                os.makedirs(target_subdir, exist_ok=True)
                shutil.copy2(os.path.join(root, file), os.path.join(target_subdir, file))
                print(f"✅ Copié : {file}")
    print("✔ Synchronisation terminée.")

if __name__ == "__main__":
    sync_promptcraft()