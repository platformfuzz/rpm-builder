%global commit      1234567890123456789012345678901234567890  # Use the actual commit hash
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           evdi
Version:        1.14.1
Release:        1%{?dist}
Summary:        A kernel module for DisplayLink devices

License:        GPL
URL:            https://github.com/DisplayLink/evdi
Source0:        %{url}/archive/%{commit}/%{name}-%{commit}.tar.gz

BuildRequires:  dkms
BuildRequires:  kernel-devel

%description
The evdi kernel module for DisplayLink devices.

%prep
%autosetup -n %{name}-%{commit}

%build
make %{?_smp_mflags} KDIR=%{_usrsrc}/kernels/$(uname -r)

%install
make INSTALL_MOD_DIR=%{buildroot}%{_kmoddir} install

git clone https://github.com/Bidski/evdi.git evdi-bidski
sudo mkdir /usr/src/evdi-1.14.1
sudo cp /evdi-bidski/module/* /usr/src/evdi-1.14.1/
sudo dkms build -m evdi -v 1.14.1 --force
sudo dkms install -m evdi -v 1.14.1

%files
%license COPYING
%{_kmoddir}/evdi.ko

%changelog
* Sun Jan 01 2023 John Doe <john.doe@example.com> - 1.14.1-1
- Initial package release