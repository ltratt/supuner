prefix = /usr/local
exec_prefix = ${prefix}
bindir = ${exec_prefix}/bin


all:
# Intentionally empty


install:
	install -d ${DESTDIR}${bindir}
	install -c -m 555 supuner ${DESTDIR}${bindir}
	install -c -m 444 supuner.1 ${DESTDIR}${prefix}/man/man1


clean:
# Intentionally empty


distrib:
	@read v?'supuner version: '; mkdir supuner-$$v; \
      cp supuner supuner.1 supuner-$$v; \
	  cp Makefile.supuner supuner-$$v/Makefile; \
	  tar cfz supuner-$$v.tar.gz supuner-$$v; \
	  rm -rf supuner-$$v
