# Gonggol Team
![](https://github.com/wecode-bootcamp-korea/21-1st-gonggol-frontend/blob/master/public/images/common/logo_tm.png?raw=true)
- [캉골](https://kangolkorea.com/) 공식 온라인스토어 클론 프로젝트.
- 2주라는 짧은 기간 동안 완성도를 높이기 위해 추가 기능은 단축시키고 화면 & 기본 CRUD를 중점으로 기능 구현한 클론 프로젝트입니다.
- 개발 초기 세팅부터 직접 구현하였으며, 아래 데모 영상에서 보이는 모든 부분은 실제 사용할 수 있는 서비스 수준으로 개발한 것입니다.
- 모든 로직은 django를 활용하여 직접 구현하였습니다.
## 프로젝트 기간 및 인원
### 2021.06.07 ~ 2021.06.18
### Frontend (3명)
- 김지민
- 오선주
- 이도윤
#### <a href ="https://github.com/wecode-bootcamp-korea/21-1st-gonggol-frontend">프론트엔드 Github 링크</a>
### Backend (3명)
- 배찬영
- 최승리
- 한성봉
#### [백엔드 Github 링크](https://github.com/wecode-bootcamp-korea/21-1st-gonggol-backend)
## 데모 영상
[![데모영상](http://img.youtube.com/vi/um9Wr2I_JRE/0.jpg)](https://www.youtube.com/watch?v=um9Wr2I_JRE)
## 적용 기술
- Front-End : React.js, sass
- Back-End : Python, Django web framework, Bcrypt, My SQL, JWT
- 협업 Tool : Slack, Trello, Gitbook, github, A-query, post-man
## 구현 기능
### 공통
- a쿼리 툴을 이용한 모델링 작성
![](https://images.velog.io/images/cj4207/post/d22c1eea-541e-4acc-a60d-c7456c88124d/%E1%84%86%E1%85%A9%E1%84%83%E1%85%A6%E1%86%AF%E1%84%85%E1%85%B5%E1%86%BC.PNG)
### 메인페이지 (배찬영님)
- 신상품, 베스트 상품 리스트 패스 파라미터로 value 받고 response ( 신상품, 베스트 임의 결정 )
### 상품목록 (한성봉)
- 카테고리 별, 상품 별 리스트 q객체 사용 조건을 추가하여 쿼리 파라미터로 value 받고 호출
- 쿼리 파라미터로 offset, limit 지정하여 그 값으로 슬라이싱후 페이징 기능 구현
- 쿼리 파라미터로 value 받고 order_by() 사용하여 정렬 기능 구현
- tag를 이용해 True, False 값으로 신상품, 세일상품, 베스트 상품 response
### 상품상세 (배찬영님)
- 패스 파라미터로 product_id 값으로 데이터 response, 각 상품들의 size 재고, 가격, discount, image, image body response
### 로그인 & 회원가입 (최승리님)
- 회원가입 정규표현식을 활용한 입력항목 유효성 체크 구현
- 회원가입 Bcrypt활용한 password 암호화 및 복호화 구현
- 로그인 JWT를 활용한 token 발행 구현
- Decorator를 활용한 회원 인가 구현
### 장바구니 (최승리님)
- Django 기초적인 CRUD 활용한 장바구니 생성, 추가, 삭제 구현
- Login Decorator를 통한 회원정보 확인 구현
## Reference
> 이 프로젝트는 캉골 사이트를 참조하여 학습목적으로 만들었습니다.
> 실무수준의 프로젝트이지만 학습용으로 만들었기 때문에 이 코드를 활용하여 이득을 취하거나 무단 배포할 경우 법적으로 문제될 수 있습니다.
> 이 프로젝트에서 사용하고 있는 사진 대부분은 위코드에서 구매한 것이므로 해당 프로젝트 외부인이 사용할 수 없습니다.
