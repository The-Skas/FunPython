import threading
import time
import pdb
import random
import sys
import webbrowser as wb

class Computer:
    """ Threading example class
    
    The run() method will be started and it will run in the background
    until the application exits.
    """

    def __init__(self, interval = 1):
        """ Constructor
        
        :type interval: int
        :param interval: Check interval, in seconds
        """
        self.interval = interval
        self.__password = random.randint(1, 100000)
        self.is_hacked = False
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

    def guess_password(self, password):
        """ Hack the computer """
        if password == self.__password:
            self.is_hacked = True
            print ''
            for x in range(130):
                binary = [ int(2 * random.random()) for i in xrange(100) ]
                binary = ''.join(map(str, binary))
                print binary + 'ACCESS GRANTED: SYSTEM HACKED!'
                time.sleep(0.01)

            wb.open('https://www.youtube.com/watch?v=vYNnPx8fZBs')

    def run(self):
        """ Method that runs forever """
        print 'Hacking Computer...\\',
        while not self.is_hacked:
            syms = ['\\',
             '|',
             '/',
             '-']
            bs = '\x08'
            for _ in range(10):
                for sym in syms:
                    sys.stdout.write('\x08%s' % sym)
                    sys.stdout.flush()
                    time.sleep(0.1)


computer = Computer(1)
time.sleep(3)