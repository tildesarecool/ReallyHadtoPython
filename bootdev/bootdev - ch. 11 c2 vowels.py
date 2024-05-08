def count_vowels(text):

    #print(text.split())

    sample_str = "Building a job-ready portfolio of coding projects does not happen overnight."
    vowel_list = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    vowel_return_set = set()
    string_to_list = []
    
    vowel_counter_lower = 0
    vowel_counter_upper = 0
    #print(text)
    #print(f"value is {'B' in vowel_set}")
    split_text = text.split()
#    print(text.split())   
    #print(str(split_text).split())

    for ichar in split_text:
#        print(ichar)
        for lchar in ichar:
#            print(f"lchar is |{lchar}|")
            if (lchar.isalnum()):
                string_to_list.append(lchar)
#            print(f"new value of string_to_set is |{string_to_set}|")
    #print(f"vowel list is {vowel_list}")
    
    #print(f"final string_to_list is |{string_to_list}|")
#    for chars in text, vowel_set:        
    #vchar = 0

    for vchar in range(len(string_to_list) ):
        if string_to_list[vchar] in vowel_list:
            print(f"char found in vowel list {string_to_list[vchar]}")
            if (string_to_list[vchar].isupper()):
                vowel_counter_upper += 1
                vowel_return_set.add(string_to_list[vchar])
                print(f"Is upper case, counter is {vowel_counter_upper}")
            elif (string_to_list[vchar].islower()):
                print(f"Is lower case, counter is {vowel_counter_lower}")
                vowel_counter_lower += 1
                vowel_return_set.add(string_to_list[vchar])

    print(f"final vowel_return_set is {vowel_return_set}")
    
    return (vowel_counter_lower + vowel_counter_upper), vowel_return_set
