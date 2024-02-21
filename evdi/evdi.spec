Name:           evdi
Version:        1.14.1
Release:        1%{?dist}
Summary:        A kernel module for DisplayLink devices

License:        GPL
URL:            https://github.com/DisplayLink/evdi
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  dkms
BuildRequires:  kernel-devel
BuildRequires:  libdrm-devel

%description
The evdi kernel module for DisplayLink devices.

%prep
%autosetup -n %{name}-%{version}

%build
cd library
make

%install
mkdir -p %{buildroot}/%{_libexecdir}/displaylink-evdi/
cp -a library/libevdi.so.%{version} %{buildroot}/%{_libexecdir}/displaylink-evdi/
ln -sf %{_libexecdir}/displaylink-evdi/libevdi.so.%{version} %{buildroot}/%{_libexecdir}/displaylink-evdi/libevdi.so

# Create DKMS configuration
mkdir -p %{buildroot}/usr/src/%{name}-%{version}/
cp -a module/* %{buildroot}/usr/src/%{name}-%{version}/
echo "PACKAGE_NAME=\"%{name}\"" > %{buildroot}/usr/src/%{name}-%{version}/dkms.conf
echo "PACKAGE_VERSION=\"%{version}\"" >> %{buildroot}/usr/src/%{name}-%{version}/dkms.conf
echo "MAKE[0]=\"make -C .\"" >> %{buildroot}/usr/src/%{name}-%{version}/dkms.conf
echo "CLEAN=\"make -C . clean\"" >> %{buildroot}/usr/src/%{name}-%{version}/dkms.conf
echo "BUILT_MODULE_NAME[0]=\"%{name}\"" >> %{buildroot}/usr/src/%{name}-%{version}/dkms.conf
echo "BUILT_MODULE_LOCATION[0]=\".\"">> %{buildroot}/usr/src/%{name}-%{version}/dkms.conf
echo "DEST_MODULE_LOCATION[0]=\"/kernel/misc\"" >> %{buildroot}/usr/src/%{name}-%{version}/dkms.conf
echo "AUTOINSTALL=\"YES\"" >> %{buildroot}/usr/src/%{name}-%{version}/dkms.conf

%files
%license LICENSE
%dir %{_prefix}/src/evdi-%{version}
%{_prefix}/src/evdi-%{version}/Kconfig
%{_prefix}/src/evdi-%{version}/LICENSE
%{_prefix}/src/evdi-%{version}/Makefile
%{_prefix}/src/evdi-%{version}/dkms.conf
%{_prefix}/src/evdi-%{version}/evdi_connector.c
%{_prefix}/src/evdi-%{version}/evdi_cursor.c
%{_prefix}/src/evdi-%{version}/evdi_cursor.h
%{_prefix}/src/evdi-%{version}/evdi_debug.c
%{_prefix}/src/evdi-%{version}/evdi_debug.h
%{_prefix}/src/evdi-%{version}/evdi_drm.h
%{_prefix}/src/evdi-%{version}/evdi_drm_drv.c
%{_prefix}/src/evdi-%{version}/evdi_drm_drv.h
%{_prefix}/src/evdi-%{version}/evdi_encoder.c
%{_prefix}/src/evdi-%{version}/evdi_fb.c
%{_prefix}/src/evdi-%{version}/evdi_gem.c
%{_prefix}/src/evdi-%{version}/evdi_i2c.c
%{_prefix}/src/evdi-%{version}/evdi_i2c.h
%{_prefix}/src/evdi-%{version}/evdi_ioc32.c
%{_prefix}/src/evdi-%{version}/evdi_modeset.c
%{_prefix}/src/evdi-%{version}/evdi_painter.c
%{_prefix}/src/evdi-%{version}/evdi_params.c
%{_prefix}/src/evdi-%{version}/evdi_params.h
%{_prefix}/src/evdi-%{version}/evdi_platform_dev.c
%{_prefix}/src/evdi-%{version}/evdi_platform_dev.h
%{_prefix}/src/evdi-%{version}/evdi_platform_drv.c
%{_prefix}/src/evdi-%{version}/evdi_platform_drv.h
%{_prefix}/src/evdi-%{version}/evdi_sysfs.c
%{_prefix}/src/evdi-%{version}/evdi_sysfs.h

%dir %{_libexecdir}/displaylink-%{name}
%{_libexecdir}/displaylink-%{name}/libevdi.so
%{_libexecdir}/displaylink-%{name}/libevdi.so.%{version}

%changelog
* Tue Dec 19 2023 John Ajera <jdcajera@gmail.com> - 1.14.1-1
- Initial package release
- modified to work with fedora39
