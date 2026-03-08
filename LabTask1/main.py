
mark = float(input("Enter a mark: "))

if mark%5>=3 and mark>=45 and mark<90:
    print(mark+(5-mark%5))
else:    print(mark)