%define		SSLVER 2.7.1
%define		APACHEVER 1.3.14
Summary:	An SSL module for the Apache Web server
Summary(de):	SSL-Modul fuer den Apache-Webserver
Summary(fr):	Un module SSL pour le serveur Web Apache
Summary(pl):	Modu³ SSL dla webserwera Apache
Name:		apache-mod_ssl
Version:	%{SSLVER}_%{APACHEVER}
Release:	2
Group:		Networking/Daemons
Group(de):	Netzwerkwesen/Server
Group(pl):	Sieciowe/Serwery
License:	BSD
Source0:	http://www.modssl.org/source/mod_ssl-%{SSLVER}-%{APACHEVER}.tar.gz
Source1:	%{name}.conf
Source2:	%{name}-server.crt
Source3:	%{name}-server.key
Source4:	%{name}-sxnet.html
Patch0:		mod_ssl-db3.patch
Patch1:		mod_ssl-cca-openssl-path.patch
URL:		http://www.modssl.org/
BuildRequires:	apache(EAPI)-devel = %{APACHEVER}
BuildRequires:	openssl-devel
BuildRequires:	openssl-tools
BuildRequires:	db3-devel
BuildRequires:	apache(EAPI)-devel = %{APACHEVER}
Requires:	apache(EAPI) = %{APACHEVER}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_pkglibdir	%(%{_sbindir}/apxs -q LIBEXECDIR)

%description
The mod_ssl project provides strong cryptography for the Apache 1.3
webserver via the Secure Sockets Layer (SSL v2/v3) and Transport Layer
Security (TLS v1) protocols by the help of the Open Source SSL/TLS
toolkit OpenSSL, which is based on SSLeay from Eric A. Young and Tim
J. Hudson.

The mod_ssl package was created in April 1998 by Ralf S. Engelschall
and was originally derived from software developed by Ben Laurie for
use in the Apache-SSL HTTP server project. The mod_ssl package is
licensed under a BSD-style licence, which basically means that you are
free to get and use it for commercial and non-commercial purposes.

%description -l de
Das mod_ssl-Projekt stellt kryptographie für den Apache 1.3-Webserver
über Secure Sockets Layer (SSL v2/v3) und Transport Layer Security
(TLS v1)-Protokolle zur Verfügung. Dazu wird das Open Source
SSL/TLS-Toolkit OpenSSL, das auf SSLeay basiert, verwendet.

%description -l fr
Le projet mod_ssl fournit de la forte cryptographie pour le serveur
web Apache 1.3 via les protocoles Secure Sockets Layer (SSL v2/v3) et
Transport Layer Security (TLS v1) avec l'aide du kit d'outils Open
Source SSL/TLS, OpenSSL, base sur SSLeay d'Eric A. Young et Tim J.
Hudson.

%description -l pl
Projekt mod_ssl ma za zadanie zapewniæ serwerowi www Apache 1.3 wysoki
poziom szyfrowania dziêki protoko³om Secure Sockets Layer (SSL v2/v3)
i Transport Layer Security (TLS v1) przy pomocy pakiety narzêdziowego
Open Source SSL/TSL -- OpenSSL, stworzonego na podstawie SSLeay Erica
A.Younga i Tima J.Hudsona.

%package -n apache-mod_sxnet
Summary:	Strong Extranet module for mod_ssl and apache
Summary(fr):	Module d'Extranet Fort pour Apache et mod_ssl
Summary(pl):	Modu³ Strong Extranet dla pakietu mod_ssl i webserwera Apache
Group:		Networking/Daemons
Group(de):	Netzwerkwesen/Server
Group(pl):	Sieciowe/Serwery
Requires:	apache = %{APACHEVER}

%description -n apache-mod_sxnet
The Strong Extranet allows you to use digital certificates to
authenticate users on your web server. Typically, your users enroll in
your Strong Extranet, under your control, through the Thawte Personal
Cert System.

%description -l fr -n apache-mod_sxnet
L'Extranet Fort vous permet d'utiliser des certificats numeriques pour
authentifier les usagers sur votre serveur web. Typiquement, vos
usagers s'enrolent dans votre Extranet Fort, sous votre controle, a
travers le Thawte Personal Cert System.

%description -l pl -n apache-mod_sxnet
Pakiet Strong Extranet umo¿liwia u¿ywanie cyfrowych certyfikatów dla
uwierzytleniania u¿ytkowników serwera www. Zwykle u¿ytkownicy
rejestruj± siê pod opiek± administratora poprzez Thawte Personal Cert
System.

%prep
%setup -q -n mod_ssl-%{SSLVER}-%{APACHEVER}
%patch0 -p1
%patch1 -p1

%build
SSL_BASE=SYSTEM
export SSL_BASE 
%configure \
	--with-apxs=%{_sbindir}/apxs \
	--enable-shared=ssl \
	--with-ssl=%{_prefix}
%{__make}

cd pkg.contrib
tar xvf sxnet.tar
cd sxnet
/usr/sbin/apxs -I%{_includedir}/openssl/ -L%{_libdir} -l ssl -l crypto -c mod_sxnet.c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir}/mod_ssl,%{_pkglibdir}} \
	$RPM_BUILD_ROOT%{_sysconfdir}/httpd \
	$RPM_BUILD_ROOT/home/httpd/html/docs

install pkg.sslmod/libssl.so $RPM_BUILD_ROOT%{_pkglibdir}
install pkg.contrib/sxnet/mod_sxnet.so $RPM_BUILD_ROOT%{_pkglibdir}

install pkg.contrib/*.sh $RPM_BUILD_ROOT%{_libdir}/mod_ssl
install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/httpd/mod_ssl.conf
install %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/httpd/server.crt
install %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/httpd/server.key

mv -f pkg.ssldoc ssl-doc
ln -sf %{_docdir}/%{name}-%{version}/ssl-doc \
        $RPM_BUILD_ROOT/home/httpd/html/docs/ssl-doc

install %{SOURCE4} sxnet.html
ln -sf %{_docdir}/%{name}-%{version}/sxnet.html \
        $RPM_BUILD_ROOT/home/httpd/html/docs/sxnet.html

strip --strip-unneeded $RPM_BUILD_ROOT%{_pkglibdir}/*.so

gzip -9nf ANNOUNCE CHANGES CREDITS NEWS README*

%post
if [ -f %{_sysconfdir}/httpd/httpd.conf ] && \
   ! grep -q "^Include.*/mod_ssl.conf" %{_sysconfdir}/httpd/httpd.conf; then
	echo "Include /etc/httpd/mod_ssl.conf" >> %{_sysconfdir}/httpd/httpd.conf
fi
if [ -f /var/lock/subsys/httpd ]; then
        /etc/rc.d/init.d/httpd restart 1>&2
else
        echo "Run \"/etc/rc.d/init.d/httpd start\" to start apache http daemon."
fi

%postun
grep -E -v "^Include.*mod_ssl.conf" /etc/httpd/httpd.conf > \
	/etc/httpd/httpd.conf.tmp
mv -f /etc/httpd/httpd.conf.tmp /etc/httpd/httpd.conf
if [ -f /var/lock/subsys/httpd ]; then
        /etc/rc.d/init.d/httpd restart 1>&2
fi

%files
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/httpd/mod_ssl.conf
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/httpd/server.crt
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/httpd/server.key
%doc *.gz
%doc ssl-doc
%doc /home/httpd/html/docs/ssl-doc

%attr(755,root,root) %{_pkglibdir}/libssl.so

%attr(755,root,root) %{_libdir}/mod_ssl/*.sh

%files -n apache-mod_sxnet
%defattr(644,root,root,755)
%attr(755,root,root) %{_pkglibdir}/mod_sxnet.so
%doc sxnet.html
%doc /home/httpd/html/docs/sxnet.html

%clean
rm -rf $RPM_BUILD_ROOT
