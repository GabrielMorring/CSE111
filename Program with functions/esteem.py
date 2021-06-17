def strongly_disagree_is_zero(answer):
    value = 0
    if answer == "D":
        value = 0
    elif answer == "d":
        value = 1
    elif answer == "a":
        value = 2
    elif answer =="A":
        value = 3
    return value
 
def strongly_disagree_is_three(answer):
    value = 0
    if answer == "D":
        value = 3
    elif answer == "d":
        value = 2
    elif answer == "a":
        value = 1
    elif answer =="A":
        value = 0
    return value


def main():
    
    print('\nThis program is an implementation of the Rosenberg Self-Esteem Scale. This program will show you ten statements that you could possibly apply to yourself. Please rate how much you agree with each of the statements by responding with one of these four letters:')

    print('\n\n\nD means you strongly disagree with the statement.')
    print('\nd means you disagree with the statement.')
    print('\na means you agree with the statement.')
    print('\nA means you strongly agree with the statement.')
    
    a = strongly_disagree_is_zero(input('\n\nI feel that I am a person of worth, at least on an equal plane with others. '))
    b = strongly_disagree_is_zero(input('All in all, I am inclined to feel that I am a failure. '))
    c = strongly_disagree_is_three(input('I feel that I have a number of good qualities. '))
    d = strongly_disagree_is_zero(input('I am able to do things as well as most other people. '))
    e = strongly_disagree_is_three(input('I feel I do not have much to be proud of. '))
    f = strongly_disagree_is_zero(input('I take a positive attitude toward myself. '))
    g = strongly_disagree_is_zero(input('On the whole, I am satisfied with myself. '))
    h = strongly_disagree_is_three(input('I wish I could have more respect for myself. '))
    i = strongly_disagree_is_three(input('I certainly feel useless at times. '))
    j = strongly_disagree_is_three(input('At times I think I am no good at all.'))

    score = a + b + c + d + e + f + g + h + i + j

    print(f'\nYour score is {score}.')


main()