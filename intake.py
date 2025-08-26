from dataclasses import dataclass, asdict
from typing import List, Optional
import json, pathlib

@dataclass
class Intake:
    when: Optional[str] = None
    where: Optional[str] = None
    people_present: Optional[List[str]] = None
    what_happened: str = ""
    usual_habits: Optional[str] = None
    boundaries_said: Optional[str] = None
    safety_risk: Optional[str] = None
    goals: Optional[List[str]] = None
    notes: Optional[str] = None

    def to_json(self) -> str:
        return json.dumps(asdict(self), ensure_ascii=False, indent=2)

    def save(self, path: str):
        p = pathlib.Path(path)
        p.write_text(self.to_json(), encoding="utf-8")
