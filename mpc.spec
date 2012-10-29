Summary:	Complex floating-point library with high precision and exact rounding
Name:		mpc
Version:	1.0.1
Release:	1
License:	LGPL 2.1+
Group:		Libraries
Source0:	http://multiprecision.org/mpc/download/%{name}-%{version}.tar.gz
# Source0-md5:	b32a2e1a3daa392372fbd586d1ed3679
# http://lists.gforge.inria.fr/pipermail/mpc-discuss/2011-February/000805.html
Patch0:		%{name}-configure.patch
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

%description devel
Header files for MPC library.

%prep
%setup -q
#%patch0 -p1

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
%{_libdir}/libmpc.la
%{_includedir}/mpc.h
%{_infodir}/mpc.info*

