
def still_spørsmål(spørsmål, riktig_svar):
    svar = input(spørsmål)

    if svar == riktig_svar:
        return 1
    
    return 0

poengsum = still_spørsmål("Hva er hovedstaden i Norge?", "Oslo")
poengsum += still_spørsmål("Hva er hovedstaden i Tyskland?", "Berlin")

print(f"Du fikk {poengsum} poeng.")

