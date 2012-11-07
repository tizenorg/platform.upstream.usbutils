Name:           usbutils
Version:        006
Release:        1
License:        GPL-2.0+
Url:            http://www.linux-usb.org/
Source:         http://downloads.sourceforge.net/linux-usb/%{name}-%{version}.tar.xz
Source1001:     usbutils.manifest

Summary:        Linux USB utilities
Group:          Applications/System
BuildRequires:  autoconf
BuildRequires:  libtool
BuildRequires:  pkgconfig(libusb-1.0)

%description
This package contains utilities for inspecting devices connected to a
USB bus.

%prep
%setup -q

%build
cp %{SOURCE1001} .
%configure \
	--datadir=%{_libdir}/usbutils

make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} pkgconfigdir=/usr/share/pkgconfig

rm -f %{buildroot}%{_libdir}/usbutils/usb.ids

%docs_package

%files
%manifest usbutils.manifest
%{_sbindir}/*
%{_bindir}/*
%{_datadir}/*
#%{_libdir}/usbutils/usb.ids
