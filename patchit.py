# universal patch
# so that mingw64+sys2 can be used on windows to compile
import os
import re

os.chdir('r:/v')

#~ fName = r"vlib\sync\sync_win.v"
#~ print('patching %s' % fName)
#~ fIn = open(fName, 'r')
#~ fData = fIn.read()
#~ fData = fData.replace('\nfn ', '\npub fn ')
#~ fOut = open(fName, 'w')
#~ fOut.write(fData)


fName = r"Makefile"
print('patching %s' % fName)
fIn = open(fName, 'r')
fData = fIn.read()
fData = (
    fData
    .replace('''${CC} -std=gnu11 -w -o v v.c -lm''', '''${CC} -std=gnu11 -DUNICODE -D_UNICODE -w -o v v.c -lm''')
    .replace('''./v -o v compiler''', '''./v -o v2 compiler''')
    .replace('''./v -cflags '${CFLAGS}' -o v compiler''', '''./v -cflags '${CFLAGS}' -o v2 compiler''')
    .replace('''strip v''', '')
)
fOut = open(fName, 'w')
fOut.write(fData)


#~ fName = r"v.c"
#~ print('patching %s' % fName)
#~ fIn = open(fName, 'r')
#~ fData = fIn.read()
#~ fData = (
    #~ fData
    #~ .replace('''//#include <WinSock2.h>''', '''#include <WinSock2.h>''')
#~ )
#~ fOut = open(fName, 'w')
#~ fOut.write(fData)

#~ fName = r"vlib\http\http_win.v"
#~ print('patching %s' % fName)
#~ fIn = open(fName, 'r')
#~ fData = fIn.read()
#~ fData = (
    #~ fData
    #~ .replace('''module http''', '''module http\nimport time''')
    #~ .replace("pos := h.index(':')", "pos = h.index(':')")
    #~ .replace("// #include <WinInet.h>", "#include <WinInet.h>")
#~ )
#~ fOut = open(fName, 'w')
#~ fOut.write(fData)

#~ fName = r"vlib\json\json_primitives.v"
#~ print('patching %s' % fName)
#~ fIn = open(fName, 'r')
#~ fData = fIn.read()
#~ fData = fData.replace('''#flag darwin -I @VROOT/thirdparty/cJSON''', '''#flag darwin -I @VROOT/thirdparty/cJSON\n#flag windows -I @VROOT/thirdparty/cJSON''')
#~ fOut = open(fName, 'w')
#~ fOut.write(fData)

#~ fName = r"vlib\gl\gl.v"
#~ print('patching %s' % fName)
#~ fIn = open(fName, 'r')
#~ fData = fIn.read()
#~ fData = fData.replace('''#flag darwin -I @VROOT/thirdparty/glad''', '''#flag darwin -I @VROOT/thirdparty/glad\n#flag windows -I @VROOT/thirdparty/glad''')
#~ fOut = open(fName, 'w')
#~ fOut.write(fData)

#~ fName = r"vlib\stbi\stbi.v"
#~ print('patching %s' % fName)
#~ fIn = open(fName, 'r')
#~ fData = fIn.read()
#~ fData = fData.replace('''#flag darwin -I @VROOT/thirdparty/stb_image''', '''#flag darwin -I @VROOT/thirdparty/stb_image\n#flag windows -I @VROOT/thirdparty/stb_image''')
#~ fOut = open(fName, 'w')
#~ fOut.write(fData)


# multiline string in V can not be translated into C code correctly
# so I have to change the ENTER into \\n, in other words, the multiline string is converted into one line string
# this is not so simple, because there is escaped character \`
#~ fName = r"vlib\gl\1shader.v"
#~ print('patching %s' % fName)
#~ fIn = open(fName, 'r')
#~ fDataOld = fIn.read()
#~ fDataNew = fDataOld
#~ lstPos = []
#~ for match in re.finditer(r"(?<![\\]) '", fDataOld, re.IGNORECASE | re.VERBOSE | re.DOTALL):
    #~ lstPos.append(match.start())
#~ for idx in range(len(lstPos)//2):
    #~ idxStart = lstPos[idx*2] + 1
    #~ idxEnd = lstPos[idx*2+1]
    #~ tmpTxt = fDataOld[idxStart: idxEnd]
    ## print('tmpTxt=', tmpTxt)
    #~ fDataNew = fDataNew.replace(tmpTxt, tmpTxt.replace('\n', '\\n'))
#~ fOut = open(fName, 'w')
#~ fOut.write(fDataNew)
#~ ##~ print(fDataNew)

#~ fName = r"examples\VCasino\VCasino.v"
#~ print('patching %s' % fName)
#~ fIn = open(fName, 'r')
#~ fDataOld = fIn.read()
#~ fDataNew = fDataOld
#~ lstPos = []
#~ for match in re.finditer(r"(?<![\\]) '", fDataOld, re.IGNORECASE | re.VERBOSE | re.DOTALL):
    #~ lstPos.append(match.start())
#~ for idx in range(len(lstPos)//2):
    #~ idxStart = lstPos[idx*2] + 1
    #~ idxEnd = lstPos[idx*2+1]
    #~ tmpTxt = fDataOld[idxStart: idxEnd]
    ## print('tmpTxt=', tmpTxt)
    #~ fDataNew = fDataNew.replace(tmpTxt, tmpTxt.replace('\n', '\\n'))
#~ fOut = open(fName, 'w')
#~ fOut.write(fDataNew)
#~ ## print(fDataNew)

# environments specified patch
#~ fName = r"vlib\glfw\glfw.v"
#~ print('patching %s' % fName)
#~ fIn = open(fName, 'r')
#~ fData = fIn.read()
#~ fData = fData.replace('''#flag windows -I/usr/local/Cellar/glfw/3.2.1/include/''', '#flag windows -IE:/msys64/mingw64include/\n#flag windows -lglfw3')
#~ fOut = open(fName, 'w')
#~ fOut.write(fData)

#~ fName = r"vlib\gg\gg.v"
#~ print('patching %s' % fName)
#~ encoding = ''
#~ try:
    #~ fIn = open(fName, 'r')
    #~ fData = fIn.read()
    #~ fIn.close()
#~ except:
    #~ fIn = open(fName, 'r', encoding='utf8')
    #~ fData = fIn.read()
    #~ fIn.close()
    #~ encoding='utf8'

#~ fData = fData.replace('''#flag linux -I.''', '#flag linux -I.\n#flag windows  -IE:/msys64/mingw64/include/freetype2')
#~ if not encoding:
    #~ fOut = open(fName, 'w')
#~ else:
    #~ fOut = open(fName, 'w', encoding=encoding)
#~ fOut.write(fData)
