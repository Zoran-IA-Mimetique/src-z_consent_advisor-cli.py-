# Zoran‑Consent‑First‑Advisor (ZCFA)

**FR · EN below**

> Conseiller “écoute d’abord” pour situations sensibles liées au **consentement** (couple, relations, intimité).  
> Objectif : aider à **raconter les faits**, **contextualiser l’habitude**, **clarifier les limites**, puis **proposer des options** — *avant* toute bascule juridique. **Avertissement : ceci n’est pas un avis juridique.**

⟦CONSENT:universal⋄LISTEN:first⋄ΔM11.3:guard⋄ETHIC:care⟧

---

## Résumé (FR)

- **150** : Conseiller “écoute d’abord” pour comprendre un geste non désiré : récit, habitudes, limites, options concrètes. Non-juridique, éthique, duplicable.  
- **350** : ZCFA structure une analyse **humaine** avant le droit : 1) récit précis, 2) habitudes/consentement implicite, 3) limites et signaux faibles, 4) risques/sécurité, 5) options (dialogue, cadrage, preuve, pro, voie juridique). Fournit un **schéma JSON d’anamnèse**, un **CLI** pas-à-pas, des **checklists** et un **ΔM11.3 guard** pour éviter la dérive. Idéal pour *advisors*, éducateurs, médiateurs, et IA conseillères.
- **1200** :  
ZCFA part d’un constat simple : dans les situations sensibles liées au **consentement**, répondre d’emblée par le Code pénal coupe la conversation et rate le contexte. La **bonne pratique** consiste à **écouter, comprendre et situer** : le même geste peut être tendre dans un cadre complice, ou intrusif s’il ignore une limite exprimée. ZCFA propose une **prise d’informations structurée** (récit → habitudes → limites → sécurité → objectifs) et un **moteur d’options** graduées : parler à froid, poser le cadre (ce que j’accepte / je refuse), documenter les faits (journal privé, mails récap), consulter un tiers (médiation, psy, association), et **seulement si la personne le souhaite**, explorer la voie juridique avec un professionnel. Le dépôt inclut :  
  - `data/schema/context_intake.schema.json` (schéma d’anamnèse)  
  - `src/z_consent_advisor/cli.py` (assistant terminal pas‑à‑pas)  
  - `docs/design.md` (raison d’être, ΔM11.3 guard, éthique)  
  - `examples/intake_example.json` (exemple anonymisé)  
  - **Checklists** (écoute active, facteurs de risque, préparation d’un rendez‑vous pro)  
  - **Disclaimer clair** : ce projet n’est **pas** un conseil juridique ni médical.  
Le but : **recentrer l’aide sur l’humain**, produire un **socle duplicable** (IA, conseillers, associations), et **normaliser l’égalité du consentement** (genre‑agnostique), tout en restant conforme (RGPD/AI Act) et traçable (EthicChain).

---

## EN (brief)

- **150**: “Listen‑first” advisor for consent‑related situations: narrative, habits, boundaries, options. Non‑legal, ethical, replicable.  
- **350**: ZCFA structures a **human layer before law**: 1) detailed narrative, 2) habits/implicit consent, 3) boundaries & weak signals, 4) risk/safety, 5) options (dialogue, framing, evidence, pro help, legal path). Includes **JSON intake schema**, **step‑by‑step CLI**, **checklists**, and a **ΔM11.3 guard**. Useful for advisors, educators, mediators, and advising AIs.

---

## Usage rapide

```bash
python -m z_consent_advisor.cli
```

Le CLI guide : **Récit → Habitudes → Limites → Sécurité → Objectifs → Options** et sauvegarde un **rapport JSON** local.  
> Les données restent **en local**. Aucune remontée réseau.

---

## Structure

- `src/z_consent_advisor/cli.py` – assistant terminal “écoute d’abord”  
- `src/z_consent_advisor/intake.py` – modèles & validation basique  
- `src/z_consent_advisor/rules.py` – moteur d’options graduées (non-juridique)  
- `data/schema/context_intake.schema.json` – schéma JSON d’anamnèse  
- `docs/design.md` – principes, ΔM11.3, EthicChain, conformité  
- `examples/intake_example.json` – exemple de saisie  
- `CHECKLISTS.md` – écoute active, signaux, limites, préparation pro  
- `DISCLAIMER.md` – **pas** un avis juridique/médical  
- `LICENSE` – MIT

---

## Avertissement

Ce dépôt est fourni à des fins **éducatives et de structuration de la parole**.  
Il **ne remplace pas** un professionnel (avocat, médecin, psychologue).

