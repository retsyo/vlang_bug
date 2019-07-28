import glob, os

os.chdir('r:/v')

V = 'v2.exe'
V = 'v.exe'

live = ''

lstDirs = []
lstFiles = []
for entry in glob.iglob('/v/examples/**', recursive=True):
    if os.path.isfile(entry) :
        if entry.endswith('.v'):
            lstFiles.append(os.path.normpath(entry))
            print('Compiling %s' % os.path.normpath(entry))
            if 'hot_code_reloading' in entry:
                live = '-live'
            else:
                live =''
            os.system('/v/%s %s -prod %s' % (V, live, os.path.normpath(entry)))
    else:
        lstDirs.append(os.path.normpath(entry))



for entry in glob.iglob('/v/**', recursive=True):
    if os.path.isfile(entry) :
        if entry.endswith('test.v'):
            lstFiles.append(os.path.normpath(entry))
            print('Compiling %s' % os.path.normpath(entry))
            if 'hot_code_reloading' in entry:
                live = '-live'
            else:
                live =''
            os.system('/v/%s %s -prod %s' % (V, live, os.path.normpath(entry)))
    else:
        lstDirs.append(os.path.normpath(entry))

#~ print(lstFiles)
#~ print(lstDirs)