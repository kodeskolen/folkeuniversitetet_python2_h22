

liste = []

ordliste = {"navn": "Hanna"}

ordliste["alder"] = 29

print(ordliste["alder"])

personliste = []
personliste.append({"navn": "Hanna", "alder": 29, 
                    "studiested": {
                        "sted": "Oslo", 
                        "utdanning": "informatikk"}
                    })
personliste.append({"navn": "Beate", "alder": 43})
personliste.append({"navn": "Paul", "alder": 56})


for indeks, person in enumerate(personliste):
    print(f"Person {indeks} har navn {person['navn']} og alder {person['alder']}")
    print(person.keys())
    print(person.values())
    print(person.items())








