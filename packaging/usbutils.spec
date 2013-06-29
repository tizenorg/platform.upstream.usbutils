Name:           usbutils
Version:        006
Release:        1
License:        GPL-2.0+
Url:            http://www.linux-usb.org/
Source:         http://downloads.sourceforge.net/linux-usb/%{name}-%{version}.tar.xz
Source1001: 	usbutils.manifest

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

make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} pkgconfigdir=/usr/share/pkgconfig

%docs_package

%files
%manifest %{name}.manifest
%license COPYING
%{_bindir}/*
%{_datadir}/*
