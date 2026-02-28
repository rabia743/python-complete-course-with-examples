def add (a : int,b : int) -> int:
    return a+b

a = add(2,3)
print(a)


from typing import List , Tuple , Dict

n: List[int] = [1, 2, 3, 4, 5]
m: Tuple[int,str] = (1, 2, 3, 4, 5,"harry")
print(n,m)
from typing import Dict

student: Dict[str, int] = {
    "ali": 20,
    "ahmed": 25,
    "hamza": 30
}

print(student)

