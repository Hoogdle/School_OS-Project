# 프로그램명 : 학점관리프로그램(객체지향)
# 작성자 : 김태영




class Grade_Management:
    def __init__(self,size=5):
        self.size_of_student = size # default로 받는 학생수
        self.name = [] # 학생의 이름 리스트
        self.id = [] # 학번 리스트
        self.total = [] # 총합점수 리스트
        self.mean = [] # 평균 리스트
        self.eng = []
        self.c = []
        self.python = []
        self.grade= [] # 성적 리스트
        self.rank= [1]*5 # 등수 리스트
    
    def input_data(self,nums = 5): # 학생 정보를 입력받는 함수
        for i in range(nums):
            print('학생의 이름을 입력하세요 :',end='')
            temp = input()
            self.name.append(temp) # 학생의 이름을 입력받아 name리스트에 저장
            print('학번을 입력하세요:',end='')
            temp = input()
            self.id.append(temp) # 학생의 학번을 입력받아 id리스트에 저장
            self.input_score()
    
    
    def input_score(self):
        temp = 0
        
        print('영어 점수를 입력하세요 :',end='')
        a = int(input())
        self.eng.append(a)
        temp += a
        print('C-언어 점수를 입력하세요 :',end='')
        a = int(input())
        self.c.append(a)
        temp += a
        print('파이썬 점수를 입력하세요 :',end='')
        a = int(input())
        self.python.append(a)
        temp += a # 국어,영어,수학 점수를 모두 총합하여 total리스트에 저장
        self.mean.append(temp/3) # total리스트의 점수를 과목수로 나눠 평균 mean리스트에 저장
        self.total.append(temp)

        
    def process_grade(self):
        for i in range(self.size_of_student):
            if self.mean[i] >= 90:
                self.grade.append('A')
            elif 80 <= self.mean[i] < 90:
                self.grade.append('B')
            elif 70 <= self.mean[i] < 80:
                self.grade.append('C')
            else:
                self.grade.append('F') # 평균에 따른 학점 부여
    

    def process_ranking(self):
        for i in range(4):
            for j in range(i,5):
                if self.total[i]<self.total[j]:
                    self.rank[i] += 1
                elif self.total[i]>self.total[j]:
                    self.rank[j] += 1
                else:
                    pass # 등수 생성 알고리즘

    def process_reranking(self):
        # global rank
        self.rank = [1]*self.size_of_student
        for i in range(self.size_of_student-1):
            for j in range(i,self.size_of_student):
                if self.total[i]<self.total[j]:
                    self.rank[i] += 1
                elif self.total[i]>self.total[j]:
                    self.rank[j] += 1
                else:
                    pass # 새로운 학생이 들어왔을 때, 등수 생성 알고리즘




    def output(self): #출력함수
        print('='*70)
        print(f'학번    이름    영어    C-언어  파이썬  총점    평균    학점    등수')
        print('='*70)
        for i in range(self.size_of_student):
            print(f'{self.id[i]:<10} {self.name[i]:<10} {self.eng[i]:<10} {self.c[i]:<10} {self.python[i]:<10} {self.total[i]:<10} {self.mean[i]:<10.2f} {self.grade[i]:<10} {self.rank[i]:<10}')

    ### 삽입함수 ###
    def insert_data(self):
        #global size_of_student
        self.size_of_student += 1
        # print(self.size_of_student)
        self.input_data(nums=1)
        if self.mean[self.size_of_student-1] >= 90:
            self.grade.append('A')
        elif 80 <= self.mean[self.size_of_student-1] < 90:
            self.grade.append('B')
        elif 70 <= self.mean[self.size_of_student-1] < 80:
            self.grade.append('C')
        else:
            self.grade.append('F') # 평균에 따른 학점 부여
        self.process_reranking()
        


    ### 삭제함수 ###
    def delete_data(self):
        # global size_of_student
        index = int(self.search_data())
        self.size_of_student -= 1
        del self.name[index] 
        del self.id[index] 
        del self.total[index] 
        del self.mean[index] 
        del self.eng[index]
        del self.c[index]
        del self.python[index]
        del self.grade[index]
        del self.rank[index]
        self.process_reranking()





    ### 탐색함수 ###
    def search_data(self):
        num_name = list(input('학번과 이름을 입력하세요').split())
        for i in range(self.size_of_student):
            if self.name[i] == num_name[0] and self.id[i] == num_name[1]:
                return i


    ### 정렬함수 ###
    def sorting(self):
        # global name,id,total,mean,eng,c,python,grade,rank
        new_name = [] # 학생의 이름 리스트
        new_id = [] # 학번 리스트
        new_total = [] # 총합점수 리스트
        new_mean = [] # 평균 리스트
        new_eng = []
        new_c = []
        new_python = []
        new_grade= [] # 성적 리스트
        new_rank= [] # 등수 리스트
        temp = list(enumerate(self.total))
        temp = sorted(temp,key = lambda x : x[1],reverse=True)
        for i in range(self.size_of_student):
            new_name.append(self.name[temp[i][0]])
            new_id.append(self.id[temp[i][0]])
            new_total.append(self.total[temp[i][0]])
            new_mean.append(self.mean[temp[i][0]])
            new_eng.append(self.eng[temp[i][0]])
            new_c.append(self.c[temp[i][0]])
            new_python.append(self.python[temp[i][0]])
            new_grade.append(self.grade[temp[i][0]])
            new_rank.append(self.rank[temp[i][0]])
        self.name = new_name
        self.id = new_id
        self.total = new_total
        self.mean = new_mean
        self.eng = new_eng
        self.c = new_c
        self.python = new_python
        self.grade = new_grade
        self.rank = new_rank
            

    


    ### 80점 이상 학생 카운트 함수 ###
    def counter(self):
        temp = 0
        for i in range(self.size_of_student):
            if self.total[i] >= 80:
                temp += 1
        print('80점 이상의 학생은 ',temp,'명 입니다.')
        


Manager = Grade_Management(5)

Manager.input_data()
Manager.process_grade()
Manager.process_ranking()
Manager.output()
Manager.insert_data()
Manager.output()
Manager.sorting()
Manager.output()
Manager.counter()
Manager.delete_data()
Manager.output()
# input_data()
# process_grade()
# process_ranking()
# output()
# delete_data()
# output()
# insert_data()
# output()
# sorting()
# output()
# counter()

