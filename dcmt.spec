Name:           dcmt
Version:        0.6.2
Release:        1%{?dist}
Summary:        Dynamic Creator of Mersenne Twister PRNGs

License:        BSD
URL:            http://www.math.sci.hiroshima-u.ac.jp/~m-mat/MT/DC/dc.html
Source0:        http://www.math.sci.hiroshima-u.ac.jp/~m-mat/MT/DC/dcmt0.6.2.tgz

%description
This is a C library for "Dynamic Creator", which dynamically generates a
parameter for a random number generator. Users can specify (1) the word size w
of generated random integers (presently w=31,32 only) (2) the period (chosen
from the list of Mersenne primes below), and (3) id-number.

When these specifications are given to a function in this library, it searches
for a set of parameters (stored in a struct type named mt_struct) of a
recursion generating a random number sequence conforming to the
specification. If we specify different id-numbers, then the set of yielded
random number sequences should be highly independent.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%global debug_package %{nil}


%prep
%autosetup


%build
cd lib
make


%install
rm -rf $RPM_BUILD_ROOT
install -m 755 -d $RPM_BUILD_ROOT/%{_libdir}
install -m 644 lib/libdcmt.a $RPM_BUILD_ROOT/%{_libdir}
install -m 755 -d $RPM_BUILD_ROOT/%{_includedir}
install -m 644 include/dc.h $RPM_BUILD_ROOT/%{_includedir}


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%license LICENSE.txt
%doc README README.jp CHANGELOG
%{_libdir}/libdcmt.a

%files devel
%doc README
%doc README.jp
%{_includedir}/dc.h
%{_libdir}/libdcmt.a


%changelog
* Wed Jul 27 2016 0.6.2 Ivan Gankevich <igankevich@ya.ru>
- Packaged everything.
