# 🌐 Intégration de la Recherche Internet dans GPT PromptCraft

Ce guide décrit comment activer et exploiter la recherche web dans un assistant GPT enrichi avec le pack PromptCraft.

---

## 🎯 Objectifs de l’intégration Web

- Récupérer des **informations à jour** sur l’IA, les technologies, ou les tendances pédagogiques.
- Enrichir les réponses générées par PromptCraft avec des **sources extérieures pertinentes**.
- Alimenter dynamiquement des prompts ou ressources grâce à la **recherche augmentée**.

---

## 🔧 Instructions personnalisées à inclure

Ajoutez à vos instructions système GPT :

> Lorsque l'utilisateur pose une question nécessitant des données actuelles, effectue une recherche Internet et intègre les résultats dans ta réponse, en mentionnant la source. Propose de sauvegarder le contenu utile dans `/resources/` sous forme de `.md` ou `.json`.

---

## 📘 Exemples de requêtes Web à exécuter

- Quelle est la dernière mise à jour de l’API OpenAI ?
- Y a-t-il des modèles alternatifs à GPT pour l'éducation ?
- Trouve des prompts récents utilisés par des journalistes avec ChatGPT.
- Recherche une étude sur les biais algorithmiques dans les modèles de langage.

---

## 💾 Sauvegarde automatique (optionnelle)

Lorsqu’une réponse Web est jugée utile :
- Enregistre-la dans : `/resources/Recherche_<sujet>.md`
- Structure :
  - 🔎 **Sujet :**
  - 📝 **Résumé de la réponse :**
  - 🌐 **Source/lien :**

---

## 🛠 Recommandations

- Activez la navigation Web dans votre assistant GPT (si disponible).
- Encadrez l’usage des recherches pour éviter les dérives (pas de requêtes sensibles).
- Vérifiez la **pertinence et la fraîcheur** des sources citées.

---

## ✅ Résultat attendu

Un assistant GPT PromptCraft capable de :
- Compléter ses réponses par des recherches actuelles
- Documenter automatiquement les découvertes dans le projet
- Agir comme un explorateur et historien de l’IA au service de vos prompts