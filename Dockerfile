FROM python
ADD . /flask_app
WORKDIR /flask_app
RUN pip install -r requirements.txt
CMD ["python", "scr/app.py"]