import os
import json

# Dictionnaire des fichiers à vérifier
CHECKS = {
    "AI_Concepts_Glossary.json": {"type": "json", "min_concepts": 10},
    "Prompt_Templates_Library.md": {"type": "markdown", "min_sections": 30},
    "Scripts/API_Call_Simulator.py": {"type": "python", "functions_required": ["call_api"]},
    "README.md": {"type": "file", "must_exist": True},
    "Mini_Project_Guide.md": {"type": "markdown", "min_steps": 4}
}

def check_glossary(path):
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return "Concepts" in data and len(data["Concepts"]) >= CHECKS[os.path.basename(path)]["min_concepts"]

def check_markdown_sections(path, min_sections):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    return content.count("#") >= min_sections

def check_python_functions(path, functions):
    with open(path, 'r', encoding='utf-8') as f:
        code = f.read()
    return all(func in code for func in functions)

def main(base_dir):
    results = {}
    for file_name, params in CHECKS.items():
        full_path = os.path.join(base_dir, file_name)
        if not os.path.exists(full_path):
            results[file_name] = "❌ Fichier manquant"
            continue

        if params["type"] == "json":
            results[file_name] = "✅" if check_glossary(full_path) else "❌ Glossaire incomplet"
        elif params["type"] == "markdown":
            min_sections = params.get("min_sections", params.get("min_steps", 0))
            results[file_name] = "✅" if check_markdown_sections(full_path, min_sections) else "❌ Sections insuffisantes"
        elif params["type"] == "python":
            results[file_name] = "✅" if check_python_functions(full_path, params["functions_required"]) else "❌ Fonctions manquantes"
        elif params["type"] == "file":
            results[file_name] = "✅" if os.path.isfile(full_path) else "❌ Fichier absent"

    # Générer rapport Markdown
    report_path = os.path.join(base_dir, "PromptCraft_Vérification_Rapport.md")
    with open(report_path, "w", encoding="utf-8") as report:
        report.write("# Rapport de Vérification PromptCraft\n\n")
        for file, status in results.items():
            report.write(f"- **{file}** : {status}\n")
    print("\nVérification terminée. Rapport généré : PromptCraft_Vérification_Rapport.md")

if __name__ == "__main__":
    base_dir = input("Entrez le chemin vers votre dossier PromptCraft : ").strip()
    main(base_dir)