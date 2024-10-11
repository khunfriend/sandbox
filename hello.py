weight = float(input(">>>"))
height = float(input(">>"))
if weight <= 0 or height <= 0 :
    print("Error")
else :
    hm = height/100
    bmi = weight/(hm**2)
    if bmi < 18.5 :
        print("Underwright")
    else :
        if bmi <25 :
           print("Normal")
        else:
            print("Overweight") 