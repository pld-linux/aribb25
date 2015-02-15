#
# Conditional build:
%bcond_without	static_libs	# static library
#
Summary:	ARIB B25 library
Summary(pl.UTF-8):	Biblioteka ARIB B25
Name:		aribb25
Version:	0.2.6
Release:	1
License:	unknown
Group:		Libraries
Source0:	http://download.videolan.org/pub/videolan/aribb25/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	f797a8f8a1bab4361d2111046aca58b6
Patch0:		%{name}-link.patch
URL:		http://www.marumo.ne.jp/
BuildRequires:	autoconf >= 2.69
BuildRequires:	automake
BuildRequires:	libtool >= 2:2
BuildRequires:	pcsc-lite-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ARIB B25 library.

%description -l pl.UTF-8
Biblioteka ARIB B25.

%package devel
Summary:	Header files for ARIB B25 library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki ARIB B25
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	pcsc-lite-devel

%description devel
Header files for ARIB B25 library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki ARIB B25.

%package static
Summary:	Static ARIB B25 library
Summary(pl.UTF-8):	Statyczna biblioteka ARIB B25
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static ARIB B25 library.

%description static -l pl.UTF-8
Statyczna biblioteka ARIB B25.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
	%{?with_static_libs:--enable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libaribb25.la
# packaged as %doc
%{__rm} $RPM_BUILD_ROOT%{_docdir}/aribb25/README.txt

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.txt
%attr(755,root,root) %{_libdir}/libaribb25.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libaribb25.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libaribb25.so
%{_includedir}/aribb25
%{_pkgconfigdir}/aribb25.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libaribb25.a
%endif
