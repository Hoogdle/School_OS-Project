# 프로그램명 : 학점관리프로그램
# 작성자 : 김태영


def input_data(): # 학생 정보를 입력받는 함수
    name = [] # 학생의 이름 리스트
    id = [] # 학번 리스트
    total_list = [] # 총합점수 리스트
    mean_list = [] # 평균 리스트
    eng_list = []
    c_list = []
    python_list = []
    
    for i in range(5):
        print('학생의 이름을 입력하세요 :',end='')
        temp = input()
        name.append(temp) # 학생의 이름을 입력받아 name리스트에 저장
        print('학번을 입력하세요:',end='')
        temp = input()
        id.append(temp) # 학생의 학번을 입력받아 id리스트에 저장
        total,mean,eng,c,python = input_score()
        total_list.append(total)
        mean_list.append(mean)
        eng_list.append(eng)
        c_list.append(c)
        python_list.append(python)

    return name,id,total_list,mean_list,eng_list,c_list,python_list

def input_score():
    total_list = 0
    mean_list = 0
    eng_list = 0
    c_list = 0
    python_list = 0

    
    print('영어 점수를 입력하세요 :',end='')
    a = int(input())
    eng_list = a
    total_list += a
    print('C-언어 점수를 입력하세요 :',end='')
    a = int(input())
    c_list = a
    total_list += a
    print('파이썬 점수를 입력하세요 :',end='')
    a = int(input())
    python_list = a
    total_list += a # 국어,영어,수학 점수를 모두 총합하여 total리스트에 저장
    mean_list = (total_list/3) # total리스트의 점수를 과목수로 나눠 평균 mean리스트에 저장

    return total_list,mean_list,eng_list,c_list,python_list

def process_grade(mean):
    grade_list = [] # 성적 리스트
    for i in range(5):
        if mean[i] >= 90:
            grade_list.append('A')
        elif 80 <= mean[i] < 90:
            grade_list.append('B')
        elif 70 <= mean[i] < 80:
            grade_list.append('C')
        else:
            grade_list.append('F') # 평균에 따른 학점 부연
    return grade_list

def process_ranking(total):
    th_list = [1]*5 # 등수 리스트
    for i in range(4):
        for j in range(i,5):
            if total[i]<total[j]:
                th_list[i] += 1
            elif total[i]>total[j]:
                th_list[j] += 1
            else:
                pass # 등수 생성 알고리즘

    return th_list

def output(id,name,eng,c,python,total,mean,grade,ranking): #출력함수
    print('='*70)
    print(f'학번    이름    영어    C-언어  파이썬  총점    평균    학점    등수')
    print('='*70)
    for i in range(5):
        print(f'{id[i]:<10} {name[i]:<10} {eng[i]:<10} {c[i]:<10} {python[i]:<10} {total[i]:<10} {mean[i]:<10.2f} {grade[i]:<10} {ranking[i]:<10}')


name,id,total,mean,eng,c,python = input_data() # 입력함수로 정보를 입력 받는다
grade = process_grade(mean) # 평균으로 grade를 계산한다
rank = process_ranking(total) # 총합으로 랭킹을 계산한다
output(id,name,eng,c,python,total,mean,grade,rank) #출력한다



    
    
    




    
        





