%global pkgname slarchive
%global pkgver 3.2
%global pkgrel 1
%global github_owner EarthScope
%global github_repo slarchive
%global debug_package %{nil}

Name:          %{pkgname}
Version:       %{pkgver}
Release:       1%{?dist}
Summary:       SEEDLink data archiving tool
License:       Apache License, Version 2.0

URL:           https://github.com/EarthScope/slarchive

Source0:       https://github.com/%{github_owner}/%{github_repo}/archive/refs/tags/v%{pkgver}.tar.gz

BuildRequires: gcc
BuildRequires: make

%description
Slarchive is a tool for archiving data from SEEDLink servers.

%prep
%setup -c -n slarchive -a 0 -T

%build
cd $RPM_BUILD_DIR/slarchive/slarchive-%{pkgver}/
make

%install
mkdir -p %{buildroot}/%{_bindir}
cp -a $RPM_BUILD_DIR/slarchive/slarchive-%{pkgver}/slarchive %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_mandir}/man1
cp -a $RPM_BUILD_DIR/slarchive/slarchive-%{pkgver}/doc/slarchive.1 %{buildroot}/%{_mandir}/man1/slarchive.1

%files
%defattr(-,root,root)
%{_bindir}/slarchive
%defattr(-,root,root)
%{_mandir}/man1/slarchive.1*

%changelog
* Tue Feb 21 2024 John Ajera <jdcajera@gmail.com> - 3.2
- Initial package release