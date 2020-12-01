import random
import operator

def create_outline():
    '''
    TODO: implement your code here
    '''
   
    course_topics = ['* Introduction to Python','* Tools of the Trade','* How to make decisions','* How to repeat code','* How to structure data','* Functions','* Modules']
    #topics = list(course_topics)
    course_topics.sort()

    #status = (['[STARTED]','[GRADED]','[COMPLETED]'])
   

    #status.sort(key= operator.itemgetter(0))
    print("Course Topics:")
    
    for course in course_topics:
        print(course)
  
    print("Problems:")
    maps = dict()
    for x in course_topics:
        maps[x] = ["Problem 1","Problem 2" ,"Problem 3"]
    for x in course_topics:
        print(f"{x} : ",end='')
        for i in range(3):
            if i == 2:
                print(f"{maps[x][i]}")
            else:
                print(f"{maps[x][i]}, ",end='')

    print("Student Progress:")
    course_topics = ([' Introduction to Python',' Tools of the Trade',' Tools of the Trade',' How to make decisions',' How to repeat code',' How to structure data',' Functions',' Modules']) 
    status = ['[STARTED]','[GRADED]','[COMPLETED]']
    problems = ["Problem 1","Problem 2" ,"Problem 3"]
    student_info = [("Hank" ,course_topics[1],problems[2],status[0]),
                    ("Xavier",course_topics[3],problems[0],status[0]),
                    ("SCarlet",course_topics[0],problems[0],status[1]),
                    ("Tchalla",course_topics[2],problems[1],status[2])]
    i = 1
    status = sorted(status, key=operator.itemgetter(0))
    for name,topic, problem,progress in student_info:
        #problem = sorted(status, key=operator.itemgetter(0))
        print(f"{i}. ",name , "-" ,topic , "-" ,problem," " ,progress )
        i += 1
    
    # new_list = sorted(status, key=operator.itemgetter(0))

if __name__ == '__main__':
    create_outline()