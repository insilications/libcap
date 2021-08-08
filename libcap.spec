#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : libcap
Version  : 2.52
Release  : 303
URL      : https://www.kernel.org/pub/linux/libs/security/linux-privs/libcap2/libcap-2.52.tar.xz
Source0  : https://www.kernel.org/pub/linux/libs/security/linux-privs/libcap2/libcap-2.52.tar.xz
Summary  : capability library: includes libcap2 file caps, setcap, getcap and capsh
Group    : Development/Tools
License  : GPL-2.0
Requires: libcap-bin = %{version}-%{release}
Requires: libcap-lib = %{version}-%{release}
Requires: libcap-man = %{version}-%{release}
BuildRequires : Linux-PAM-dev
BuildRequires : Linux-PAM-dev32
BuildRequires : attr-dev
BuildRequires : gcc
BuildRequires : gcc-abi
BuildRequires : gcc-dev
BuildRequires : gcc-dev32
BuildRequires : gcc-doc
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libs-math
BuildRequires : gcc-libstdc++32
BuildRequires : gcc-libubsan
BuildRequires : gcc-locale
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : grep
BuildRequires : ldd
BuildRequires : libgcc1
BuildRequires : libstdc++
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
This is a library for getting and setting POSIX.1e (formerly POSIX 6)
draft 15 capabilities.

%package bin
Summary: bin components for the libcap package.
Group: Binaries

%description bin
bin components for the libcap package.


%package dev
Summary: dev components for the libcap package.
Group: Development
Requires: libcap-lib = %{version}-%{release}
Requires: libcap-bin = %{version}-%{release}
Provides: libcap-devel = %{version}-%{release}
Requires: libcap = %{version}-%{release}

%description dev
dev components for the libcap package.


%package dev32
Summary: dev32 components for the libcap package.
Group: Default
Requires: libcap-lib32 = %{version}-%{release}
Requires: libcap-bin = %{version}-%{release}
Requires: libcap-dev = %{version}-%{release}

%description dev32
dev32 components for the libcap package.


%package lib
Summary: lib components for the libcap package.
Group: Libraries

%description lib
lib components for the libcap package.


%package lib32
Summary: lib32 components for the libcap package.
Group: Default

%description lib32
lib32 components for the libcap package.


%package man
Summary: man components for the libcap package.
Group: Default

%description man
man components for the libcap package.


%package staticdev
Summary: staticdev components for the libcap package.
Group: Default
Requires: libcap-dev = %{version}-%{release}

%description staticdev
staticdev components for the libcap package.


%package staticdev32
Summary: staticdev32 components for the libcap package.
Group: Default
Requires: libcap-dev32 = %{version}-%{release}

%description staticdev32
staticdev32 components for the libcap package.


%prep
%setup -q -n libcap-2.52
cd %{_builddir}/libcap-2.52
pushd %{_builddir}
cp -a %{_builddir}/libcap-2.52 build32
popd

%build
unset http_proxy
unset https_proxy
unset no_proxy
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1628431898
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
## altflags1 content
export CFLAGS="-g3 -ggdb -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc -Wl,--build-id=sha1"
## -fno-tree-vectorize: disable -ftree-vectorize thus disable -ftree-loop-vectorize and -ftree-slp-vectorize
## -Ofast -ffast-math
## -funroll-loops maybe dangerous
## -Wl,-z,max-page-size=0x1000
## -pthread -lpthread
## -Wl,-Bsymbolic-functions
export CXXFLAGS="-g3 -ggdb -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -fvisibility-inlines-hidden -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc -Wl,--build-id=sha1"
#
export FCFLAGS="-g3 -ggdb -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc -Wl,--build-id=sha1"
export FFLAGS="-g3 -ggdb -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc -Wl,--build-id=sha1"
export CFFLAGS="-g3 -ggdb -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc -Wl,--build-id=sha1"
#
export LDFLAGS="-g3 -ggdb -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -static-libstdc++ -static-libgcc -Wl,--build-id=sha1"
#
export AR=/usr/bin/gcc-ar
export RANLIB=/usr/bin/gcc-ranlib
export NM=/usr/bin/gcc-nm
#
export MAKEFLAGS=%{?_smp_mflags}
#
%global _lto_cflags 1
#global _lto_cflags %{nil}
%global _disable_maintainer_mode 1
#%global _disable_maintainer_mode %{nil}
#
export CCACHE_DISABLE=true
export CCACHE_NOHASHDIR=true
export CCACHE_CPP2=true
export CCACHE_SLOPPINESS=pch_defines,time_macros,locale,file_stat_matches,file_stat_matches_ctime,include_file_ctime,include_file_mtime,modules,system_headers,clang_index_store,file_macro
#export CCACHE_SLOPPINESS=modules,include_file_mtime,include_file_ctime,time_macros,pch_defines,file_stat_matches,clang_index_store,system_headers,locale
#export CCACHE_SLOPPINESS=pch_defines,time_macros,locale,clang_index_store,file_macro
export CCACHE_DIR=/var/tmp/ccache
export CCACHE_BASEDIR=/builddir/build/BUILD
#export CCACHE_LOGFILE=/var/tmp/ccache/cache.debug
#export CCACHE_DEBUG=true
#export CCACHE_NODIRECT=true
#
export LD_LIBRARY_PATH="/usr/nvidia/lib64:/usr/nvidia/lib64/vdpau:/usr/nvidia/lib64/xorg/modules/drivers:/usr/nvidia/lib64/xorg/modules/extensions:/usr/local/cuda/lib64:/usr/lib64/haswell:/usr/lib64/dri:/usr/lib64/chromium:/usr/lib64:/usr/lib64/pulseaudio:/usr/lib64/alsa-lib:/usr/lib64/gstreamer-1.0:/usr/lib64/pipewire-0.3:/usr/lib64/spa-0.2:/usr/lib:/aot/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin:/aot/intel/oneapi/compiler/latest/linux/lib:/aot/intel/oneapi/mkl/latest/lib/intel64:/aot/intel/oneapi/tbb/latest/lib/intel64/gcc4.8:/usr/share:/usr/lib64/wine:/usr/nvidia/lib32:/usr/nvidia/lib32/vdpau:/usr/lib32:/usr/lib32/wine"
#
export LIBRARY_PATH="/usr/nvidia/lib64:/usr/nvidia/lib64/vdpau:/usr/nvidia/lib64/xorg/modules/drivers:/usr/nvidia/lib64/xorg/modules/extensions:/usr/local/cuda/lib64:/usr/lib64/haswell:/usr/lib64/dri:/usr/lib64/chromium:/usr/lib64:/usr/lib64/pulseaudio:/usr/lib64/alsa-lib:/usr/lib64/gstreamer-1.0:/usr/lib64/pipewire-0.3:/usr/lib64/spa-0.2:/usr/lib:/aot/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin:/aot/intel/oneapi/compiler/latest/linux/lib:/aot/intel/oneapi/mkl/latest/lib/intel64:/aot/intel/oneapi/tbb/latest/lib/intel64/gcc4.8:/usr/share:/usr/lib64/wine:/usr/nvidia/lib32:/usr/nvidia/lib32/vdpau:/usr/lib32:/usr/lib32/wine"
#
export PATH="/usr/lib64/ccache/bin:/usr/local/cuda/bin:/usr/nvidia/bin:/usr/bin/haswell:/usr/bin:/usr/sbin"
#
export CPATH="/usr/local/cuda/include"
#
export DISPLAY=:0
export __GL_SYNC_TO_VBLANK=0
export __GL_SYNC_DISPLAY_DEVICE=DFP-1
export VDPAU_NVIDIA_SYNC_DISPLAY_DEVICE=DFP-1
export LANG=en_US.UTF-8
export XDG_CONFIG_DIRS=/usr/share/xdg:/etc/xdg
export XDG_SEAT=seat0
export XDG_SESSION_TYPE=tty
export XDG_CURRENT_DESKTOP=KDE
export XDG_SESSION_CLASS=user
export XDG_VTNR=1
export XDG_SESSION_ID=1
export XDG_RUNTIME_DIR=/run/user/1000
export XDG_DATA_DIRS=/usr/local/share:/usr/share
export KDE_SESSION_VERSION=5
export KDE_SESSION_UID=1000
export KDE_FULL_SESSION=true
export KDE_APPLICATIONS_AS_SCOPE=1
export VDPAU_DRIVER=nvidia
export LIBVA_DRIVER_NAME=vdpau
export LIBVA_DRIVERS_PATH=/usr/lib64/dri
export GTK_RC_FILES=/etc/gtk/gtkrc
export FONTCONFIG_PATH=/usr/share/defaults/fonts
## altflags1 end
make  %{?_smp_mflags}   LIBATTR=yes PAM_CAP=yes INDENT= SYSTEM_HEADERS=/usr/include RAISE_SETFCAP=no BUILD_COPTS="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc -Wl,--build-id=sha1" LDFLAGS="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc -lpthread -Wl,--build-id=sha1" V=1 VERBOSE=1

pushd ../build32/
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
unset LD_LIBRARY_PATH
unset LIBRARY_PATH
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
unset FCFLAGS
unset FFLAGS
unset CFFLAGS
export CFLAGS="-O2 -ffat-lto-objects -fuse-linker-plugin -pipe -fPIC -m32 -mstackrealign -march=native -mtune=native"
export CXXFLAGS="-O2 -ffat-lto-objects -fuse-linker-plugin -fvisibility-inlines-hidden -pipe -fPIC -m32 -mstackrealign -march=native -mtune=native"
export LDFLAGS="-O2 -ffat-lto-objects -fuse-linker-plugin -pipe -fPIC -m32 -mstackrealign -march=native -mtune=native"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
make  %{?_smp_mflags}   LIBATTR=yes PAM_CAP=yes INDENT= SYSTEM_HEADERS=/usr/include RAISE_SETFCAP=no lib=/usr/lib32 LIBATTR=yes PAM_CAP=yes INDENT= SYSTEM_HEADERS=/usr/include RAISE_SETFCAP=no V=1 VERBOSE=1
popd

%check
export LANG=C.UTF-8
unset http_proxy
unset https_proxy
unset no_proxy
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
make test || : 
make sudotest || :

%install
export SOURCE_DATE_EPOCH=1628431898
rm -rf %{buildroot}
pushd ../build32/
%make_install32 DESTDIR=%{buildroot} prefix=/usr SBINDIR=/usr/bin RAISE_SETFCAP=no DESTDIR=%{buildroot} LIBDIR=/usr/lib32 prefix=/usr SBINDIR=/usr/bin RAISE_SETFCAP=no PAM_CAP=no
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
    pushd %{buildroot}/usr/lib32/pkgconfig
    for i in *.pc ; do ln -s $i 32$i ; done
    popd
fi
popd
%make_install DESTDIR=%{buildroot} prefix=/usr SBINDIR=/usr/bin RAISE_SETFCAP=no
## install_append content
mkdir -p %{buildroot}/usr/lib32/pkgconfig
sed 's/64/32/g' %{buildroot}/usr/lib64/pkgconfig/libcap.pc > %{buildroot}/usr/lib32/pkgconfig/libcap.pc
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/capsh
/usr/bin/getcap
/usr/bin/getpcaps
/usr/bin/setcap

%files dev
%defattr(-,root,root,-)
/usr/include/sys/capability.h
/usr/include/sys/psx_syscall.h
/usr/lib64/libcap.so
/usr/lib64/libpsx.so
/usr/lib64/pkgconfig/libcap.pc
/usr/lib64/pkgconfig/libpsx.pc
/usr/lib64/security/pam_cap.so

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libcap.so
/usr/lib32/libpsx.so
/usr/lib32/pkgconfig/32libcap.pc
/usr/lib32/pkgconfig/32libpsx.pc
/usr/lib32/pkgconfig/libcap.pc
/usr/lib32/pkgconfig/libpsx.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libcap.so.2
/usr/lib64/libcap.so.2.52
/usr/lib64/libpsx.so.2
/usr/lib64/libpsx.so.2.52

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libcap.so.2
/usr/lib32/libcap.so.2.52
/usr/lib32/libpsx.so.2
/usr/lib32/libpsx.so.2.52

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/capsh.1
/usr/share/man/man3/cap_clear.3
/usr/share/man/man3/cap_clear_flag.3
/usr/share/man/man3/cap_compare.3
/usr/share/man/man3/cap_copy_ext.3
/usr/share/man/man3/cap_copy_int.3
/usr/share/man/man3/cap_drop_bound.3
/usr/share/man/man3/cap_dup.3
/usr/share/man/man3/cap_free.3
/usr/share/man/man3/cap_from_name.3
/usr/share/man/man3/cap_from_text.3
/usr/share/man/man3/cap_func_launcher.3
/usr/share/man/man3/cap_get_bound.3
/usr/share/man/man3/cap_get_fd.3
/usr/share/man/man3/cap_get_file.3
/usr/share/man/man3/cap_get_flag.3
/usr/share/man/man3/cap_get_mode.3
/usr/share/man/man3/cap_get_pid.3
/usr/share/man/man3/cap_get_proc.3
/usr/share/man/man3/cap_get_secbits.3
/usr/share/man/man3/cap_iab.3
/usr/share/man/man3/cap_iab_fill.3
/usr/share/man/man3/cap_iab_from_text.3
/usr/share/man/man3/cap_iab_get_proc.3
/usr/share/man/man3/cap_iab_get_vector.3
/usr/share/man/man3/cap_iab_init.3
/usr/share/man/man3/cap_iab_set_proc.3
/usr/share/man/man3/cap_iab_set_vector.3
/usr/share/man/man3/cap_iab_to_text.3
/usr/share/man/man3/cap_init.3
/usr/share/man/man3/cap_launch.3
/usr/share/man/man3/cap_launcher_callback.3
/usr/share/man/man3/cap_launcher_set_chroot.3
/usr/share/man/man3/cap_launcher_set_iab.3
/usr/share/man/man3/cap_launcher_set_mode.3
/usr/share/man/man3/cap_launcher_setgroups.3
/usr/share/man/man3/cap_launcher_setuid.3
/usr/share/man/man3/cap_mode.3
/usr/share/man/man3/cap_mode_name.3
/usr/share/man/man3/cap_new_launcher.3
/usr/share/man/man3/cap_set_fd.3
/usr/share/man/man3/cap_set_file.3
/usr/share/man/man3/cap_set_flag.3
/usr/share/man/man3/cap_set_mode.3
/usr/share/man/man3/cap_set_proc.3
/usr/share/man/man3/cap_set_secbits.3
/usr/share/man/man3/cap_setgroups.3
/usr/share/man/man3/cap_setuid.3
/usr/share/man/man3/cap_size.3
/usr/share/man/man3/cap_to_name.3
/usr/share/man/man3/cap_to_text.3
/usr/share/man/man3/capgetp.3
/usr/share/man/man3/capsetp.3
/usr/share/man/man3/libcap.3
/usr/share/man/man3/libpsx.3
/usr/share/man/man3/psx_syscall.3
/usr/share/man/man3/psx_syscall3.3
/usr/share/man/man3/psx_syscall6.3
/usr/share/man/man8/getcap.8
/usr/share/man/man8/getpcaps.8
/usr/share/man/man8/setcap.8

%files staticdev
%defattr(-,root,root,-)
/usr/lib64/libcap.a
/usr/lib64/libpsx.a

%files staticdev32
%defattr(-,root,root,-)
/usr/lib32/libcap.a
/usr/lib32/libpsx.a
