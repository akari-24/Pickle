import pickle

# 1. Leader Numbers
leader = {}
leader["Jacore Baptiste"] = '(845) 200-6250'
leader["Josiah Johnson"] = '(510) 860-5112'
leader["Richard Kamau"] = '(510) 228-5623'
leader["Andrew Lubega"] = '(925) 727-4611'
leader["Aris Cater"] = '(845) 200-6250'
leader["Gaberiel Reader"] = '(845) 200-6250'

# 2. create/open pod_nbrs.pkl file
pod_file = open("pod_nbrs.pkl","wb")

# 3. write leaders numbers
pickle.dump(leader,pod_file)

# 4. members numbers
members = {}
members["Akari"] = "510-500-2206"
members["Morris"] = "925-286-5922"
members["Moussa"] = "415-717-8414"
members["Prince"] = "510-472-0804"

# 5. add number =s to file
pickle.dump(members,pod_file)

# 6. close pod_nbrs.pkl file
pod_file.close()

# 7.
pod_file = open("pod_nbrs.pkl","rb")

# 8.
print("Pod Leaders: ")
for key, value in leader.items():
    print(key, value)
print("\n")

# 9.
print("Members: ")
for key, value in members.items():
    print(key, value)
print("\n")

# 10.
pod_file.close()
