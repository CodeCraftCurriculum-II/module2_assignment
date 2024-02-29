
from ansi import *
from httpUtils import *
import json

print(ANSICodes.Clear)
print("Starting Assignment 2")

# SETUP 
myPersonalID = "ShhDonotTellAnyoneSpecialSecretNumberCombo" # GET YOUR PERSONAL ID FROM THE ASSIGNMENT PAGE https://mm-203-module-2-server.onrender.com/
baseURL = "https://mm-203-module-2-server.onrender.com/"
startEndpoint = "start/" # baseURl + startEndpoint + myPersonalID
taskEndpoint = "task/"   # baseURl + taskEndpoint + myPersonalID + "/" + taskID

##### REGISTRATION
# We start by registering and getting the first task
startRespons = HttpUtils.Get(baseURL + startEndpoint + myPersonalID)
print(f"Start:\n{ANSICodes.Colors.Magenta}{startRespons.content}{ANSICodes.Reset}\n\n") # Print the response from the server to the console
taskID = "aaa" # We get the taskID from the previous response and use it to get the task (look at the console output to find the taskID)

##### FIRST TASK 
# Fetch the details of the task from the server.
print("Task 1")
task1Response = HttpUtils.Get(baseURL + taskEndpoint + myPersonalID + "/" + taskID) # Get the task from the server
print(task1Response)
task1 = json.loads(task1Response.content)

result = sum(int(p.strip()) for p in task1["parameters"].split(","))

#Send the answer to the server
task1AnswerResponse =  HttpUtils.Post(baseURL + taskEndpoint + myPersonalID + "/" + taskID, result)
print(f"Answer: {ANSICodes.Colors.Green}{task1AnswerResponse}{ANSICodes.Reset}")

taskID = "bbb" # We get the taskID from the previous response and use it to get the task (look at the console output to find the taskID)

print("\n-----------------------------------\n")

##### FIRST TASK 
# Fetch the details of the task from the server.
print("Task 2")
task2Response = HttpUtils.Get(baseURL + taskEndpoint + myPersonalID + "/" + taskID) # Get the task from the server
print(task2Response)
task2 = json.loads(task2Response.content)

answer2 = "I scream for ice cream"
if("ice cream" not in task2["parameters"]):
    answer2 = "I will have a cup of tea"

#Send the answer to the server
task2AnswerResponse =  HttpUtils.Post(baseURL + taskEndpoint + myPersonalID + "/" + taskID, answer2)
print(f"Answer: {ANSICodes.Colors.Green}{task2AnswerResponse}{ANSICodes.Reset}")