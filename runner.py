import platform,os

sys=platform.system()

if 'Windows' in sys:
    os.system(r'httprunner .\demo\testcases\login.yaml')
else:
    os.system(r'httprunner demo/testcases/login.yaml')




