### 라이브러리

```bash
python -m venv .venv
.venv/Scripts/activate.ps1  # 윈도우
source ./venv/bin/activate #리눅스

pip install fastapi uvicorn beanie
uvicorn PLANNER.testmongodb.py:app --reload #--reload는 수정할때마다 반영한다는 뜻뜻
```

```bash
git init
powershell -> New-Item .gitignore       # data. .vevn , __pycache__
linux -> touch .gitignore

git add {올릴파일}
git commit -m "first commit}
git branch -M main
git remote -V
git remote add origin {깃허브레포지토리 주소}
git push -u origin main
```

```bash
root
|--src\
|   |--models/
|   |-routes/
|   |-main.py
|--.gitignore
|--project.toml
|--README.md
```

# 플래너 만들기
* 로그인
    * 이메일, 비밀번호
* 이벤트 추가 및 삭제, 업데이트
    * 제목, 이미지, 설명, 태그, 위치, 날짜