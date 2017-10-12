'''
Created on Oct 5, 2017

@author: Sku293
'''
filename = 'alice.txt'
def word_count(filename):
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)
    else:
        # Count the approximate number of words in the file.
      words = contents.split()
      num_words = len(words)
      print("The file " + filename + " has about " + str(num_words) + " words.")
      
filenames=["alice.txt","programming.txt","pi_digits.txt","programming.doc"]
for file_name in filenames:
    word_count(file_name)