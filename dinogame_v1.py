"""
pip install pygame
"""

# pygame 모듈 갔다 쓰겠다
import pygame
import sys

#pygame 초기화
pygame.init()

# 변수 2개 한 번에 선언
WIDTH, HEIGHT = 800, 400
# 게임화면 생성
screen=pygame.display.set_mode((WIDTH,HEIGHT))
#프로그램 제목 지어주기
pygame.display.set_caption("jump game")
#프레임 속도 제어용 시계 객체
clock=pygame.time.Clock()


# 변수,튜플, 게임 만들 때 빼곤 안 씀
WHITE=(255,255,255)
BLACK=(0,0,0)


# 공룡 설정 변수

#크기
dino_width,dino_height=50,50
#x좌표
dino_x=50
#화면 크기 대비 동적으로 y값 계산
dino_y=HEIGHT-dino_height
#속도
dino_velocity=0
#중력
gravity= 0.5
# 점프 시 위로 오라갈 힘
jump_strength=-10
# 점프 중인지 여부확인
is_jumping=False


#장애물
obstacle_width,obstacle_height=20,50
obstacle_x=WIDTH
obstacle_y=HEIGHT-obstacle_height
obstacle_speed=5

#게임 루프 시작
running=True
while running:
    # 화면을 하얀색으로 지움 (매 프레임 초기화)
    screen.fill(WHITE)
    
    # 이벤트 처리 (종료감지). 창을 닫으면 게임 종료
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

    # 키보드 감지 (스페이스 바 점프)
    keys=pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and not is_jumping:
        dino_velocity= jump_strength
        is_jumping=True
    
    # 중력 적용
    dino_velocity+=gravity
    dino_y+=dino_velocity
    if dino_y >= HEIGHT - dino_height:
        dino_y = HEIGHT - dino_height
        is_jumping = False
    
    # 장애물 이동
    obstacle_x -= obstacle_speed
    if obstacle_x < 0:
        # 왼쪽 끝까지 가면 다시 오른쪽으로 이동
        obstacle_x = WIDTH
    
    # 충돌 검사
    dino_rect=pygame.Rect(dino_x,dino_y,dino_width,dino_height)
    obstacle_rect=pygame.Rect(obstacle_x,obstacle_y,obstacle_width,obstacle_height)

    # dino 랑 장애물이랑 충돌했으면 프로그램 종료
    if dino_rect.colliderect(obstacle_rect):
        print("충돌! 게임 오버")
        running=False

    # 캐릭터와 장애물 화면에 그리기
    #공룡
    pygame.draw.rect(screen,BLACK,dino_rect)
    #장애물
    pygame.draw.rect(screen,BLACK,obstacle_rect)

    #화면 업데이트
    pygame.display.update()
    #초당 60 프레임 유지
    clock.tick(60)