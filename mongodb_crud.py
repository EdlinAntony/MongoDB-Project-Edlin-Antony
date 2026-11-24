from pymongo import MongoClient
import pprint

client = MongoClient('mongodb://localhost:27017/')

db_product = client['productdb']
collection_students = db_product['productdb']

student_data = [
    {"rno":10, "sname":"ammu", "age":25, "course":"bcom", "address":"pune", "fname":"mahadevappa", "mname":"uma", "aadrno":74567346573, "phno":647864878686},
    {"rno":11, "sname":"marthi", "age":23, "course":"bba", "address":"Chennai", "fname":"gonesh", "mname":"chandramma", "aadrno":8745687345, "phno":78569827},
    {"rno":12, "sname":"Savitha", "age":26, "course":"mba", "address":"delhi", "fname":"Sanjeev", "mname":"Kavitha", "aadrno":876498375, "phno":3875970898},
    {"rno":13, "sname":"Surya", "age":29, "course":"mca", "address":"Mumbai", "fname":"anand", "mname":"Sujatha", "aadrno":84569834759, "phno":97509246503},
    {"rno":14, "sname":"ashwath", "age":30, "course":"mba", "address":"pune", "fname":"Sanjay", "mname":"kala", "aadrno":37548723482, "phno":8756984750},
    {"rno":15, "sname":"kalpa", "age":39, "course":"bba", "address":"Chennai", "fname":"nagappa", "mname":"Laxmi", "aadrno":784659839, "phno":765873465974},
    {"rno":16, "sname":"manju", "age":27, "course":"bcom", "address":"delhi", "fname":"Siddappa", "mname":"kenchamma", "aadrno":786459827509, "phno":7659384650},
    {"rno":17, "sname":"dhanu", "age":20, "course":"mca", "address":"pune", "fname":"lakkappa", "mname":"vidya", "aadrno":8645934659835, "phno":437856734859}
]

collection_students.delete_many({})
collection_students.insert_many(student_data)
print("--- Inserted into ProductDB ---")

print("\n1. Students with Age > 20:")
pprint.pprint(list(collection_students.find({"age": {"$gt": 20}}, {"_id": 0, "sname": 1, "age": 1})))

print("\n2. Students in 'bcom' course:")
pprint.pprint(list(collection_students.find({"course": {"$eq": "bcom"}}, {"_id": 0, "sname": 1, "course": 1})))

db_info = client['infotechdb']
collection_courses = db_info['infotechdb']

course_data = [
    {"name": "chaitanya", "age": 20, "email": "chai@infoteach.com", "course": [{"name": "mongodb", "duration": 7}, {"name": "java", "duration": 30}]},
    {"name": "shalini", "age": 17, "email": "shalini@infoteach.com", "course": [{"name": "basic computer", "duration": 30}, {"name": "python", "duration": 30}]}
]
collection_courses.delete_many({})
collection_courses.insert_many(course_data)
print("\n--- Inserted into InfotechDB (Nested Courses) ---")
