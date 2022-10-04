# create a dictionary to store names of states and their capitals

states = dict()
n=int(input("How many states are there : "))
for i in range(n):
      state = input(" enter name of the state :")
      capital = input("enter name of hte capital :")
      states[state] = capital

print(" Created dictionary is :", states)
temp = input("enter the state to display capital : ")
print(states[temp])
