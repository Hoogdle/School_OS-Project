### Program name : Grade Management
### 작성자 : 김태영

### 5명의 학생의 정보를 넣기 위한 dictionary 선언 ###
database = []

### 입력함수 ###
def get_data():
    for i in range(5):
        data = list(input('학번,이름,영어점수,C-언어 점수,파이썬 점수를 입력하세요.').split())
        # 학번 : 0 / 이름 : 1 / 영어 점수 : 2 / C-언어 점수 : 3 / 파이썬 점수 : 4 
        database.append(data)
################

### 총점/평균 계산 함수 ###
def cal_total_mean(database):
    for i in range(5):
        total = database[i][2] + database[i][3] + database[i][4]
        mean = total/3
        database[i].append(total,mean) # total,5 / mean,6
################

### 학점 계산 함수 ###
def cal_grade(database):
    for i in range(5):
        if database[i][6] > 90:
            database[i].append('A')
        elif 80<= database[i][6] < 90:
            database[i].append('B')
        elif 70<= database[i][6] < 80:
            database[i].append('C')
        else:
            database[i].append('F')
################

### 등수 계산 함수 ###
def cal_rank(database):
    temp = 1 # 등수 리스트
    for i in range(4):
        for j in range(i,5):
            if database[i][5]<database[j][5]:
                temp += 1
            elif database[i][5]>database[j][5]:
                temp += 1
            else:
                pass # 등수 생성 알고리즘
        database[i].append(temp) # rank, 7
        temp = 1
################


### 삭제 함수 ###
def remove_info(database):
    print('학생의 이름을 입력하세요')
    name = input()
    for i in range(5):
        if name == database[i][1]:
            del database[i]
################





    


            
 





