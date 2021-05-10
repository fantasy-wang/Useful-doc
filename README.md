# M1_zbar

apple M1 use python zbar <br />
<br/>
For those who use apple with M1 <br />
If you want to install zbar pacage with conda, the normal way may not useful. <br />
here are the comfortable way: <br />

The anaconda environment only supports X86_64 architecture software <br />
The zbar installed by brew is a C library of the ARM64 architecture <br />

firstly, install conda-forge: <br />
secondly, install zbar using brew: <br />
```shell
arch -arm64 brew install zbar
```

thirdly, remember the path: my path is 
```shell
/opt/homebrew/Cellar/zbar/0.23.90
```

then
```shell
conda search pyzbar 
conda install pyzbar(if not work, use the next one)
pip install pyzbar
```


finally, miniforge install zbar
```shell
$ cp /opt/homebrew/Cellar/zbar/0.23.90/lib/pkgconfig/zbar.pc ~/miniforge3/lib/pkgconfig
$ cp /opt/homebrew/Cellar/zbar/0.23.90/lib/libzbar.0.dylib ~/miniforge3/lib/
$ cd ~/miniforge3/lib/
$ ln -s libzbar.0.dylib libzbar.dylib
```

<br /><br /><br /><br />

mac m1 conda环境使用zbar识别二维码的要点记录 <br />

> anaconda的环境只支持X86_64架构的软件 <br />
> brew安装的zbar是ARM64架构的C库 <br />

conda-forge的方案请参考：


安装zbar
```shell
$ brew install zbar #在arm64架构的机器用这个命令会抛出异常
$ arch -arm64 brew install zbar #这个才是正确姿势
```


安装路径大概是这个：

```shell
/opt/homebrew/Cellar/zbar/0.23.90 #记住路径，后面要用到
```

安装pyzbar
#依据miniforge3 的环境
```shell
$ conda search pyzbar #官方依据拒绝使用pip search了
$ conda install pyzbar #没有搜索到资源的话 pip install pyzbar
```

miniforeg3环境使用zbar库
```shell
$ cp /opt/homebrew/Cellar/zbar/0.23.90/lib/pkgconfig/zbar.pc ~/miniforge3/lib/pkgconfig
$ cp /opt/homebrew/Cellar/zbar/0.23.90/lib/libzbar.0.dylib ~/miniforge3/lib/
$ cd ~/miniforge3/lib/
$ ln -s libzbar.0.dylib libzbar.dylib
```

本文参考：https://www.gushiciku.cn/dl/0pAlv
