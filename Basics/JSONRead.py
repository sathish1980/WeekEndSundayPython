import json


class JsonREad:

#REad based on dictonaty
    def JSONReadData(self):
        person = '{"name": "Bob", "languages": ["English", "French"]}'
        person_dict = json.loads(person)

        # Output: {'name': 'Bob', 'languages': ['English', 'French']}
        print(person_dict)

        # Output: ['English', 'French']
        print(person_dict['languages'])

        print(person_dict['name'])

        for eachvalue in  person_dict['languages']:
            print(eachvalue)


    def REadJsonFromFile(self):
        with open('C:\\Users\\sathishkumar\\PycharmProjects\\weekendSunday\\input\\Input.Json','r') as f:
            data =json.load(f)

        for eachvalue in data:
            print(eachvalue)
            print(data[eachvalue])
            acttype= type(data[eachvalue])
            if acttype == list:
                for each in data[eachvalue]:
                    print(each)
        print(data)
        for eachvalue in data['Hotels']:
            print(eachvalue)

    def WriteJsonFile(self):

        person_dict = {"name": "Bob",
                   "languages": ["English", "French"],
                   "married": True,
                   "age": 32
                   }

        with open('person.txt', 'w') as json_file:
            json.dump(person_dict, json_file)
        
    def GitBrachconcept(self):
        print("Branconcept")

obj=JsonREad()
obj.JSONReadData()
obj.REadJsonFromFile()
obj.WriteJsonFile()