'''
sampleDict = { 
   "class":[ 
      "student":{ 
         "name":"Mike",
         "marks":{ 
            "physics":70,
            "history":80
         }
      ]
   }
}

'''

temp_dict = {
   "grades": {
      "math": {
         "assignment": [95, 90, 76, 89],
         "finals": 90
      },
      "english": {
         "assignment": [95, 70, 66, 89],
         "finals": 70
      },
      "science": {
         "assignment": [75, 85, 65, 97],
         "finals": 70
      }
   },
   "student": "Alex"
}

print(temp_dict["grades"]["english"]["assignment"])

temp_dict["grades"]["english"]["average"] = sum(temp_dict["grades"]["english"]["assignment"]) / len(temp_dict["grades"]["english"]["assignment"])
temp_dict["grades"]["english"]["final_avg"] = (temp_dict["grades"]["english"]["average"] + temp_dict["grades"]["english"]["finals"]) / 2

print(temp_dict)