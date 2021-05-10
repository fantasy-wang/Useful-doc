# M1_zbar
apple M1 use python zbar
For those who use apple with M1
If you want to install zbar pacage with conda, the normal way may not useful.
here are the comfortable way:

The anaconda environment only supports X86_64 architecture software
The zbar installed by brew is a C library of the ARM64 architecture

firstly, install conda-forge: 
secondly, install zbar using brew:
> arch -arm64 brew install zbar

thirdly, remember the path: my path is 
> /opt/homebrew/Cellar/zbar/0.23.90

then,
> conda search pyzbar 
> conda install pyzbar(if not work, use the next one)
> pip install pyzbar

finally, miniforge install zbar
> $ cp /opt/homebrew/Cellar/zbar/0.23.90/lib/pkgconfig/zbar.pc ~/miniforge3/lib/pkgconfig
> $ cp /opt/homebrew/Cellar/zbar/0.23.90/lib/libzbar.0.dylib ~/miniforge3/lib/
> $ cd ~/miniforge3/lib/
> $ ln -s libzbar.0.dylib libzbar.dylib
