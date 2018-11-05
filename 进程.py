import os
pid =os.fork()
if pid == 0:
    print('z',os.getpid(),os.getppid())
else:
    print('f',os.getpid())


