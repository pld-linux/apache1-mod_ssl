%define		SSLVER		2.8.28
%define		APACHEVER	1.3.37
%define		apxs		/usr/sbin/apxs1
%define		mod_name	ssl
Summary:	An SSL module for the Apache Web server
Summary(cs.UTF-8):	Modul s podporou silného šifrování pro WWW server Apache
Summary(da.UTF-8):	Krypteringsunderstøttelse for webtjeneren Apache
Summary(de.UTF-8):	SSL-Modul für den Apache-Webserver
Summary(es.UTF-8):	Soporte criptofráfico para el servidor de WWW Apache
Summary(fr.UTF-8):	Un module SSL pour le serveur Web Apache
Summary(id.UTF-8):	Interpreter Perl untuk web server Apache
Summary(is.UTF-8):	Perl túlkur fyrir Apache vefþjóninn
Summary(it.UTF-8):	Supporto di crittografia per il server Web Apache
Summary(ja.UTF-8):	Apache Web サーバー用の暗号サポート
Summary(nb.UTF-8):	Krypteringsstøtte for webtjeneren Apache
Summary(pl.UTF-8):	Moduł SSL dla serwera WWW Apache
Summary(pt.UTF-8):	O suporte de cifra para o servidor Web Apache
Summary(ru.UTF-8):	Модуль поддержки SSL в Apache
Summary(sl.UTF-8):	Podpora za šifriranje za spletni strežnik Apache
Summary(sv.UTF-8):	Kryptografistöd till webbservern Apache
Summary(uk.UTF-8):	Модуль підтримки SSL в Apache
Name:		apache1-mod_%{mod_name}
Version:	%{SSLVER}_%{APACHEVER}
Release:	4
License:	BSD
Group:		Networking/Daemons
Source0:	http://www.modssl.org/source/mod_%{mod_name}-%{SSLVER}-%{APACHEVER}.tar.gz
# Source0-md5:	5e9486a86fcd4efef395f58fd795aaea
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
BuildRequires:	db-devel >= 4.1
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	openssl-tools >= 0.9.7d
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRequires:	sed >= 4.0
Requires(triggerpostun):	grep
Requires(triggerpostun):	sed >= 4.0
Requires:	apache1-base >= %{APACHEVER}
# see the config
Requires:	apache1-mod_log_config
Requires:	apache1-mod_setenvif
Provides:	apache(mod_ssl) = %{version}-%{release}
Obsoletes:	apache-mod_ssl < 2
Obsoletes:	mod_ssl
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_pkglibdir	%(%{apxs} -q LIBEXECDIR 2>/dev/null)
%define		_sysconfdir	%(%{apxs} -q SYSCONFDIR 2>/dev/null)
%define		_pkglogdir	%(%{apxs} -q PREFIX 2>/dev/null)/logs

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

%description -l cs.UTF-8
Modul mod_ssl pro WWW server Apache umožňuje použití silného šifrování
komunikace klienta (WWW prohlížeč) a serveru - SSL (Secure Sockets
Layer) a TLS (Transport Layer Security) protokoly.

%description -l de.UTF-8
Das mod_ssl-Projekt stellt kryptographie für den Apache 1.3-Webserver
über Secure Sockets Layer (SSL v2/v3) und Transport Layer Security
(TLS v1)-Protokolle zur Verfügung. Dazu wird das Open Source
SSL/TLS-Toolkit OpenSSL, das auf SSLeay basiert, verwendet.

%description -l es.UTF-8
El módulo mod_ssl proporciona la criptografía para el servidor Web
Apache, los sockets seguros, los protocolos de la seguridad (SSL) y de
la capa tranparente (TLS).

%description -l fr.UTF-8
Le projet mod_ssl fournit de la forte cryptographie pour le serveur
web Apache 1.3 via les protocoles Secure Sockets Layer (SSL v2/v3) et
Transport Layer Security (TLS v1) avec l'aide du kit d'outils Open
Source SSL/TLS, OpenSSL, base sur SSLeay d'Eric A. Young et Tim J.
Hudson.

%description -l it.UTF-8
Il modulo mod_ssl fornisce un supporto di crittografia molto potente
per il server Web Apache tramite i protocolli SSL (Secure Sockets
Layer) e i protocolli TLS (Transport Layer Security).

%description -l ja.UTF-8
mod_ssl モジュールは、SSL (Secure Sockets Layer) および TLS (Transport
Layer Security) プロトコルを介して Apache Web サーバー用の強力な暗号化
機能を提供します。

%description -l pl.UTF-8
Projekt mod_ssl ma za zadanie zapewnić serwerowi WWW Apache 1.3 wysoki
poziom szyfrowania dzięki protokołom Secure Sockets Layer (SSL v2/v3)
i Transport Layer Security (TLS v1) przy pomocy pakiety narzędziowego
Open Source SSL/TSL -- OpenSSL, stworzonego na podstawie SSLeay Erica
A.Younga i Tima J.Hudsona.

%description -l pt.UTF-8
O módulo mod_ssl oferece uma criptografia robusta para o servidor Web
Apache através dos protocolos SSL (Secure Sockets Layer) e TLS
(Transport Layer Security).

%description -l ru.UTF-8
Apache -- мощный свободно распространяемый сервер а также и самым
популярный в Internet'е (он используется на более, чем 50%% серверов в
мире). Эта версия включает в себя поддержку SSL v2, v3 и TLS v1.

%description -l sv.UTF-8
Modulen mod_ssl förser webbservern Apache med stark kryptografi via
protokollen SSL (Secure Sockets Layer) och TLS (Transport Layer
Security).

%description -l uk.UTF-8
Apache -- потужний вільно розповсюджуваний сервер HTTP. Це
найпопулярніший сервер у світі (використовується більш як на 50%%
серверів). Ця версія містить підтримку SSL v2, v3 та TLS v1.

%package devel
Summary:	Header files for mod_ssl
Summary(pl.UTF-8):	Pliki nagłówkowe dla mod_ssl
Group:		Development/Building
Requires:	apache1-devel >= %{APACHEVER}

%description devel
Header files for mod_ssl.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla mod_ssl.

%package -n apache1-mod_sxnet
Summary:	Strong Extranet module for mod_ssl and apache
Summary(fr.UTF-8):	Module d'Extranet Fort pour Apache et mod_ssl
Summary(pl.UTF-8):	Moduł Strong Extranet dla pakietu mod_ssl i serwera WWW Apache
Group:		Networking/Daemons
Requires(triggerpostun):	grep
Requires(triggerpostun):	sed >= 4.0
Requires:	apache1(EAPI) >= %{APACHEVER}
Obsoletes:	apache-mod_sxnet < 2

%description -n apache1-mod_sxnet
The Strong Extranet allows you to use digital certificates to
authenticate users on your web server. Typically, your users enroll in
your Strong Extranet, under your control, through the Thawte Personal
Cert System.

%description -n apache1-mod_sxnet -l fr.UTF-8
L'Extranet Fort vous permet d'utiliser des certificats numeriques pour
authentifier les usagers sur votre serveur web. Typiquement, vos
usagers s'enrolent dans votre Extranet Fort, sous votre controle, a
travers le Thawte Personal Cert System.

%description -n apache1-mod_sxnet -l pl.UTF-8
Pakiet Strong Extranet umożliwia używanie cyfrowych certyfikatów dla
uwierzytelniania użytkowników serwera WWW. Zwykle użytkownicy
rejestrują się pod opieką administratora poprzez Thawte Personal Cert
System.

%prep
%setup -q -n mod_%{mod_name}-%{SSLVER}-%{APACHEVER}
%patch1 -p1
%patch2 -p1
%patch3 -p1

%{__perl} -pi -e 's@ /lib /usr/lib @ /%{_lib} /usr/%{_lib} @' pkg.sslmod/libssl.module

cd pkg.contrib
tar xvf sxnet.tar

%build
SSL_BASE=SYSTEM; export SSL_BASE
%configure \
	--with-apxs=%{apxs} \
	--enable-shared=ssl \
	--with-ssl=%{_prefix}

%{__make}

cd pkg.contrib/sxnet
%{apxs} -DMalloc=malloc -DFree=free -I%{_includedir}/openssl -L%{_libdir} -l ssl -l crypto -c mod_sxnet.c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir}/mod_%{mod_name},%{_pkglibdir},%{_pkglogdir}} \
	$RPM_BUILD_ROOT%{_includedir}/apache1 \
	$RPM_BUILD_ROOT%{_sysconfdir}/conf.d \
	$RPM_BUILD_ROOT/etc/logrotate.d

install pkg.sslmod/libssl.so $RPM_BUILD_ROOT%{_pkglibdir}
install pkg.contrib/sxnet/mod_sxnet.so $RPM_BUILD_ROOT%{_pkglibdir}

install pkg.contrib/*.sh $RPM_BUILD_ROOT%{_libdir}/mod_%{mod_name}
install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/conf.d/40_mod_%{mod_name}.conf
install %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/server.crt
install %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/server.key
install %{SOURCE5} $RPM_BUILD_ROOT/etc/logrotate.d/apache1-mod_%{mod_name}

cp -a pkg.ssldoc ssl-doc

install %{SOURCE4} sxnet.html
echo 'LoadModule sxnet_module	modules/mod_sxnet.so' > \
	$RPM_BUILD_ROOT%{_sysconfdir}/conf.d/90_mod_sxnet.conf

install pkg.sslmod/*.h $RPM_BUILD_ROOT%{_includedir}/apache1

> $RPM_BUILD_ROOT%{_pkglogdir}/ssl_engine_log
> $RPM_BUILD_ROOT%{_pkglogdir}/ssl_request_log

%clean
rm -rf $RPM_BUILD_ROOT

%post
%service -q apache restart

%postun
if [ "$1" = "0" ]; then
	%service -q apache restart
fi

%triggerpostun -- apache1-mod_ssl < 2.8.22_1.3.33-1.7
if grep -q '^Include conf\.d/\*\.conf' /etc/apache/apache.conf; then
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
	sed -i -e '/^\(Add\|Load\)Module.*mod_sxnet\.\(so\|c\)/d' /etc/apache/apache.conf
fi

%post -n apache1-mod_sxnet
%service -q apache restart

%postun -n apache1-mod_sxnet
if [ "$1" = "0" ]; then
	%service -q apache restart
fi

%files
%defattr(644,root,root,755)
%doc ANNOUNCE CHANGES CREDITS NEWS README* ssl-doc
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_ssl.conf
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/server.crt
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/server.key
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/logrotate.d/*
%attr(640,root,root) %ghost %{_pkglogdir}/*

%attr(755,root,root) %{_pkglibdir}/libssl.so

%dir %{_libdir}/mod_%{mod_name}
%attr(755,root,root) %{_libdir}/mod_%{mod_name}/*.sh

%files devel
%defattr(644,root,root,755)
%{_includedir}/apache1/*.h

%files -n apache1-mod_sxnet
%defattr(644,root,root,755)
%doc sxnet.html
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_sxnet.conf
%attr(755,root,root) %{_pkglibdir}/mod_sxnet.so
