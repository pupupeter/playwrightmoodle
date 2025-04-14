# playwrightmoodle

# 📘 자동 추출기 & Gemini 코드 생성기

이 Python 도구는 **Playwright 자동화**와 **Google의 Gemini API**를 결합하여 다음을 도와줍니다:

- NTNU Moodle에 자동 로그인  
- 과제 지시사항 추출  
- 설명이 포함된 전체 코드 초안 생성  
- 구조화된 HTML 페이지 및 `.py` 스크립트로 출력  

---

## 🚀 주요 기능

- ✅ NTNU Moodle 자동 로그인  
- ✅ "1132 Programming Language" 강의로 이동  
- ✅ **"Assignment 4 Requirements"** 공지사항 찾기 및 열기  
- ✅ Moodle에서 과제 내용 추출  
- ✅ **Gemini**에 내용을 전송하여 코드 및 설명 생성  
- ✅ 내용을 깔끔한 HTML 형식으로 정리  
- ✅ 생성된 Python 코드를 별도의 `.py` 파일로 저장  

---

## 🛠 사용 방법

### 1. 필수 패키지 설치

```bash
pip install python-dotenv playwright google-generativeai
playwright install
```
### 2. .env 파일 설정
루트 폴더에 .env 파일을 생성하고 다음과 같은 자격 정보를 입력하세요:

```
PASSWORD=your_moodle_password
GEMINI_API_KEY=your_gemini_api_key
```

### 3. 스크립트에서 사용자명 수정
Python 스크립트를 열고 Moodle 계정 사용자명을 실제 정보로 바꾸세요:

```
USERNAME = "your_account"
```
### 4. 스크립트 실행
```
python main.py
```
⚠️ 파일명이 main.py가 아니라면 해당 파일명으로 실행하세요.



### 📂 출력 파일


```
homework.html
```
스타일이 적용된 HTML 파일로 다음을 포함합니다:

-추출된 Moodle 과제 내용

-Gemini가 생성한 코드와 설명
```
generated_code.py
```

AI가 생성한 Python 코드만 포함된 파일로, 바로 테스트하거나 수정이 가능합니다.



### 💡 참고 사항
이 도구는 교육 목적의 지원 및 코드 프로토타입 제작을 위해 설계되었습니다.

다음과 같은 경우에 유용합니다:

✏️ 과제 지시사항을 빠르게 추출할 때

🤖 명확한 설명이 포함된 AI 생성 코드가 필요할 때

💼 개발 초기 단계에서 시간을 절약하고 싶을 때

⚠️ 책임감 있게 사용하세요: AI가 생성한 내용을 제출 전 반드시 검토하고 수정하세요. 제출 내용은 본인의 이해를 반영해야 합니다.


### 🧠 기술 스택
Playwright – 헤드리스 브라우저 자동화

Google Generative AI (Gemini) – 텍스트 및 코드 생성

Python – 스크립트 및 자동화

dotenv – 보안 환경변수 관리
