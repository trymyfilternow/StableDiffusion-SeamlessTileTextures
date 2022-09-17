import os, time

# USER CHANGABLE ARGUMENTS

# Generate tiling images
tiling = True

# BEGIN RELAUNCHER PYTHON CODE

common_arguments = ""

if tiling == True:
    common_arguments += "--tiling "
else:
    inbrowser_argument = ""

n = 0
while True:
    print('Relauncher: Launching...')
    if n > 0:
        print(f'\tRelaunch count: {n}')
    os.system("python scripts/webui.py --tiling")
    print('Relauncher: Process is ending. Relaunching in 0.5s...')
    n += 1
    time.sleep(0.5)
