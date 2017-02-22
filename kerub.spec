%global logdir		%{_localstatedir}/log/%{name}
%global datadir		%{_sharedstatedir}/%{name}
%global configdir	%{_sysconfdir}/%{name}
%global loc_configdir	%{_sysconfdir}/%{name}/local
%global cls_configdir	%{_sysconfdir}/%{name}/cluster
%global wardir		%{_datadir}/%{name}


Name:		kerub
Version:	master
Release:	0.2
Summary:	Kerub is an Infrastructure as a Service prototype

Group:		Cloud Management Tools
License:	Apache license 2.0
URL:		https://github.com/kerubistan/kerub
Source0:	https://github.com/kerubistan/%{name}/archive/%{version}.tar.gz
Source2:	ROOT.xml

BuildArch:	noarch
BuildRequires:	maven
Requires:	java-1.8.0-openjdk-headless,tomcat

%description
Kerub is an Infrastructure as a Service prototype project to demonstrate 
SLA-based workload planning

%prep
echo prep
%setup -q


%build
mvn package

%install
install -dm 775 %{buildroot}%{logdir}
install -dm 755 %{buildroot}%{datadir}
install -dm 755 %{buildroot}%{configdir}
install -dm 755 %{buildroot}%{configdir}/local
install -dm 755 %{buildroot}%{configdir}/config
install -dm 755 %{buildroot}%{loc_configdir}
install -dm 755 %{buildroot}%{cls_configdir}
install -dm 755 %{buildroot}%{wardir}
install -dm 755 %{buildroot}%{_datadir}/tomcat/conf/Catalina/localhost/
install -dm 755 %{buildroot}%{_datadir}/

install -pm 644 target/${name}*.war %{buildroot}%{wardir}/%{name}.war

install -pm 640 %{_sourcedir}/ROOT.xml %{buildroot}%{_datadir}/tomcat/conf/Catalina/localhost/
install -pm 640 %{_sourcedir}/shiro.ini %{buildroot}%{configdir}
install -pm 640 %{_sourcedir}/logback.xml %{buildroot}%{configdir}
install -pm 640 %{_sourcedir}/keystore.jks %{buildroot}%{configdir}
install -pm 640 %{_sourcedir}/kerub.properties.local %{buildroot}%{configdir}/local/kerub.properties
install -pm 640 %{_sourcedir}/kerub.properties.cluster %{buildroot}%{configdir}/cluster/kerub.properties

%files
%doc
%{_datadir}/kerub/kerub.war
%{configdir}
%config(noreplace) %{configdir}/shiro.ini
%config(noreplace) %{configdir}/logback.xml
%config(noreplace) %{configdir}/keystore.jks
%{configdir}/local
%config(noreplace) %{configdir}/local/kerub.properties
%{configdir}/cluster
%config(noreplace) %{configdir}/cluster/kerub.properties
%attr(0774, root, tomcat) %{datadir}
%attr(0774, root, tomcat) %{logdir}
%{_datadir}/tomcat/conf/Catalina/localhost/ROOT.xml
%attr(0770, root, tomcat) %{_datadir}/tomcat/conf/Catalina/localhost/ROOT.xml


%changelog

