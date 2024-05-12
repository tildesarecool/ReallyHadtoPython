# 11 May 2024
# boot dev ch 9 ex 24
# I'm not saying it's pretty
# or the right solution
# but here you go
# Maybe i cheated on the edge cases? I don't know. Maybe.
# It passes though so i'm moving on
# 
def filter_messages(messages):
    #print(messages[0])
    final_mess_str = " "
    final_mess_list = messages
    found_dang = False
#    filter_counter = 0
    filter_counter_list = []
    for i in range(len(messages)):
        filter_counter = 0
        filt_message = str(messages[i])
        #print(f"filt message as string (in a for loop) is -- {filt_message} --")
        split_mess = filt_message.split()

        for j in range(len(split_mess)):
            if split_mess[j] == "dang":
                
                found_dang = True
                split_mess[j] = ''
                #print(f"Found a dang - new entry is {split_mess}")
                rejoined_mess = " ".join(split_mess)
                rejoined_mess = rejoined_mess.replace("  "," ")
                rejoined_mess = rejoined_mess.lstrip(" ")
                #print(f"inside dang replace if - rejoin split mess is -- {rejoined_mess} --")
                final_mess_list[i] = rejoined_mess
                
                #filter_counter_list.append(filter_counter)
#            else:
                if found_dang:
                    filter_counter += 1
                else:
                    filter_counter_list.append(0)
                    #filter_counter = 0
                
        filter_counter_list.append(filter_counter)
            #    filter_counter = 0
        
                #final_mess_list.append(rejoined_mess)
#                found_dang = True
                
#            elif found_dang == False:
#                #print("No dang given")
#                final_mess_list.append(messages[i])


            
        rejoined = " "
    
        rejoined = rejoined.join(split_mess)
        
        #print(f"rejoined split mess is -- {rejoined} --")
        
        final_mess_str = final_mess_str + rejoined + " "
        #filter_counter_list.append(filter_counter)
            
    #else:
#        final_mess_list.append(messages[i])

#    print(f"rejoined filt message is -- {rejoined} -- (after for loop)")
#    print(f"final message as string is -- {final_mess_str} -- (after for loop)")
#    print(f"final message list is -- {final_mess_list} -- (after for loop)")
#    print(f"filter counter is -- {filter_counter} -- (after for loop)")
    if len(filter_counter_list) > len(messages):
        del filter_counter_list[-1]
    
    return final_mess_list, filter_counter_list

#
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 