Summary:	Framebuffer utilities for changing video modes
Summary(pl):	Narzêdzie do zmieniania ustawieñ framebuffera
Name:		fbset
Version:	2.1
Release:	23
License:	GPL
Group:		Applications/System
Source0:	http://home.tvd.be/cr26864/Linux/fbdev/%{name}-%{version}.tar.gz
# Source0-md5: e547cfcbb8c1a4f2a6b8ba4acb8b7164
Source1:	%{name}.init
Source2:	%{name}.sysconfig
Source3:	%{name}-fb.modes
Patch0:		%{name}-fixmode.patch
Patch1:		%{name}-from-kgicon.patch
URL:		http://home.tvd.be/cr26864/Linux/fbdev/
BuildRequires:	bison
BuildRequires:	flex
Requires(post,preun):	/sbin/chkconfig
Requires:	open
Requires:	sed
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqfiles	/usr/sbin/modeline2fb

%description
fbset is a utility for querying and changing video modes of fbcon
terminals.

Note: modeline2fb script (which translates XFree86 modelines to
fb.modes entries) requires perl.

%description -l pl
fbset jest narzêdziem do sprawdzania i zmieniania trybu graficznego na
terminalach fbcon.

Uwaga: skrypt modeline2fb (s³u¿±cy do t³umaczenia modeline'ów XFree86
na wpisy fb.modes) wymaga perla.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__make} CC="%{__cc} %{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/{sysconfig,rc.d/init.d} \
	$RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man{5,8}}

install fbset $RPM_BUILD_ROOT%{_sbindir}
install modeline2fb $RPM_BUILD_ROOT%{_sbindir}
install fb.modes.5 $RPM_BUILD_ROOT%{_mandir}/man5
install fbset.8 $RPM_BUILD_ROOT%{_mandir}/man8

install %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/fb.modes

install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/fbset
install %{SOURCE2} $RPM_BUILD_ROOT/etc/sysconfig/fbset
rm -r etc/CVS

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig --add fbset

%preun
if [ "$1" = "0" ]; then
	/sbin/chkconfig --del fbset
fi

%files
%defattr(644,root,root,755)
%doc etc/*
%attr(755,root,root) %{_sbindir}/fbset
%attr(755,root,root) %{_sbindir}/modeline2fb
%attr(754,root,root) /etc/rc.d/init.d/fbset
%config(noreplace) %verify(not size mtime md5) /etc/sysconfig/fbset
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/fb.modes
%{_mandir}/man*/*
