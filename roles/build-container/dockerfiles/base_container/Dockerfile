FROM centos:7
MAINTAINER G.CUPILLARD (Sogeti France)

RUN yum update -y 
RUN yum install epel-release -y 
RUN yum install python-pip gcc python-devel git cmake3 -y
RUN pip install virtualenv
RUN virtualenv /root/venv
RUN /root/venv/bin/pip install pandas scipy peakutils matplotlib statsmodels pyyaml datetime cython pystan seaborn keras
RUN /root/venv/bin/pip install influxdb
#RUN /root/venv/bin/pip install fbpropher
# Build and install lingpuarray for Theano
# RUN git clone https://github.com/Theano/libgpuarray.git  && cd ./libgpuarray && git checkout tags/v0.6.2 -b v0.6.2 && mkdir Build && cd ./Build && cmake .. -DCMAKE_BUILD_TYPE=Release && make && make install && cd .. && python setup.py build && python setup.py install

COPY internal-lib/ano  /root/venv/lib/python2.7/ano
COPY internal-lib/config  /root/venv/lib/python2.7/config
COPY internal-lib/influxds  /root/venv/lib/python2.7/influxds
COPY internal-lib/test  /root/venv/lib/python2.7/test
COPY internal-lib/trend  /root/venv/lib/python2.7/trend
COPY internal-lib/utils  /root/venv/lib/python2.7/utils

WORKDIR /root/
EXPOSE 6500
