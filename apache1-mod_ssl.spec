%define		SSLVER 2.8.8
%define		APACHEVER 1.3.24
%define 	apxs	/usr/sbin/apxs
Summary:	An SSL module for the Apache Web server
Summary(cs):	Modul s podporou silného ¹ifrování pro WWW server Apache
Summary(da):	Krypteringsunderstøttelse for webtjeneren Apache
Summary(de):	SSL-Modul für den Apache-Webserver
Summary(es):	Soporte criptofráfico para el servidor de red Apache
Summary(fr):	Un module SSL pour le serveur Web Apache
Summary(id):	Interpreter Perl untuk web server Apache
Summary(is):	Perl túlkur fyrir Apache vefþjóninn
Summary(it):	Supporto di crittografia per il server Web Apache
Summary(ja):	Apache Web ¥µ¡¼¥Ð¡¼ÍÑ¤Î°Å¹æ¥µ¥Ý¡¼¥È
Summary(no):	Krypteringsstøtte for webtjeneren Apache
Summary(pl):	Modu³ SSL dla webserwera Apache
Summary(pt):	O suporte de cifra para o servidor Web Apache
Summary(ru):	íÏÄÕÌØ ÐÏÄÄÅÒÖËÉ SSL × Apache
Summary(sl):	Podpora za ¹ifriranje za spletni stre¾nik Apache
Summary(sv):	Kryptografistöd till webbservern Apache
Summary(uk):	íÏÄÕÌØ Ð¦ÄÔÒÉÍËÉ SSL × Apache
Name:		apache-mod_ssl
Version:	%{SSLVER}_%{APACHEVER}
Release:	1
License:	BSD
Group:		Networking/Daemons
Source0:	http://www.modssl.org/source/mod_ssl-%{SSLVER}-%{APACHEVER}.tar.gz
Source1:	%{name}.conf
Source2:	%{name}-server.crt
Source3:	%{name}-server.key
Source4:	%{name}-sxnet.html
Source5:	%{name}.logrotate
Patch1:		mod_ssl-cca-openssl-path.patch
Patch2:		mod_ssl-db3.patch
URL:		http://www.modssl.org/
BuildRequires:	apache(EAPI)-devel = %{APACHEVER}
BuildRequires:	openssl-devel >= 0.9.6a
BuildRequires:	openssl-tools >= 0.9.6a
BuildRequires:	db3-devel
BuildRequires:	%{apxs}
Requires:	apache(EAPI) >= %{APACHEVER}
Provides:	mod_ssl
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	mod_ssl

%define		_pkglibdir	%(%{apxs} -q LIBEXECDIR)

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

%description -l cs
"Modul mod_ssl pro WWW server Apache umo¾òuje pou¾ití silného
¹ifrování\n" "komunikace klienta (WWW prohlí¾eè) a serveru - SSL
(Secure Sockets Layer)\n" "a TLS (Transport Layer Security)
protokoly."

%description -l de
Das mod_ssl-Projekt stellt kryptographie für den Apache 1.3-Webserver
über Secure Sockets Layer (SSL v2/v3) und Transport Layer Security
(TLS v1)-Protokolle zur Verfügung. Dazu wird das Open Source
SSL/TLS-Toolkit OpenSSL, das auf SSLeay basiert, verwendet.

%description -l es
"El módulo modd_ssl proporciona la criptografía para el servidor
Web\n" "Apache, los sockets seguros, los protocolos de la seguridad
(SSL) y de la\n" "capa tranparente (TLS)."

%description -l fr
Le projet mod_ssl fournit de la forte cryptographie pour le serveur
web Apache 1.3 via les protocoles Secure Sockets Layer (SSL v2/v3) et
Transport Layer Security (TLS v1) avec l'aide du kit d'outils Open
Source SSL/TLS, OpenSSL, base sur SSLeay d'Eric A. Young et Tim J.
Hudson.

%description -l it
"Il modulo mod_ssl fornisce un supporto di crittografia molto potente
per\n" "il server Web Apache tramite i protocolli SSL (Secure Sockets
Layer) e i\n" "protocolli TLS (Transport Layer Security)."

%description -l ja
"mod_ssl ¥â¥¸¥å¡¼¥ë¤Ï¡¢SSL (Secure Sockets Layer) ¤ª¤è¤Ó TLS
(Transport \n" "Layer Security) ¥×¥í¥È¥³¥ë¤ò²ð¤·¤Æ Apache Web
¥µ¡¼¥Ð¡¼ÍÑ¤Î¶¯ÎÏ¤Ê°Å¹æ²½\n" "µ¡Ç½¤òÄó¶¡¤·¤Þ¤¹¡£"

%description -l pl
Projekt mod_ssl ma za zadanie zapewniæ serwerowi www Apache 1.3 wysoki
poziom szyfrowania dziêki protoko³om Secure Sockets Layer (SSL v2/v3)
i Transport Layer Security (TLS v1) przy pomocy pakiety narzêdziowego
Open Source SSL/TSL -- OpenSSL, stworzonego na podstawie SSLeay Erica
A.Younga i Tima J.Hudsona.

%description -l pt
"O módulo mod_ssl oferece uma criptografia robusta para o servidor
Web\n" "Apache através dos protocolos SSL (Secure Sockets Layer) e TLS
(Transport\n" "Layer Security)."

%description -l ru
Apache -- ÍÏÝÎÙÊ Ó×ÏÂÏÄÎÏ ÒÁÓÐÒÏÓÔÒÁÎÑÅÍÙÊ ÓÅÒ×ÅÒ Á ÔÁËÖÅ É ÓÁÍÙÍ
ÐÏÐÕÌÑÒÎÙÊ × Internet'Å (ÏÎ ÉÓÐÏÌØÚÕÅÔÓÑ ÎÁ ÂÏÌÅÅ, ÞÅÍ 50%% ÓÅÒ×ÅÒÏ× ×
ÍÉÒÅ). üÔÁ ×ÅÒÓÉÑ ×ËÌÀÞÁÅÔ × ÓÅÂÑ ÐÏÄÄÅÒÖËÕ SSL v2, v3 É TLS v1.

%description -l sv
"Modulen mod_ssl förser webbservern Apache med stark kryptografi
via\n" "protokollen SSL (Secure Sockets Layer) och TLS (Transport
Layer\n" "Security)."

%description -l uk
Apache -- ÐÏÔÕÖÎÉÊ ×¦ÌØÎÏ ÒÏÚÐÏ×ÓÀÄÖÕ×ÁÎÉÊ ÓÅÒ×ÅÒ http. ãÅ
ÎÁÊÐÏÐÕÌÑÒÎ¦ÛÉÊ ÓÅÒ×ÅÒ Õ Ó×¦Ô¦ (×ÉËÏÒÉÓÔÏ×Õ¤ÔØÓÑ Â¦ÌØÛ ÑË ÎÁ 50%%
ÓÅÒ×ÅÒ¦×). ãÑ ×ÅÒÓ¦Ñ Í¦ÓÔÉÔØ Ð¦ÄÔÒÉÍËÕ SSL v2, v3 ÔÁ TLS v1.

%package -n apache-mod_sxnet
Summary:	Strong Extranet module for mod_ssl and apache
Summary(fr):	Module d'Extranet Fort pour Apache et mod_ssl
Summary(pl):	Modu³ Strong Extranet dla pakietu mod_ssl i webserwera Apache
Group:		Networking/Daemons
Requires:	apache(EAPI) >= %{APACHEVER}

%description -n apache-mod_sxnet
The Strong Extranet allows you to use digital certificates to
authenticate users on your web server. Typically, your users enroll in
your Strong Extranet, under your control, through the Thawte Personal
Cert System.

%description -n apache-mod_sxnet -l fr
L'Extranet Fort vous permet d'utiliser des certificats numeriques pour
authentifier les usagers sur votre serveur web. Typiquement, vos
usagers s'enrolent dans votre Extranet Fort, sous votre controle, a
travers le Thawte Personal Cert System.

%description -n apache-mod_sxnet -l pl
Pakiet Strong Extranet umo¿liwia u¿ywanie cyfrowych certyfikatów dla
uwierzytleniania u¿ytkowników serwera www. Zwykle u¿ytkownicy
rejestruj± siê pod opiek± administratora poprzez Thawte Personal Cert
System.

%prep
%setup -q -n mod_ssl-%{SSLVER}-%{APACHEVER}
%patch1 -p1
%patch2 -p1

%build
SSL_BASE=SYSTEM
export SSL_BASE
%configure \
	--with-apxs=%{apxs} \
	--enable-shared=ssl \
	--with-ssl=%{_prefix}
%{__make}

cd pkg.contrib
tar xvf sxnet.tar
cd sxnet
%{apxs} -DMalloc=malloc -DFree=free -I%{_includedir}/openssl -L%{_libdir} -l ssl -l crypto -c mod_sxnet.c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir}/mod_ssl,%{_pkglibdir}} \
	$RPM_BUILD_ROOT%{_sysconfdir}/httpd \
	$RPM_BUILD_ROOT/etc/logrotate.d

install pkg.sslmod/libssl.so $RPM_BUILD_ROOT%{_pkglibdir}
install pkg.contrib/sxnet/mod_sxnet.so $RPM_BUILD_ROOT%{_pkglibdir}

install pkg.contrib/*.sh $RPM_BUILD_ROOT%{_libdir}/mod_ssl
install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/httpd/mod_ssl.conf
install %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/httpd/server.crt
install %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/httpd/server.key
install %{SOURCE5} $RPM_BUILD_ROOT/etc/logrotate.d/apache-mod_ssl

mv -f pkg.ssldoc ssl-doc

install %{SOURCE4} sxnet.html

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

%preun
if [ "$1" = "0" ]; then
	grep -E -v "^Include.*mod_ssl.conf" %{_sysconfdir}/httpd/httpd.conf > \
		%{_sysconfdir}/httpd/httpd.conf.tmp
	mv -f %{_sysconfdir}/httpd/httpd.conf.tmp %{_sysconfdir}/httpd/httpd.conf
	if [ -f /var/lock/subsys/httpd ]; then
	        /etc/rc.d/init.d/httpd restart 1>&2
	fi
fi

%post -n apache-mod_sxnet
/usr/sbin/apxs -e -a -n sxnet %{_pkglibdir}/mod_sxnet.so 1>&2
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
fi

%preun -n apache-mod_sxnet
if [ "$1" = "0" ]; then
	/usr/sbin/apxs -e -A -n sxnet %{_pkglibdir}/mod_sxnet.so 1>&2
	if [ -f /var/lock/subsys/httpd ]; then
		/etc/rc.d/init.d/httpd restart 1>&2
	fi
fi
						
%files
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/httpd/mod_ssl.conf
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/httpd/server.crt
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/httpd/server.key
%attr(640,root,root) %config(noreplace) /etc/logrotate.d/*
%doc *.gz
%doc ssl-doc

%attr(755,root,root) %{_pkglibdir}/libssl.so

%dir %{_libdir}/mod_ssl
%attr(755,root,root) %{_libdir}/mod_ssl/*.sh

%files -n apache-mod_sxnet
%defattr(644,root,root,755)
%attr(755,root,root) %{_pkglibdir}/mod_sxnet.so
%doc sxnet.html

%clean
rm -rf $RPM_BUILD_ROOT
