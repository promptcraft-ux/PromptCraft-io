
# 📂 Fichier : PromptCraft_Verification_Script.py

import json
import os
import re

def check_prompt_templates(md_path="Prompt_Templates_Library.md"):
    if not os.path.exists(md_path):
        print(f"[✗] Fichier introuvable : {md_path}")
        return [], []

    with open(md_path, encoding="utf-8") as f:
        content = f.read()

    sections = re.findall(r"## (.+?)\n", content)
    prompts = re.findall(r'- "(.+?)"', content)
    
    print(f"📚 Sections trouvées : {len(sections)}")
    print(f"✒️ Prompts listés : {len(prompts)}")
    return sections, prompts

def cross_check_examples(json_path="Prompt_Examples_By_Objectives.json"):
    if not os.path.exists(json_path):
        print(f"[✗] Fichier introuvable : {json_path}")
        return []

    with open(json_path, encoding="utf-8") as f:
        data = json.load(f)

    covered = sorted(set(example["Objectif"].lower() for example in data))
    print(f"🎯 Objectifs couverts : {len(covered)} → {covered}")
    return covered

def identify_gaps(sections, covered_objectives):
    normalized_sections = [s.lower().strip() for s in sections]
    missing = [obj for obj in normalized_sections if obj not in covered_objectives]
    if missing:
        print(f"⚠️ Objectifs présents dans les templates mais absents des exemples : {missing}")
    else:
        print("✅ Tous les objectifs des templates sont couverts par des exemples.")

if __name__ == "__main__":
    print("🔍 Vérification des fichiers PromptCraft...\n")
    sections, _ = check_prompt_templates()
    covered_objectives = cross_check_examples()
    identify_gaps(sections, covered_objectives)
