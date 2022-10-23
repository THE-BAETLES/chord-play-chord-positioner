FROM python:3.7.5-slim-buster AS compile-image

LABEL maintainer "chobe1<chobe0719@gmail.com>"
LABEL serverType="Chord Positioner Worker Server"

COPY . /chordPositionerServer
WORKDIR /chordPositionerServer

ENV SERVER_PORT 3000

RUN pip install -r requirements.txt
EXPOSE 3000

ENTRYPOINT ["uvicorn", "server:app", "--reload" ,"--host","0.0.0.0", "--port","3000"]