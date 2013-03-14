
%define plugin	svdrpservice
%define name	vdr-plugin-%plugin
%define version	0.0.4
%define rel	3

Summary:	VDR plugin: SVDRP client
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL+
URL:		http://vdr.schmirler.de/
Source:		http://vdr.schmirler.de/svdrpservice/vdr-%plugin-%version.tgz
BuildRequires:	vdr-devel >= 1.6.0
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
%vdr_plugin_prep

%vdr_plugin_params_begin %plugin
# Default server IP and optional port (e.g. 192.168.0.1:2001).
# If no port is given, the default SVDRP port 2001 is assumed.
var=DEFAULT_SERVER
param=DEFAULT_SERVER
%vdr_plugin_params_end

%build
%vdr_plugin_build

%install
%vdr_plugin_install

install -D -m644 svdrpservice.h %buildroot%_includedir/vdr/%plugin/svdrpservice.h

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY

%files -n %plugin-devel
%defattr(-,root,root)
%{_includedir}/vdr/%{plugin}


%changelog
* Tue Jul 28 2009 Anssi Hannula <anssi@mandriva.org> 0.0.4-2mdv2010.0
+ Revision: 401088
- rebuild for new VDR

* Tue Jul 14 2009 Anssi Hannula <anssi@mandriva.org> 0.0.4-1mdv2010.0
+ Revision: 395761
- new version
- drop i18n patch, fixed upstream
- update license tag
- include sysconfig file

* Fri Mar 20 2009 Anssi Hannula <anssi@mandriva.org> 0.0.3-10mdv2009.1
+ Revision: 359372
- rebuild for new vdr

* Mon Apr 28 2008 Anssi Hannula <anssi@mandriva.org> 0.0.3-9mdv2009.0
+ Revision: 197984
- rebuild for new vdr

* Sat Apr 26 2008 Anssi Hannula <anssi@mandriva.org> 0.0.3-8mdv2009.0
+ Revision: 197729
- add vdr_plugin_prep
- bump buildrequires on vdr-devel
- adapt to gettext i18n of VDR 1.6 (semi-automatic patch)

* Fri Jan 04 2008 Anssi Hannula <anssi@mandriva.org> 0.0.3-7mdv2008.1
+ Revision: 145209
- rebuild for new vdr

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 29 2007 Anssi Hannula <anssi@mandriva.org> 0.0.3-6mdv2008.1
+ Revision: 103219
- rebuild for new vdr

* Sun Jul 08 2007 Anssi Hannula <anssi@mandriva.org> 0.0.3-5mdv2008.0
+ Revision: 50053
- rebuild for new vdr

* Thu Jun 21 2007 Anssi Hannula <anssi@mandriva.org> 0.0.3-4mdv2008.0
+ Revision: 42136
- rebuild for new vdr

* Sat May 05 2007 Anssi Hannula <anssi@mandriva.org> 0.0.3-3mdv2008.0
+ Revision: 22705
- rebuild for new vdr

* Tue May 01 2007 Anssi Hannula <anssi@mandriva.org> 0.0.3-2mdv2008.0
+ Revision: 19887
- add devel subpackage

* Tue May 01 2007 Anssi Hannula <anssi@mandriva.org> 0.0.3-1mdv2008.0
+ Revision: 19882
- Import vdr-plugin-svdrpservice

