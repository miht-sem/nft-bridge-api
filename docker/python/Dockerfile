FROM python:3.10 as compiler
ENV PYTHONUNBUFFERED 1

COPY ./nft_api nft_api

WORKDIR /nft_api

RUN python -m venv /opt/venv

# Enable venv
ENV PATH="/opt/venv/bin:$PATH"

RUN pip install -Ur requirements.txt


FROM python:3.10 as runner

COPY ./nft_api nft_api

WORKDIR /nft_api

COPY --from=compiler /opt/venv /opt/venv

# Enable venv
ENV PATH="/opt/venv/bin:$PATH"
#COPY ./nft_api nft_api

RUN python manage.py migrate

CMD ["python","manage.py","runserver", "0.0.0.0:8000"]