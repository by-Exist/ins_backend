# Instagram Clone Project - Backend

## 시작하기 전

- 에듀케스트에서 제공되는 SPA 방식 인스타그램 클론 강좌에서 백앤드 코드를 저장하는 레포지토리.

## requirements

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

## DB

### E-R Model 설계

- ./_erd/.vuerd.json을 vscode 익스텐션 "ERD Editor"를 활용하여 open
- 사진...

## 여담

- 시간을 다루는 라이브러리를 정해서 치트시트를 따로 마련해야겠다.
- django-pydenticon은 사용하지 않도록 한다. avatar가 없을 때 대체 이미지를 사용하도록 지정하는 것은 백엔드의 역할보다는 프론트엔드의 역할이라고 생각되기 때문이다.
- serializers.SerializerMethodField를 사용해서 follow중인지 아닌지를 판단하는 로직을 삽입해보았다. 마음에 든다.