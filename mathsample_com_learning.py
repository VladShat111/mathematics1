# levels
# Beginner_jump
# Easy_jump
# Standart_jump
# Professional_jump
# Hardcore_jump

# import mathsample_com_learning_module_of_logic


import random
from mathsample_com_Controller import CounterOfShowQuantityOfSamles
from mathsample_com_Controller import СounterOfUnswers
from mathsample_com_Controller import generalCountCorrect
from mathsample_com_Data_info import Beginner_jump, Easy_jump, Standart_jump, Professional_jump, Hardcore_jump





class BasicLogicForFirstApp:

    @CounterOfShowQuantityOfSamles

    def __init__(self, serial_number, number01, sign, number02, equals_sign, answer):
        self.serial_number = serial_number
        self.number01 = number01
        self.sign = sign
        self.number02 = number02
        self.equals_sign = equals_sign
        self.answer = answer

    @СounterOfUnswers


    def check_answer(self, try_answer):
        return try_answer == self.answer

    #@generalCountCorrect(CountCorrect)
if __name__=='__main__':
    UserInput = int(input('Enter level: '
                          '1 - Beginner_jump, '
                          '2 - Easy_jump, '
                          '3 - Standart_jump, '
                          '4 - Professional_jump, '
                          '5 - Hardcore_jump'))


    question_list = []

    if UserInput == 1:
        Beginner_jump_for_use = Beginner_jump

        for serial_number, number01, sign, number02, equals_sign, answer in Beginner_jump_for_use:
            print('Solve example:')
            print(number01, sign, number02, equals_sign, '?')
            current_question = BasicLogicForFirstApp(serial_number, number01, sign, number02, equals_sign, answer)
            question_list.append(current_question)

            if current_question.check_answer(input('What answer?')):
                first_is_correct_some_good_worlds = [
                    'Unbelievable!',
                    'Super!',
                    'Wow! Brilliant!',
                    'Amazing!',
                    'Awesome!',
                    'Wonderful',
                    'Perfect',
                    'Cosmically cool!',
                    'Charmingly!',
                    'Adorably!',
                    'Inspiring',
                    'Breathtaking!',
                    'Spectacularly',
                    'It’s impossible!',
                    'It can’t be true!',
                    'I can’t believe it!',
                    'Incredible!',
                    'I’m speechless!',
                    'How amazing!',
                    'I am astounded!',
                    'I am shocked!',
                    'That’s a good one!',
                    'I can’t imagine you did that!',
                    'I’ll believe it when pigs fly!',
                ]
                CountCorrect = True
                print(random.choice(first_is_correct_some_good_worlds))

            elif current_question.check_answer(input('Try, one more')):
                print('Excellent, Street forward!')

            elif current_question.check_answer(input('Try, last time')):
                print('Good job, Street ahead!')

            else:
                print(number01, sign, number02, equals_sign, answer)

                motivated_worlds = [
                    'Do not worry, street ahead!',
                    'Opportunities don’t happen, you create them',
                    'If you do not think about the future, you cannot have one',
                    'Every solution breeds new problems',
                    'If you fall asleep now, you will dream',
                    'If you study now, you will live your dream',
                    'When you think it is too late, the truth is, it is still early',
                    'Studying is not about time.It is about effort',
                    'If you don not walk today, you will have to run tomorrow',
                    'Even now, your enemies are eagerly flipping through books',
                    'Success is walking from failure to failure with no loss of enthusiasm',
                    'Setting goals is the first step in turning the invisible into the visible',
                    'Too many of us are not living our dreams because we are living our fears',
                    'Success is 99 % failure',
                    'Problems are not stop signs, they are guidelines',
                    'What would you do if you were not afraid',
                ]
                print(random.choice(motivated_worlds))
                incorrect = []
                incorrect.append(current_question)


    if UserInput == 2:
        Easy_jump_for_use = Easy_jump

        for serial_number, number01, sign, number02, equals_sign, answer in Easy_jump_for_use:
            print(number01, sign, number02, equals_sign,  '?')
            current_question = BasicLogicForFirstApp(serial_number, number01, sign, number02, equals_sign, answer)
            question_list.append(current_question)

            if current_question.check_answer(input('What answer?')):
                first_is_correct_some_good_worlds2 = [
                    'Unbelievable!',
                    'Super!',
                    'Wow! Brilliant!',
                    'Amazing!',
                    'Awesome!',
                    'Wonderful',
                    'Perfect',
                    'Cosmically cool!',
                    'Charmingly!',
                    'Adorably!',
                    'Inspiring',
                    'Breathtaking!',
                    'Spectacularly',
                    'It’s impossible!',
                    'It can’t be true!',
                    'I can’t believe it!',
                    'Incredible!',
                    'I’m speechless!',
                    'How amazing!',
                    'I am astounded!',
                    'I am shocked!',
                    'That’s a good one!',
                    'I can’t imagine you did that!',
                    'I’ll believe it when pigs fly!',
                ]
                CountCorrect = True
                print(random.choice(first_is_correct_some_good_worlds2))

            elif current_question.check_answer(input('Try, one more')):
                print('Excellent, Street forward!')

            elif current_question.check_answer(input('Try, last time')):
                print('Good job, Street ahead!')

            else:
                print(number01, sign, number02, equals_sign, answer)

                motivated_worlds2 = [
                    'Do not worry, street ahead!',
                    'Opportunities don’t happen, you create them',
                    'If you do not think about the future, you cannot have one',
                    'Every solution breeds new problems',
                    'If you fall asleep now, you will dream',
                    'If you study now, you will live your dream',
                    'When you think it is too late, the truth is, it is still early',
                    'Studying is not about time.It is about effort',
                    'If you don not walk today, you will have to run tomorrow',
                    'Even now, your enemies are eagerly flipping through books',
                    'Success is walking from failure to failure with no loss of enthusiasm',
                    'Setting goals is the first step in turning the invisible into the visible',
                    'Too many of us are not living our dreams because we are living our fears',
                    'Success is 99 % failure',
                    'Problems are not stop signs, they are guidelines',
                    'What would you do if you were not afraid',
                ]
                print(random.choice(motivated_worlds2))
                incorrect = []
                incorrect.append(current_question)


    if UserInput == 3:
        Standart_jump_for_use = Standart_jump

        for serial_number, number01, sign, number02, equals_sign, answer in Standart_jump_for_use:
            print(number01, sign, number02, equals_sign,  '?')
            current_question = BasicLogicForFirstApp(serial_number, number01, sign, number02, equals_sign, answer)
            question_list.append(current_question)

            if current_question.check_answer(input('What answer?')):
                first_is_correct_some_good_worlds3 = [
                    'Unbelievable!',
                    'Super!',
                    'Wow! Brilliant!',
                    'Amazing!',
                    'Awesome!',
                    'Wonderful',
                    'Perfect',
                    'Cosmically cool!',
                    'Charmingly!',
                    'Adorably!',
                    'Inspiring',
                    'Breathtaking!',
                    'Spectacularly',
                    'It’s impossible!',
                    'It can’t be true!',
                    'I can’t believe it!',
                    'Incredible!',
                    'I’m speechless!',
                    'How amazing!',
                    'I am astounded!',
                    'I am shocked!',
                    'That’s a good one!',
                    'I can’t imagine you did that!',
                    'I’ll believe it when pigs fly!',
                ]
                CountCorrect = True
                print(random.choice(first_is_correct_some_good_worlds3))

            elif current_question.check_answer(input('Try, one more')):
                print('Excellent, Street forward!')

            elif current_question.check_answer(input('Try, last time')):
                print('Good job, Street ahead!')

            else:
                print(number01, sign, number02, equals_sign, answer)

                motivated_worlds3 = [
                    'Do not worry, street ahead!',
                    'Opportunities don’t happen, you create them',
                    'If you do not think about the future, you cannot have one',
                    'Every solution breeds new problems',
                    'If you fall asleep now, you will dream',
                    'If you study now, you will live your dream',
                    'When you think it is too late, the truth is, it is still early',
                    'Studying is not about time.It is about effort',
                    'If you don not walk today, you will have to run tomorrow',
                    'Even now, your enemies are eagerly flipping through books',
                    'Success is walking from failure to failure with no loss of enthusiasm',
                    'Setting goals is the first step in turning the invisible into the visible',
                    'Too many of us are not living our dreams because we are living our fears',
                    'Success is 99 % failure',
                    'Problems are not stop signs, they are guidelines',
                    'What would you do if you were not afraid',
                ]
                print(random.choice(motivated_worlds3))
                incorrect = []
                incorrect.append(current_question)


    if UserInput == 4:
        Professional_jump_for_use = Professional_jump

        for serial_number, number01, sign, number02, equals_sign, answer in Professional_jump_for_use:
            print(number01, sign, number02, equals_sign,  '?')
            current_question = BasicLogicForFirstApp(serial_number, number01, sign, number02, equals_sign, answer)
            question_list.append(current_question)

            if current_question.check_answer(input('What answer?')):
                first_is_correct_some_good_worlds4 = [
                    'Unbelievable!',
                    'Super!',
                    'Wow! Brilliant!',
                    'Amazing!',
                    'Awesome!',
                    'Wonderful',
                    'Perfect',
                    'Cosmically cool!',
                    'Charmingly!',
                    'Adorably!',
                    'Inspiring',
                    'Breathtaking!',
                    'Spectacularly',
                    'It’s impossible!',
                    'It can’t be true!',
                    'I can’t believe it!',
                    'Incredible!',
                    'I’m speechless!',
                    'How amazing!',
                    'I am astounded!',
                    'I am shocked!',
                    'That’s a good one!',
                    'I can’t imagine you did that!',
                    'I’ll believe it when pigs fly!',
                ]
                CountCorrect = True
                print(random.choice(first_is_correct_some_good_worlds4))

            elif current_question.check_answer(input('Try, one more')):
                print('Excellent, Street forward!')

            elif current_question.check_answer(input('Try, last time')):
                print('Good job, Street ahead!')

            else:
                print(number01, sign, number02, equals_sign, answer)

                motivated_worlds4 = [
                    'Do not worry, street ahead!',
                    'Opportunities don’t happen, you create them',
                    'If you do not think about the future, you cannot have one',
                    'Every solution breeds new problems',
                    'If you fall asleep now, you will dream',
                    'If you study now, you will live your dream',
                    'When you think it is too late, the truth is, it is still early',
                    'Studying is not about time.It is about effort',
                    'If you don not walk today, you will have to run tomorrow',
                    'Even now, your enemies are eagerly flipping through books',
                    'Success is walking from failure to failure with no loss of enthusiasm',
                    'Setting goals is the first step in turning the invisible into the visible',
                    'Too many of us are not living our dreams because we are living our fears',
                    'Success is 99 % failure',
                    'Problems are not stop signs, they are guidelines',
                    'What would you do if you were not afraid',
                ]
                print(random.choice(motivated_worlds4))
                incorrect = []
                incorrect.append(current_question)


    if UserInput == 5:
        Hardcore_jump_for_use = Hardcore_jump

        for serial_number, number01, sign, number02, equals_sign, answer in Hardcore_jump_for_use:
            print(number01, sign, number02, equals_sign,  '?')
            current_question = BasicLogicForFirstApp(serial_number, number01, sign, number02, equals_sign, answer)
            question_list.append(current_question)

            if current_question.check_answer(input('What answer?')):
                first_is_correct_some_good_worlds5 = [
                    'Unbelievable!',
                    'Super!',
                    'Wow! Brilliant!',
                    'Amazing!',
                    'Awesome!',
                    'Wonderful',
                    'Perfect',
                    'Cosmically cool!',
                    'Charmingly!',
                    'Adorably!',
                    'Inspiring',
                    'Breathtaking!',
                    'Spectacularly',
                    'It’s impossible!',
                    'It can’t be true!',
                    'I can’t believe it!',
                    'Incredible!',
                    'I’m speechless!',
                    'How amazing!',
                    'I am astounded!',
                    'I am shocked!',
                    'That’s a good one!',
                    'I can’t imagine you did that!',
                    'I’ll believe it when pigs fly!',
                ]
                CountCorrect = True
                print(random.choice(first_is_correct_some_good_worlds5))

            elif current_question.check_answer(input('Try, one more')):
                print('Excellent, Street forward!')

            elif current_question.check_answer(input('Try, last time')):
                print('Good job, Street ahead!')

            else:
                print(number01, sign, number02, equals_sign, answer)

                motivated_worlds5 = [
                    'Do not worry, street ahead!',
                    'Opportunities don’t happen, you create them',
                    'If you do not think about the future, you cannot have one',
                    'Every solution breeds new problems',
                    'If you fall asleep now, you will dream',
                    'If you study now, you will live your dream',
                    'When you think it is too late, the truth is, it is still early',
                    'Studying is not about time.It is about effort',
                    'If you don not walk today, you will have to run tomorrow',
                    'Even now, your enemies are eagerly flipping through books',
                    'Success is walking from failure to failure with no loss of enthusiasm',
                    'Setting goals is the first step in turning the invisible into the visible',
                    'Too many of us are not living our dreams because we are living our fears',
                    'Success is 99 % failure',
                    'Problems are not stop signs, they are guidelines',
                    'What would you do if you were not afraid',
                ]
                print(random.choice(motivated_worlds5))
                incorrect = []
                incorrect.append(current_question)



    # далее строительный мусор ))))))))

    """Class to calculate of user behavior"""
    """
    def __init__(self, number_of_correct_answers, number_of_incorrect_answers, amount_of_time_spent_on_one_example,
                 amount_of_time_spent_on_one_section):
        self.number_of_correct_answers = number_of_correct_answers
        self.number_of_incorrect_answers = number_of_incorrect_answers
        self.amount_of_time_spent_on_one_example = amount_of_time_spent_on_one_example
        self.amount_of_time_spent_on_one_section = amount_of_time_spent_on_one_section
    """

    #        while not current_question.check_answer(input('Enter answer, please')):
    #            print('This is not correct answer, try one more')9