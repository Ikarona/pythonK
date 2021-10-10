def superposition(funmod, funseq):
    funres=[]
    for i, funq in enumerate(funseq):
        def f(x, funq = funq):
            return funmod(funq(x))
        funres.append(f)
    return funres