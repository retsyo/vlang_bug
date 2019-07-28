cd /r
rm -rf /r/v

git clone https://github.com/vlang/v
cd v

python3 ~/_v/patchit.py

make

#~ ./v.exe -prod -o v2.exe compiler # Use V to build itself to make sure it works
mv v2.exe v.exe
strip v.exe

python3 ~/_v/compileDemo.py

python3 ~/_v/checkit.py

