import json, sys, pathlib
from .intake import Intake
from .rules import suggest_options

PROMPT = """
ZCFA – Écoute d’abord
— Les réponses restent locales. Ce n’est pas un avis juridique. —

1) Raconte ce qui s’est passé (what_happened):
> """

def ask(prompt: str) -> str:
    print(prompt, end="")
    return sys.stdin.readline().strip()

def main():
    print(PROMPT)
    what = ask("")
    where = ask("\nOù cela s'est-il passé ? > ")
    when = ask("Quand ? > ")
    people = ask("Des personnes présentes ? (séparées par des virgules) > ")
    usual = ask("D'habitude, comment ça se passe entre vous ? > ")
    boundaries = ask("As-tu déjà exprimé des limites ? Lesquelles ? > ")
    risk = ask("Y a‑t‑il un risque/sentiment d’insécurité ? > ")
    goals = ask("Tes objectifs (ex: réparer, poser un cadre, pro, juridique) séparés par des virgules > ")
    notes = ask("Autre chose à ajouter ? > ")

    intake = Intake(
        what_happened=what,
        where=where or None,
        when=when or None,
        people_present=[p.strip() for p in people.split(",") if p.strip()] or None,
        usual_habits=usual or None,
        boundaries_said=boundaries or None,
        safety_risk=risk or None,
        goals=[g.strip() for g in goals.split(",") if g.strip()] or None,
        notes=notes or None
    )

    report = json.loads(intake.to_json())
    options = suggest_options(report)
    report["suggested_options"] = options

    out = pathlib.Path("report.json")
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\n→ Rapport sauvegardé dans {out.resolve()}\n")
    print("Suggestions:")
    for i, opt in enumerate(options, 1):
        print(f"{i}. {opt}")

if __name__ == "__main__":
    main()
