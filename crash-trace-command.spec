Name:          crash-trace-command
Version:       3.0
Release:       2
Summary:       Crash utility's trace extension module
License:       GPLv2
Source:        crash-trace-command-%{version}.tar.gz
URL:           http://people.redhat.com/anderson/extensions/crash-trace-command-%{version}.tar.gz
Buildroot:     %{_tmppath}/crash-trace-command-root
BuildRequires: zlib-devel lzo-devel snappy-devel crash-devel >= 7.3.0-2 gcc
Requires:      trace-cmd crash >= 7.3.0-2

Patch0001:     0001-Makefile-set-DT_SONAME-to-trace.so.patch
Patch0002:     0002-Makefile-fix-build-failure-on-aarch64-and-ppc64le.patch
Patch0003:     0001-crash-trace-command-3.0-add-loongarch64-support.patch

%description
This package provides a trace extension module for the crash utility,
allowing it to read ftrace data from a core dump file.

%prep
%autosetup -n crash-trace-%{version} -p1

%build
make

%install
install -d %{buildroot}%{_libdir}/crash/extensions/
cp %{_builddir}/crash-trace-%{version}/trace.so %{buildroot}%{_libdir}/crash/extensions/

%files
%defattr(-,root,root)
%{_libdir}/crash/extensions/trace.so
%doc COPYING

%changelog
* Mon May 16 2022 Huang Yang <huangyang@loongson.cn> - 3.0-2
- add loongarch64 support

* Tue Jan 18 2022 SimpleUpdate Robot <tc@openeuler.org> - 3.0-1
- Upgrade to version 3.0

* Mon May 31 2021 baizhonggui <baizhonggui@huawei.com> - 2.0-16
- Add gcc in BuildRequires

* Sat Nov 23 2019 fengbing <fengbing7@huawei.com> - 2.0-15
- Package init
