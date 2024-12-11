### 모듈 임포트하기
from random import choice

places = ["McDonalds", "KFC", "Burger King", 
            "Taco Bell", "Wendys", "Arbys", "Pizza Hut"]

def pick():
    return choice(places)