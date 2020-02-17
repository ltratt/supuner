PREFIX ?= /usr/local
MAN_PREFIX ?= ${PREFIX}/man

all:
# Intentionally empty


install:
	install -d ${PREFIX}/bin
	install -c -m 555 supuner ${PREFIX}/bin
	install -d ${MAN_PREFIX}/man1
	install -c -m 444 supuner.1 ${MAN_PREFIX}/man1/supuner.1


clean:
# Intentionally empty


distrib:
	@read v?'supuner version: '; mkdir supuner-$$v; \
      cp supuner supuner.1 supuner-$$v; \
	  cp Makefile.supuner supuner-$$v/Makefile; \
	  tar cfz supuner-$$v.tar.gz supuner-$$v; \
	  rm -rf supuner-$$v
