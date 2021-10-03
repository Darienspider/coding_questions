#there are 2 ways

base_test = 'Doomedapple7565'

def reverse_string(string_here):
    backwards = ''
    for i in string_here[::-1]:
        backwards+=i
    return backwards

def palindrome_detect(original):
    backwards = reverse_string(original)
    if original == backwards:
        print(f'Reveresed String returned as a palindrome')
    else:
        print('Not a Palindrome')

def matching_charecters(base_string):
    charecters = {}
    counter = 0

    for chars in base_string:
        charecters[chars] = 0
    
    for chars in base_string:
        if chars in charecters:
            charecters[chars] = charecters[chars]+1
                
    return charecters
    """
    [12:37 PM] Vex: Can do this in one step by utilizing collections.counter
    [12:37 PM] Vex: It's job is to do this
    [12:38 PM] Vex: If it didn't exist you'd use setdefault
    @Vex
    Can do this in one step by utilizing collections.counter
    [12:38 PM] Doomedapple7565: the assignment seemed like it wanted me to reinvent the wheel basically.
    [12:39 PM] Vex: Then use setdefault
    NEW
    [12:40 PM] Vex: This shouldn't be a double iteration and you don't need a conditional
    """

# test = matching_charecters('Shadarien Williams')

# for index,value in enumerate(test.keys()):
#     if test[value] == 1:
#         print(index+1,value)

def count_vowels(base_string):
    counter = 0
    vowel_bank = ['a','e','i','o','u','y']
    charecter_bank = {}
    for i in base_string:
        if i in vowel_bank:
            counter +=1
    
    charecter_bank['Vowels'] = counter
    print(f' For Base String {base_string}: {charecter_bank}')

def if_anagram(base_string):
    """
    An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
    typically using all the original letters exactly once.
    """
    #TODO: Study this, way too complicated at this time
    letter_bank = []
    for i in base_string:
        letter_bank.append(i)
    
def small_and_large(array_here):
    smallest = 0
    largest = 0
    for i in array_here:
        try:
            print('array is an interger array')

        except:
            print('array is a string array')

small_and_large(["Ford", "Volvo", "BMW"])
# small_and_large([1,800,32])