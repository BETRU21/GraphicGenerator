strTest = "1.0,2,4.89,-972"
intermediateList = strTest.split(",")
final = list(map(float, intermediateList))
print(final)