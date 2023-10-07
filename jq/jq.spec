%global name      jq
%global version   1.7
%global release   1

# This is spec file maintained by developers of JQ, not by a OS distro.
# Your OS of choice will likely ignore this RPM spec file.
Summary:          Command-line JSON processor
Name:             jq
Version:          %{version}
Release:          %{release}%{?dist}
Source0:          https://github.com/jqlang/jq/archive/jq-%{version}.tar.gz
URL:              https://jqlang.github.io/jq
License:          BSD
AutoReqProv:      no

BuildRequires:    autoconf
BuildRequires:    automake
BuildRequires:    bison
BuildRequires:    flex
BuildRequires:    gcc
BuildRequires:    libtool
BuildRequires:    make
BuildRequires:    oniguruma-devel
BuildRequires:    python39
BuildRequires:    readline-devel
BuildRequires:    valgrind

Group:            Applications/System

# Disables debug packages and stripping of binaries:
%global _enable_debug_package 0
%global debug_package %{nil}
%global __os_install_post %{nil}

# Crank up the compression
%define _binary_payload w7.lzdio

%description
jq is a command-line JSON processor

%prep
%setup -c -n %{name}-%{version}

%build
cd %{_builddir}/%{name}-%{version}/%{name}-%{name}-%{version}
autoreconf -i
echo "Building in: \"$(pwd)\""
%if "%{devbuild}" == "yes"
./configure --prefix=%{_prefix} --enable-devel
%else
./configure --prefix=%{_prefix}
%endif
make

%install
echo "Installing to: \"%{buildroot}\""
cd %{_builddir}/%{name}-%{version}/%{name}-%{name}-%{version}
pwd
make install DESTDIR=%{buildroot}
%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/jq
%if "%{devbuild}" == "yes"
%{_libexecdir}/%{name}/jq_test
%{_libexecdir}/%{name}/testdata
%endif
%{_datadir}/doc/%{name}/AUTHORS
%{_datadir}/doc/%{name}/COPYING
%{_datadir}/doc/%{name}/NEWS.md
%{_datadir}/doc/%{name}/README.md
%{_datadir}/man/man1/jq.1
%{_includedir}/jq.h
%{_includedir}/jv.h
%{_prefix}/lib/libjq.a
%{_prefix}/lib/libjq.la
%{_prefix}/lib/libjq.so
%{_prefix}/lib/libjq.so.1
%{_prefix}/lib/libjq.so.1.0.4
%{_prefix}/lib/pkgconfig/libjq.pc

%pre

%post

%changelog
* Fri Oct 6 2023 John Ajera <jdcajera@gmail.com> - 1.7-1.el8.x86_64
- Initial RPM release
