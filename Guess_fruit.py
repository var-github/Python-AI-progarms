from sklearn import tree
# tree because we are using descision tree
features = [[140, 0], [130, 0], [150, 1], [170, 1]]
# 0 for smooth
# 1 for bumpy
labels = ["apple", "apple", "orange", "orange"]
clf = tree.DecisionTreeClassifier()
# fit means train
clf = clf.fit(features, labels)
print("Enter characteristics of fruit:")
weight = ""
smooth = ""
while True:
    ans = input("Enter weight in grams\n")
    if ans.isdigit():
        if int(ans) < 1:
            print("Weight has to be a positive integer")
        elif int(ans) > 200:
            print("Weight cannot be so much")
        else:
            weight = ans
            break
    else:
        print("Weight has to be a positive integer")

while True:
    ans = input("Enter smoothness(0-smooth, 1-rough)\n")
    if ans.isdigit():
        if int(ans) != 0 and int(ans) != 1:
            print("Smoothness can only be 0 or 1")
        else:
            smooth = ans
            break
    else:
        print("Please enter a positive integer(0/1)")

print("I think it is an " + str(clf.predict([[weight, smooth]])[0]))
