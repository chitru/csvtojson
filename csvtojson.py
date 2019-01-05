import csv, json

csvFilePath = "titanic.csv"
jsonFilePath = "titanic.json"

#reading csv and adding data to dictionary
data = {}
with open(csvFilePath) as csvFile:
    csvReader = csv.DictReader(csvFile)
    for csvRow in csvReader:
        passenger_id = csvRow['PassengerId']
        data[passenger_id] = csvRow 

#write to json file
with open('jsonFilePath', 'w') as jsonFile:
    jsonFile.write(json.dumps(data, indent=4))