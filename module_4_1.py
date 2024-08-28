import true_math as tm
import fake_math as fm
from random import randint

n1 = randint(21,40)
n2 = randint(1,10)
print(tm.divide(n1, n2))
print(tm.divide(n1, 0))

n1 = randint(n1,100)
n2 = randint(n2,30)
print(fm.divide(n1, n2))
print(fm.divide(n1, 0))