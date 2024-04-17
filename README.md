# app_name_server

app_name의 서버 레포지토리입니다.

## 간단 소개

app_name은 운동 도우미 웹/앱입니다.
자신의 운동 기록을 관리할 수 있고, 남들과 이야기할 수 있는 앱입니다.
app_name은 운동 도우미 웹/

## 동기

팀원중 한분이 운동을 하시고, 팀장인 제 친구가 트레이너이기 때문에 도움을 쉽게 구할 수 있기 때문에 선택했습니다.

## 역할

최지석

- 요구사항 취합 및 정리
- Url Mapping 기초 설계
- CI & CD
~~- 프론트엔드(기반)~~
- MyHealthInfo App
- ExercisesInfo App

이수현

- fe 디자인(Figma)
- 와이어프레임 취합
- Community App

임빈

- 문서화
- 건강 정보 앱
- ExercisesInfo App

안효준

- 문서화
- Profile App
~~- 프론트엔드(페이지)~~

## 프론트엔드

~~<https://github.com/orm-backend-final-project-2-2/final-project-client>~~

## 기능

1. 프로필
   - 로그인, 회원가입, 로그아웃을 기본적으로 제공한다.
   - 프로필에서 자신의 정보를 편집할 수 있다.
   - 비밀번호 찾기로 email을 입력해 재설정 링크를 발송한다.
2. 커뮤니티
   - 기본적인 커뮤니티
   - 카테고리, 댓글, 대댓글, 좋아요 기능이 있음.
   -
3. 운동정보
   - 운동에 대한 정보(운동 이름, 난이도, 자극부위, 필요정보(세트, 속도, 반복 등..)를 조회할 수 있다.
   - 관리자만 편집 가능한 페이지
4. 내 운동
    1. 건강 정보
        - 내가 가장 최근에 입력한 건강 정보를 볼 수 있다.
        - 내 최근 건강 정보를 입력할 수 있다.
    2. 루틴
        - 운동 수행정보(세트, 무게, 반복수, 시간, 속도) 와 휴식(시간)을 조합해서 하루 운동에 대한 루틴을 만들 수 있다.
        - 해당 루틴을 남들과 공유할 수 있다.
        - 루틴을 완료해서 기록을 남길 수 있다.
    3. 주간 루틴
        - 일주일에 대한 루틴 정보를 조회할 수 있다.
        - 원하는 요일에 사용자가 가지고있는 루틴을 배치하거나 생성할 수 있다.
    4. 식단
       - 자신이 먹은 식단을 사진과 제목으로 기록할 수 있다.
       - 최근 30일간의 자신의 식단을 조회할 수 있다.
    5. 기타
       - 최근 30일간의 내 루틴 수행 정보를 잔디 형태로 표시해줌
       - 내 운동 정보를 간단하게 커뮤니티에 올릴 수 있는 기능

## 기술 스택

### Frontend

<img src="https://img.shields.io/badge/Flutter-02569B?style=for-the-badge&logo=Flutter&logoColor=white"> <img src="https://img.shields.io/badge/Dart-0175C2?style=for-the-badge&logo=Dart&logoColor=white"> <img src="https://img.shields.io/badge/Material Design-757575?style=for-the-badge&logo=Material-Design&logoColor=white">

### Backend

<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white"> <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=Django&logoColor=white"> <img src="https://img.shields.io/badge/Django Rest Framework-092E20?style=for-the-badge&logo=Django&logoColor=white">

### InfraStructure

<img src="https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=Amazon AWS&logoColor=white"> <img src="https://img.shields.io/badge/NGINX-269539?style=for-the-badge&logo=NGINX&logoColor=white"> <img src="https://img.shields.io/badge/Gunicorn-342D7E?style=for-the-badge&logo=Gunicorn&logoColor=white"> <img src="https://img.shields.io/badge/Firebase-FFCA28?style=for-the-badge&logo=Firebase&logoColor=black">

### Project Management

<img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=Git&logoColor=white"> <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=GitHub&logoColor=white"> <img src="https://img.shields.io/badge/Notion-ffffff?style=for-the-badge&logo=Notion&logoColor=black"> <img src="https://img.shields.io/badge/Figma-F24E1E?style=for-the-badge&logo=Figma&logoColor=white">

## 설계

### WBS

### Requirements

#### Account Requirements

| Feature | Summary | Description | Type | Priority | Assignee |
| --- | --- | --- | --- | --- | --- |
| 회원가입 | 회원가입 | 사용자는 email과 password, username를 전달해 회원가입을 할 수 있다. | 기능 | 1 | 안효준 |
|| 회원가입 권한 확인 | 로그인하지 않은 사용자만 회원가입을 할 수 있다. | 비기능 | 2 | 안효준 |
|| email 중복 확인 | 중복된 email로 회원가입을 할 수 없다. | 기능 | 1 | 안효준 |
|| email 길이 제한 | email은 50자 이내로 입력해야 한다. | 비기능 | 2 | 안효준 |
|| email 형식 확인 | email 형식에 맞지 않는 email로 회원가입을 할 수 없다. | 비기능 | 3 | 안효준 |
|| password 길이 제한 | password는 8자 이상 20자 이하로 입력해야 한다. | 비기능 | 2 | 안효준 |
|| password 형식 확인 | password 형식에 맞지 않는 password로 회원가입을 할 수 없다. | 비기능 | 3 | 안효준 |
|| username 중복 확인 | 중복된 username으로 회원가입을 할 수 없다. | 기능 | 1 | 안효준 |
|| username 길이 제한 | username은 20자 이내로 입력해야 한다. | 비기능 | 2 | 안효준 |
|| username 형식 확인 | username 형식에 맞지 않는 username으로 회원가입을 할 수 없다. | 비기능 | 3 | 안효준 |
|| 회원가입 성공 | email, password, username을 모두 알맞게 입력하면 회원가입에 성공한다. | 기능 | 1 | 안효준 |
| 로그인 | 로그인 | 사용자는 email과 password를 전달해 로그인을 할 수 있다. | 기능 | 1 | 안효준 |
|| 로그인 실패 by wrong email | 등록되지 않은 email로 로그인을 할 수 없다. | 기능 | 1 | 안효준 |
|| 로그인 실패 by wrong password | 등록된 email과 일치하지 않는 password로 로그인을 할 수 없다. | 기능 | 1 | 안효준 |
|| 로그인 성공 | 등록된 email과 password가 일치하면 로그인에 성공한다. | 기능 | 1 | 안효준 |
|| 로그인 성공 시 JWT 발급 | 로그인에 성공하면 JWT 토큰을 발급받는다. | 기능 | 2 | 안효준 |
|| 토큰 보안 | JWT 토큰은 암호화되어야 한다. | 비기능 | 3 | 안효준 |
|| 토큰 만료 기한 | JWT 토큰은 60분 동안 유효하다. | 기능 | 2 | 안효준 |
|| 로그인 권한 확인 | 로그인하지 않은 사용자만 로그인을 할 수 있다. | 비기능 | 2 | 안효준 |
| 로그아웃 | 로그아웃 | 사용자는 로그아웃을 할 수 있다. | 기능 | 1 | 안효준 |
|| JWT 무효화 | 로그아웃 시 JWT 토큰을 무효화한다. | 기능 | 2 | 안효준 |
|| 로그아웃 권한 확인 | 로그인한 사용자만 로그아웃을 할 수 있다. | 기능 | 2 | 안효준 |
| 프로필 조회 | 자신 프로필 조회 | 로그인한 사용자는 자신의 프로필을 조회할 수 있다. | 기능 | 1 | 안효준 |
|| 프로필 페이지 접근 권한 확인 | 로그인한 사용자만 프로필 페이지에 접근할 수 있다. | 기능 | 1 | 안효준 |
|| 프로필 정보 변경 | 사용자는 자신의 프로필 정보를 변경할 수 있다. | 기능 | 1 | 안효준 |
|| 프로필 정보 변경 실패 by 중복 username | 사용자가 이미 등록된 username으로 프로필 정보를 변경하려 시도하면 실패한다. | 기능 | 1 | 안효준 |
|| 프로필 정보 변경 실패 by username 형식 | 사용자가 형식을 충족하지 않는 username으로 프로필 정보를 변경하려 시도하면 실패한다. | 기능 | 2 | 안효준 |
|| 프로필 정보 변경 실패 by username 길이 | 사용자가 일정 길이 이상의 username으로 프로필 정보를 변경하려 시도하면 실패한다. | 기능 | 2 | 안효준 |
|| 프로필 정보 변경 성공 | 사용자가 프로필 정보 변경 양식을 모두 만족한 상태로 프로필 정보를 변경하려 시도하면 성공한다. | 기능 | 1 | 안효준 |
| 비밀번호 찾기 | 비밀번호 찾기 | 사용자는 email을 전달해 비밀번호 재설정 링크를 받을 수 있다. | 기능 | 3 | 안효준 |
|| 비밀번호 재설정 요청 | 사용자는 비밀번호 재설정 페이지에서 새로운 비밀번호로 비밀번호 재설정 요청을 할 수 있다. | 기능 | 3 | 안효준 |
|| 비밀번호 재설정 실패 by pw 형식 | 사용자가 특정 형식을 충족하지 않는 비밀번호로 비밀번호 재설정을 시도했을 시 실패한다. | 기능 | 3 | 안효준 |
|| 비밀번호 재설정 실패 by pw 길이 | 사용자가 일정 길이 이상의 비밀번호로 비밀번호 재설정을 시도했을 시 실패한다. | 기능 | 3 | 안효준 |
|| 비밀번호 재설정 성공 | 사용자가 비밀번호 재설정 양식을 모두 만족한 상태로 비밀번호 재설정을 시도했을 시 성공한다. | 기능 | 3 | 안효준 |

#### Community Requirements

| Feature | Summary | Description | FunctionalType | Priority | Assignee |
| --- | --- | --- | --- | --- | --- |
| Post | 게시판 접근 | 사용자는 게시판에서 게시글들에 대한 정보를 확인할 수 있다. | 기능 | 1 | 이수현 |
| | 게시판 접근 권한 확인 | 로그인하지 않은 사용자도 게시판에 접근할 수 있다. | 비기능 | 2 | 이수현 |
| | 게시글 작성 | 사용자는 게시글을 작성할 수 있다. | 기능 | 1 | 이수현 |
| | 게시글 작성 권한 확인 | 로그인한 사용자만 게시글을 작성할 수 있다. | 비기능 | 2 | 이수현 |
| | 게시글 작성 실패 by title 길이 | 게시글의 제목은 50자 이내로 작성해야 한다. | 비기능 | 2 | 이수현 |
| | 게시글 작성 실패 by title 형식 | 게시글의 제목은 특정 형식을 충족해야 한다. | 비기능 | 3 | 이수현 |
| | 게시글 작성 실패 by content 길이 | 게시글의 내용은 6000자 이내로 작성해야 한다. | 비기능 | 2 | 이수현 |
| | 게시글 작성 실패 by content 형식 | 게시글의 내용은 특정 형식을 충족해야 한다. | 비기능 | 3 | 이수현 |
| | 게시글 작성 성공 | 게시글의 제목과 내용을 모두 알맞게 입력하면 게시글 작성에 성공한다. | 기능 | 1 | 이수현 |
| | 게시글 조회 | 사용자는 게시글을 조회할 수 있다. | 기능 | 1 | 이수현 |
| | 게시글 조회 권한 확인 | 로그인하지 않은 사용자도 게시글을 조회할 수 있다. | 비기능 | 2 | 이수현 |
| | 게시글 수정 | 사용자는 자신이 작성한 게시글을 수정할 수 있다. | 기능 | 1 | 이수현 |
| | 게시글 수정 권한 확인 | 로그인한 사용자만 자신이 작성한 게시글을 수정할 수 있다. | 비기능 | 2 | 이수현 |
| | 게시글 수정 실패 by title 길이 | 게시글의 제목은 50자 이내로 작성해야 한다. | 비기능 | 2 | 이수현 |
| | 게시글 수정 실패 by title 형식 | 게시글의 제목은 특정 형식을 충족해야 한다. | 비기능 | 3 | 이수현 |
| | 게시글 수정 실패 by content 길이 | 게시글의 내용은 6000자 이내로 작성해야 한다. | 비기능 | 2 | 이수현 |
| | 게시글 수정 실패 by content 형식 | 게시글의 내용은 특정 형식을 충족해야 한다. | 비기능 | 3 | 이수현 |
| | 게시글 수정 실패 by 타인 요청 | 타인이 작성한 게시글을 수정하려 시도하면 실패한다. | 기능 | 1 | 이수현 |
| | 게시글 수정 성공 | 게시글의 제목과 내용을 모두 알맞게 입력하면 게시글 수정에 성공한다. | 기능 | 1 | 이수현 |
| | 게시글 삭제 | 사용자는 자신이 작성한 게시글을 삭제할 수 있다. | 기능 | 1 | 이수현 |
| | 게시글 삭제 권한 확인 | 로그인한 사용자만 자신이 작성한 게시글을 삭제할 수 있다. | 비기능 | 2 | 이수현 |
| | 게시글 삭제 실패 by 타인 요청 | 타인이 작성한 게시글을 삭제하려 시도하면 실패한다. | 기능 | 1 | 이수현 |
| | 게시글 삭제 성공 | 자신이 작성한 게시글을 삭제하면 게시글 삭제에 성공한다. | 기능 | 1 | 이수현 |
| Comment | 댓글 목록 조회 | 사용자는 게시글에 작성된 댓글들을 조회할 수 있다. | 기능 | 1 | 이수현 |
| | 댓글 작성 | 사용자는 게시글에 댓글을 작성할 수 있다. | 기능 | 1 | 이수현 |
| | 댓글 작성 권한 확인 | 로그인한 사용자만 댓글을 작성할 수 있다. | 비기능 | 2 | 이수현 |
| | 댓글 작성 실패 by content 길이 | 댓글의 내용은 500자 이내로 작성해야 한다. | 비기능 | 2 | 이수현 |
| | 댓글 작성 실패 by content 형식 | 댓글의 내용은 특정 형식을 충족해야 한다. | 비기능 | 3 | 이수현 |
| | 댓글 작성 성공 | 댓글의 내용을 알맞게 입력하면 댓글 작성에 성공한다. | 기능 | 1 | 이수현 |
| | 댓글 수정 | 사용자는 자신이 작성한 댓글을 수정할 수 있다. | 기능 | 1 | 이수현 |
| | 댓글 수정 권한 확인 | 로그인한 사용자만 자신이 작성한 댓글을 수정할 수 있다. | 비기능 | 2 | 이수현 |
| | 댓글 수정 실패 by content 길이 | 댓글의 내용은 500자 이내로 작성해야 한다. | 비기능 | 2 | 이수현 |
| | 댓글 수정 실패 by content 형식 | 댓글의 내용은 특정 형식을 충족해야 한다. | 비기능 | 3 | 이수현 |
| | 댓글 수정 실패 by 타인 요청 | 타인이 작성한 댓글을 수정하려 시도하면 실패한다. | 기능 | 1 | 이수현 |
| | 댓글 수정 성공 | 댓글의 내용을 알맞게 입력하면 댓글 수정에 성공한다. | 기능 | 1 | 이수현 |
| | 댓글 삭제 | 사용자는 자신이 작성한 댓글을 삭제할 수 있다. | 기능 | 1 | 이수현 |
| | 댓글 삭제 권한 확인 | 로그인한 사용자만 자신이 작성한 댓글을 삭제할 수 있다. | 비기능 | 2 | 이수현 |
| | 댓글 삭제 실패 by 타인 요청 | 타인이 작성한 댓글을 삭제하려 시도하면 실패한다. | 기능 | 1 | 이수현 |
| | 댓글 삭제 성공 | 자신이 작성한 댓글을 삭제하면 댓글 삭제에 성공한다. | 기능 | 1 | 이수현 |
| SubComment | 대댓글 목록 조회 | 사용자는 댓글에 작성된 대댓글들을 조회할 수 있다. | 기능 | 1 | 이수현 |
| | 대댓글 작성 | 사용자는 댓글에 대댓글을 작성할 수 있다. | 기능 | 1 | 이수현 |
| | 대댓글 작성 권한 확인 | 로그인한 사용자만 대댓글을 작성할 수 있다. | 비기능 | 2 | 이수현 |
| | 대댓글 작성 실패 by content 길이 | 대댓글의 내용은 500자 이내로 작성해야 한다. | 비기능 | 2 | 이수현 |
| | 대댓글 작성 실패 by content 형식 | 대댓글의 내용은 특정 형식을 충족해야 한다. | 비기능 | 3 | 이수현 |
| | 대댓글 작성 성공 | 대댓글의 내용을 알맞게 입력하면 대댓글 작성에 성공한다. | 기능 | 1 | 이수현 |
| | 대댓글 수정 | 사용자는 자신이 작성한 대댓글을 수정할 수 있다. | 기능 | 1 | 이수현 |
| | 대댓글 수정 권한 확인 | 로그인한 사용자만 자신이 작성한 대댓글을 수정할 수 있다. | 비기능 | 2 | 이수현 |
| | 대댓글 수정 실패 by content 길이 | 대댓글의 내용은 500자 이내로 작성해야 한다. | 비기능 | 2 | 이수현 |
| | 대댓글 수정 실패 by content 형식 | 대댓글의 내용은 특정 형식을 충족해야 한다. | 비기능 | 3 | 이수현 |
| | 대댓글 수정 실패 by 타인 요청 | 타인이 작성한 대댓글을 수정하려 시도하면 실패한다. | 기능 | 1 | 이수현 |
| | 대댓글 수정 성공 | 대댓글의 내용을 알맞게 입력하면 대댓글 수정에 성공한다. | 기능 | 1 | 이수현 |
| | 대댓글 삭제 | 사용자는 자신이 작성한 대댓글을 삭제할 수 있다. | 기능 | 1 | 이수현 |
| | 대댓글 삭제 권한 확인 | 로그인한 사용자만 자신이 작성한 대댓글을 삭제할 수 있다. | 비기능 | 2 | 이수현 |
| | 대댓글 삭제 실패 by 타인 요청 | 타인이 작성한 대댓글을 삭제하려 시도하면 실패한다. | 기능 | 1 | 이수현 |
| | 대댓글 삭제 성공 | 자신이 작성한 대댓글을 삭제하면 대댓글 삭제에 성공한다. | 기능 | 1 | 이수현 |
| Like | 좋아요 | 사용자는 게시글과 댓글에 좋아요를 누를 수 있다. | 기능 | 1 | 이수현 |
| | 좋아요 권한 확인 | 로그인한 사용자만 좋아요를 누를 수 있다. | 비기능 | 2 | 이수현 |
| | 좋아요 실패 by 중복 요청 | 이미 좋아요를 누른 게시글이나 댓글에 다시 좋아요를 누르려 시도하면 실패한다. | 기능 | 2 | 이수현 |

#### MyHealthInfo Requirements

| Feature | Summary | Description | FunctionalType | Priority | Asignee |
| --- | --- | --- | --- | --- | --- |
| MyHealthInfo | 건강 정보 조회 | 사용자는 최근 1달간의 건강 정보를 조회할 수 있다. | 기능 | 1 | 최지석 |
| | 건강 정보 조회 권한 확인 | 로그인한 사용자만 건강 정보를 조회할 수 있다. | 비기능 | 2 | 최지석 |
| | 건강 정보 생성 | 사용자는 건강 정보를 생성할 수 있다. | 기능 | 1 | 최지석 |
| | 건강 정보 생성 권한 확인 | 로그인한 사용자만 건강 정보를 생성할 수 있다. | 비기능 | 2 | 최지석 |
| | 건강 정보 생성 실패 by weight | 사용자가 부적절한 몸무게로 건강 정보를 생성하려 시도하면 실패한다. | 비기능 | 2 | 최지석 |
| | 건강 정보 생성 실패 by height | 사용자가 부적절한 키로 건강 정보를 생성하려 시도하면 실패한다. | 비기능 | 2 | 최지석 |
| | 건강 정보 생성 실패 by age | 사용자가 부적절한 나이로 건강 정보를 생성하려 시도하면 실패한다. | 비기능 | 2 | 최지석 |
| | 건강 정보 생성 성공 | 사용자가 건강 정보 생성 양식을 모두 만족한 상태로 건강 정보를 생성하려 시도하면 성공한다. | 기능 | 1 | 최지석 |
| | 건강 정보 조회 | 사용자는 건강 정보를 조회할 수 있다. | 기능 | 1 | 최지석 |
| | 건강 정보 조회 권한 확인 | 로그인한 사용자만 건강 정보를 조회할 수 있다. | 비기능 | 2 | 최지석 |
| | 최근 건강 정보 조회 | 사용자는 가장 최근에 등록한 건강 정보를 조회할 수 있다. | 기능 | 1 | 최지석 |
| Diet | 식단 목록 조회 | 사용자는 최근 1달간의 식단을 조회할 수 있다. | 기능 | 1 | 최지석 |
| | 식단 목록 조회 권한 확인 | 로그인한 사용자만 식단을 조회할 수 있다. | 비기능 | 2 | 최지석 |
| | 식단 조회 | 사용자는 식단을 조회할 수 있다. | 기능 | 1 | 최지석 |
| | 식단 조회 권한 확인 | 로그인한 사용자만 식단을 조회할 수 있다. | 비기능 | 2 | 최지석 |
| | 식단 생성 | 사용자는 식단을 생성할 수 있다. | 기능 | 1 | 최지석 |
| | 식단 생성 권한 확인 | 로그인한 사용자만 식단을 생성할 수 있다. | 비기능 | 2 | 최지석 |
| | 식단 생성 실패 by content 길이 | 식단 메뉴 길이는 100자 이내로 작성해야 한다. | 비기능 | 2 | 최지석 |
| | 식단 생성 실패 by content 형식 | 식단 메뉴는 특정 형식을 충족해야 한다. | 비기능 | 3 | 최지석 |
| | 식단 생성 성공 | 사용자가 식단 생성 양식을 모두 만족한 상태로 식단을 생성하려 시도하면 성공한다. | 기능 | 1 | 최지석 |
| Routine | 루틴 목록 조회 | 사용자는 루틴 목록을 조회할 수 있다. | 기능 | 1 | 최지석 |
| | 루틴 목록 조회 권한 확인 | 로그인한 사용자만 루틴 목록을 조회할 수 있다. | 비기능 | 2 | 최지석 |
| | 루틴 생성 | 사용자는 루틴을 생성할 수 있다. | 기능 | 1 | 최지석 |
| | 루틴 생성 권한 확인 | 로그인한 사용자만 루틴을 생성할 수 있다. | 비기능 | 2 | 최지석 |
| | 루틴 생성 실패 by title 길이 | 루틴의 제목은 50자 이내로 작성해야 한다. | 비기능 | 2 | 최지석 |
| | 루틴 생성 실패 by title 형식 | 루틴의 제목은 특정 형식을 충족해야 한다. | 비기능 | 3 | 최지석 |
| | 루틴 좋아요 | 사용자는 루틴에 좋아요를 누를 수 있다. | 기능 | 1 | 최지석 |
| | 루틴 좋아요 권한 확인 | 로그인한 사용자만 루틴에 좋아요를 누를 수 있다. | 비기능 | 2 | 최지석 |
| | 루틴 좋아요 실패 by 중복 요청 | 이미 좋아요를 누른 루틴에 다시 좋아요를 누르려 시도하면 실패한다. | 기능 | 2 | 최지석 |
| | 루틴 좋아요 성공 | 좋아요를 누르지 않은 루틴에 좋아요를 누르면 좋아요 성공한다. | 기능 | 1 | 최지석 |
| WeeklyRoutine | 주간 루틴 목록 조회 | 사용자는 주간 루틴에서 주간 루틴을 조회할 수 있다. | 기능 | 1 | 최지석 |
| | 주간 루틴 목록 조회 권한 확인 | 로그인한 사용자만 주간 루틴 목록을 조회할 수 있다. | 비기능 | 2 | 최지석 |
| | 주간 루틴 조회 실패 by 타인 요청 | 타인이 작성한 주간 루틴을 조회하려 시도하면 실패한다. | 기능 | 1 | 최지석 |
| | 주간 루틴 생성 | 사용자는 주간 루틴을 생성할 수 있다. | 기능 | 1 | 최지석 |
| | 주간 루틴 생성 권한 확인 | 로그인한 사용자만 주간 루틴을 생성할 수 있다. | 비기능 | 2 | 최지석 |
| | 오늘의 루틴 조회 | 사용자는 주간 루틴에서 오늘의 루틴을 조회할 수 있다. | 기능 | 1 | 최지석 |
| | 오늘의 루틴 완료 | 사용자는 오늘의 루틴을 완료할 수 있다. | 기능 | 1 | 최지석 |
| | 오늘의 루틴 완료 권한 확인 | 로그인한 사용자만 오늘의 루틴을 완료할 수 있다. | 비기능 | 2 | 최지석 |
| | 오늘의 루틴 완료 실패 by 타인 요청 | 타인이 작성한 오늘의 루틴을 완료하려 시도하면 실패한다. | 기능 | 1 | 최지석 |

#### ExerciseInfo Requirements

| Feature | Summary | Description | FunctionalType | Priority | Asignee |
| --- | --- | --- | --- | --- | --- |
| Exercise | 운동 목록 조회 | 사용자는 운동 목록을 조회할 수 있다. | 기능 | 1 | 임빈 |
| | 운동 목록 조회 권한 확인 | 로그인하지 않은 사용자도 운동 목록을 조회할 수 있다. | 비기능 | 2 | 임빈 |
| | 운동 조회 | 사용자는 특정 운동을 조회할 수 있다. | 기능 | 1 | 임빈 |
| | 운동 조회 권한 확인 | 로그인하지 않은 사용자도 특정 운동을 조회할 수 있다. | 비기능 | 2 | 임빈 |
| | 운동 생성 | 관리자만 운동을 생성할 수 있다. | 기능 | 1 | 임빈 |
| | 운동 생성 실패 by title 길이 | 운동의 제목은 50자 이내로 작성해야 한다. | 비기능 | 2 | 임빈 |
| | 운동 생성 실패 by title 형식 | 운동의 제목은 특정 형식을 충족해야 한다. | 비기능 | 3 | 임빈 |
| | 운동 생성 실패 by content 길이 | 운동의 내용은 1000자 이내로 작성해야 한다. | 비기능 | 2 | 임빈 |
| | 운동 생성 실패 by content 형식 | 운동의 내용은 특정 형식을 충족해야 한다. | 비기능 | 3 | 임빈 |
| | 운동 생성 성공 | 관리자가 운동 생성 양식을 모두 만족한 상태로 운동을 생성하려 시도하면 성공한다. | 기능 | 1 | 임빈 |
| | 운동 수정 | 관리자만 운동을 수정할 수 있다. | 기능 | 1 | 임빈 |
| | 운동 수정 실패 by title 길이 | 운동의 제목은 50자 이내로 작성해야 한다. | 비기능 | 2 | 임빈 |
| | 운동 수정 실패 by title 형식 | 운동의 제목은 특정 형식을 충족해야 한다. | 비기능 | 3 | 임빈 |
| | 운동 수정 실패 by content 길이 | 운동의 내용은 1000자 이내로 작성해야 한다. | 비기능 | 2 | 임빈 |
| | 운동 수정 실패 by content 형식 | 운동의 내용은 특정 형식을 충족해야 한다. | 비기능 | 3 | 임빈 |
| | 운동 수정 성공 | 관리자가 운동 수정 양식을 모두 만족한 상태로 운동을 수정하려 시도하면 성공한다. | 기능 | 1 | 임빈 |
| | 운동 삭제 | 관리자만 운동을 삭제할 수 있다. | 기능 | 1 | 임빈 |

### Diagrams

#### Sequence Diagram

#### Entity-Relationship Diagram

```mermaid
erDiagram
%%account
    User {
        int id PK
        str email UK
        str username UK
        str password
        int last_health_info FK "HealthInfo_id"
        datetime created_at
    }

    User ||--o| HealthInfo : last_health_info
%%my_health_info
    HealthInfo {
        int id PK
        int user FK "User_id"
        int age
        float weight
        float height
        date date
    }

    HealthInfo }|--|| User : user

    Routine {
        int id PK
        int author FK "User_id"
        str title
        int liked_users FK "User_id"
        int like_count
    }

    Routine }|--o| User : author
    Routine }|--o{ User : liked_users

    MirroredRoutine {
        int id PK
        int original_routine FK "Routine_id"
        str title
        str authored_name
    }

    MirroredRoutine ||--o| Routine : original_routine
%%exercises_info
    ExercisesInfo {
        int id PK
        int author FK "User_id"
        str name
        str description
        str video_url
    }

    ExercisesInfo }|--|| User : author

    FocusArea {
        int id PK
        int exercise FK "Exercise_id"
        str focus_area
    }

    FocusArea }|--|| ExercisesInfo : exercise

    ExerciseAttribute {
        int id PK
        int exercise FK "Exercise_id"
        bool need_set
        bool need_rep
        bool need_weight
        bool need_speed
        bool need_duration
    }

    ExerciseAttribute ||--|| ExercisesInfo : exercise
%%my_healhth_info
    ExerciseInRoutine {
        int id PK
        int routine FK "Routine_id"
        int mirrored_routine FK "MirroredRoutine_id"
        int exercise FK "Exercise_id"
        int order
    }

    ExerciseInRoutine }|--o| Routine : routine
    ExerciseInRoutine }|--|| MirroredRoutine : mirrored_routine
    ExerciseInRoutine }|--|| ExercisesInfo : exercise

    ExerciseInRoutineAttribute {
        int id PK
        int exercise_in_routine FK "ExerciseInRoutine_id"
        int set
        int rep
        float weight
        float speed
        float duration
    }

    ExerciseInRoutineAttribute ||--|| ExerciseInRoutine : exercise_in_routine

    UsersRoutine {
        int id PK
        int user FK "User_id"
        int routine FK "Routine_id"
        int mirrored_routine FK "MirroredRoutine_id"
        bool is_author
        bool need_update
    }

    UsersRoutine }|--|| User : user
    UsersRoutine }|--o| Routine : routine
    UsersRoutine }|--|| MirroredRoutine : mirrored_routine

    RoutineStreak {
        int id PK
        int user_id FK "User_id"
        int mirrored_routine FK "MirroredRoutine_id"
        date date
    }

    RoutineStreak }|--|| User : user
    RoutineStreak }|--o| MirroredRoutine : mirrored_routine

    WeeklyRoutine {
        int id PK
        int user FK "User_id"
        int day_index
        int users_routine FK "UsersRoutine_id"
    }

    WeeklyRoutine }|--|| User : user
    WeeklyRoutine }|--|| UsersRoutine : users_routine
%%community
    Post {
        int id PK
        int author FK "User_id"
        str title
        str content
        int liked_users FK "User_id"
        int like_count
    }

    Post }o--|| User : author
    Post }o--o{ User : liked_users

    Comment {
        int id PK
        int author FK "User_id"
        int post FK "Post_id"
        str content
    }

    Comment }o--|| User : author
    Comment }o--|| Post : post

    SubComment {
        int id PK
        int author FK "User_id"
        int comment FK "Comment_id"
        str content
    }

    SubComment }o--|| User : author
    SubComment }o--|| Comment : comment
```

## TDD

최소한의 구조 구현(빈 url, 간단한 모델, 빈 뷰셋, 빈 시리얼라이저) 후 TC 작성 -> 구현 -> 리팩토링 -> 반복

django의 TestCase를 사용해 실제로는 db를 변경하지 않았고, 모든 코드에서 db를 복사해서 테스트하였음

### test 자동화

feature-app_name/FeatureName 을 push시 브런치에서  
python manage.py app_name.tests.FeatureNameTestCase 실행하게 설정하였음
각 기능을 구현할 때 관련된 TC를 묶어서 테스트

```
name: Run Feature Branch Tests

on:
  push:
    branches:
      - feature-**

jobs:
  test:
    name: Run Feature Branch Tests
    runs-on: ubuntu-latest
    steps:
    - name: Checkout code
      uses: actions/checkout@v3

    - name: Set up Python
      uses: actions/setup-python@v3
      with:
        python-version: '3.12.0'

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt

    - name: Run tests
      env:
        DJANGO_SECRET_KEY: ${{ secrets.DJANGO_SECRET_KEY }}
      run: |
        output=$(python3 utils/parse_feature_branch.py ${{ github.ref }})
        read app_name tc_name <<< $output
        python3 manage.py test ${app_name}.tests.${tc_name}
```

### Utils

테스트를 위한 util 모듈을 작성하여 테스트 도중에 활용함

#### fake_data.py

[fake_data.py](https://github.com/orm-backend-final-project-2-2/final-project-server/blob/main/utils/fake_data.py)

Faker 라이브러리를 사용해 실제 모델의 데이터와 유사한 가짜 데이터를 생성

FakeModel 클래스를 먼저 제작하고, 이를 상속받아 실제 모델을 모방한 FakeModel을 제작

CREATE request에 해당하는 데이터를 생성하거나,

실제 모델 오브젝트를 생성하는 작업을 하였음

#### parse_feature_branch.py

[parse_feature_branch.py](https://github.com/orm-backend-final-project-2-2/final-project-server/blob/main/utils/parse_feature_branch.py)

feature-app_name/FeatureName 을 파싱하여 app_name과 tc_name을 반환하는 파이썬 스크립트

위에서 사용한 github action에서 현재 브런치에서 사용하는 TestCase를 실행하기 위해서 사용하였음

#### reset_database_schemes.py

[reset_database_schemes.py](https://github.com/orm-backend-final-project-2-2/final-project-server/blob/main/utils/reset_database_schemes.py)

다른 사람이 작업한 앱이 develop 브런치에 merge되었을 때, 가끔 데이터베이스가 꼬이는 문제가 일어났음

제작된 앱 이름들과 프로젝트 네임을 받아 마이그레이션을 초기화하고 db를 리셋하는 스크립트

## 배포

FE - 크로스플랫폼 제작이기 때문에 기존 경험이 있는 firebase hosting과 app distribution를 사용하기로 하였음

## 트러블슈팅

### Django 테스트

1. 모델 내용을 변경하지 않고 그 모델을 참조하는 다른 모델을 조회 시 불일치하는 문제

모델을 변경시킬때마다 save를 통해 변경해주어야 함

2.

## 프로젝트 회고

### 느낀점

## 최지석

## 안효준

## 이수현
