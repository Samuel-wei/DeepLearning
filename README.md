# DeepLearning
ownJune 28, 2021 

# Reference links
docker容器下配置jupyter notebook: [https://blog.csdn.net/leng_yan/article/details/87208363](https://blog.csdn.net/leng_yan/article/details/87208363)
利用Docker环境配置jupyter notebook服务器: [https://blog.csdn.net/eswai/article/details/79437428](https://blog.csdn.net/eswai/article/details/79437428)
解决远程问题： [https://blog.csdn.net/Accepted_Lam/article/details/103837677](https://blog.csdn.net/Accepted_Lam/article/details/103837677)

[GitHub fchollet / deep-learnig-with-python-notebooks](https://github.com/fchollet/deep-learning-with-python-notebooks)

# Dockerfile make custom image
## Device
Jetson AGX Xavier

git repository

samuelwei/DeepLearning/PythonDeepLearning/jupyternotebook/build/


## Build image
    
    $ sudo docker build -t pdl_jupyternotebook:r32.5.0-tf2.3-py3 -f DeepLearning/PythonDeepLearning/build/Dockerfile .
   > #在哪个文件夹内执行此命令，那么context 会推送本目录下的文件作为context文件到Docker remote端

    $ sudo docker build -t pdl_jupyternotebook:r32.5.0-tf2.3-py3 .
    
   > -t <ImageName, pythondeeplearningjupyternotebook:r32.5.0-tf2.3-py3>

**Use format:**
    
    docker build [选项] <上下文路径/URL/->
    



# Running container

## PythonDeepLearning container
   
July 10, 2021 on Jetson NX

    $ NV_GPU=0 nvidia-docker run -it --name pdl_jupyternotebook -p 2888:8888 -v /home/workspace/DeepLearning/:/home/workspace/DeepLearning/ -w /home/workspace/DeepLearning/PythonDeepLearning/ --restart=always samuelwei/pdl_jupyternotebook:r32.5.0-tf2.3-py3 /bin/bash

> NV_GPU=0 nvidia-docker
> NV_GPU=0 选择第0个GPU设备
> 用nvidia-docker才能启用GPU
> 如果不用GPU，直接用docker命令就行

> -it
> -i 以交互模式运行容器，通常与 -t 同时使用
> -t 为容器重新分配一个伪输入终端，通常与 -i 同时使用

> 启动设备就启动容器
> --restart=always

>  –name 后面跟容器的名称，notebook-server是我自定义的名字，可以随便改；

> -p 端口映射，如xxxx:yyyy将主机的xxxx端口映射到容器内的yyyy端口，jupyter notebook默认使用8888端口，7777是我自定义的，不冲突就好；

> -v 路径映射 /a : /b将主机的/a路径映射到容器的/b，根据自己的需要手动修改
> --volumes-from dbdata  使用数据卷容器dbdata，另外一个容器专门存放数据使用

> eswai/tf140py2:1.0是我使用的镜像名称和版本号，根据具体需要修改

> 启动镜像后执行的命令，即启动容器内的命令
> /bin/bash 
> /jupyter notebook &
    
    
Always restart:

    $ sudo docker update --restart=always <containerID>
    
    

May 14, 2022  on Jetson Xavier

    $ sudo NV_GPU=0 nvidia-docker run -it --name dl_jupyternotebook -p 2888:8888 -v /home/workspace/DeepLearning/:/home/workspace/DeepLearning/ -w /home/workspace/DeepLearning/ --restart=always samuelwei/pdl_jupyternotebook:r32.5.0-tf2.3-py3 /bin/bash
    
July 12, 2022 on Jetson old_AGX

    $ sudo NV_GPU=0 nvidia-docker run -it --name pdl_jupyternotebook -p 2288:22 --privileged=true -v /home/workspace/DeepLearning/:/home/workspace/DeepLearning/ -w /home/workspace/DeepLearning/ --restart=always samuelwei/pdl_jupyternotebook:r32.5.0-tf2.3-py3 /bin/bash
    
# 3 配置jupyter notebook
[https://blog.csdn.net/eswai/article/details/79437428](https://blog.csdn.net/eswai/article/details/79437428)

## 3.0 此时已经进入容器内终端，如果容器已关，请先start再attach

root@5805ad32505e:/home/workspace/DeepLearning#

## 3.1 创建存放jupyter notebook的文件夹
    $ cd /dbdata/DeepLearning/PythonDeepLearning/ #格式 $ cd <映射目标>
    $ mkdir jupyternotebook #格式 $ mkdir <存放notebook的文件夹>
此时相当于在主机的/home/eswai下创建了jupyter文件夹

## 3.2 如果容器内没有jupyter notebook，需要安装一下
    
    $ pip3 install jupyter notebook
    

## 3.3 配置jupyter notebook

    $ ipython
    
output:

    In [1]: from notebook.auth import passwd

    In [2]: passwd()
    
    Enter password: 
    Verify password: 
    Passwords do not match.
    Enter password: wmp797007
    Verify password: wmp797007
    Out[2]: 'argon2:$argon2id$v=19$m=10240,t=10,p=8$nV3BGCYeuvxTJPWMvCHWiw$vFkidx/zXHvwMNtQQ4yeIA'

    In [3]: 
    

execute:

    $ jupyter notebook --generate-config
    
output:
    
    Writing default config to: /root/.jupyter/jupyter_notebook_config.py
Change the configurate:    

    $ vim /root/.jupyter/jupyter_notebook_config.py
    
修改内容如下

    # 允许root启动
    c.NotebookApp.allow_remote_access = True #允许远程访问
    c.NotebookApp.allow_root = True
    c.NotebookApp.ip='*'#×允许任何ip访问
    c.NotebookApp.open_browser = False
    c.NotebookApp.password = 'argon2:$argon2id$v=19$m=10240,t=10,p=8$5reTOnFAQh6t6+HrgtSFFA$Q4nJ1raguPZ1Ycj3MQdgnw'
    c.NotebookApp.port =8888 #可自行指定一个端口, 访问时使用该端口
    
    
## 3.4 开启notebook
在主机终端下开启：
Usage: sudo docker exec <notebook-server containerID or container names> jupyter notebook &
    
    $ sudo docker exec ce4d755e41e5 jupyter notebook &
    $ sudo docker exec pdl_jupyternotebook jupyter notebook &

在容器下开启：
    
    $ jupyter notebook --allow-root
    $ jupyter notebook &
    $ Ctrl+c #退出jupyter

按`Ctrl+P+Q`退出容器但不关闭

## 启动使用
打开链接： http://[主机IP]:[配置映射的主机端口]/tree?token=[自定义的token]


May 14, 2022  update Xavier
[http://sharebee88.qicp.vip:28890/](http://sharebee88.qicp.vip:28890/)

August 20, 2021 NX

192.168.0.102:2888

[http://sharebee.wicp.top:57184/](http://sharebee.wicp.top:57184/)

passwd: sharebee

# Troubleshooting

## error: command 'aarch64-linux-gnu-gcc' failed with exit status 1
output error:

    aarch64-linux-gnu-gcc -pthread -DNDEBUG -g -fwrapv -O2 -Wall -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -fPIC -DUSE__THREAD -DHAVE_SYNC_SYNCHRONIZE -I/usr/include/ffi -I/usr/include/libffi -I/usr/include/python3.6m -c c/_cffi_backend.c -o build/temp.linux-aarch64-3.6/c/_cffi_backend.o
    c/_cffi_backend.c:15:10: fatal error: ffi.h: No such file or directory
     #include <ffi.h>
              ^~~~~~~
    compilation terminated.
    error: command 'aarch64-linux-gnu-gcc' failed with exit status 1
    
solving method:    
[https://raspberrypi.stackexchange.com/questions/94695/failed-building-wheel-for-cffi-on-model-3b](https://raspberrypi.stackexchange.com/questions/94695/failed-building-wheel-for-cffi-on-model-3b)

    ciffi depends on libffi, so I had to first install the libffi-dev package. Install it using:

    $ sudo apt install libffi-dev

The package might be different if you are using some other distro.

add `apt install libffi-dev` to Dockerfile command `RUN`

## ERROR: Failed to build one or more wheels

output error:

    Building wheels for collected packages: argon2-cffi, cffi
      Running setup.py bdist_wheel for argon2-cffi ... error
      Complete output from command /usr/bin/python3 -u -c "import setuptools, tokenize;__file__='/tmp/pip-build-cg8bc4i7/argon2-cffi/setup.py';f=getattr(tokenize, 'open', open)(__file__);code=f.read().replace('\r\n', '\n');f.close();exec(compile(code, __file__, 'exec'))" bdist_wheel -d /tmp/tmplaftfnq8pip-wheel- --python-tag cp36:
      ERROR: Failed to build one or more wheels
      Traceback (most recent call last):
        File "/usr/local/lib/python3.6/dist-packages/setuptools/installer.py", line 75, in fetch_build_egg
          subprocess.check_call(cmd)
        File "/usr/lib/python3.6/subprocess.py", line 311, in check_call
          raise CalledProcessError(retcode, cmd)
      subprocess.CalledProcessError: Command '['/usr/bin/python3', '-m', 'pip', '--disable-pip-version-check', 'wheel', '--no-deps', '-w', '/tmp/tmpmjdecu1n', '--quiet', 'cffi']' returned non-zero exit status 1.
      
solving method:    
[https://raspberrypi.stackexchange.com/questions/94695/failed-building-wheel-for-cffi-on-model-3b](https://raspberrypi.stackexchange.com/questions/94695/failed-building-wheel-for-cffi-on-model-3b)

    ciffi depends on libffi, so I had to first install the libffi-dev package. Install it using:

    $ sudo apt install libffi-dev

The package might be different if you are using some other distro.

add `apt install libffi-dev` to Dockerfile command `RUN`





