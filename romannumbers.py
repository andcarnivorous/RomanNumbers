def romantodecimals():
    
    data = input("Insert Roman Number >>>")
    counter = 0

    ### I-IX ####

    for x in range(len(data)):
        if data[x] == "I":
            if x == (len(data)-1) or data[x+1] not in ("X", "V"):
                counter += 1
            elif data[x+1] == "V":
                counter += 0
            elif data[x+1] == "X":
                counter += 0
        if data[x] == "V":
            if x == 0 or data[x-1] != "I":
                counter += 5
            elif data[x-1] == "I":
                counter += 4

        #### X #####         
        if data[x] == "X":

            if x == (len(data)-1):
                if len(data) == 1:
                    counter += 10

                elif data[x-1] not in ("I"):
                    counter += 10

                elif data[x-1] == "I":
                    counter += 9
            elif data[x+1] == "L":
                counter += 0
            elif data[x+1] == "C":
                counter += 0

            elif x == 0:
                if data[x+1] not in ("L","C"):
                    counter += 10
                elif data[x+1] in ("C"):
                    counter += 0

            elif data[x+1] not in ("L", "C") and data[x-1] not in ("I"):
                counter += 10

                
        #### L ####
        if data[x] == "L":
            if x == 0 or data[x-1] != "X":
                counter += 50
            elif data[x-1] == "X":
                counter += 40


        #### C #####
        if data[x] == "C":

            if x == 0:
                if data[x+1] not in ("D","M"):
                    counter += 100

            elif x == (len(data)-1):
                if len(data) == 1:
                    counter += 100

                elif data[x-1] not in ("X"):
                    counter += 100

                elif data[x-1] == "X":
                    counter += 90
            elif data[x+1] == "D":
                counter += 0

            elif data[x-1] in ("X"):
                counter += 90
            elif data[x+1] in ("D", "M"):
                counter += 0
            else:
                counter += 100

                
        ### D ####                
        if data[x] == "D":
            if x == 0 or data[x-1] != "C":
                counter += 500
            elif data[x-1] == "C":
                counter += 400

        if data[x] == "M":
            if x == 0 or data[x-1] != "C":
                counter += 1000
            elif data[x-1] == "C":
                counter += 900

        else:
            print("")
            
        print("adding: ", counter)
    print(counter)


while True:
    converter()

