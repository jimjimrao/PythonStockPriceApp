FROM python:3


# ADD src .
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
ENV PORT=8501
EXPOSE 8501
ENTRYPOINT ["streamlit", "run", "./src/app.py", "--server.port=8501", "--server.address=0.0.0.0"]