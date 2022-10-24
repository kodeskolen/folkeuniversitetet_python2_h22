
with open("ball.txt") as f:
    balltekst = f.read()
    
print(balltekst)

balltekst = balltekst.lower()

bokstaver = {}

for bokstav in balltekst:
    if bokstav not in bokstaver:
        bokstaver[bokstav] = 0
        
    bokstaver[bokstav] += 1
    
#print(bokstaver)

print(bokstaver["\n"])

for bokstav, antall in bokstaver.items():
    print(f"Bokstav '{bokstav}': {antall}")