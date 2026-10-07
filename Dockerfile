FROM jenkins/jenkins:lts

USER root

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        python3 \
        python3-pip \
        python3-venv \
        chromium \
        chromium-driver \
        curl \
        ca-certificates \
        tar \
    && rm -rf /var/lib/apt/lists/*

# Install Jenkins plugins required by the pipeline.
RUN jenkins-plugin-cli --plugins "git allure-jenkins-plugin workflow-aggregator"

# Install Allure Commandline for optional local CLI usage inside the container.
ARG ALLURE_VERSION=2.46.1
RUN curl -fsSL "https://github.com/allure-framework/allure2/releases/download/${ALLURE_VERSION}/allure-${ALLURE_VERSION}.tgz" -o /tmp/allure.tgz \
    && tar -xzf /tmp/allure.tgz -C /opt/ \
    && ln -s "/opt/allure-${ALLURE_VERSION}/bin/allure" /usr/local/bin/allure \
    && rm /tmp/allure.tgz

USER jenkins
