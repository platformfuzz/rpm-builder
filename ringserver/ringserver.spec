%global pkgname ringserver
%global pkgver 2020.075
%global pkgrel 1
%global github_owner EarthScope
%global github_repo ringserver
%global debug_package %{nil}

Name:          %{pkgname}
Version:       %{pkgver}
Release:       1%{?dist}
Summary:       Generic packet ring buffer with network interfaces
License:       Apache License, Version 2.0

URL:           https://github.com/EarthScope/ringserver

Source0:       https://github.com/%{github_owner}/%{github_repo}/archive/refs/tags/v%{pkgver}.tar.gz

BuildRequires: gcc
BuildRequires: make

%description
Ringserver is a tool for transporting packetized snippets of time series data.

%prep
%setup -c -n ringserver -a 0 -T

%build
cd $RPM_BUILD_DIR/ringserver/ringserver-%{pkgver}/
make

%install
mkdir -p %{buildroot}/%{_bindir}
cp -a $RPM_BUILD_DIR/ringserver/ringserver-%{pkgver}/ringserver %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_mandir}/man1
cp -a $RPM_BUILD_DIR/ringserver/ringserver-%{pkgver}/doc/ringserver.1 %{buildroot}/%{_mandir}/man1/ringserver.1
mkdir  -m 755 -p %{buildroot}/%{_sysconfdir}/
sed -e "s#^RingDirectory ring#RingDirectory %{_sharedstatedir}/ring#" < $RPM_BUILD_DIR/ringserver/%{name}-%{version}/doc/ring.conf > %{buildroot}/%{_sysconfdir}/ring.conf
mkdir  -m 755 -p %{buildroot}/%{_sharedstatedir}/ring/

%pre
if ! id ringserver >& /dev/null; then 
 useradd -c "ringserver user" -r -s /bin/false -u 350 -d / ringserver 2> /dev/null
fi

%files
%defattr(-,root,root)
%{_bindir}/ringserver
%defattr(-,root,root)
%doc %{_mandir}/man1/ringserver.1*
%config(noreplace) %{_sysconfdir}/ring.conf
%attr(-,ringserver,ringserver) %dir %{_sharedstatedir}/ring/

%changelog
* Tue Feb 21 2024 John Ajera <jdcajera@gmail.com> - 2020.075
- Initial package release