FROM python
ADD . /todo
WORKDIR /todo
RUN pip install -r requirements.txt
CMD ["python", "scr/app.py"]