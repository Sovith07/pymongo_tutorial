import pymongo
from pymongo import MongoClient

uri = "mongodb://localhost:27017/"
client = MongoClient(uri)

db=client.todo_db
tasks_collection=db.tasks

#insert function
def create_task(description):
    task={
        'task':description
    }
    result=tasks_collection.insert_one(task)
    print(f'task created with id: {result.inserted_id}')

#read function
def read_task():
    tasks=tasks_collection.find()
    for docs in tasks:
        print(f'{docs['task']}')


while True:
    print("\n1. Create Task")
    print("2. View Task")
    print("3. Exit")

    choice=input("Enter your choice: ")

    if choice=='1':
        description=input("enter your task")
        create_task(description)
    if choice=='2':
        read_task()
    if choice=='3':
        break
    else:
        print("give valid option")

