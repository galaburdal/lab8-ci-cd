# Lab 8 — CI/CD Pipeline

## Project
BDD UI automation with Behave + Selenium + Allure, executed in Jenkins/Docker.

## Local test
```bash
python3 -m pip install -r requirements.txt
python3 -m behave
```

## Build Jenkins image
```bash
docker build -t my-jenkins .
```

## Run Jenkins
```bash
docker run -d -p 8080:8080 -p 50000:50000 \
  -v jenkins_home:/var/jenkins_home \
  --name jenkins my-jenkins
```

Open http://localhost:8080.

## Jenkinsfile
Before pushing, replace `YOUR_LOGIN/YOUR_REPO` in `Jenkinsfile` with the real GitHub repository path.
