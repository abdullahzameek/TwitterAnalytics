csv_file = open("nyufollowers.csv", "r")
csv_file.readline()

words = ["NYU", "nyu", "NYU Abu Dhabi", "New York University Abu Dhabi", "nyuad", "NYUAD"]
# words2 = ["harvard", "Harvard"]
filter_words = ["Lecturer","Professor","Instructor", "Faculty", "faculty", "professor", "instructor","professor", "lecturer"]
users = []
filtered = True
for line in csv_file:
    line = line.split(",")
    for word in words:
        try:
            if word in line[6]:
                if line not in users:
                    for word in filter_words:
                        if word in line[6]:
                            filtered = False
                    if filtered:
                        users.append(line)
                    filtered = True
        except:
            print("invalid line")

print(users)
print(len(users))

nyu_users = open("nyu_users2.csv", "w+")
for user in users:
    line = ",".join(user)
    nyu_users.write(line)

nyu_users.close()
csv_file.close()
