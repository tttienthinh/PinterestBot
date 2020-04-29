import sys
from time import sleep

while True:
    try:
        print('Hello World')
        sleep(1)
    except KeyboardInterrupt:
        sys.exit()
    except:
        print(sys.exc_info()[0])