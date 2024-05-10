'''
boot.dev
chap 9 #24


FILTER MESSAGES
You are about to write a bit more code in a single function than you have before.

Do not try to write it all at once. Start with the outermost loop, and work your way inwards. 
Add extra print() statements and run your code often to make sure it's doing what you expect. 
Just make sure to remove the extra print() statements before submitting your code.

Running your code often to make sure each line is doing what you expect is called "debugging". 
All programmers, even seasoned professionals, break large problems down into small ones that they can debug line by line.

ASSIGNMENT
We need to filter the profanity out of our game's live chat feature! Complete the filter_messages function. 
It takes a list of chat messages as input and returns 2 new lists:

A list of the same messages but with all instances of the word dang removed.
A list containing the number of dang words that were removed from the message at that particular index.
For example:

messages = ["dang it bobby!", "look at it go"]
filter_messages(messages) # returns ["it bobby!", "look at it go"], [1, 0]
Copy icon
Here are the steps for you to follow:

Create the 2 empty lists that you'll return at the end. One for the filtered messages, and one for counts of words removed.
For each message in the input list:
Split the message into a list of words using the .split() string method (see below for help).
Create a new empty list for all the non-bad words for this message.
Create a counter variable and set it to 0. We'll increment this when we remove words from this message.
For each word in the message:
If the word is dang, increment the counter
If it is not dang, add the word to the non-bad word list you created
Join the list of non-bad words into a single string using the .join() method (see below for help)
Append the new clean message to the final list of filtered messages
Append the count of bad words removed to its list
Return the filtered messages first, then the counters
TIPS
SPLIT A STRING INTO A LIST OF WORDS
The .split() method is called on a string. If you don't pass it any arguments, it will just split the words in the string on the whitespace.

message = "hello there sam"
words = message.split()
print(words)
# Prints: ["hello", "there", "sam"]
Copy icon
JOIN A LIST OF STRINGS INTO A SINGLE STRING
The .join() method is called on a delimiter (what goes between all the words in the list), and takes a list of strings as input.

list_of_words = ["hello", "there", "sam"]
sentence = " ".join(list_of_words)
print(sentence)
# Prints: "hello there sam"

'''

def filter_messages(messages):
    #print(messages[0])
    final_mess_str = " "
    for i in range(len(messages)):
        filt_message = str(messages[i])
        print(f"filt message as string (in a for loop) is -- {filt_message} --")
        split_mess = filt_message.split()

        for j in range(len(split_mess)):
            if split_mess[j] == "dang":
                
                split_mess[j] = "darn"
                print(f"Found a dang - new entry is {split_mess}")
            else:
                print("No dang given")
        rejoined = " "
    
        rejoined = rejoined.join(split_mess)
        
        print(f"rejoined split mess is -- {rejoined} --")
        
        final_mess_str = final_mess_str + rejoined + " "

    print(f"rejoined filt message is -- {rejoined} -- (after for loop)")
    print(f"final message is -- {final_mess_str} -- (after for loop)")
#    rejoined = " "
#
#    rejoined = rejoined.join(split_mess)
#    
#    print(f"rejoined split mess is -- {rejoined} --")
    


    
#    for i in range(len(messages)):
#    for "dang" in filt_message:
#        print("Found a dang")

#    print(f"message as string is -- {filt_message} --")
#    
#    split_mess = "this is a string".split()
#    print(f"split message as string is -- {split_mess} --")

#    split_mess = filt_message.split(messages[1])
#    print(f"message as string is -- {split_mess} --")    
    
#    joined_message = filt_message.join(messages[0])
#    print(f"message as string is -- {joined_message} --")
    
#    filt_message = str(messages[0])
#    print(f"filt message as string is -- {filt_message} --")

    #print(f"split filt message 0 is -- {split_mess[0]} --")
    #split_mess = str(split_mess)    