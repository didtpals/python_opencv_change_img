import cv2
import sys # 프로그램을 종료주기 위해 import한 sys 라이브러리 ( 따로 pip install 해줄 필요는 없음 )
           
def ReadDefaultImg():
    img = cv2.imread("img.jpg")
  
    cv2.imshow('jeongho', img)

def ReadReducedGrayImg():
    img = cv2.imread("img.jpg", cv2.IMREAD_GRAYSCALE)
  
    cv2.imshow('jeongho', img)

def ReadReducedGrayScale2Img():
    img = cv2.imread("img.jpg", cv2.IMREAD_REDUCED_GRAYSCALE_2)
  
    cv2.imshow('jeongho', img)
    
def ReadReducedReverseImg():
    img = cv2.imread("img.jpg")
    img = cv2.flip(img, 1) # flip 함수를 사용해 좌우를 뒤집음

    cv2.imshow('jeongho', img)

def ReadReducedLineImg():
    img = cv2.imread("img.jpg")
    img = cv2.Canny(img, 50, 100) # Canny 함수를 사용해 털 하나하나 세세히 윤곽선을 그림

    cv2.imshow('jeongho', img)

def ReadReduceCuttingImg():
    img = cv2.imread("img.jpg") 
    cv2.imshow('jeongho', img) # 원본 이미지 출력

    gray_img = cv2.imread("img.jpg", cv2.IMREAD_GRAYSCALE)

    img = img[100:300, 100:400] # 이미지의 세로, 가로 범위를 설정해주고 표시하면 설정한 범위만큼 이미지 출력
    cv2.imshow('1_cutting_jeongho', img)

    gray_img = gray_img[300:500, 100:400]
    cv2.imshow('2_cutting_jeongho', gray_img)

def ReadReduceBlurImg():
    img = cv2.imread("img.jpg")
    img = cv2.GaussianBlur(img, (29,29),0) # GaussianBlur 함수를 사용해 이미지의 선명도를 바꿔줌

    cv2.imshow('jeongho', img)

def Cv1MeanImg():
    img = cv2.imread("whatiscv.jpg") # OpenCV에 CV의 의미 이미지
    cv2.imshow('jeongho', img)

def Cv2MeanImg():
    img = cv2.imread("CV.jpg")
    cv2.imshow('jeongho', img)

def EventSwitch(key):
    if key == -1:
        cv2.destroyAllWindows()
        sys.exit()

    # 변수 안에 들어간 키의 값은 ascii code로 (아스키 코드) 이는 미국 ANSI 에서 만든 표준 코드 체계, 주로 통신용 코드에 사용 

    # ascii code에서 97은 소문자 a ( 기본 이미지를 읽어오는 함수를 실행 )
    elif key == 97:
        ReadDefaultImg()

    # ascii code에서 98은 소문자 b ( 이미지를 회색, 흑백으로 읽어오는 함수를 실행 )
    elif key == 98:
        ReadReducedGrayImg()

    # ascii code에서 99은 소문자 c ( 이미지를 원래 이미지 크기에서 반으로 작아직 회색, 흑백으로 읽어오는 함수를 실행 )
    elif key == 99:
        ReadReducedGrayScale2Img()

    # ascii code에서 100은 소문자 d ( 이미지를 반대로 뒤집어 이미지를 보여주는 함수를 실행 )
    elif key == 100:
        ReadReducedReverseImg()

    # ascii code에서 101은 소문자 e ( 이미지에 윤곽선을 그린 이미지를 보여주는 함수를 실행 )
    elif key == 101:
        ReadReducedLineImg()

    # ascii code에서 102은 소문자 f ( 이미지를 잘라서 보여주는 함수를 실행 )
    elif key == 102:
        ReadReduceCuttingImg()

    # ascii code에서 103은 소문자 g ( 이미지를 흐리게 만들어 보여주는 함수를 실행 )
    elif key == 103:
        ReadReduceBlurImg()

    elif key == 104:
        Cv1MeanImg()

    elif key == 105:
        Cv2MeanImg()

    # 지정된 키가 없으면 바로 exit 함수를 사용해 프로그램 강제 종료
    else:
        cv2.destroyAllWindows()
        sys.exit()

ReadDefaultImg() # 처음 반복문이 실행되기 전에 최초로 1번 이미지를 그려줌

while True:
    # EnterKeyEvent라는 함수를 만들어 어느 키를 누르면 그 키의 값이 key_down_value 변수 안에 들어감
    # 또한 EventSwitch 함수에 지정된 key가 아닐경우 프로그램은 종료.  
    key_down_value = cv2.waitKeyEx(0) # waitKeyEx 함수는 특정 키가 입력될 때까지 무한정 멈춤

    cv2.destroyAllWindows() # 계속 쌓이는 이미지를 꺼주기 위함

    EventSwitch(key_down_value) # key_down_value 변수를 EventSwitch라는 함수에 key_down_value를 인자로 보내주면 해당 함수에서는 받은 값에 따른 특정 동작을 하게 됨





# ____--------------------------________--------------------------________--------------------------________--------------------------________--------------------------________--------------------------________--------------------------____

# ReadDefaultImg() # 처음 반복문이 실행되기 전에 최초로 1번 이미지를 그려줌

# while True
    # 키 입력 대기
    # 키 입력 받으면 이미지 지움
    # 입력 받은 키를 확인해 이미지 표시

    # 키 입력 대기
    # 키 입력 받으면 이미지 지움
    # 입력 받은 키를 확인해 이미지 표시

    # 키 입력 대기
    # 키 입력 받으면 이미지 지움
    # 입력 받은 키를 확인해 이미지 표시

    # 키 입력 대기
    # 키 입력 받으면 이미지 지움
    # 입력 받은 키를 확인해 이미지 표시

    # 키 입력 대기
    # 키 입력 받으면 이미지 지움
    # 입력 받은 키를 확인해 이미지 표시