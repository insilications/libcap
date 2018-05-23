Name:           libcap
Version:        2.25
Release:        21
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
BuildRequires: gcc-dev32
BuildRequires: gcc-libgcc32
BuildRequires: gcc-libstdc++32
BuildRequires: glibc-dev32
BuildRequires: glibc-libc32

%description
Library for manipulating POSIX capabilities.

%package dev
Summary:        Library for manipulating POSIX capabilities
Group:          devel
Requires:       %{name} = %{version}
Requires:       attr-dev

%description dev
Library for manipulating POSIX capabilities.

%package lib32
Summary:        Library for manipulating POSIX capabilities
Group:          devel
Requires:       %{name} = %{version}
Requires:       attr-dev
Requires:       libcap
Provides:	libcap.so.2

%description lib32
Library for manipulating POSIX capabilities.

%package dev32
Summary:        Library for manipulating POSIX capabilities
Group:          devel
Requires:       %{name} = %{version}
Requires:       attr-dev libcap-lib32

%description dev32
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
pushd ..
cp -a libcap-%{version} build32
popd

%build
make %{?_smp_mflags} lib=%{_libdir} LIBATTR=yes PAM_CAP=yes INDENT= SYSTEM_HEADERS=%{_includedir} RAISE_SETFCAP=no

pushd ../build32/
export CFLAGS="$CFLAGS -m32"
export LDFLAGS="$LDFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
make %{?_smp_mflags} lib=/usr/lib32 LIBATTR=yes PAM_CAP=no INDENT= SYSTEM_HEADERS=%{_includedir} RAISE_SETFCAP=no CFLAGS="$CFLAGS -m32"
popd

%install
pushd ../build32/
export CFLAGS="$CFLAGS -m32"
export LDFLAGS="$LDFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
make install DESTDIR=%{buildroot} LIBDIR=/usr/lib32  prefix=%{_prefix} SBINDIR=%{_sbindir} RAISE_SETFCAP=no PAM_CAP=no
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do mv $i 32$i ; done
popd
fi
popd

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

%files dev32
/usr/lib32/libcap.so


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

%files lib32
/usr/lib32/libcap.so.*
