Summary: Framebuffer utilities for changing video modes.
Name: fbset
Version: 2.0.19990118
Release: 2
Copyright: GPL
Group: Applications/System
Source: http://www.cs.kuleuven.ac.be/~geert/bin/fbset-19990118.tar.gz
Patch: fbset-2.0-pre-19981028.patch
BuildRoot: /var/tmp/%{name}-root

%description
fbset is a utility for querying and changing video modes of fbcon consoles.

%prep
%setup -q -n fbset
%patch -p1

%build
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/dev
mkdir -p $RPM_BUILD_ROOT/usr/sbin
mkdir -p $RPM_BUILD_ROOT/usr/man/man5
mkdir -p $RPM_BUILD_ROOT/usr/man/man8
make install PREFIX=$RPM_BUILD_ROOT
strip $RPM_BUILD_ROOT/usr/sbin/fbset
%ifarch sparc sparc64
mkdir -p $RPM_BUILD_ROOT/etc
cp etc/fb.modes.ATI $RPM_BUILD_ROOT/etc/fb.modes
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/dev/*
/usr/sbin/*
/usr/man/man[58]/*
%ifarch sparc sparc64
%config /etc/fb.modes
%endif
