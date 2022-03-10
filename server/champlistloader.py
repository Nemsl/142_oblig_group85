from core import Champion


def _parse_champ(champ_text: str) -> Champion:
    print(champ_text)
    name, rock, paper, scissors = champ_text.split(sep=',')
    return Champion(name, float(rock), float(paper), float(scissors))


def from_csv(chumps):
    champions = {}

    for line in chumps.split("\n"):
        champ = _parse_champ(line)
        champions[champ.name] = champ
    return champions


def load_some_champs(chumps):
    return from_csv(chumps)