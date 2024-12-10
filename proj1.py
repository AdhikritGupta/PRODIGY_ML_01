import json
import os

file_path = 'data.json'
class TaskManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.tasks = self._load_tasks()

    def _load_tasks(self):
        with open(self.file_path, 'r') as file:
            data = json.load(file)
        return data['tasks']

    def reloadTasks(self):
        self.tasks = self._load_tasks

    def totalTasks(self):
        return len(self.tasks)


    def addTask(self, description, status):
        newId = len(self.tasks)+1
        newTask = {
            "id": newId,
            "description": description,
            "status": status
        }
        self.tasks.append(newTask)

        self.saveTasks()

        print(f"Task added: {newTask}")
    
    def updateTask(self, id, description):
        # print(type(self.tasks)) -> <class 'list'>
        update = {}
        for task in self.tasks:
            if task['id']==id: 
                if description == "":
                    description = task['description']
                task['description'] = description
                update = task
                break
        
        self.saveTasks()
        print(f"Updated Task: {update}")
        
    def deleteTask(self, id):
        delete = {}
        for task in self.tasks:
            if task['id']==id:
                delete = task
                self.tasks.remove(task)
                break
        self.saveTasks()
        print(f"Deleted Task: {delete}")    

    def changeStatus(self, id, status):
        change = {}
        for task in self.tasks:
            if task['id']==id:
                if status == "":
                    status = task['status']
                task['status'] = status
                change = task
                break
        self.saveTasks()
        print(f"Changed task status: {change}")

    def saveTasks(self):
        with open(self.file_path, 'w') as file:
            json.dump({"tasks": self.tasks}, file, indent=2)


    def viewAll(self):
        print("All Tasks: ")
        for task in self.tasks:
            print(f"ID: {task['id']}, Description: {task['description']}, Status: {task['status']}")

    def viewNotDone(self):
        print("Pending Tasks:")
        for task in self.tasks:
            if task['status'] == "Pending":
                print(f"ID: {task['id']}, Description: {task['description']}")
        print()


    def viewProg(self):
        print("In Progress Tasks:")
        for task in self.tasks:
            if task['status'] == "In Progress":
                print(f"ID: {task['id']}, Description: {task['description']}")
        print()


    def viewDone(self):
        print("Completed Tasks:")
        for task in self.tasks:
            if task['status'] == "Done":
                print(f"ID: {task['id']}, Description: {task['description']}")
        print()



def main():
    print("***Welcome to CLI Task Manager built using Python***")
    print("1. Add new task   2. Update Existing Task   3. Delete Task")
    print("4. Change Task Status   5. View Tasks   0. Exit")
    i=1
    while i!=0:
        i = int(input("Enter your choice: "))
        if i==0:
            break
        taskManager = TaskManager(file_path)

        if i==1:
            desc = input("Enter Description: ")
            stat = input("Enter status (default Pending): ")
            if stat == "":
                stat = "Pending"
            else:
                if status != "Done" and status != "Pending" and status != "In Progress":
                    print("Invalid status!")
                    continue
            taskManager.addTask(desc, stat)
        
        elif i==2:
            id = int(input("Enter the id of task to update: "))
            if id > taskManager.totalTasks():
                print("Invalid id!")
                continue
            desc = input("Enter updated description (Press enter if no change): ")
            if id > taskManager.totalTasks:
                print("Invalid id!")
            else:
                taskManager.updateTask(id, desc)
        
        elif i==3:
            id = int(input("Enter task id to delete: "))
            if id > taskManager.totalTasks():
                print("Invalid id!")
            else:
                taskManager.deleteTask(id)
        
        elif i==4:
            id = int(input("Enter task id to update status: "))
            if id > taskManager.totalTasks():
                print("Invalid id!")
                continue
            status = input("Enter updated status (Press enter if no change): ")
            if status != "":
                if status != "Done" and status != "Pending" and status != "In Progress":
                    print("Invalid Status!")
            else:
                taskManager.changeStatus(id, status)
        
        elif i==5:
            print("Select which tasks to view:")
            print("1. All Tasks  2. Tasks done")
            print("3. Tasks in progress   4. Tasks not done")
            j = int(input())
            if j==1:
                taskManager.viewAll()
            elif j==2:
                taskManager.viewDone()
            elif j==3:
                taskManager.viewProg()
            elif j==4:
                taskManager.viewNotDone()
            else:
                print("Invalid choice")
        else:
            print("Invalid choice, Try again!")

    print("Thank you, have a great day!")

if __name__ == '__main__':
    main()