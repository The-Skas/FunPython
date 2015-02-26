import pip


def install(package):
	pip.main(['install', package])

install('gitpython')
install('http://www.pygame.org/ftp/pygame-1.9.2a0.win32-py2.7.msi')
