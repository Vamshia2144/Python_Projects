# -*- coding: utf-8 -*-
"""
Created on Thu May 14 19:10:44 2026

@author: avams
"""


Tasks=[]
while True:
    print("1.Add Task")
    print("2.View Task")
    print("3.Delete Task")
    print("4.Exit")
    
    Choice=input("Enter the Choice:\n")
    
    if Choice=='1':
        task=input("Enter the task:\n")
        Tasks.append(task)
        print("Added Task")
    elif Choice=='2':
        for i,task in enumerate(Tasks,start=1):
            print(f"{i}.{task}")
    elif Choice=='3':
        num=int(input("Enter Task Number to delete::\n"))
        if num>1 or num<=len(Tasks):
            Tasks.pop(num-1)
        else:
            print("Invalid Task number")
    elif Choice=='4':
        break
    else:
        print("Invalid Choice")        
            
