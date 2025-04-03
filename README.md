### 라이브러리

```bash
python -m venv .venv
.venv/Scripts/activate.ps1  # 윈도우
source ./venv/bin/activate #리눅스

pip install fastapi uvicorn beanie
uvicorn PLANNER.testmongodb.py:app --reload #--reload는 수정할때마다 반영한다는 뜻뜻
```