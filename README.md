# 2D Game Programming Term Project

1. 게임 소개
  - 제목: I Wanna Escape The Maze
  - 원작 게임: I Wanna be The Guy 시리즈
  - 원작 게임 스크린샷:
  
    ![14680_00000bac](https://user-images.githubusercontent.com/32869007/94267583-d1d76700-ff76-11ea-86eb-9de2cf83d27f.png)
    ![vJULVO](https://user-images.githubusercontent.com/32869007/94267606-dbf96580-ff76-11ea-8490-48ce47555032.png)
  - 게임의 목적 및 방법: 즉사 장애물이 가득 설치된 미로를 점프를 이용하여 탈출
2. Game State
  - Scene 개수: 5
  - Scene 이름: Logo, Title, Game Play, Control Manual, Game Over
3. Logo State
  - 설명: 게임을 실행하면 맨 처음 실행되는 Scene이며 게임 실행 후 5초간 표시된다.
  - 객체 목록: 없음
  - 처리 이벤트 종류: 마우스 클릭(`SDL_QUIT`), 키보드 클릭(`SDLK_ESCAPE`)
  - 타 State 이동 조건 및 방법: 게임 실행 후 5초가 지나면 자동적으로 Title State로 이동한다.
4. Title State
  - 설명: 게임 타이틀과 스틸 컷 및 게임 스타트/종료 버튼을 화면에 출력.
  - 객체 목록: Start 버튼, Quit 버튼
  - 처리 이벤트 종류: 마우스 클릭(`SDL_MOUSEBUTTONDOWN`, `SDL_QUIT`), 키보드 클릭(`SDLK_ESCAPE`)
  - 타 State 이동 조건 및 방법: 마우스로 Start 버튼을 클릭하면 Control Manual State로 이동
5. Control Manual State
  - 설명: 게임 내 오브젝트 설명 및 캐릭터 플레이(조작) 방법 설명.
  - 객체 목록: 시작 버튼
  - 처리 이벤트 종류: 마우스 클릭(`SDL_MOUSEBUTTONDOWN`, `SDL_QUIT`), 키보드 클릭(`SDLK_ESCAPE`)
  - 타 State 이동 조건 및 방법: 시작 버튼을 마우스로 클릭하면 Game Play State로 이동
6. Game Play State
  - 설명: 실제 인게임 플레이 화면을 출력.
  - 객체 목록: 플레이어 캐릭터, 장애물, 총알, 세이브 포인트, 블럭
  - 처리 이벤트 종류: 키보드 클릭(`SDLK_UP`, `SDLK_DOWN`, `SDLK_LEFT`, `SDLK_RIGHT`, `SDLK_LCTRL`, `SDLK_SPACE`)
                     개발자 모드 한정 게임 플레이 도중 게임 종료 키(`SDLK_LCTRL`+`SDLK_LALT`+`SDLK_ESCAPE`)
  - 타 State 이동 조건 및 방법: 게임 내에서 사망 시 Game Over State로 이동, 게임 플레이 도중 Title State로의 이동이나 게임 종료는 지원하지 않을 예정.
7. Game Over State
  - 설명: 플레이어 사망 시 Game Play State 위에 Game Over State를 덧붙여서 표시, Game Over 문자가 표시될 예정.
  - 객체 목록: 없음
  - 처리 이벤트 종류: 키보드 클릭(`SDLK_r`)
  - 타 State 이동 조건 및 방법: r키를 누르면 가장 최근 세이브된 상태로 Game Play State로 이동. 게임 종료는 게임을 클리어해야만 가능하도록 구현할 예정.
8. 필요한 기술
  - 타 과목에서 배운 기술: 이미지 내에서 특정 색 제거하여 배경을 투명화
  - 배울 것으로 기대되는 기술: 비트 단위 충돌판정
  - 강의를 요청할 추가 기술: 비트 단위 충돌판정
  
  ![다이어그램](https://user-images.githubusercontent.com/32869007/94274876-35ff2880-ff81-11ea-8604-4692098f45d2.jpg)
