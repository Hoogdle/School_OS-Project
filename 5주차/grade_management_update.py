# 프로그램명 : 학점관리프로그램
# 작성자 : 김태영

size_of_student = 5 # default로 받는 학생수
name = [] # 학생의 이름 리스트
id = [] # 학번 리스트
total = [] # 총합점수 리스트
mean = [] # 평균 리스트
eng = []
c = []
python = []
grade= [] # 성적 리스트
rank= [1]*5 # 등수 리스트

def input_data(nums = 5): # 학생 정보를 입력받는 함수
    
    for i in range(nums):
        print('학생의 이름을 입력하세요 :',end='')
        temp = input()
        name.append(temp) # 학생의 이름을 입력받아 name리스트에 저장
        print('학번을 입력하세요:',end='')
        temp = input()
        id.append(temp) # 학생의 학번을 입력받아 id리스트에 저장
        input_score()
        


def input_score():
    temp = 0
    
    print('영어 점수를 입력하세요 :',end='')
    a = int(input())
    eng.append(a)
    temp += a
    print('C-언어 점수를 입력하세요 :',end='')
    a = int(input())
    c.append(a)
    temp += a
    print('파이썬 점수를 입력하세요 :',end='')
    a = int(input())
    python.append(a)
    temp += a # 국어,영어,수학 점수를 모두 총합하여 total리스트에 저장
    mean.append(temp/3) # total리스트의 점수를 과목수로 나눠 평균 mean리스트에 저장
    total.append(temp)

def process_grade():
    for i in range(size_of_student):
        if mean[i] >= 90:
            grade.append('A')
        elif 80 <= mean[i] < 90:
            grade.append('B')
        elif 70 <= mean[i] < 80:
            grade.append('C')
        else:
            grade.append('F') # 평균에 따른 학점 부여
    

def process_ranking():
    for i in range(4):
        for j in range(i,5):
            if total[i]<total[j]:
                rank[i] += 1
            elif total[i]>total[j]:
                rank[j] += 1
            else:
                pass # 등수 생성 알고리즘

def process_reranking():
    global rank
    rank = [1]*size_of_student
    for i in range(size_of_student-1):
        for j in range(i,size_of_student):
            if total[i]<total[j]:
                rank[i] += 1
            elif total[i]>total[j]:
                rank[j] += 1
            else:
                pass # 새로운 학생이 들어왔을 때, 등수 생성 알고리즘




def output(): #출력함수
    print('='*70)
    print(f'학번    이름    영어    C-언어  파이썬  총점    평균    학점    등수')
    print('='*70)
    for i in range(size_of_student):
        print(f'{id[i]:<10} {name[i]:<10} {eng[i]:<10} {c[i]:<10} {python[i]:<10} {total[i]:<10} {mean[i]:<10.2f} {grade[i]:<10} {rank[i]:<10}')

### 삽입함수 ###
def insert_data():
    global size_of_student
    size_of_student += 1
    input_data(nums=1)
    if mean[size_of_student-1] >= 90:
        grade.append('A')
    elif 80 <= mean[size_of_student-1] < 90:
        grade.append('B')
    elif 70 <= mean[size_of_student-1] < 80:
        grade.append('C')
    else:
        grade.append('F') # 평균에 따른 학점 부여
    process_reranking()
    


### 삭제함수 ###
def delete_data():
    global size_of_student
    size_of_student -= 1
    index = int(search_data())
    del name[index] 
    del id[index] 
    del total[index] 
    del mean[index] 
    del eng[index]
    del c[index]
    del python[index]
    del grade[index]
    del rank[index]
    process_reranking()





### 탐색함수 ###
def search_data():
    num_name = list(input('학번과 이름을 입력하세요').split())
    for i in range(size_of_student):
        if name[i] == num_name[0] and id[i] == num_name[1]:
            return i


### 정렬함수 ###
def sorting():
    global name,id,total,mean,eng,c,python,grade,rank
    new_name = [] # 학생의 이름 리스트
    new_id = [] # 학번 리스트
    new_total = [] # 총합점수 리스트
    new_mean = [] # 평균 리스트
    new_eng = []
    new_c = []
    new_python = []
    new_grade= [] # 성적 리스트
    new_rank= [] # 등수 리스트
    temp = list(enumerate(total))
    temp = sorted(temp,key = lambda x : x[1],reverse=True)
    for i in range(size_of_student):
        new_name.append(name[temp[i][0]])
        new_id.append(id[temp[i][0]])
        new_total.append(total[temp[i][0]])
        new_mean.append(mean[temp[i][0]])
        new_eng.append(eng[temp[i][0]])
        new_c.append(c[temp[i][0]])
        new_python.append(python[temp[i][0]])
        new_grade.append(grade[temp[i][0]])
        new_rank.append(rank[temp[i][0]])
    name = new_name
    id = new_id
    total = new_total
    mean = new_mean
    eng = new_eng
    c = new_c
    python = new_python
    grade = new_grade
    rank = new_rank
        

    


### 80점 이상 학생 카운트 함수 ###
def counter():
    temp = 0
    for i in range(size_of_student):
        if total[i] >= 80:
            temp += 1
    print('80점 이상의 학생은 ',temp,'명 입니다.')


### 실행 결과
input_data()
process_grade()
process_ranking()
output()
delete_data()
output()
insert_data()
output()
sorting()
output()
counter()







    
    
    




    
        





