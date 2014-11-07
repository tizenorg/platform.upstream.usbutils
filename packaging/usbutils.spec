Name:           usbutils
Version:        007
Release:        0
License:        GPL-2.0+
Url:            http://www.linux-usb.org/
Source:         https://www.kernel.org/pub/linux/utils/usb/usbutils/%{name}-%{version}.tar.xz
Source1001:     usbutils.manifest

Summary:        Linux USB utilities
Group:          Base/Device Management
BuildRequires:  autoconf
BuildRequires:  libtool
BuildRequires:  pkgconfig(libusb-1.0)

%description
This package contains utilities for inspecting devices connected to a
USB bus.

%prep
%setup -q
cp %{SOURCE1001} .

%build
%configure \
    --datadir=%{_datadir}/hwdata \
    --disable-usbids

%__make %{?_smp_mflags}

%install
%make_install pkgconfigdir=/usr/share/pkgconfig

%docs_package

%files
%manifest %{name}.manifest
%license COPYING
%{_bindir}/*
%{_datadir}/*
