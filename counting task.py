#getting input

String = input("Enter the number using comma :")
k=int(input("Enter the number you need to get after adding :"))
#Converting to integer
StringArray = String.split(",")

IntegerArray = [int(numeric_string) for numeric_string in StringArray]

#Processing the data
Length=(len(IntegerArray)-1)
num_a= 0
num_b= 1

loop=True
while loop:
    Possible_Number= IntegerArray[num_a] + IntegerArray[num_b]
    if Possible_Number == k:
        loop = False
        print("True")
    else:
        if num_b == Length:
            if num_a == Length:
                print("False")
                loop = False
            else:
                num_a= num_a+1
                num_b= num_a+1
                if num_b > Length:
                    loop = False
                    print("False")
        else:
            num_b= num_b+1



