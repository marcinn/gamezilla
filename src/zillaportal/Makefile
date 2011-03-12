.DEFAULT_GOAL = development
.PHONY = development clean dist configure

help:
	@echo "  development - run buildout on current code"
	@echo "  clean - rm py[co] files"
	@echo "  dist - rm eggs, parts, downloads, bootstrap.py"
	@echo "  compile - compile .py files"


bootstrap.py :
	wget http://svn.zope.org/*checkout*/zc.buildout/trunk/bootstrap/bootstrap.py

bin/buildout : bootstrap.py
	python bootstrap.py

development: bin/buildout compile 
	python bin/buildout
	@echo
	@echo "run 'make configure' to create default config files"

clean:
	find . -name '*.py[oc~]'| xargs rm -f

dist: clean
	rm -rf bin develop-eggs eggs parts .installed.cfg downloads bootstrap.py

compile:
	python -c 'import compileall;  compileall.compile_dir("./gamezilla/", force=True, quiet=True);'
	@echo
	@echo

gamezilla/development.py:
	@echo "create gamezilla/development.py"
	@echo "from settings import *" > gamezilla/development.py
	@echo "DEBUG = True" >> gamezilla/development.py
	@echo "TEMPLATE_DEBUG = DEBUG" >> gamezilla/development.py

gamezilla/production.py:
	@echo "create gamezilla/production.py"
	@echo "from settings import *" > gamezilla/production.py

configure: gamezilla/development.py
