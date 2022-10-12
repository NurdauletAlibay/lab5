stud_grades = [
  {"name": "Daulet","grades": [5, 5, 5, 5, 4]},
  {"name": "Arlan","grades": [4, 5, 5, 4, 5]},
  {"name": "Aigerim","grades": [4, 5, 4, 4, 5]},
  {"name": "Nurdaulet","grades": [5, 5, 5, 4, 5]},
  {"name": "Nurbek","grades": [5, 4, 5, 4, 4]},
  {"name": "Arman","grades": [5, 5, 5, 4, 5]},
  {"name": "Ayazhan","grades": [5, 5, 5, 4, 5]}
]
def get_stud_grades(students):
  string = str(input('Student: '))
  for student in students:
  if student["name"] == string:
  print(student["grades"])
    
get_stud_grades(stud_grades)