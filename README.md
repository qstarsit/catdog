# CatDog

Dit is de code die hoort bij de deom van de Meetup op 09-11-2022.

https://www.meetup.com/nl-NL/Qstars-IT-Opensource-Redhat-Meetups

## Vereisten

- Een GitHub account met een repo waarin deze code staat (je kunt deze repo forken)
- Een OpenShift omgeving (https://openshift.redhat.com/try) en een login token
- Een DockerHub account en een gegenereerde Personal Access Token
- De volgende Action Secrets in je repo:
  - DOCKERHUB_TOKEN
  - DOCKERHUB_USERNAME
  - OC_TOKEN
- Een goede bak koffie/thee

## Code

In deze repo vind je de code om een simpele API. Deze heeft een `/owners` endpoint. Hier kun je ook een enkele resource opvragen met `/owners/{id}`. Op dit moment is alleen id 1 beschikbaar.

Daarnaast vind je een Dockerfile die, middels een Universal Base Image, een image maakt om uit te rollen op OpenShift.

Tot slot vind je onder `.github/workflows/` een aantal yaml bestanden. Hierin staan de actions gedefineerd om de API geautomatiseerd uit te rollen naar RedHat OpenShift, inclusief een aantal simpele testen.

Er is een `hello-world` tag beschikbaar. Dit was de eerste versie van de applicatie om de CI/CD straat in te richten.

## Dev omgeving

Om de API lokaal te starten kun je gebruik maken van het volgende commando (dit commando werkt voor Docker en Podman). Draait dit commando vanuit de root van het project:

`docker run --rm --name catdog -v ${pwd}/catdog:/opt/app-root/src/catdog -p 8000:8000 ironrain/catdog --reload`
