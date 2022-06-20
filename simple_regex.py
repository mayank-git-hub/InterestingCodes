import sys


def match(string, pattern):
    
    """Recursive
    """
    string_index = 0
    pattern_index = 0
    while pattern_index < len(pattern) and string_index < len(string):
        if pattern[pattern_index] == '.':
            string_index += 1
            pattern_index += 1
        elif pattern[pattern_index] == '*':
            character = pattern[pattern_index+1]
            num_possibility = 0
            while string[string_index + num_possibility] == character:
                num_possibility += 1
            for i in range(num_possibility + 1):
                new_answer = match(string[string_index + i:], pattern[pattern_index + 2:])
                if new_answer:
                    return True
            return False                
        elif string[string_index] == pattern[pattern_index]:
            string_index += 1
            pattern_index += 1
        else:
            return False
    
    return string_index == len(string) and pattern_index == len(pattern)


def matchLinear(string, pattern):
    
    """Linear
    """
    string_index = 0
    
    # Remove matching characters
    
    new_pattern = ''

    while string_index < len(string) and len(pattern) != 0:
        if pattern[0] == '*':
            if len(new_pattern) == 0:
                new_pattern += pattern[1]
            elif new_pattern[-1] != pattern[1]:
                new_pattern += pattern[1]
            pattern = pattern[2:]
        elif string[string_index] == pattern[0] or pattern[0] == '.':
            string = string[:string_index] + string[string_index+1:]
            pattern = pattern[1:]
        else:
            string_index += 1
    
    if len(pattern) != 0:
        return False
    
    if len(string) == 0:
        return True

    new_string = string[0]
    for string_i in string[1:]:
        if string_i == new_string[-1]:
            continue
        new_string += string_i
        
    string_index = 0
    pattern_index = 0
    while pattern_index < len(new_pattern) and string_index < len(new_string):
        if new_pattern[pattern_index] == new_string[string_index]:
            pattern_index += 1
            string_index += 1
        else:
            pattern_index += 1
            
    return string_index == len(new_string)
    

if __name__ == '__main__':
    
    
    # [[string, patter]]
    question_set = [
        ['abbabc', 'a*bb*a*ab*ab*b.'],
        ['abbc', 'a*bbc'],
        ['ac', 'a*bc'],
        ['abbbbcyzz', 'a*bc.z'],
        ['abc', 'a*bc'],
        ['abc', 'a.c'],
        ['abc', 'abc']
    ]
    print([matchLinear(*i) for i in question_set])
    
