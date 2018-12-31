FROM jenkins/jenkins:lts
USER root
RUN apt-get update
RUN apt-get install -y ruby-build
RUN rm -rf /var/lib/apt/lists/*
