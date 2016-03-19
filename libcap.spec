Name:           libcap
Version:        2.25
Release:        13
License:        GPL-2.0 BSD-3-Clause
Summary:        Library for manipulating POSIX capabilities
Url:            http://sites.google.com/site/fullycapable/
Group:          base
Source0:         https://www.kernel.org/pub/linux/libs/security/linux-privs/libcap2/libcap-2.25.tar.xz
Patch1:         include-sys-xattr.patch
Patch2:		cflags.patch
BuildRequires:  grep
BuildRequires:  attr-dev
BuildRequires:  Linux-PAM-dev
BuildRequires:  ldd

%description
Library for manipulating POSIX capabilities.

%package dev
Summary:        Library for manipulating POSIX capabilities
Group:          devel
Requires:       %{name} = %{version}
Requires:       attr-dev

%description dev
Library for manipulating POSIX capabilities.

%package doc
Summary:        Library for manipulating POSIX capabilities
Group:          doc

%description doc
Library for manipulating POSIX capabilities.

%package bin
Summary:        Library for manipulating POSIX capabilities
Group:          base

%description bin
Library for manipulating POSIX capabilities.

%prep
%setup -q
#%patch1 -p1
%patch2 -p1

%build
make %{?_smp_mflags} lib=%{_libdir} LIBATTR=yes PAM_CAP=yes INDENT= SYSTEM_HEADERS=%{_includedir} RAISE_SETFCAP=no

%install
make install DESTDIR=%{buildroot} LIBDIR=%{_libdir} prefix=%{_prefix} SBINDIR=%{_sbindir} RAISE_SETFCAP=no

# library must have executable bits set for rpm4 ELF provides to work correctly
chmod 0755 %{buildroot}%{_libdir}/libcap.so.*

find %{buildroot} -name "*.a" -delete

#mkdir -p %{buildroot}/usr/lib64/pkgconfig/
#mv %{buildroot}/usr/pkgconfig/libcap.pc %{buildroot}/usr/lib64/pkgconfig/

%files dev
%{_includedir}/sys/capability.h
%{_libdir}/libcap.so
/usr/lib64/pkgconfig/*.pc

%files doc
%{_mandir}/man1/*.1
%{_mandir}/man8/*.8
%{_mandir}/man3/*.3

%files bin
%{_sbindir}/capsh
%{_sbindir}/getpcaps
%{_sbindir}/setcap
%{_sbindir}/getcap

%files
%{_libdir}/libcap.so.*
%{_libdir}/security/pam_cap.so

