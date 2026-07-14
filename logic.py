def calcola_audit(dati):
    # Algoritmo di calcolo del rischio (Formula di base)
    # Più alto è il punteggio, più è alto il rischio
    rischio = (11 - dati['replaceable']) * 7 + (dati['ai_dep'] * 5) - (dati['upskilling'] / 1000)

    # Proiezione valore (semplificata)
    valore_futuro = dati['income'] * (1 + (dati['ambition']/20)) * (1 - (rischio/200))

    return {
        "rischio": int(rischio),
        "valore_futuro": int(valore_futuro * 5)
    }
