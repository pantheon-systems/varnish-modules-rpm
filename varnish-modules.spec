%define datecode  %(date +%Y%m%d%H%M)

%define nr_ver  0.9.1
%define release_number %{datecode}

Name:		varnish-modules
Version:	%{nr_ver}
Release:	%{release_number}%{dist}
Summary:	A collection of modules ("vmods") extending Varnish.
License:	GPL
URL:        https://github.com/varnish/varnish-modules

Source0:	https://download.varnish-software.com/varnish-modules/varnish-modules-%{nr_ver}.tar.gz

BuildRequires:  varnish-libs-devel

%description
This is a collection of modules ("vmods") extending Varnish VCL used for describing HTTP request/response policies with additional capabilities.
https://github.com/varnish/varnish-modules

%prep
%setup -n varnish-modules-%{nr_ver}

%build
./configure && make

%install
make install DESTDIR=%{buildroot}

%files
/usr/lib64/varnish/vmods/libvmod_cookie.la
/usr/lib64/varnish/vmods/libvmod_cookie.so
/usr/lib64/varnish/vmods/libvmod_header.la
/usr/lib64/varnish/vmods/libvmod_header.so
/usr/lib64/varnish/vmods/libvmod_saintmode.la
/usr/lib64/varnish/vmods/libvmod_saintmode.so
/usr/lib64/varnish/vmods/libvmod_softpurge.la
/usr/lib64/varnish/vmods/libvmod_softpurge.so
/usr/lib64/varnish/vmods/libvmod_tcp.la
/usr/lib64/varnish/vmods/libvmod_tcp.so
/usr/lib64/varnish/vmods/libvmod_var.la
/usr/lib64/varnish/vmods/libvmod_var.so
/usr/lib64/varnish/vmods/libvmod_vsthrottle.la
/usr/lib64/varnish/vmods/libvmod_vsthrottle.so
/usr/lib64/varnish/vmods/libvmod_xkey.la
/usr/lib64/varnish/vmods/libvmod_xkey.so
/usr/local/share/doc/varnish-modules/LICENSE
/usr/local/share/doc/varnish-modules/README.rst

%changelog
* Fri Sep 16 2016 Kyle Ibrahim <kibrahim@pantheon.io>
- initial commit of .spec
