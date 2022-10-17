FROM python
WORKDIR /flask_app
COPY . ./
EXPOSE 5000
RUN pip install -r requirements.txt
WORKDIR /flask_app/scr
CMD ["python", "app.py"]