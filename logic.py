def calcola_audit(dati):
    # Logica di calcolo ponderata
    # Pesa di più la sostituibilità e la dipendenza da AI
    raw_risk = (11 - dati['replaceable']) * 5 + (dati['ai_dep'] * 6) - (dati['upskilling'] / 800)
    # Normalizzazione complessa per evitare risultati piatti
    rischio = max(0, min(100, int(raw_risk * 1.2)))
    
    # Proiezione con moltiplicatore di ambizione
    valore_futuro = dati['income'] * (1 + (dati['ambition'] / 15)) * (1 - (rischio / 300))
    
    return {
        "rischio": rischio,
        "valore_futuro": int(valore_futuro * 5),
        "status": "CRITICAL" if rischio > 60 else "STABLE" if rischio > 30 else "OPTIMAL"
    }
