# 1. Instagram Clone Project - Backend

## 1.1. [ 목차 ]

- [1. Instagram Clone Project - Backend](#1-instagram-clone-project---backend)
  - [1.1. [ 목차 ]](#11--목차-)
  - [1.2. [ 시작하기 전에... ]](#12--시작하기-전에-)
  - [1.3. [ requirements ]](#13--requirements-)
  - [1.4. [ DB ]](#14--db-)
    - [1.4.1. E-R Model 설계](#141-e-r-model-설계)
  - [1.5. [ Local apps ]](#15--local-apps-)
    - [1.5.1. accountapp](#151-accountapp)
    - [1.5.2. instagramapp](#152-instagramapp)
  - [1.6. [ 여담 ]](#16--여담-)
  - [1.7. [ 앞으로... ]](#17--앞으로-)

## 1.2. [ 시작하기 전에... ]

- 에듀케스트에서 제공되는 SPA 방식 인스타그램 클론 강좌를 수강한 뒤 코드를 저장하는 레포지토리

## 1.3. [ requirements ]

- dev

    ```requirements
    django==3.1.5
    django-environ==0.4.5
    django-debug-toolbar==3.2
    Pillow==8.1.0
    djangorestframework
    django-cors-headers
    djangorestframework-jwt
    ```

- prod

    ```requirements
    django==3.1.5
    django-environ==0.4.5
    Pillow==8.1.0
    djangorestframework
    django-cors-headers
    djangorestframework-jwt
    ```

## 1.4. [ DB ]

### 1.4.1. E-R Model 설계

- ![E-R Model](_image\E-R_Model\e-r_model.png)

## 1.5. [ Local apps ]

### 1.5.1. accountapp

- 모델
  ![model](_image\accountapp\user_model.png)
- 뷰
  ![view](_image\accountapp\user_view.png)
- 시리얼라이저
  ![serializer](_image\accountapp\user_serializer.png)

### 1.5.2. instagramapp

- 모델
  ![model](_image\instagramapp\ins_model.png)
- 뷰
  ![view](_image\instagramapp\ins_view.png)
- 시리얼라이저
  ![serializer](_image\instagramapp\ins_serializer.png)

## 1.6. [ 여담 ]

- time 관련 라이브러리를 선택하여 치트시트를 따로 마련해야겠다.
- django-pydenticon은 사용하지 않도록 한다. avatar가 없을 때 대체 이미지를 사용하도록 지정하는 것도 서버의 자원이며, null로 처리하여 프론트에서 다루도록 한다.
- serializers.SerializerMethodField를 사용해서 follow중인지 아닌지를 판단하는 로직을 삽입해보았다. 마음에 든다.
- 여태 django-environ으로 환경변수를 다루었다. 검색을 통해 찾아보니, django-environ-docker를 통해 자동으로 docker-compose에 설정된 secrets를 읽어올 수 있는 버전도 있었다. 해당 라이브러리 위주로 활용해야겠다.
  - setting이 나눠져있는 구조(common, dev, prod)를 바꿔야 한다(dev, prod).
  - 환경변수를 불러오는 방식이 달라지기 때문.
  - 다른 방법이 있을까?
- Azure의 스토리지, DB에 Vultr 서버 대여 및 Portainer 설치, 만든 이미지를 Docker hub에 푸시 후 이미지 빌드까지 수행하여 Backend로써 동작할 api를 구현했다. 80번 요청이 바로 gunicorn으로 접속되는 방식이라 비효율적이겠지만, nginx를 사용하는 방법을 모르므로 지금은 넘긴다.
- api에 ssl을 적용하지 않았다. azure의 storage에 배포한 서버를 통해 api 통신을 받을 때, 걸린다. 회원가입이 불가능하기 때문에 테스트를 진행할 수 없었다.
  - vultr가 아닌 azure를 통해 api 서버를 배포했다면 건너 뛸 수 있는 과정이었다.
  - ssl을 구매하고 테스트까지 진행하는 방법도 있겠지만 그를 제외하고도 우선적으로 학습해야 할 것이 많기에, 실제 배포까지의 과정은 수행하지 않고 프로젝트를 종료하기로 한다.

## 1.7. [ 앞으로... ]

- Docker Documentation을 활용하여 Docker 훈련 및 치트시트를 마련한다.
- Nginx가 무엇인지, Gunicorn이 무엇인지에 대한 개념을 정리한다.
- 시간 관련 파이썬 라이브러리를 하나 익힌다.