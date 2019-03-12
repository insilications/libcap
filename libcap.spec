#
# Please don't borrow from this package / spec file, this is not a good example
#


Name:           libcap
Version:        2.26
Release:        27
License:        GPL-2.0 BSD-3-Clause
Summary:        Library for manipulating POSIX capabilities
Url:            http://sites.google.com/site/fullycapable/
Group:          base
Source0:         https://www.kernel.org/pub/linux/libs/security/linux-privs/libcap2/libcap-2.26.tar.xz
Patch1:		cflags.patch
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
Requires:       libcap = %{version}
Requires:       attr-dev

%description dev
Library for manipulating POSIX capabilities.

%package extras
Summary:        Library for manipulating POSIX capabilities
Group:          devel
Requires:       libcap = %{version}
Requires:       attr-dev

%description extras
Library for manipulating POSIX capabilities.

%package lib32
Summary:        Library for manipulating POSIX capabilities
Group:          devel
Requires:       libcap = %{version}
Requires:       attr-dev
Requires:       libcap

%description lib32
Library for manipulating POSIX capabilities.

%package dev32
Summary:        Library for manipulating POSIX capabilities
Group:          devel
Requires:       libcap = %{version}
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
%patch1 -p1
pushd ..
cp -a libcap-%{version} build32
popd

%build
make %{?_smp_mflags} lib=/usr/lib64 LIBATTR=yes PAM_CAP=yes INDENT= SYSTEM_HEADERS=/usr/include RAISE_SETFCAP=no

pushd ../build32/
export CFLAGS="$CFLAGS -m32"
export LDFLAGS="$LDFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
make %{?_smp_mflags} lib=/usr/lib32 LIBATTR=yes PAM_CAP=no INDENT= SYSTEM_HEADERS=/usr/include RAISE_SETFCAP=no CFLAGS="$CFLAGS -m32"
popd

%install
pushd ../build32/
export CFLAGS="$CFLAGS -m32"
export LDFLAGS="$LDFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
make install DESTDIR=%{buildroot} LIBDIR=/usr/lib32  prefix=/usr SBINDIR=/usr/bin RAISE_SETFCAP=no PAM_CAP=no
mkdir -p %{buildroot}/usr/lib32/pkgconfig
install -m0644 libcap/libcap.pc %{buildroot}/usr/lib32/pkgconfig/
popd

make install DESTDIR=%{buildroot} LIBDIR=/usr/lib64 prefix=/usr SBINDIR=/usr/bin RAISE_SETFCAP=no

# library must have executable bits set for rpm4 ELF provides to work correctly
chmod 0755 %{buildroot}/usr/lib64/libcap.so.*
chmod 0755 %{buildroot}/usr/lib32/libcap.so.*

#mkdir -p %{buildroot}/usr/lib64/pkgconfig/
#mv %{buildroot}/usr/pkgconfig/libcap.pc %{buildroot}/usr/lib64/pkgconfig/

%files dev
/usr/include/sys/capability.h
/usr/lib64/pkgconfig/libcap.pc
/usr/lib64/libcap.a

%files dev32
/usr/lib32/libcap.so
/usr/lib32/pkgconfig/libcap.pc
 /usr/lib32/libcap.a


%files doc
/usr/share/man/man1/*.1
/usr/share/man/man8/*.8
/usr/share/man/man3/*.3

%files bin
/usr/bin/capsh
/usr/bin/getpcaps
/usr/bin/setcap
/usr/bin/getcap

%files
/usr/lib64/libcap.so.*
/usr/lib64/security/pam_cap.so

%files extras
/usr/lib64/libcap.so

%files lib32
/usr/lib32/libcap.so.*
