Summary:	Framebuffer utilities for changing video modes
Summary(pl):	NardzÍdzie do zmieniania trybu graficznego we framebufferze
Name:		fbset
Version:	2.1
Release:	16
License:	GPL
Group:		Applications/System
Group(cs):	Aplikace/SystÈm
Group(da):	Programmer/System
Group(de):	Applikationen/System
Group(es):	Aplicaciones/Sistema
Group(fr):	Applications/SystËme
Group(is):	Forrit/Kerfisforrit
Group(it):	Applicazioni/Sistema
Group(ja):	•¢•◊•Í•±°º•∑•Á•Û/•∑•π•∆•‡
Group(no):	Applikasjoner/System
Group(pl):	Aplikacje/System
Group(pt):	AplicaÁıes/Sistema
Group(pt_BR):	AplicaÁıes/Sistema
Group(ru):	“…Ãœ÷≈Œ…—/Û…”‘≈Õ¡
Group(sl):	Programi/Sistem
Group(sv):	Till‰mpningar/System
Group(uk):	“…ÀÃ¡ƒŒ¶ “œ«“¡Õ…/Û…”‘≈Õ¡
Source0:	http://home.tvd.be/cr26864/Linux/fbdev/%{name}-%{version}.tar.gz
Source1:	%{name}.init
Source2:	%{name}.sysconfig
Patch0:		%{name}-fixmode.patch
URL:		http://home.tvd.be/cr26864/Linux/fbdev/
BuildRequires:	bison
BuildRequires:	flex
Prereq:		/sbin/chkconfig
Requires:	open
Requires:	sed
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
fbset is a utility for querying and changing video modes of fbcon
terminals.

%description -l pl
fbset jest narzÍdziem do sprawdzania i zmieniania trybu graficznego na
terminalach fbcon.

%prep
%setup -q
%patch -p1

%build
%{__make} CC="%{__cc} %{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/etc/{sysconfig,rc.d/init.d},%{_sbindir},%{_mandir}/man{5,8}}

install fbset $RPM_BUILD_ROOT%{_sbindir}
install fb.modes.5 $RPM_BUILD_ROOT%{_mandir}/man5
install fbset.8 $RPM_BUILD_ROOT%{_mandir}/man8

install etc/fb.modes.ATI $RPM_BUILD_ROOT%{_sysconfdir}/fb.modes

install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/fbset
install %{SOURCE2} $RPM_BUILD_ROOT/etc/sysconfig/fbset

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
%attr(755,root,root) %{_sbindir}/fbset
%attr(754,root,root) /etc/rc.d/init.d/fbset
%config(noreplace) %verify(not size mtime md5) /etc/sysconfig/fbset
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/fb.modes
%{_mandir}/man*/*
