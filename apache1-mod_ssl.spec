%define SSLVER 2.3.5
%define APACHEVER 1.3.6
Summary: An SSL module for the Apache Web server.
Summary(de): SSL-Modul fuer den Apache-Webserver
Summary(fr): Un module SSL pour le serveur Web Apache
Name: mod_ssl
Version: %{SSLVER}_%{APACHEVER}
Release: 11mdk
Group: System Environment/Daemons
Source0: http://www.modssl.org/source/mod_ssl-%{SSLVER}-%{APACHEVER}.tar.bz2
Source1: httpd.conf.ssl
Source2: server.crt
Source3: server.key
Source4: sxnet.html
Patch0: ssl.patch.bz2
Copyright: BSD
BuildRoot: /var/tmp/%{name}-root
Requires: webserver openssl

%description
The mod_ssl project provides strong cryptography for the Apache 1.3 webserver 
via the Secure Sockets Layer (SSL v2/v3) and Transport Layer Security (TLS v1) 
protocols by the help of the Open Source SSL/TLS toolkit OpenSSL, which is 
based on SSLeay from Eric A. Young and Tim J. Hudson. 

The mod_ssl package was created in April 1998 by Ralf S. Engelschall and was 
originally derived from software developed by Ben Laurie for use in the 
Apache-SSL HTTP server project. The mod_ssl package is licensed under a 
BSD-style licence, which basically means that you are free to get and use it 
for commercial and non-commercial purposes. 

%description -l de
Das mod_ssl-Projekt stellt kryptographie für den Apache 1.3-Webserver über
Secure Sockets Layer (SSL v2/v3) und Transport Layer Security (TLS
v1)-Protokolle zur Verfügung. Dazu wird das Open Source SSL/TLS-Toolkit
OpenSSL, das auf SSLeay basiert, verwendet.

%description -l fr
Le projet mod_ssl fournit de la forte cryptographie pour le serveur web
Apache 1.3 via les protocoles Secure Sockets Layer (SSL v2/v3) et Transport Layer
Security (TLS v1) avec l'aide du kit d'outils Open Source SSL/TLS, OpenSSL,
base sur SSLeay d'Eric A. Young et Tim J. Hudson.


%package sxnet
Summary: Strong Extranet module for mod_ssl and apache
Summary(fr): Module d'Extranet Fort pour Apache et mod_ssl
Group: System Environment/Daemons
%description sxnet
The Strong Extranet allows you to use digital certificates to authenticate
users on your web server. Typically, your users enroll in your Strong 
Extranet, under your control, through the Thawte Personal Cert System.  

%description -l fr
L'Extranet Fort vous permet d'utiliser des certificats numeriques pour
authentifier les usagers sur votre serveur web. Typiquement, vos usagers
s'enrolent dans votre Extranet Fort, sous votre controle, a travers le
Thawte Personal Cert System.

%prep
%setup -n mod_ssl-%{SSLVER}-%{APACHEVER}


cd pkg.sslmod
%patch -p1 

%build
export SSL_BASE=SYSTEM
CFLAGS="$RPM_OPT_FLAGS" ./configure --with-apxs=/usr/sbin/apxs
make

cd pkg.contrib
tar xvf sxnet.tar
cd sxnet
apxs -I/usr/include/openssl/ -L/usr/lib -l ssl -l crypto -c mod_sxnet.c

%install

rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/lib/apache
install -m 755 pkg.sslmod/libssl.so $RPM_BUILD_ROOT/usr/lib/apache
install -m 755 pkg.contrib/sxnet/mod_sxnet.so $RPM_BUILD_ROOT/usr/lib/apache
mkdir -p $RPM_BUILD_ROOT/usr/local/ssl/mod_ssl
install -m 755 pkg.contrib/*.sh $RPM_BUILD_ROOT/usr/local/ssl/mod_ssl
mkdir -p $RPM_BUILD_ROOT/etc/httpd/conf
install -m 644 $RPM_SOURCE_DIR/httpd.conf.ssl $RPM_BUILD_ROOT/etc/httpd/conf
install -m 644 $RPM_SOURCE_DIR/server.crt $RPM_BUILD_ROOT/etc/httpd/conf
install -m 644 $RPM_SOURCE_DIR/server.key $RPM_BUILD_ROOT/etc/httpd/conf
mkdir -p $RPM_BUILD_ROOT/home/httpd/html/ssl-doc
install -m 644 $RPM_BUILD_DIR/mod_ssl-%{SSLVER}-%{APACHEVER}/pkg.ssldoc/* $RPM_BUILD_ROOT/home/httpd/html/ssl-doc 
mkdir -p $RPM_BUILD_ROOT/home/httpd/html/sxnet
install -m 644 $RPM_SOURCE_DIR/sxnet.html $RPM_BUILD_ROOT/home/httpd/html/sxnet/index.html

%post
if [ -f /etc/httpd/conf/httpd.conf ] && ! grep -q "^Include.*httpd.conf.ssl" /etc/httpd/conf/httpd.conf; then
    echo "Include conf/httpd.conf.ssl" >> /etc/httpd/conf/httpd.conf
fi
/etc/rc.d/init.d/httpd restart

%postun
touch /etc/httpd/conf/httpd.conf.ssl
/etc/rc.d/init.d/httpd restart


%files
%defattr(-,root,root)
%dir /etc/httpd/conf
%config /etc/httpd/conf/httpd.conf.ssl
%config /etc/httpd/conf/server.crt
%config /etc/httpd/conf/server.key
%doc ANNOUNCE
%doc CHANGES
%doc CREDITS
%doc LICENSE
%doc NEWS
%doc README
%doc README.GlobalID
%doc README.Patents
%doc README.Support
%doc README.Versions
%doc README.Wishes

%dir /home/httpd
%dir /home/httpd/html
/home/httpd/html/ssl-doc

%dir /usr
%dir /usr/lib
%dir /usr/lib/apache
/usr/lib/apache/libssl.so

%dir /usr/local/ssl
%dir /usr/local/ssl/mod_ssl
/usr/local/ssl/mod_ssl/*.sh

%files sxnet
/usr/lib/apache/mod_sxnet.so
/home/httpd/html/sxnet

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Fri Jun 25 1999 Bernhard Rosenkränzer <bero@mandrakesoft.de>
- 2.3.5
- spec file cleanups

* Sat Jun 05 1999 Jean-Michel Dault <jmdault@netrevolution.com>
- moved documentation in html
- rebuilt for the new optimized apache

* Sun May 30 1999 Jean-Michel Dault <jmdault@netrevolution.com>
- updated to 2.3.1
- add fr locale
- added sxnet (Secure ExtraNet) package from Thawte

* Sun May 23 1999 Bernhard Rosenkränzer <bero@mandrakesoft.com>
- handle RPM_OPT_FLAGS
- add de locale
- don't require openssl-devel
