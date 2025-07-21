**THIS PROJECT IS PART OF MY INTERNSHIP ONLY**
1. สร้างและเข้า virtual env
python3 -m venv ocr-env
source ocr-env/bin/activate
2. ติดตั้ง lib
pip install fastapi uvicorn httpx
3. รัน FastAPI ด้วย uvicorn
uvicorn ocr_main:app --host 0.0.0.0 --port 8118 --reload
