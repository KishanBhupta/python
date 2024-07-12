"""
create a dictonary/list of the detail of the student with following operations 
1 add details of the student 
2 show the details of the student 
3 serch student by the student no 
4 find the avg marks and sort into the bubble sort 
5 exit 
"""
studentDictonry = {}
avgDictonary = {}
listAvg=[]
studentList = [{'no': 10, 'name': 'kb', 'marks': [90, 95, 70, 80]}, {'no': 20, 'name': 'mkb', 'marks': [90, 60, 50, 70]},{'no': 30, 'name': 'mkb', 'marks': [90, 60, 70, 80]}]
while True :
    print("1. Add the student \n 2. show detail of the student \n 3. search the student data \n 4. avg marks with sorting \n 5.exit  ")
    chooseOption = int(input("please choose any number :"))

    # add the data of the student 
    if chooseOption == 1:
        studentMarks = []
        
        studentNo = int(input("Enter a student no :"))
        studentName = input("Enter name of student :")
        for i in range(1,4):
            marks = int(input("Enter a marks :"))
            studentMarks.append(marks)
        
        studentDictonry = {"no":studentNo , "name":studentName , "marks":studentMarks}
        studentList.append(studentDictonry)
        
    # show the data in the list 
    
    elif chooseOption == 2:
       for i in studentList :
           print(i)
           
    elif chooseOption == 3:
        searchStudent = int(input("Enter a student number :"))
        for i in range(len(studentList)) :
               if(searchStudent == studentList[i]["no"]):
                   print(studentList[i])
                   
    elif chooseOption == 4:
        for i in range(len(studentList)):
            # print(studentList[i]["marks"])
            total = 0
            for j in range(len(studentList[i]["marks"])):
               total += studentList[i]["marks"][j]
            avg = total/3
            avgMarks = float("%.2f"%avg)
            avgDictonary = {"no":studentList[i]["no"],"avgmarks":avgMarks}
            listAvg.append(avgDictonary)

            for i in range(len(listAvg)):
                for j in range(len(listAvg)-i-1):
                    if(listAvg[j]["avgmarks"]<listAvg[j+1]["avgmarks"]):
                        listAvg[j] , listAvg[j+1] =listAvg[j+1] , listAvg[j]   
            print(listAvg)
    elif chooseOption ==5:
        break 