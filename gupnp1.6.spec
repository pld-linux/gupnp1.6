#
# Conditional build:
%bcond_without	apidocs		# gi-docgen based API documentation
%bcond_without	vala		# Vala API
%bcond_without	static_libs	# static library

Summary:	UPnP library based on GObject and libsoup
Summary(pl.UTF-8):	Biblioteka UPnP oparta na bibliotekach GObject i libsoup
Name:		gupnp1.6
# note: 1.6.x is stable, 1.7.x unstable
Version:	1.6.8
Release:	2
License:	LGPL v2+
Group:		Libraries
Source0:	https://download.gnome.org/sources/gupnp/1.6/gupnp-%{version}.tar.xz
# Source0-md5:	6152851a7e731f45eaf0b77263567c23
URL:		https://wiki.gnome.org/Projects/GUPnP
BuildRequires:	docbook-dtd412-xml
BuildRequires:	docbook-dtd44-xml
BuildRequires:	docbook-dtd45-xml
BuildRequires:	docbook-style-xsl
BuildRequires:	glib2-devel >= 1:2.70
BuildRequires:	gobject-introspection-devel >= 1.36.0
BuildRequires:	gssdp1.6-devel >= 1.6.2
%{?with_apidocs:BuildRequires:	gi-docgen >= 2021.1}
BuildRequires:	libsoup3-devel >= 3.0
BuildRequires:	libxml2-devel >= 1:2.6.30
BuildRequires:	libxslt-progs
BuildRequires:	meson >= 0.54.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.042
BuildRequires:	sed >= 4.0
BuildRequires:	tar >= 1:1.22
%{?with_vala:BuildRequires:	vala >= 2:0.20}
%{?with_vala:BuildRequires:	vala-gssdp1.6 >= 1.6.2}
BuildRequires:	xz
Requires:	glib2 >= 1:2.70
Requires:	gssdp1.6 >= 1.6.2
Requires:	libsoup3 >= 3.0
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
Requires:	glib2-devel >= 1:2.70
Requires:	gssdp1.6-devel >= 1.6.2
Requires:	libsoup3-devel >= 3.0
Requires:	libxml2-devel >= 1:2.6.30

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
BuildArch:	noarch

%description apidocs
gupnp API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API gupnp.

%package -n vala-gupnp1.6
Summary:	Vala API for gupnp library
Summary(pl.UTF-8):	API języka Vala dla biblioteki gupnp
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	vala >= 2:0.20
Requires:	vala-gssdp1.6 >= 1.6.2
BuildArch:	noarch

%description -n vala-gupnp1.6
Vala API for gupnp library.

%description -n vala-gupnp1.6 -l pl.UTF-8
API języka Vala dla biblioteki gupnp.

%prep
%setup -q -n gupnp-%{version}

%build
%meson \
	%{!?with_static_libs:--default-library=shared} \
	-Dcontext_manager=network-manager \
	%{?with_apidocs:-Dgtk_doc=true}

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

%if %{with apidocs}
install -d $RPM_BUILD_ROOT%{_gidocdir}
%{__mv} $RPM_BUILD_ROOT%{_docdir}/gupnp-1.6 $RPM_BUILD_ROOT%{_gidocdir}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README.md
%attr(755,root,root) %{_bindir}/gupnp-binding-tool-1.6
%attr(755,root,root) %{_libdir}/libgupnp-1.6.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgupnp-1.6.so.0
%{_libdir}/girepository-1.0/GUPnP-1.6.typelib
%{_mandir}/man1/gupnp-binding-tool-1.6.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgupnp-1.6.so
%{_datadir}/gir-1.0/GUPnP-1.6.gir
%{_includedir}/gupnp-1.6
%{_pkgconfigdir}/gupnp-1.6.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libgupnp-1.6.a
%endif

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gidocdir}/gupnp-1.6
%endif

%if %{with vala}
%files -n vala-gupnp1.6
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/gupnp-1.6.deps
%{_datadir}/vala/vapi/gupnp-1.6.vapi
%endif
