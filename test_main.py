
import pytest

from main import get_level, main

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
@pytest.mark.parametrize(
        (
            "xp","expected_level"
        ), 
        [
            (1,"Ferro"),
            (2,"Ferro"),
            (10,"Ferro"),
            (1000,"Ferro"),
            (1001,"Bronze"),
            (1002,"Bronze"),
            (1010,"Bronze"),
            (2000,"Bronze"),
            (2001,"Prata"),
            (2002,"Prata"),
            (2010,"Prata"),
            (5000,"Prata"),
            (5001,"Ouro"),
            (5002,"Ouro"),
            (5010,"Ouro"),
            (7000,"Ouro"),
            (7001,"Platina"),
            (7002,"Platina"),
            (7010,"Platina"),
            (8000,"Platina"),
            (8001,"Ascendente"),
            (8002,"Ascendente"),
            (8010,"Ascendente"),
            (9000,"Ascendente"),
            (9001,"Imortal"),
            (9002,"Imortal"),
            (9010,"Imortal"),
            (10000,"Imortal"),
            (10001,"Radiante"),
            (10002,"Radiante"),
            (10010,"Radiante"),
        ]
)
def test_get_level(xp:int,expected_level:str):

    level: str = get_level(xp=xp)
    
    assert level == expected_level

@pytest.mark.parametrize(
        (
            "name","xp","expected_level"
        ), 
        [
            ("Lucas",1,"Ferro"),
            ("Lucas",2,"Ferro"),
            ("Lucas",10,"Ferro"),
            ("Lucas",1000,"Ferro"),
            ("Lucas",1001,"Bronze"),
            ("Lucas",1002,"Bronze"),
            ("Lucas",1010,"Bronze"),
            ("Lucas",2000,"Bronze"),
            ("Lucas",2001,"Prata"),
            ("Dolores",2002,"Prata"),
            ("Dolores",2010,"Prata"),
            ("Dolores",5000,"Prata"),
            ("Dolores",5001,"Ouro"),
            ("Dolores",5002,"Ouro"),
            ("Dolores",5010,"Ouro"),
            ("Dolores",7000,"Ouro"),
            ("Dolores",7001,"Platina"),
            ("Dolores",7002,"Platina"),
            ("Dolores",7010,"Platina"),
            ("Dolores",8000,"Platina"),
            ("Dolores",8001,"Ascendente"),
            ("Dolores",8002,"Ascendente"),
            ("Dolores",8010,"Ascendente"),
            ("Vanessa",9000,"Ascendente"),
            ("Vanessa",9001,"Imortal"),
            ("Vanessa",9002,"Imortal"),
            ("Vanessa",9010,"Imortal"),
            ("Vanessa",10000,"Imortal"),
            ("Vanessa",10001,"Radiante"),
            ("Vanessa",10002,"Radiante"),
            ("Vanessa",10010,"Radiante"),
        ]
)
def test_main(name:str,xp:int,expected_level:str):

    expected_str: str = f"O Herói de nome {name} está no nível de {expected_level}"
    test_str = main(name,xp)
    
    assert test_str == expected_str