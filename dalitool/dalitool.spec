%global pkgname dalitool
%global pkgver 2023.335
%global pkgrel 1
%global github_owner EarthScope
%global github_repo dalitool
%global debug_package %{nil}

Name:          %{pkgname}
Version:       %{pkgver}
Release:       1%{?dist}
Summary:       Tool for processing Dali binary data files
License:       GPL-3.0

URL:           https://github.com/EarthScope/dalitool

Source0:       https://github.com/%{github_owner}/%{github_repo}/archive/refs/tags/v%{pkgver}.tar.gz

BuildRequires: gcc
BuildRequires: make

%description
Dalitool is a tool for processing Dali binary data files.

%prep
%setup -c -n dalitool -a 0 -T

%build
cd $RPM_BUILD_DIR/dalitool/dalitool-%{pkgver}/
make

%install
mkdir -p %{buildroot}/%{_bindir}
cp -a $RPM_BUILD_DIR/dalitool/dalitool-%{pkgver}/dalitool %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_mandir}/man1
cp -a $RPM_BUILD_DIR/dalitool/dalitool-%{pkgver}/doc/dalitool.1 %{buildroot}/%{_mandir}/man1/dalitool.1

%files
%defattr(-,root,root)
%{_bindir}/dalitool
%defattr(-,root,root)
%{_mandir}/man1/dalitool.1*

%changelog
* Tue Feb 21 2024 John Ajera <jdcajera@gmail.com> - 2023.335
- Initial package release