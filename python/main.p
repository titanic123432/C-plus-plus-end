from tkinter import *
from court import *                       # 사용자 정의 court 모듈 불러오기
from ball import *                        # 사용자 정의 ball 모듈 불러오기
from racket import*

# 윈도 창과 캔버스의 가로, 세로 길이
width, height = 745, 374

win = Tk()
win.title("Tennis Game")
win.geometry("745x374+150+150")
win.resizable(False, False)

# Court 클래스 생성
court = Court(win, width, height, "court.png")                                    

# 공의 좌표를 캔버스의 중앙으로 저장
x1, y1 = width / 2, height / 2
x2, y2 = x1 + 30, y1 + 30

# Ball 클래스 생성
ball = Ball(court, x1, y1, x2, y2)         
                       
# 게임 진행 함수 정의 
def play_game() :
    global wineer

    #배트와 공이 충돌
    red_racket.dectect_collision(ball)
    green_racket.dectect_collision(ball)

    #왼쪽 벽 충돌
    if ball.x1 <= 5:
        winner = "green"
        ball.stop_ball()

    #오른쪽 벽 충돌
    if bal.x1 + ball.width >= court.width - 5:
        winner = "red"
        ball. stop_ball()

    #ball 객체 움직이는 함수 호출
    ball.move_ball()
    #1초에 50번 game_flow() 함수 호출
    win.after(50,game_flow)
# 게임 진행 함수 호출
#play_game()

win.mainloop()
