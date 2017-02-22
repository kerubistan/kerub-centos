# kerub-centos

[Kerub](https://github.com/kerubistan/kerub) packaging for [centos](http://centos.org)

## Notes

* this package builds on tomcat since the jetty packaged in centos7 is both archaic and non-functional

* recommended pre-installation:
  * if you run kerub in a virtual machine, please add a RNG device to the VM

* recommended post-installation steps:
  * configure clustering
  * change the controller key
  * setup security
  * modify motd
  * set tomcat autostart ```sysctl enable tomcat```

