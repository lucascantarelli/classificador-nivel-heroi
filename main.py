
import sys


def get_level(xp:int) -> str:
    """ 
    Se XP for menor do que 1.000 = Ferro
    Se XP for entre 1.001 e 2.000 = Bronze
    Se XP for entre 2.001 e 5.000 = Prata
    Se XP for entre 5.001 e 7.000 = Ouro
    Se XP for entre 7.001 e 8.000 = Platina
    Se XP for entre 8.001 e 9.000 = Ascendente
    Se XP for entre 9.001 e 10.000= Imortal
    Se XP for maior ou igual a 10.001 = Radiante
    """
    level: str = ""
    if xp <= 1000 :
        level = "Ferro"
    elif xp >= 1001 and xp <= 2000:
        level = "Bronze"
    elif xp >= 2001 and xp <= 5000:
        level = "Prata"
    elif xp >= 5001 and xp <= 7000:
        level = "Ouro"
    elif xp >= 7001 and xp <= 8000:
        level = "Platina"
    elif xp >= 8001 and xp <= 9000:
        level = "Ascendente"
    elif xp >= 9001 and xp <= 10000:
        level = "Imortal"
    elif xp >= 10001:
        level = "Radiante"

    return level

def main(hero_name:str,hero_xp) -> str:
    return f"O Herói de nome {hero_name} está no nível de {get_level(xp=hero_xp)}"


if __name__ == "__main__":
    print(main(hero_name=sys.argv[1],hero_xp=int(sys.argv[2])))