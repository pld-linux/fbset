Summary:	Framebuffer utilities for changing video modes.
Summary(pl):	Nardzêdzie do zmieniania trybu graficznego we framebufferze
Name:		fbset
Version:	2.0.19990118
Release:	4
License:	GPL
Group:		Applications/System
Group(pl):	Aplikacje/System
Source0:	http://www.cs.kuleuven.ac.be/~geert/bin/%{name}-19990118.tar.gz
Source1:	fbset.init
Source2:	fbset.sysconfig
URL:		http://www.cs.kuleuven.ac.be/~geert/Console/
Requires: open
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
fbset is a utility for querying and changing video modes of fbcon
consoles.

%description -l pl
fbset jest narzêdziem do sprawdzania i zmieniania trybu graficznego na
konsolach fbcon.

%prep
%setup -q -n fbset

%build
%{__make} OPTFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/etc/{sysconfig,rc.d/init.d},%{_sbindir},%{_mandir}/man{5,8}}

install -s fbset $RPM_BUILD_ROOT%{_sbindir}
install fb.modes.5 $RPM_BUILD_ROOT%{_mandir}/man5
install fbset.8 $RPM_BUILD_ROOT%{_mandir}/man8

install etc/fb.modes.ATI $RPM_BUILD_ROOT%{_sysconfdir}/fb.modes

install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/fbset
install %{SOURCE2} $RPM_BUILD_ROOT/etc/sysconfig/fbset

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man*/*

%post
/sbin/chkconfig --add fbset

%preun
if [ "$1" = "0" ]; then
	/sbin/chkconfig --del fbset
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/fbset
%attr(754,root,root) /etc/rc.d/init.d/fbset
%config(noreplace) %verify(not size mtime md5) /etc/sysconfig/fbset
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/fb.modes
%{_mandir}/man8/*
