%bcond_with x

Name:           xsetroot
Version:        1.1.0
Release:        0
License:        MIT
Summary:        Utility to set X root window parameter
Url:            http://xorg.freedesktop.org/
Group:          System/X11/Utilities
Source0:        http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
Source1001: 	xsetroot.manifest
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xbitmaps)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xmuu)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
# This was part of the xorg-x11 package up to version 7.6

%if !%{with x}
ExclusiveArch:
%endif

%description
The xsetroot program allows you to tailor the appearance of the
background ("root") window on a workstation display running X.

%prep
%setup -q
cp %{SOURCE1001} .

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%manifest %{name}.manifest
%defattr(-,root,root)
%doc COPYING README
%{_bindir}/xsetroot
%{_mandir}/man1/xsetroot.1%{?ext_man}

%changelog
