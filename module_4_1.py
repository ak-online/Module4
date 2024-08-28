import true_math as tm
import fake_math as fm
import random

n1 = random.randint(21,40)
n2 = random.randint(1,10)
print(tm.divide(n1, n2))
print(tm.divide(n1, 0))

n1 = random.randint(n1,100)
n2 = random.randint(n2,30)
print(fm.divide(n1, n2))
print(fm.divide(n1, 0))