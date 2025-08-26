from typing import Dict, List

def suggest_options(intake: Dict) -> List[str]:
    options = []
    # Always start with listen-first steps
    options.append("Parler à froid, décrire ses ressentis, demander ce que l'autre a compris.")
    options.append("Poser un cadre écrit : ce que j’accepte / n’accepte pas (frontières claires).")

    # Boundaries
    b = (intake.get("boundaries_said") or "").strip().lower()
    if b:
        options.append("Rappeler les limites déjà exprimées et l'importance de leur respect.")
    else:
        options.append("Exprimer pour la première fois ses limites de façon claire et bienveillante.")

    # Safety
    risk = (intake.get("safety_risk") or "").strip().lower()
    if any(k in risk for k in ["peur","risque","violence","pression","danger"]):
        options.append("Prioriser la sécurité : lieu sûr, personne de confiance, pro (médiation / psy / association).")

    # Documentation
    options.append("Écrire un récapitulatif factuel (date/heure/lieu, faits, ressenti) pour soi / un pro.")

    # Goals -> legal
    goals = [g.lower() for g in (intake.get("goals") or [])]
    if any(g in goals for g in ["agir juridiquement","porter plainte","avocat","divorce"]):
        options.append("Consulter un avocat pour options juridiques adaptées (ce dépôt n'est pas un avis juridique).")

    # ΔM11.3: avoid hasty moral judgment
    options.append("ΔM11.3: éviter jugements hâtifs; reformuler et vérifier la compréhension.")
    return options
