def select_student(z,g):
    accepted = []
    refused = []
    for i in range(0, len(z)):
        note = z[i][1]
        if note >= g:
            accepted.append(z[i])
        if note < g:
            refused.append(z[i])
    toto = sorted(accepted, key=lambda w: w[1], reverse=True)
    tutu = sorted(refused, key=lambda w: w[1])
    dico = {'Accepted': str(toto), 'Refused': str(tutu)}
    return(print(dico))
