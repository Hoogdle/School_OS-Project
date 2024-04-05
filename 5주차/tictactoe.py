### 프로그램명 : 틱텍토
### 작성자 : 김태영

### 사용자가 O, 컴퓨터가 X로 가정
### 사용자가 먼저 선공한다고 가정

import numpy as np # 2차원 배열을 사용하기위한 넘파이 라이브러리 
import random # 컴퓨터의 동작을 위한 랜덤 숫자 받기

area = np.zeros((3,3),dtype='int32') # O와 X가 들어갈 배열(O대신 1, X대신 2가 들어감)
area_show = np.array([[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]) # 출력용도로 사용할 배열
possible_area = [[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]] # 수를 둘 때 마다 해당 수 인덱스의 요소 삭제
possible_index = 9 # 남은 칸 확인
print(area_show)


def check_for_end(): # 게임이 끝나는 조건을 확인하기 위한 함수
    temp_u = np.array([1,1,1]) # 사용자가 이기는 경우
    temp_c = np.array([2,2,2]) # 컴퓨터가 이기는 경우
    diagonal_l2r = np.array([area[0][0],area[1][1],area[2][2]]) # area 배열의 대각선(왼->오)
    diagonal_r2l = np.array([area[0][2],area[1][1],area[2][0]]) # area 배열의 대각선(오->왼)

    if np.array_equal(diagonal_l2r,temp_u): # 행이 빙고인 경우 확인
            print('사용자 승리!')
            exit()
    elif np.array_equal(diagonal_l2r,temp_c):
            print('컴퓨터 승리!')
            exit()
    elif np.array_equal(diagonal_r2l,temp_u):
            print('사용자 승리!')
            exit()
    elif np.array_equal(diagonal_r2l,temp_c):
            print('컴퓨터 승리!')
            exit()

    for i in range(3):
        if np.array_equal(area[i],temp_u): #열이 빙고인 경우 확인
            print('사용자 승리!')
            exit()
        elif np.array_equal(area[i],temp_c):
            print('컴퓨터 승리!')
            exit()
        elif np.array_equal(area[:,i],temp_u):
            print('사용자 승리!')
            exit()
        elif np.array_equal(area[:,i],temp_c):
            print('컴퓨터 승리!')
            exit()
    if np.count_nonzero(area) == 9: # 칸이 모두 찬 경우, 무승부로 판결(칸이 모두 찼을 때 승자가 발생하면 위의 조건에서 먼저 처리됨.)
          print('무승부입니다!')
          exit()
    

def put_the_token(): # 각 자 말을 두게 해주는 함수
    global possible_index # 함수 외의 영역에 선언된 변수를 변경하기 위한 global 키워드
    x,y = map(int,input("사용자의 차례입니다. 빈칸 중'O'를 넣을 위치를 입력하세요 : ").split()) # 사용자가 말을 둘 위치 받기
    possible_area.remove([x,y]) # 사용자에게 입력 받은 말의 위치 정보를 전역에 선언된 인덱스 리스트에서 제거
    area[x][y] = 1 # 입력 받은 위치정보로 바둑판 갱신
    area_show[x][y] = 'O' # 출력을 위한 바둑판 갱신
    possible_index -= 1 # 남은 칸수 1개 줄이기
    if possible_index == 0: # 만약 칸수가 0개인 경우 종료 조건을 검사하여 각 상황에 맞게 게임 종료하기
        check_for_end()
        print('무승부입니다!')
        exit()
    index = random.randrange(0,possible_index) # 남은 칸 수를 범위로 하여 랜덤하게 숫자 한 개 선택
    value = possible_area.pop(index) # 해당 숫자의 해당하는 인덱스를 하나 빼오기
    possible_index -= 1 # 남은 칸수 1개 줄이기
    x_c, y_c = value[0],value[1] # 랜덤하게 뽑힌 위치 정보 받기
    area[x_c][y_c] = 2 # 입력 받은 위치정보로 바둑판 갱신
    area_show[x_c][y_c] = 'X' # 출력을 위한 바둑판 갱신
    
 
def show():
     print(area_show) # 출력을 위한 바둑판 보여주기

while(True):
    check_for_end() # 종료 조건 검사
    put_the_token() # 말 두기
    show() # 판 보여주기
    
    
    