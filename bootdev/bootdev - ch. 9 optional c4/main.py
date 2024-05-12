def get_test_score(answer_sheet, student_answers):


    new_student_answers = student_answers[1:len(student_answers)]


    correct_count = 0
    wrong_count = 0
    final_percentage: float

    for i in range(len(answer_sheet)):
        if answer_sheet[i] == new_student_answers[i]:
            correct_count += 1
        else:
            wrong_count += 1

    if wrong_count == 0:
        final_percentage = float(100)

    if wrong_count > 0:
        final_percentage = 100 - ((wrong_count / (len(answer_sheet))) * 100)

    
    

#    print(f"asnwer sheet is {answer_sheet}, student answers is {student_answers}, new student answers is {new_student_answers}")    

    name = student_answers[0]
    print(f"name is {name}")
    return name, final_percentage
    
    pass



#def get_test_score(answer_sheet, student_answers):

 #   correct_count = 0
 #   wrong_count = 0
 #   final_percentage: float

#    for i in range(len(answer_sheet)):
#        if answer_sheet[i] == student_answers[i]:
#            correct_count += 1
#        else:
#            wrong_count += 1

#    if wrong_count == 0:
#        return float(100)

#    if wrong_count > 0:
#        final_percentage = 100 - ((wrong_count / (len(answer_sheet))) * 100)

#    print(f"correct count is {correct_count}, wrong count is {wrong_count}, and final percent is {final_percentage}")
        

#    return final_percentage

