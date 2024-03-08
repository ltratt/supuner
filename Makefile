PREFIX ?= /usr/local
BINDIR ?= ${PREFIX}/bin

MANDIR.${PREFIX} = ${PREFIX}/share/man
MANDIR./usr/local = /usr/local/man
MANDIR. = /usr/share/man
MANDIR ?= ${MANDIR.${PREFIX}}

all:
# Intentionally empty


install:
	install -d ${DESTDIR}${BINDIR}
	install -c -m 555 supuner ${DESTDIR}${BINDIR}
	install -d ${DESTDIR}${MANDIR}/man1
	install -c -m 444 supuner.1 ${DESTDIR}${MANDIR}/man1/supuner.1


clean:
# Intentionally empty


distrib:
	@read v?'supuner version: '; mkdir supuner-$$v; \
	  cp supuner supuner.1 Makefile CHANGES.md README.md test.py supuner-$$v; \
	  tar cfz supuner-$$v.tar.gz supuner-$$v; \
	  rm -rf supuner-$$v
