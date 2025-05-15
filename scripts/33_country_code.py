import csv, json


with open("33_country_codes.json","r") as file:
    data=json.load(file)
    print(data)
    







codes = {"country": [
          {
              "countryCode": "AD",
              "countryName": "Andorra",
              "continentName": "Europe"
          },
          {
              "countryCode": "AE",
              "countryName": "United Arab Emirates",
              "continentName": "Asia"
          },
          {
              "countryCode": "AF",
              "countryName": "Afghanistan",
              "continentName": "Asia"
          }
        ]
    }

codesc=[]
countries=[]
continrnt=[]


print(codes["country"][0]["countryName"])

for code in data["country"]:
    codesc.append(code["countryCode"])
    countries.append(code["countryName"])
    continrnt.append(code["continentName"])



print(codesc)
print(countries)
print(continrnt)


def save_csv(codesc, countries, continrnt):
    with open("myCSV1.csv", "w", newline="") as file:
        writer=csv.writer(file)
        writer.writerow(["country Code","country Name","continent Name"])
        print(codesc,countries,continrnt)
        for i in range(1,len(countries)):
            writer.writerow([codesc[i],countries[i],continrnt[i]])
            
        
save_csv(codesc,countries,continrnt)

