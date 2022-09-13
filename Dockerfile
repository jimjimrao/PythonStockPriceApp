FROM python:3


# ADD src .
COPY requirements.txt .
RUN pip install --no-cache-dir numpy pandas matplotlib streamlit yfinance ta

COPY . .

ENTRYPOINT ["streamlit", "run", "./src/app.py", "--server.port=8501", "--server.address=0.0.0.0"]