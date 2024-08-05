"""
--think of dictionaries as 'tables'
--{Key: value}
{"Bug": "an error in that program that prevents the program from running as expected"}
--when creating a dictionary with multiple 'items' you need to be careful in formatting it for readability

"""

programming_dictionary = {
  "Bug": "an error in that program that prevents the program from running as expected"
  ,"Function": "a piece of code that you can easily call over and over again."

}

# ## Retrieve from dictionary
# print(programming_dictionary["Bug"])

# ## add to dictionary; python will add add'l commas automatically
# programming_dictionary["Loop"] = "The action of doing something over and over again."
# print(programming_dictionary)

# ## empty dictionary
# programs_dictionary = {}

# ## wipe dictionary
# # programming_dictionary = {}
# # print(programming_dictionary)

# ## edit item in dictionary
# programming_dictionary["Bug"] = "A six-legged creature"
# print(programming_dictionary)

## loop through dictionary
# for thing in programming_dictionary:
#   print(thing)
#   """
#   produces only the keys
#   """

# for key in programming_dictionary:
#   print(key) 
#   print(programming_dictionary[key])

##################################################################################

## Student Score exercise
# student_scores = {
#   "Harry": 81
#   ,"Ron": 78
#   ,"Hermione": 99
#   ,"Draco": 74
#   ,"Neville": 62
# }

# student_grades = {}
# g = ""
# for ss in student_scores:
#   score = student_scores[ss]
#   if 91 <= int(score) <= 100:
#     g = "Outstanding"
#   elif 81 <= int(score) <= 90:
#     g = "Exceeds Expectations"
#   elif 71 <= int(score) <= 80:
#     g = "Acceptable"
#   elif int(score) <= 70:
#     g = "Fail"
#   student_grades[ss] = g
# print(student_grades)

##################################################################################

## Nesting
"""
--Typcial Dictionary format
dictionary {
  Key: Value
  ,Key2: Value2
  ,...
}

--Including Lists & Other Dictionaries within a given dictionary
--the structure of the dictionary 'object' can get very complicated
dictionary {
  Key: [List]
  ,Key2: {Dictionary}
}
"""

## Example
## Typical dictionary
Capitals = {
  "France": "Paris"
  ,"Germany": "Berlin"
}

""" This will not work
# travel_log = {
#   "France": "Paris","Lille","Dijon"
# } """

## Dictionary with nested lists
travel_log = {
  # key: list[]
  "France": ["Paris","Lille","Dijon"]
  ,"Germany": ["Berlin", "Hamburg", "Stuttgart"]
}

## Nest list within a list is valid Python code
## [a,b,[c,d]]
## but it's not very useful structure when compared to a dictionary

## Dictionary with nested dictionaries
## cities_visited and total_visits dictionaries for each city within the travel_log dictionary

travel_log = {
  # key: dictionary{}
  "France": {
    "cities_visited": ["Paris","Lille","Dijon"] 
    ,"total_visits": 12
    ,
  }
  ,"Germany": {
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"]
    ,"total_visits": 5
  }
}

## Nest dictionaries within a list
## lists are accessed via position, dictionaries are accessed via unique key
"""
list [{
  Key: [List]
  ,Key2: {Dict}
}
,{
  Key: Value
  ,Key: Value
}
}]
"""

travel_log = [
  {
    "country": "France"
    ,"cities_visited": ["Paris","Lille","Dijon"]
    ,"total_visits": 12
  }
  ,{
    "country": "Germany"
    ,"cities_visited": ["Berlin", "Hamburg", "Stuttgart"]
    ,"total_visits": 5
  }
]