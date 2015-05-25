Summary:	Complex floating-point library with high precision and exact rounding
Name:		mpc
Version:	1.0.2
Release:	2
License:	LGPL 2.1+
Group:		Libraries
Source0:	http://multiprecision.org/mpc/download/%{name}-%{version}.tar.gz
# Source0-md5:	68fadff3358fb3e7976c7a398a0af4c3
URL:		http://multiprecision.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gmp-devel
BuildRequires:	libtool
BuildRequires:	mpfr-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The MPC library is a C library for the arithmetic of complex numbers
with arbitrarily high precision and correct rounding of the result. It
is built upon and follows the same principles as MPFR.

%package devel
Summary:	Header files for MPC library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gmp-devel
Requires:	mpfr-devel

%description devel
Header files for MPC library.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__automake}
%{__autoconf}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO
%attr(755,root,root) %ghost %{_libdir}/libmpc.so.3
%attr(755,root,root) %{_libdir}/libmpc.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmpc.so
%{_includedir}/mpc.h
%{_infodir}/mpc.info*

