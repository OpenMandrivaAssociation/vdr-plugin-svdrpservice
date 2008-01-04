
%define plugin	svdrpservice
%define name	vdr-plugin-%plugin
%define version	0.0.3
%define rel	7

Summary:	VDR plugin: SVDRP client
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://vdr.schmirler.de/
Source:		http://vdr.schmirler.de/svdrpservice/vdr-%plugin-%version.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.4.1-6
Requires:	vdr-abi = %vdr_abi

%description
This plugin offers SVDRP connections as a service to other plugins.
Connecting to streamdev's VTP server port is possible, too. VTP provides
a subset of the SVDRP commands but in contrast to SVDRP it can handle
multiple connections at a time.

There's no reason to load this plugin if no other plugin relies on it.

%package -n %plugin-devel
Summary:	Development headers for svdrpservice VDR plugin
Group:		Development/C++
Requires:	vdr-devel

%description -n %plugin-devel
Development headers for svdrpservice VDR plugin needed for building
some plugins depending on svdrpservice.

%prep
%setup -q -n %plugin-%version

%build
%vdr_plugin_build

%install
rm -rf %{buildroot}
%vdr_plugin_install

install -D -m644 svdrpservice.h %buildroot%_includedir/vdr/%plugin/svdrpservice.h

%clean
rm -rf %{buildroot}

%post
%vdr_plugin_post %plugin

%postun
%vdr_plugin_postun %plugin

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY

%files -n %plugin-devel
%defattr(-,root,root)
%{_includedir}/vdr/%{plugin}
