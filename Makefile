date=$(shell date +%Y%m%d)

clean:
	rpmdev-wipetree
	rm -f kerub.spec

all: rpms

kerub.spec:
	echo version will be $(date)
	cat kerub.spec.in | sed -e 's/VERSION/$(date)/g' > kerub.spec


rpms: sources kerub.spec
	rpmbuild -ba kerub.spec

rpmdirs:
	rpmdev-setuptree

sources: rpmdirs 
	spectool -g -R kerub.spec
	#TODO: this looks like I am doing half of spectool's job
	cp ROOT.xml `rpm --eval "%{_sourcedir}"`
	cp keystore.jks `rpm --eval "%{_sourcedir}"`
	cp shiro.ini `rpm --eval "%{_sourcedir}"`
	cp logback.xml `rpm --eval "%{_sourcedir}"`
	cp kerub.properties.local `rpm --eval "%{_sourcedir}"`
	cp kerub.properties.cluster `rpm --eval "%{_sourcedir}"`

