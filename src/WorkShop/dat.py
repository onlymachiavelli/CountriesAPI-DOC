
import ast
myFile = open("countries.txt", "r")
myResult = open("count.txt", "w")
result = []
myCountries = ast.literal_eval(myFile.readlines()[0])
for i in range(6):
    print(f"Is { myCountries[i]['CountryName']} a country ? ")
    while(1):
        print("Answer y/n")
        ans = input().upper()
        if(ans == "Y" or "N"):
            break
    if(ans == "Y"):
        while(True):
            print(f"Enter { myCountries[i]['CountryName']} Flag Url")
            myCountries[i]["Flag"] = input()
            print(f"Enter { myCountries[i]['CountryName']} Phone Code")
            myCountries[i]["PhoneCode"] = input()
            if(len(myCountries[i]["Flag"]) > 0 and len(myCountries[i]["PhoneCode"]) > 0):
                break
        result.append(myCountries[i])
        print(
            f"You added  { myCountries[i]['CountryName']} to the country list")
    else:
        print(f"Deleted {myCountries[i]['CountryName']}")
myResult.write(str(result))
"""


import ast
myFile = open("countries.txt", "r")
lines = myFile.readlines()
print(len(lines))
newFile = open("coun.txt", "w")
res = ast.literal_eval(lines[0])
for i in range(len(res)):
    res[i]["Flag"] = input("Enter Flag of " + res[i]["CountryName"] + " : ")
    # res[i]["CountryCode"] = input(
    # "Enter countrycode of " + res[i]["CountryName"] + " : ")
    if (len(res[i]["Flag"]) == 0):
        res.pop(i)

newFile.write(res)
newFile.close()
myFile.close()
import requests as req
datas = open("countries.txt", "w")
apiCall = "https://disease.sh/v3/covid-19/countries/"

countries = []
allcoun = []

res = req.get(apiCall)
for i in range(len(res.json())):
    allcoun.append(
        res.json()[i]["country"]
    )
    countries.append(
        {
            "CountryName": res.json()[i]["country"],
            "Continent": res.json()[i]["continent"],
            "ISO2": res.json()[i]["countryInfo"]["iso2"],
            "ISO3": res.json()[i]["countryInfo"]["iso3"],
            "PhoneCode": "ND",
            "Flag": "ND",
        }
    )

datas.write(str(countries))

print(i)
for j in range(len(allcoun)):
    print(allcoun[j] + "\n")
"""
