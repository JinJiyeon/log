# FROM : 베이스 이미지
FROM python:3.8

# COPY : 현재 디렉토리에서 파일들 복사하기
COPY ./01_single_service /jigu
COPY requirements.txt /jigu

# WORKDIR : 도커가 열리면 여기를 바라본다
WORKDIR /jigu

# RUN : FROM 베이스 이미지에서 실행
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# ENTRYPOINT : 무조건 실행
# CMD : 컨테이너 기동 시 실행
CMD ["python", "main.py"]

