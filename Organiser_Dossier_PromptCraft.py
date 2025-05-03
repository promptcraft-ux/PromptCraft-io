import os
import shutil

BASE_DIR = os.path.expanduser("~/Documents/PromptCraft")

FOLDER_MAP = {
    "archives": ["PromptCraft_AI_Guide_Enriched.zip"],
    "documents": [
        "Guide_Debutant_AI.md",
        "Prompt_Templates_Library.md",
        "Techniques_Modernes_Prompting.md",
        "Mini_Project_Guide.md",
        "Fondamentaux_Prompting_2025.md",
        "Recursos_AI_NLP_Transformadores_y_Modelos_de_Lenguaje_Fundamentos.md",
        "Resources_Learning_AI.md"
    ],
    "scripts": [
        "PromptCraft_Verification_Script.py",
        "Lancer_Verification_PromptCraft.bat"
    ],
    "resources": [
        "AI_Concepts_Glossary.json",
        "Prompt_Examples_By_Objectives.csv",
        "API_Configuration_Template.yaml"
    ],
    "examples": [
        "Examples_Prompts",
        "Exemples_Prompts"
    ],
    "manuels": [
        "README.md",
        "PromptCraft_Vérification_Rapport.md"
    ]
}

def move_file_or_dir(filename, target_dir):
    src = os.path.join(BASE_DIR, filename)
    dest_folder = os.path.join(BASE_DIR, target_dir)
    dest = os.path.join(dest_folder, os.path.basename(filename))
    if os.path.exists(src):
        os.makedirs(dest_folder, exist_ok=True)
        shutil.move(src, dest)
        print(f"✔ Déplacé : {filename} → {target_dir}/")
    else:
        print(f"⚠ Fichier introuvable : {filename}")

def main():
    print(f"Réorganisation de {BASE_DIR}...")
    for folder, items in FOLDER_MAP.items():
        for item in items:
            move_file_or_dir(item, folder)
    print("✅ Réorganisation terminée.")

if __name__ == "__main__":
    main()