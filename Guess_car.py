from sklearn import tree
# number of seater : horsepower
features = [[2, 100], [6, 25], [1, 300], [1, 1000], [4, 100], [10, 100]]
# 1 means race car, 2 means family car
labels = ["race", "family", "race", "race", "family", "family"]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)

power = ""
seats = ""
while True:
    ans = input("Enter horsepower\n")
    if ans.isdigit():
        if int(ans) < 1:
            print("Horsepower has to be a positive integer")
        elif int(ans) > 5000:
            print("Horsepower cannot be so much")
        else:
            power = ans
            break
    else:
        print("Horsepower has to be a positive integer")

while True:
    ans = input("Enter number of seats (1-6)\n")
    if ans.isdigit():
        if int(ans) < 1 or int(ans) > 6:
            print("The number of seats can only be between 0 to 6")
        else:
            seats = ans
            break
    else:
        print("Please enter a positive integer between 0 to 6")
print("I think it is a " + str(clf.predict([[seats, power]])[0]) + " car")
