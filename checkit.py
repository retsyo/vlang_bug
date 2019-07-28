import glob, os

os.chdir('r:/v')


for entry in glob.iglob('/v/examples/**', recursive=True):
    if os.path.isfile(entry):
        if entry.endswith('.v'):
            t = os.path.normpath(entry.replace('.v', '.exe'))
            if os.path.isfile(t):
                print('found: %s' % t)

for entry in glob.iglob('/v/**', recursive=True):
    if os.path.isfile(entry):
        if entry.endswith('test.v'):
            t = os.path.normpath(entry.replace('.v', '.exe'))
            if os.path.isfile(t):
                print('found: %s' % t)

print('\n')


for entry in glob.iglob('/v/examples/**', recursive=True):
    if os.path.isfile(entry):
        if entry.endswith('.v'):
            t = os.path.normpath(entry.replace('.v', '.exe'))
            if not os.path.isfile(t):
                print('not found: %s' % t)

for entry in glob.iglob('/v/**', recursive=True):
    if os.path.isfile(entry):
        if entry.endswith('test.v'):
            t = os.path.normpath(entry.replace('.v', '.exe'))
            if not os.path.isfile(t):
                print('not found: %s' % t)