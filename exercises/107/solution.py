def select_student(z, g):
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
    dico = {'Accepted': toto, 'Refused': tutu}
    return(print(dico))

my_class = [['Kermit Wade', 27], ['Hattie Schleusner', 67], ['Ben Ball', 5], ['William Lee', 2]]

select_student(my_class, 20)
