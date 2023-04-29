print("Welcome to the quiz game!")
print("You are asket to answer all the questions correctly. If you do get more than half of the questions correct, you win, and if noy, you lose!")

def quiz():
    play = (input("Are you ready? [y/n]: ")).lower()
    correct_count = 0
    num_of_questions = 0

    if play == 'y' or play == 'yes':
        question1 = (input("What does CPU stand for? -> ")).lower()
        num_of_questions += 1
        if question1 == 'central processing unit':
            print('Correct!')
            correct_count += 1
        else:
            print('Inorrect -__-')

        question2 = (input("What does GPU stand for? -> ")).lower()
        num_of_questions += 1
        if question2 == 'graphics processing unit':
            print('Correct!')
            correct_count += 1
        else:
            print('Inorrect -__-')

        question3 = (input("What does GUI stand for? -> ")).lower()
        num_of_questions += 1
        if question3 == 'graphical user interface':
            print('Correct!')
            correct_count += 1
        else:
            print('Inorrect -__-')

        question4 = (input("What does RAM stand for? -> ")).lower()
        num_of_questions += 1
        if question4 == 'random access memory':
            print('Correct!')
            correct_count += 1
        else:
            print('Inorrect -__-')
    
        if correct_count >= num_of_questions//2:
            return f"Your score is {correct_count} out of {num_of_questions}, and You Won!"
        else:
            return f"Your score is {correct_count} out of {num_of_questions}, and you Lost!"
        
    elif play == 'n' or play == 'no':
        print('Have a wonderfull day')
    else:
        quiz()

print(quiz())