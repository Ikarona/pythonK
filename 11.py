def superposition(funmod, funseq):
    funres=[]
    for i, funq in enumerate(funseq):
        def f(funq = funq):
            nonlocal funres
            # funres.append(lambda funmod,funq: funmod(funq()))
            funres.append(funmod(funq()))

    return funres

from math import *
F = superposition(abs, (sin, cos))
for i in F:
    print(i)
print(F[0](-1), F[1](-1), F[0](2), F[1](2))