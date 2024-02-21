%global pkgname slink2dali
%global pkgver 0.8
%global pkgrel 1
%global github_owner EarthScope
%global github_repo slink2dali
%global debug_package %{nil}

Name:          %{pkgname}
Version:       %{pkgver}
Release:       1%{?dist}
Summary:       SEEDLink to DataLink client
License:       Apache License, Version 2.0

URL:           https://github.com/EarthScope/slink2dali

Source0:       https://github.com/%{github_owner}/%{github_repo}/archive/refs/tags/v%{pkgver}.tar.gz

BuildRequires: gcc
BuildRequires: make

%description
slink2dali is a tool for converting data from SEEDLink servers to DALI format.

%prep
%setup -c -n slink2dali -a 0 -T

%build
cd $RPM_BUILD_DIR/slink2dali/slink2dali-%{pkgver}/
make

%install
mkdir -p %{buildroot}/%{_bindir}
cp -a $RPM_BUILD_DIR/slink2dali/slink2dali-%{pkgver}/slink2dali %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_mandir}/man1
cp -a $RPM_BUILD_DIR/slink2dali/slink2dali-%{pkgver}/doc/slink2dali.1 %{buildroot}/%{_mandir}/man1/slink2dali.1

%files
%defattr(-,root,root)
%{_bindir}/slink2dali
%defattr(-,root,root)
%{_mandir}/man1/slink2dali.1*

%changelog
* Tue Feb 21 2024 John Ajera <jdcajera@gmail.com> - 0.8
- Initial package release