# 프로그램명 : 학점관리프로그램
# 작성자 : 김태영

name = [] # 학생의 이름 리스트
id = [] # 학번 리스트
total_list = [0]*5 # 총합점수 리스트
mean_list = [] # 평균 리스트
grade_list = [] # 성적 리스트
th_list = [1]*5 # 등수 리스트


for i in range(5):
    print('학생의 이름을 입력하세요 :',end='')
    temp = input()
    name.append(temp) # 학생의 이름을 입력받아 name리스트에 저장
    print('학번을 입력하세요:',end='')
    temp = input()
    id.append(temp) # 학생의 학번을 입력받아 id리스트에 저장
    print('국어 점수를 입력하세요 :',end='')
    a = int(input())
    total_list[i] += a
    print('영어 점수를 입력하세요 :',end='')
    a = int(input())
    total_list[i] += a
    print('수학 점수를 입력하세요 :',end='')
    a = int(input())
    total_list[i] += a # 국어,영어,수학 점수를 모두 총합하여 total리스트에 저장
    mean_list.append(total_list[i]/3) # total리스트의 점수를 과목수로 나눠 평균 mean리스트에 저장
    if mean_list[i] >= 90:
        grade_list.append('A')
    elif 80 <= mean_list[i] < 90:
        grade_list.append('B')
    elif 70 <= mean_list[i] < 80:
        grade_list.append('C')
    else:
        grade_list.append('F') # 평균에 따른 학점 부연
    
for i in range(4):
    for j in range(i,5):
        if total_list[i]<total_list[j]:
            th_list[i] += 1
        elif total_list[i]>total_list[j]:
            th_list[j] += 1
        else:
            pass # 등수 생성 알고리즘

for i in range(5): # 표로 출력
    print('==================')
    print(f'{name[i]} : {id[i]} 학생의 total : {total_list[i]}')
    print(f'{name[i]} : {id[i]} 학생의 mean : {mean_list[i]}')
    print(f'{name[i]} : {id[i]} 학생의 grade : {grade_list[i]}')
    print(f'{name[i]} : {id[i]} 학생의 등수 : {th_list[i]}')
    
    
    




    
        





