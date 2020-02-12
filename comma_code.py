spam = ['apples', 'bananas', 'tofu', 'cats']

def comma_code(list):
    string = ''
    for i in range(len(list) - 1):
        string += list[i] + ", "
    string + "and " + spam[-1]
    print(string + "and " + spam[-1])
    
comma_code(spam)