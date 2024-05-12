# 11 May 2024
# ch. 9 c5 - "double string"
# 
# really seems like this shouldn't be so hard
# but i'm still working on it
# 
# 
# 
# 
# 
# 

def double_string(string):

    double_it: string = ""
    newly_doubled_string: string = ""
    newly_doubled_list = []

    for i in string:
        #print(f"i is --{i}--")
        doubled_it = i + i
        double_it = str(double_it)
        #print(f"type of double it is --{type(doubled_it}--")
        print(f"double it is --{doubled_it}--")
        newly_doubled_list.append(i + i)
        

        #double_string = doubled_string.join(double_it)

        #newly_doubled_string = newly_doubled_string.join(double_it)
        #print(f"newly_doubled_string is --{newly_doubled_string + i}--")

        #doubled_string
        
    print(f"newly doubled it list is --{newly_doubled_list}--")
    #print(f"double string is --{doubled_string}--")

    for i in range(len(newly_doubled_list)):
        
        first_word = str(newly_doubled_list[i])
        
        
        print(f"first word is --{first_word}--")

