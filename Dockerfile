FROM registry.access.redhat.com/ubi9/python-39:1-86

# Niet nodig! https://catalog.redhat.com/software/containers/ubi9/python-39/61a61032bfd4a5234d59629e?container-tabs=technical-information
# WORKDIR /app

USER 1001

COPY --chown=1001 requirements.txt .

RUN pip install -r requirements.txt

COPY --chown=1001 catdog catdog

EXPOSE 8000

ENTRYPOINT [ "uvicorn", "catdog.main:app", "--host", "0.0.0.0", "--port", "8000" ] 