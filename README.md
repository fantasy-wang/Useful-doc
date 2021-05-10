# M1_zbar
apple M1 use python zbar <br />
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
