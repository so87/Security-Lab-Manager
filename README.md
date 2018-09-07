# CTF-scoreboard
[![Build Status](https://jenkins.owens-netsec.com/buildStatus/icon?job=Continuous-Integration-CTF)](https://jenkins.owens-netsec.com/job/Continuous-Integration-CTF/) 
[![Quality Gate](https://sonarqube.owens-netsec.com/api/badges/gate?key=ctfscoreboard)](https://sonarqube.owens-netsec.com/dashboard/index/ctfscoreboard/)
[![Vulnerabilities](https://sonarqube.owens-netsec.com/api/badges/measure?key=ctfscoreboard&metric=vulnerabilities)](https://sonarqube.owens-netsec.com/dashboard/index/ctfscoreboard)
[![bugs](https://sonarqube.owens-netsec.com/api/badges/measure?key=ctfscoreboard&metric=bugs)](https://sonarqube.owens-netsec.com/dashboard/index/ctfscoreboard)
[![code_smells](https://sonarqube.owens-netsec.com/api/badges/measure?key=ctfscoreboard&metric=code_smells)](https://sonarqube.owens-netsec.com/dashboard/index/ctfscoreboard)
[![coverage](https://sonarqube.owens-netsec.com/api/badges/measure?key=ctfscoreboard&metric=coverage)](https://sonarqube.owens-netsec.com/dashboard/index/ctfscoreboard)
[![lines](https://sonarqube.owens-netsec.com/api/badges/measure?key=ctfscoreboard&metric=lines)](https://sonarqube.owens-netsec.com/dashboard/index/ctfscoreboard)


This is my senior project at the University of Evansville.  This application is meant to be easily run by educators and enthusiasts to learn security.  Users can launch security exercises.  If they complete the exercise, they can submit their unique value to the application.  Administrators can login to see if users completed their exercises.

# How can I run this?
This system can be run on both Centos7(ubuntu coming soon) and Windows because of docker!  If you run on windows, make sure docker for windows is installed: https://docs.docker.com/docker-for-windows/install/ . Also make sure that you meet all requirements.  If you run on linux, you are all good to go!  My build script installs docker for you.
</br>
</br>
You need to run everything as administrator.  There are security implications to running the docker daemon as a user because that allows for easier command and control. 
</br>
1. run "git clone https://github.com/so87/Security-Lab-Manager.git"
2. run "build-windows.bat" or "build-linux.sh" depending on whether you are linux or windows
3. if you need to stop or stop run "start-stop-windows.bat" or "start-stop-linux.sh" and that's it!
