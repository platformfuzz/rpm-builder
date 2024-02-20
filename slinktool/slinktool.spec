%global pkgname slinktool
%global pkgver 4.5.0
%global pkgrel 1
%global github_owner EarthScope
%global github_repo slinktool
%global debug_package %{nil}

Name:          %{pkgname}
Version:       %{pkgver}
Release:       1%{?dist}
Summary:       Command-line tool for interacting with seismological data centers
License:       GPL-3.0

URL:           https://github.com/EarthScope/slinktool

Source0:       https://github.com/%{github_owner}/%{github_repo}/archive/refs/tags/v%{pkgver}.tar.gz

BuildRequires: gcc
BuildRequires: make

%description
Slinktool is a set of tools for working with SEED Link (SLINK) servers.

%prep
%setup -c -n slinktool -a 0 -T

%build
cd $RPM_BUILD_DIR/slinktool/slinktool-%{pkgver}/
make

%install
mkdir -p %{buildroot}/%{_bindir}
cp -a $RPM_BUILD_DIR/slinktool/slinktool-%{pkgver}/slinktool %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_mandir}/man1
cp -a $RPM_BUILD_DIR/slinktool/slinktool-%{pkgver}/doc/slinktool.1 %{buildroot}/%{_mandir}/man1/slinktool.1

%files
%defattr(-,root,root)
%{_bindir}/slinktool
%defattr(-,root,root)
%{_mandir}/man1/slinktool.1*

%changelog
* Tue Feb 21 2024 John Ajera <jdcajera@gmail.com> - 4.5.0
- Initial package release