
with open("ball.txt") as f:
    balltekst = f.read()
    
print(balltekst)

#if "hopp" in balltekst:
#    print("Hopp er i teksten.")
    
#for bokstav in balltekst:
#    print(bokstav)
'''
print(balltekst[10])
print(balltekst[10:20])
print()
print(balltekst[10:])
print("-------")
print(balltekst[:20])
print(balltekst[-10:])

hopp_indeks = balltekst.find("hopp")
print(balltekst[hopp_indeks:hopp_indeks+len("hopp")])
'''

# '\n' : new line
# '\t' : tab
# ' '  : space

import random

print()

balltekst_linjer = balltekst.split('\n')
print(balltekst_linjer)
print("---------")

random.shuffle(balltekst_linjer)
print(balltekst_linjer)
print("---------")

print('\n'.join(balltekst_linjer))
print("---------")

print('Jeg heter "Hanna"')
















