# TODO
#  - other language's descriptions look weird, backslashes and quotes
%define		SSLVER		2.8.22
%define		APACHEVER	1.3.33
%define		apxs		/usr/sbin/apxs1
%define		mod_name	ssl
Summary:	An SSL module for the Apache Web server
Summary(cs):	Modul s podporou silného ¹ifrování pro WWW server Apache
Summary(da):	Krypteringsunderstøttelse for webtjeneren Apache
Summary(de):	SSL-Modul für den Apache-Webserver
Summary(es):	Soporte criptofráfico para el servidor de WWW Apache
Summary(fr):	Un module SSL pour le serveur Web Apache
Summary(id):	Interpreter Perl untuk web server Apache
Summary(is):	Perl túlkur fyrir Apache vefþjóninn
Summary(it):	Supporto di crittografia per il server Web Apache
Summary(ja):	Apache Web ¥µ¡¼¥Ð¡¼ÍÑ¤Î°Å¹æ¥µ¥Ý¡¼¥È
Summary(nb):	Krypteringsstøtte for webtjeneren Apache
Summary(pl):	Modu³ SSL dla serwera WWW Apache
Summary(pt):	O suporte de cifra para o servidor Web Apache
Summary(ru):	íÏÄÕÌØ ÐÏÄÄÅÒÖËÉ SSL × Apache
Summary(sl):	Podpora za ¹ifriranje za spletni stre¾nik Apache
Summary(sv):	Kryptografistöd till webbservern Apache
Summary(uk):	íÏÄÕÌØ Ð¦ÄÔÒÉÍËÉ SSL × Apache
Name:		apache1-mod_%{mod_name}
Version:	%{SSLVER}_%{APACHEVER}
Release:	1.13
License:	BSD
Group:		Networking/Daemons
Source0:	http://www.modssl.org/source/mod_%{mod_name}-%{SSLVER}-%{APACHEVER}.tar.gz
# Source0-md5:	cdfdf1f576f77768c90825b43b462405
Source1:	%{name}.conf
Source2:	%{name}-server.crt
Source3:	%{name}-server.key
Source4:	%{name}-sxnet.html
Source5:	%{name}.logrotate
Patch1:		mod_%{mod_name}-cca-openssl-path.patch
Patch2:		mod_%{mod_name}-db3.patch
Patch3:		%{name}-nohttpd.patch
URL:		http://www.modssl.org/
BuildRequires:	%{apxs}
BuildRequires:	apache1-devel = %{APACHEVER}
BuildRequires:	apache1-devel >= 1.3.33-2
BuildRequires:	db-devel >= 4.1
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	openssl-tools >= 0.9.7d
BuildRequires:	sed >= 4.0
Requires(post,preun):	apache1
Requires(triggerpostun):	grep
Requires(triggerpostun):	sed >= 4.0
Requires:	apache1 >= %{APACHEVER}
Requires:	apache1 >= 1.3.33-2
Obsoletes:	mod_ssl
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_pkglibdir	%(%{apxs} -q LIBEXECDIR 2>/dev/null)
%define		_sysconfdir	%(%{apxs} -q SYSCONFDIR 2>/dev/null)

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
El módulo mod_ssl proporciona la criptografía para el servidor Web
Apache, los sockets seguros, los protocolos de la seguridad (SSL) y
de la capa tranparente (TLS).

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
Projekt mod_ssl ma za zadanie zapewniæ serwerowi WWW Apache 1.3 wysoki
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
Apache -- ÐÏÔÕÖÎÉÊ ×¦ÌØÎÏ ÒÏÚÐÏ×ÓÀÄÖÕ×ÁÎÉÊ ÓÅÒ×ÅÒ HTTP. ãÅ
ÎÁÊÐÏÐÕÌÑÒÎ¦ÛÉÊ ÓÅÒ×ÅÒ Õ Ó×¦Ô¦ (×ÉËÏÒÉÓÔÏ×Õ¤ÔØÓÑ Â¦ÌØÛ ÑË ÎÁ 50%%
ÓÅÒ×ÅÒ¦×). ãÑ ×ÅÒÓ¦Ñ Í¦ÓÔÉÔØ Ð¦ÄÔÒÉÍËÕ SSL v2, v3 ÔÁ TLS v1.

%package devel
Summary:	Header files for mod_ssl
Summary(pl):	Pliki nag³ówkowe dla mod_ssl
Group:		Development/Building
Requires:	apache1-devel >= %{APACHEVER}

%description devel
Header files for mod_ssl.

%description devel -l pl
Pliki nag³ówkowe dla mod_ssl.

%package -n apache1-mod_sxnet
Summary:	Strong Extranet module for mod_ssl and apache
Summary(fr):	Module d'Extranet Fort pour Apache et mod_ssl
Summary(pl):	Modu³ Strong Extranet dla pakietu mod_ssl i serwera WWW Apache
Group:		Networking/Daemons
Requires(triggerpostun):	%{apxs}
Requires:	apache1(EAPI) >= %{APACHEVER}
Requires:	apache1 >= 1.3.33-2

%description -n apache1-mod_sxnet
The Strong Extranet allows you to use digital certificates to
authenticate users on your web server. Typically, your users enroll in
your Strong Extranet, under your control, through the Thawte Personal
Cert System.

%description -n apache1-mod_sxnet -l fr
L'Extranet Fort vous permet d'utiliser des certificats numeriques pour
authentifier les usagers sur votre serveur web. Typiquement, vos
usagers s'enrolent dans votre Extranet Fort, sous votre controle, a
travers le Thawte Personal Cert System.

%description -n apache1-mod_sxnet -l pl
Pakiet Strong Extranet umo¿liwia u¿ywanie cyfrowych certyfikatów dla
uwierzytelniania u¿ytkowników serwera WWW. Zwykle u¿ytkownicy
rejestruj± siê pod opiek± administratora poprzez Thawte Personal Cert
System.

%prep
%setup -q -n mod_%{mod_name}-%{SSLVER}-%{APACHEVER}
%patch1 -p1
%patch2 -p1
%patch3 -p1

%{__perl} -pi -e 's@ /lib /usr/lib @ /%{_lib} /usr/%{_lib} @' pkg.sslmod/libssl.module

%build
SSL_BASE=SYSTEM; export SSL_BASE
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
install -d $RPM_BUILD_ROOT{%{_libdir}/mod_%{mod_name},%{_pkglibdir}} \
	$RPM_BUILD_ROOT%{_includedir}/apache1 \
	$RPM_BUILD_ROOT%{_sysconfdir}/conf.d \
	$RPM_BUILD_ROOT/etc/logrotate.d

install pkg.sslmod/libssl.so $RPM_BUILD_ROOT%{_pkglibdir}
install pkg.contrib/sxnet/mod_sxnet.so $RPM_BUILD_ROOT%{_pkglibdir}

install pkg.contrib/*.sh $RPM_BUILD_ROOT%{_libdir}/mod_%{mod_name}
install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/conf.d/40_mod_%{mod_name}.conf
install %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/server.crt
install %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/server.key
install %{SOURCE5} $RPM_BUILD_ROOT/etc/logrotate.d/apache-mod_%{mod_name}

cp -a pkg.ssldoc ssl-doc

install %{SOURCE4} sxnet.html
echo 'LoadModule sxnet_module	modules/mod_sxnet.so' > \
	$RPM_BUILD_ROOT%{_sysconfdir}/conf.d/90_mod_sxnet.conf

install pkg.sslmod/*.h $RPM_BUILD_ROOT%{_includedir}/apache1

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f /var/lock/subsys/apache ]; then
	/etc/rc.d/init.d/apache restart 1>&2
else
	echo "Run \"/etc/rc.d/init.d/apache start\" to start apache HTTP daemon."
fi

%preun
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/apache ]; then
		/etc/rc.d/init.d/apache restart 1>&2
	fi
fi

%triggerpostun -- apache1-mod_ssl < 2.8.22_1.3.33-1.7
if grep -q '^Include conf\.d' /etc/apache/apache.conf; then
	sed -i -e '
		/^Include.*mod_%{mod_name}.conf/d
	' /etc/apache/apache.conf
else
	# they're still using old apache.conf
	sed -i -e '
		s,^Include.*mod_%{mod_name}.conf,Include %{_sysconfdir}/conf.d/*_mod_%{mod_name}.conf,
	' /etc/apache/apache.conf
fi

%triggerpostun -- apache1-mod_sxnet < 2.8.22_1.3.33-1.9
# check that they're not using old apache.conf
if grep -q '^Include conf\.d' /etc/apache/apache.conf; then
	%{apxs} -e -A -n sxnet %{_pkglibdir}/mod_sxnet.so 1>&2
fi

%post -n apache1-mod_sxnet
if [ -f /var/lock/subsys/apache ]; then
	/etc/rc.d/init.d/apache restart 1>&2
fi

%preun -n apache1-mod_sxnet
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/apache ]; then
		/etc/rc.d/init.d/apache restart 1>&2
	fi
fi

%files
%defattr(644,root,root,755)
%doc ANNOUNCE CHANGES CREDITS NEWS README* ssl-doc
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/conf.d/*_mod_ssl.conf
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/server.crt
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/server.key
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) /etc/logrotate.d/*

%attr(755,root,root) %{_pkglibdir}/libssl.so

%dir %{_libdir}/mod_%{mod_name}
%attr(755,root,root) %{_libdir}/mod_%{mod_name}/*.sh

%files devel
%defattr(644,root,root,755)
%{_includedir}/apache1/*.h

%files -n apache1-mod_sxnet
%defattr(644,root,root,755)
%doc sxnet.html
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/conf.d/*_mod_sxnet.conf
%attr(755,root,root) %{_pkglibdir}/mod_sxnet.so
