# 2D Game Programming Term Project

1. 게임 소개
  - 제목: I Wanna Escape The Maze
  - 원작 게임: I Wanna be The Guy 시리즈
  - 원작 게임 스크린샷:
  
    ![14680_00000bac](https://user-images.githubusercontent.com/32869007/94267583-d1d76700-ff76-11ea-86eb-9de2cf83d27f.png)
    ![vJULVO](https://user-images.githubusercontent.com/32869007/94267606-dbf96580-ff76-11ea-8490-48ce47555032.png)
  - 게임의 목적 및 방법: 즉사 장애물이 가득 설치된 미로를 점프를 이용하여 탈출
  - 게임 컨셉: 회피 난이도 극악인 미로를 점프와 미세 컨트롤로 탈출하는 플랫포머 게임
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
  - 배울 것으로 기대되는 기술: 각 이미지의 비트맵 단위 충돌 판정
  - 강의를 요청할 추가 기술: 파이썬에서의 배경 투명화
  
  ![다이어그램](https://user-images.githubusercontent.com/32869007/94274876-35ff2880-ff81-11ea-8604-4692098f45d2.jpg)
  
개발 범위
| 내용            | 최소 범위                                                                    | 추가 범위                           |
| :------------: | --------------------------------------------------------------------------- | ----------------------------------- |
| 캐릭터 컨트롤   | 4방향 ~ 8방향(상하좌우 + 좌상/하, 우상/하) <br/>키보드로 캐릭터를 이동           | 캐릭터가 바라보는 방향은 좌우 Only    |
| 캐릭터 기술     | Z키 입력 시 총알 발사                                                         | Z키 연타 시 일정 간격을 두고 연사     |
| 맵             | 스테이지 5개                                                                 | 각 스테이지는 방의 개념으로 제작      |
| 난이도         | 방을 하나씩 지날 때마다 난이도 증가                                             | 난이도 증가 시 다양한 트랩 이벤트 추가 |
| 게임 기능      | 총알로 세이브 블록 명중 시 상황을 그대로 세이브 <br/>기본 벽은 전부 블록으로 막혀있으며 일부 부분 안 막힌 곳으로 가면 다음 스테이지로 진출 <br/>R키 입력 시 세이브 지점에서 재시작 <br/>플레이 중 사망 시 강제 종료 불가능 <br/>점프 키 입력 지속 시간에 따른 점프 높이 적용 | 게임 시작 전 조작법을 표시하는 페이지 표시 <br/>개발자 디버깅용 게임 종료 커맨드 별도 존재 <br/>설정에서 게임 사운드, 조작 키 변경 가능 |
| 사운드         | SE: 사격, 점프, 더블점프, 피격, 세이브 <br/>BGM: 로고, 타이틀(메인), 인게임, 사망, 클리어 ||
| 애니메이션     | 사격, 점프, 걷기, 가만히 서있기, 낙하 ||

개발 일정
| 주차  | 개발 범위 | 개발 내용 |
| :---: | ----------------------- | ---------------------------------------------------------------------------------- |
| 1주차 | 자료 수집 | 1. 인게임 내 사용될 리소스 수집 <br/> 2. 게임 맵 디자인 구상 및 구체화 |
| 2주차 | 기본 Game State 제작 | 1. 게임 내 사용될 Game State 제작 <br/>2. 각 메뉴에 쓰일 마우스 동작 구현 |
| 3주차 | 플레이어 기본 오브젝트 | 1. 플레이어 애니메이션 구현 <br/>2. 캐릭터 기본 동작 구현 |
| 4주차 | 장애물 기본 오브젝트 | 1. 장애물과 플레이어 충돌 판정 구현 <br/>2. 장애물 월드 공간에 배치 |
| 5주차 | 플레이어 최종 및 중간점검 | 1. 일부 장애물과 충돌 시 사망하도록 이벤트 처리 <br/>2. 개발 상황 중간 점검 및 버그 픽스 |
| 6주차 | 장애물 최종 | 1. 함정 이벤트 처리 |
| 7주차 | 사운드 삽입 및 최종 보완 | 1. FMOD를 이용하여 게임 내 사운드 삽입 <br/>2. 기타 부족한 부분 보완 |
| 8주차 | 마무리 | 1. 최종 점검, 버그 픽스 및 릴리즈 |

개발 진척도
| 내용            | 최소 범위                                                                    | 추가 범위                           | 구현률                         |
| :------------: | --------------------------------------------------------------------------- | ----------------------------------- | ------------------------------ |
| 캐릭터 컨트롤   | 4방향 ~ 8방향(상하좌우 + 좌상/하, 우상/하) <br/>키보드로 캐릭터를 이동           | 캐릭터가 바라보는 방향은 좌우 Only    | 100%                           |
| 캐릭터 기술     | Z키 입력 시 총알 발사                                                         | Z키 연타 시 일정 간격을 두고 연사     | 100%                           |
| 맵             | 스테이지 5개                                                                 | 각 스테이지는 방의 개념으로 제작      | 100%                            |
| 난이도         | 방을 하나씩 지날 때마다 난이도 증가                                             | 난이도 증가 시 다양한 트랩 이벤트 추가 | 70%                           |
| 게임 기능      | 총알로 세이브 블록 명중 시 상황을 그대로 세이브 <br/>기본 벽은 전부 블록으로 막혀있으며 일부 부분 안 막힌 곳으로 가면 다음 스테이지로 진출 <br/>R키 입력 시 세이브 지점에서 재시작 <br/>플레이 중 사망 시 강제 종료 불가능 <br/>점프 키 입력 지속 시간에 따른 점프 높이 적용 | 게임 시작 전 조작법을 표시하는 페이지 표시 <br/>개발자 디버깅용 게임 종료 커맨드 별도 존재 <br/>설정에서 게임 사운드, 조작 키 변경 가능 | 70%                  |
| 사운드         | SE: 사격, 점프, 더블점프, 피격, 세이브 <br/>BGM: 로고, 타이틀(메인), 인게임, 사망, 클리어 || 100%                        |
| 애니메이션     | 점프, 걷기, 가만히 서있기, 낙하 || 100%                   |

미구현된 내용
| 내용 | 사유 |
| --- | ---- |
| 4방향~8방향 캐릭터 이동 | 키보드로 직접적으로 이동하는 것은 좌우방향 뿐이고 상하는 중력과 점프키를 이용하여 이동 |
| 난이도 증가시 트랩 이벤트 추가 | 개발 시간 부족으로 인한 미구현 |
| 플레이 중 사망 시 강제 종료 불가능 | 실제 플레이 결과 게임의 난이도가 너무 높아 조기 종료를 위해 구현 |
| 개발자 디버깅용 게임 종료 커맨드 | 일반 유저도 사용 가능한 종료 키 구현으로 구현 되었다고 볼 수 있음 |
| 점프 키 입력 지속 시간에 따른 점프 높이 적용 | 기술적 한계 및 개발 시간 부족으로 인한 미구현 |
| 게임 시작 전 조작법 표시 | 개발 시간 부족으로 인한 미구현 |
| 설정에서 게임 사운드, 조작 키 변경 가능 | 기술적 한계 및 개발 시간 부족으로 인한 미구현 |

개발 과정에서의 난항
- 캐릭터의 충돌체크 과정에서 긴 시간을 소비
- 버그 수정 후 바로 나타나는 다른 버그가 연쇄적으로 나타남