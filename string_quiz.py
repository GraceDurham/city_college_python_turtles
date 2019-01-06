
# Counts how many times byte appears in the sentence below which is twice
print("Some bytes and byte array operations assume the use of ASCII compatible binary formats".count("byte"))


def count_word(word):
    """This function counts how manys letter in word or length of the sentence"""

    count = 0
    for i in range(len(word)):
        # if word[i] == letter:
    	count = count + 1
        
    return count 

    # second option return(len(word))   
def main():
    
    print(count_word("The programming language you will be learning is Python. Python is an example of a high-level language; other high-level languages you might have heard of are C++, PHP, and Java."))
    
main()

