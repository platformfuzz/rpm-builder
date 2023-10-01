%global pkgname yq
%global pkgver 4.35.2
%global pkgrel 1
%global github_owner mikefarah
%global github_repo yq
%global github_tag v%{pgkver}

%define debug_package %{nil}

Name:       %{pkgname}
Version:    %{pkgver}
Release:    %{pkgrel}%{?dist}
Summary:    YAML processor and query tool
License:    MIT
URL:        https://github.com/%{github_owner}/%{github_repo}
Source0:    https://github.com/%{github_owner}/%{github_repo}/archive/refs/tags/v%{pkgver}.tar.gz

# Build dependencies (if any)
BuildRequires: golang >= 1.20

%description
%{pkgname} is a lightweight and portable command-line YAML processor and query tool. It allows you to easily manipulate and query YAML files using a simple and intuitive syntax.

%clean
# rm -rf %{source}
rm -rf %{buildroot}

%prep
%autosetup -n %{pkgname}-%{pkgver}

%build
# Build commands go here
go build -o %{name}

%install
# Installation commands go here
mkdir -p %{buildroot}%{_bindir}
install -D -m 755 %{name} %{buildroot}%{_bindir}

%files
# Adjust the binary location if needed
%license LICENSE
%{_bindir}/%{name}

%changelog
* Tue Sep 26 2023 John Ajera <jdcajera@gmail.com> - 4.35.2-1.el8.x86_64
- Initial build
- Update to 4.35.2 release
