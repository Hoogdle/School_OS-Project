### Program name : Grade Management
### �ۼ��� : ���¿�

### 5���� �л��� ������ �ֱ� ���� dictionary ���� ###
database = []

### �Է��Լ� ###
def get_data():
    for i in range(5):
        data = list(input('�й�,�̸�,��������,C-��� ����,���̽� ������ �Է��ϼ���.').split())
        # �й� : 0 / �̸� : 1 / ���� ���� : 2 / C-��� ���� : 3 / ���̽� ���� : 4 
        database.append(data)
################

### ����/��� ��� �Լ� ###
def cal_total_mean(database):
    for i in range(5):
        total = database[i][2] + database[i][3] + database[i][4]
        mean = total/3
        database[i].append(total,mean) # total,5 / mean,6
################

### ���� ��� �Լ� ###
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

### ��� ��� �Լ� ###
def cal_rank(database):
    temp = 1 # ��� ����Ʈ
    for i in range(4):
        for j in range(i,5):
            if database[i][5]<database[j][5]:
                temp += 1
            elif database[i][5]>database[j][5]:
                temp += 1
            else:
                pass # ��� ���� �˰���
        database[i].append(temp) # rank, 7
        temp = 1
################


### ���� �Լ� ###
def remove_info(database):
    print('�л��� �̸��� �Է��ϼ���')
    name = input()
    for i in range(5):
        if name == database[i][1]:
            del database[i]
################





    


            
 





