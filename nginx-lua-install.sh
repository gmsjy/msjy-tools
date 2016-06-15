#!/bin/bash

WORKDIR=$(pwd)/

#wget http://luajit.org/download/LuaJIT-2.0.4.tar.gz
#tar zxvf LuaJIT-2.0.4.tar.gz
#cd LuaJIT-2.0.4
#./configure --prefix=/usr/local/
#make&&make install
#wget -O ngx_devel_kit-0.3.0.tar.gz   https://github.com/simpl/ngx_devel_kit/archive/v0.3.0.tar.gz 
#wget -O lua-nginx-module.0.10.5.tar.gz  https://github.com/openresty/lua-nginx-module/archive/v0.10.5.tar.gz
tar zxvf ngx_devel_kit-0.3.0.tar.gz
tar zxvf lua-nginx-module.0.10.5.tar.gz

#pcre install
wget ftp://ftp.csx.cam.ac.uk/pub/software/programming/pcre/pcre-8.37.tar.gz
tar zxvf pcre-8.37.tar.gz

#nginx install
wget http://nginx.org/download/nginx-1.10.1.tar.gz
tar zxvf nginx-1.10.1.tar.gz
cd nginx-1.10.1
export LUAJIT_LIB=/usr/local/lib
export LUAJIT_INC=/usr/local/include/luajit-2.0

./configure --prefix=/opt/nginx --add-module=${WORKDIR}/ngx_devel_kit --add-module=${WORKDIR}/lua-nginx-module  
make && make install
