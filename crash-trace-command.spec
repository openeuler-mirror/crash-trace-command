Name:          crash-trace-command
Version:       2.0
Release:       15
Summary:       Crash utility's trace extension module
License:       GPLv2
Source:        crash-trace-command-%{version}.tar.gz
URL:           http://people.redhat.com/anderson/extensions/crash-trace-command-%{version}.tar.gz
Buildroot:     %{_tmppath}/crash-trace-command-root
BuildRequires: zlib-devel lzo-devel snappy-devel crash-devel >= 7.2.0-2
Requires:      trace-cmd crash >= 7.2.0-2

Patch0001:     trace_compiler_warnings.patch
Patch0002:     replace_obsolete_init_and_fini.patch
Patch0003:     sigsegv_on_calloc_failure.patch
Patch0004:     initialize_trace_dat.patch
Patch0005:     ARM64.patch
Patch0006:     linux_3.10_support.patch
Patch0007:     ppc64le.patch
Patch0008:     linux_4.2_support.patch
Patch0009:     TRACE_EVENT_FL_TRACEPOINT_flag.patch
Patch0010:     big_endian_nr_pages.patch
Patch0011:     ppc64_ring_buffer_read.patch
Patch0012:     ftrace_event_call_rh_data.patch

%description
This package provides a trace extension module for the crash utility,
allowing it to read ftrace data from a core dump file.

%prep
%autosetup -n %{name}-%{version} -p1

%build
make

%install
install -d %{buildroot}%{_libdir}/crash/extensions/
cp %{_builddir}/crash-trace-command-%{version}/trace.so %{buildroot}%{_libdir}/crash/extensions/

%files
%defattr(-,root,root)
%{_libdir}/crash/extensions/trace.so
%doc COPYING

%changelog
* Sat Nov 23 2019 fengbing <fengbing7@huawei.com> - 2.0-15
- Package init