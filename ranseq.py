'''
ranseq.py
A module to generate sequences.

History
-------
12-28-2015
Intitial version. Some logic incorporated from an earlier script sbgen.py,
also authored by wgray.
'''

# For translations following the number-letter format
def num_hyphen_letter(num1,num2,let1,let2,step=1):
    '''
    This function takes a number range (num1, num2,) an optional
    step and a letter range (let1, let2) and returns a formatted list
    ['1-A','2-A',...]
    '''

    from string import ascii_uppercase as ascii_caps
    
    # Get number range
    numbers = range(num1,num2+1,step)
    
    # Get letter range
    let_range = ascii_caps.find(let1),ascii_caps.find(let2)
    letters = ascii_caps[let_range[0]:let_range[1]+1]

    num_letters = []
    for num in numbers:
        for letter in letters:
            num_letters.append("{}-{}".format(num,letter))

    return num_letters
