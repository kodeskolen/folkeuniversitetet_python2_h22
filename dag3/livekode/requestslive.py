import requests as req
import json

results = req.get("https://www.boredapi.com/api/activity")
#print(results.text)

results = json.loads(results.text)

print(results["activity"])

results = req.get("http://universities.hipolabs.com/search?name=University&country=United+States")
#print(results.text)

results = json.loads(results.text)

for university in results:
    print(f"{university['name']} : {university['web_pages'][0]}")
    
kompendium = req.get("https://github.com/kodeskolen/folkeuniversitetet_python2_h22/raw/main/kompendium.pdf")
with open("kompendium.pdf", "wb") as f:
    f.write(kompendium.content)

