Summary:	UPnP library
Summary(pl.UTF-8):	Biblioteka UPnP
Name:		gupnp
Version:	0.3
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://www.gupnp.org/sources/%{name}-%{version}.tar.gz
# Source0-md5:	cec6ee39845d77d27ce121b3aeb665e5
URL:		http://gupnp.org/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1:1.9
BuildRequires:	gssdp-devel >= 0.3
BuildRequires:	gtk-doc >= 1.0
BuildRequires:	libtool >= 2:1.5
BuildRequires:	libuuid-devel >= 1.36
BuildRequires:	pkgconfig
BuildRequires:	shared-mime-info
Requires:	shared-mime-info
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GUPnP is an object-oriented open source framework for creating UPnP
devices and control points, written in C using GObject and libsoup.
The GUPnP API is intended to be easy to use, efficient and flexible.

%description -l pl.UTF-8
GUPnp to zorientowany obiektowo, mający otwarte źródła szkielet do
tworzenia urządzeń i punktów sterujących UPnP, napisany w C z użyciem
bibliotek GObject i libsoup. API GUPnp ma być łatwe w użyciu, wydajne
i elastyczne.

%package devel
Summary:	Header files for gupnp
Summary(pl.UTF-8):	Pliki nagłówkowe gupnp
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gssdp-devel >= 0.3
Requires:	libuuid-devel >= 1.36

%description devel
This package contains header files for the Linux SDK for UPnP Devices
(gupnp).

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe dla linuksowego pakietu
programistycznego do urządzeń UPnP (gupnp).

%package static
Summary:	Static gupnp libraries
Summary(pl.UTF-8):	Statyczne biblioteki gupnp
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static gupnp libraries.

%description static -l pl.UTF-8
Statyczne biblioteki gupnp.

%package apidocs
Summary:	gupnp API documentation
Summary(pl.UTF-8):	Dokumentacja API gupnp
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
gupnp API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API gupnp.

%prep
%setup -q

%build
%{__gtkdocize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-html-dir=%{_gtkdocdir}
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
%doc ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libgupnp-1.0.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgupnp-1.0.so
%{_libdir}/libgupnp-1.0.la
%{_includedir}/gupnp-1.0
%{_pkgconfigdir}/gupnp-1.0.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgupnp-1.0.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/gupnp