Summary:	Xsp extension library
Summary(pl.UTF-8):	Biblioteka rozszerzenia Xsp
Name:		libxsp
Version:	1.2.3
Release:	1
License:	MIT-like
Group:		Libraries
Source0:	http://repository.maemo.org/pool/bora/free/source/%{name}_%{version}-4.tar.gz
# Source0-md5:	a7cee9e78e7a9bb6ed810f4f83ea1d43
URL:		http://maemo.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	xspproto >= 1.2
BuildRequires:	xorg-lib-libXext-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains Xsp extension library. There are two users for
Xsp: end-user calibration application, and the media player.

%description -l pl.UTF-8
Ten pakiet zawiera bibliotekę rozszerzenia Xsp. Są dwa zastosowania
Xsp: aplikacja użytkownika do kalibracji i odtwarzacz multimedialny.

%package devel
Summary:	Header files for Xsp library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Xsp
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xspproto >= 1.2
Requires:	xorg-lib-libXext-devel

%description devel
Header files for Xsp library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Xsp.

%package static
Summary:	Static Xsp library
Summary(pl.UTF-8):	Statyczna biblioteka Xsp
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Xsp library.

%description static -l pl.UTF-8
Statyczna biblioteka Xsp.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README
%attr(755,root,root) %{_libdir}/libXsp.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXsp.so
%{_libdir}/libXsp.la
%{_includedir}/X11/extensions/Xsp.h
%{_pkgconfigdir}/xsp.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libXsp.a
