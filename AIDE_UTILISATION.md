
# 🧪 Guide d’utilisation – Script de Vérification PromptCraft

## 🎯 Objectif
Ce script permet de vérifier automatiquement que tous les types de prompts présents dans `Prompt_Templates_Library.md` ont bien des exemples correspondants dans `Prompt_Examples_By_Objectives.json`.

---

## 📁 Arborescence recommandée

```
PromptCraft/
├── scripts/
│   └── PromptCraft_Verification_Script.py
├── prompts/
│   ├── Prompt_Templates_Library.md
│   └── Prompt_Examples_By_Objectives.json
```

---

## 🛠️ Comment l’exécuter

1. Ouvrir **Visual Studio Code**
2. Cliquer sur **"Open Folder"** et sélectionner votre dossier `PromptCraft`
3. Dans VS Code, ouvrir un terminal (`Terminal > New Terminal`)
4. Exécuter la commande suivante :

```bash
python scripts/PromptCraft_Verification_Script.py
```

💡 *Si vous êtes sous PowerShell, utilisez :*

```powershell
python .\scripts\PromptCraft_Verification_Script.py
```

---

## ✅ Résultat attendu

- 📚 Liste des sections détectées dans les templates
- 🎯 Objectifs couverts dans les exemples
- ⚠️ Avertissements si des catégories sont orphelines (non illustrées)

---

## 💡 Astuce

Utilisez ce rapport pour :
- Ajouter des exemples manquants
- Corriger ou renommer des catégories floues
- Identifier les domaines mal couverts

---

📌 Pour toute amélioration, pensez à versionner ce fichier dans GitHub avec votre projet `PromptCraft`.
