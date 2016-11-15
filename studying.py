def reverse_a_string(string_to_reverse):
    #convert the string to an array of chars
    string_to_reverse_array = list(string_to_reverse)
    #set my pointer for the beginning and for the end
    i = 0
    j = len(string_to_reverse) - 1
    #now iterate through the array of chars swapping each word until your pointers pass each other
    while(i < j):
        #remember to declare a swap space
        tmp = None
        tmp = string_to_reverse_array[i]
        string_to_reverse_array[i] = string_to_reverse_array[j]
        string_to_reverse_array[j] = tmp
        i = i + 1
        j = j - 1
    #join back the array of chars back into a string and return
    return ''.join(string_to_reverse_array)

def reverse_a_sentence(sentence_to_reverse):
    #first simply flip all the characters
    backwards_string = reverse_a_string(sentence_to_reverse)
    #now split them into "words" (in the sense that they're separated by spaces)
    backwards_string_array = backwards_string.split(' ')
    #one pointer to track each word we're going to flip'
    i = 0
    #flip each word and store it in place
    for word_to_reverse in backwards_string_array:
        backwards_string_array[i] = reverse_a_string(word_to_reverse)
        i = i + 1
    #join all the words together again to form the sentence
    return ' '.join(backwards_string_array)

sentence = "fantastical word" 
print "original sentence is " + sentence    
output = reverse_a_sentence(sentence)
print "sentence reversed is " + output