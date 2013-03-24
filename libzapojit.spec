Summary:	GLib/GObject wrapper for the SkyDrive and Hotmail REST APIs
Name:		libzapojit
Version:	0.0.3
Release:	1
License:	LGPL v2.1
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libzapojit/0.0/%{name}-%{version}.tar.xz
# Source0-md5:	9de0d94e2c6a86852133a6f2f0b5fee1
URL:		http://live.gnome.org/Zapojit
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gnome-online-accounts-devel
BuildRequires:	gobject-introspection-devel
BuildRequires:	intltool
BuildRequires:	json-glib-devel
BuildRequires:	libsoup-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	rest-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libzapojit is a GLib/GObject wrapper for the SkyDrive and Hotmail REST
APIs.

%package devel
Summary:	Header files for libzapojit library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libzapojit library.

%package apidocs
Summary:	libzapojit API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
API documentation for libzapojit library.

%prep
%setup -q

# kill gnome common deps
sed -i -e 's/GNOME_COMPILE_WARNINGS.*//g'	\
    -i -e 's/GNOME_MAINTAINER_MODE_DEFINES//g'	\
    -i -e 's/GNOME_COMMON_INIT//g'		\
    -i -e 's/GNOME_CXX_WARNINGS.*//g'		\
    -i -e 's/GNOME_DEBUG_CHECK//g' configure.ac

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules	\
	--disable-static	\
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/libzapojit

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %ghost %{_libdir}/libzapojit-0.0.so.0
%attr(755,root,root) %{_libdir}/libzapojit-0.0.so.*.*.*
%{_libdir}/girepository-1.0/Zpj-0.0.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libzapojit-0.0.so
%{_libdir}/libzapojit-0.0.la
%{_includedir}/libzapojit-0.0
%{_pkgconfigdir}/zapojit-0.0.pc
%{_datadir}/gir-1.0/Zpj-0.0.gir

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libzapojit-0.0

