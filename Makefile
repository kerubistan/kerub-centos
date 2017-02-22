
clean:
	rpmdev-wipetree

all: rpms

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

