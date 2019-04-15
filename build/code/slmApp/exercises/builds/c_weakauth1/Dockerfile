FROM ubuntu:16.04
# setup ssh, gcc, and gdb
RUN apt-get update && apt-get install -y openssh-server && apt-get -y install gcc mono-mcs && apt-get -y install gdb && rm -rf /var/lib/apt/lists/*
RUN mkdir /var/run/sshd
RUN useradd -ms /bin/bash slm
RUN echo 'slm:slm' | chpasswd
RUN echo 'PasswordAuthentication yes\nAllowUsers root slm' >> /etc/ssh/sshd_config
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd
ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

# setup the exercise
COPY app.c /home/slm/app.c
RUN gcc -w /home/slm/app.c -o /home/slm/app
RUN rm /home/slm/app.c
RUN chmod u+s /home/slm/app

#copy over the flag
COPY root.txt /root/root.txt

EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]