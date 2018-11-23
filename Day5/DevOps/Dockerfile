FROM ubuntu:16.04
MAINTAINER Jeganathan Swaminathan <jegan@tektutor.org>

RUN apt-get update && apt-get install -y openssh-server python-minimal
RUN apt-get update && apt-get install -y openjdk-8-jdk-headless maven 
RUN mkdir /var/run/sshd
RUN echo 'root:root' | chpasswd
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

#Create the .ssh folder under root home and copy ansible control machine public key
RUN mkdir -p /root/.ssh
COPY authorized_keys /root/.ssh/authorized_keys

#This opens ups port 22 for ssh server and opens port 80 for any web servers
EXPOSE 22
EXPOSE 80 


#Configures the ssh server as startup application when containers starts
CMD ["/usr/sbin/sshd", "-D"]
