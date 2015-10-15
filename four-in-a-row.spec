%define url_ver	%(echo %{version}|cut -d. -f1,2)
%define _disable_rebuild_configure 1

Name:		four-in-a-row
Version:	3.18.1
Release:	1
Summary:	GNOME Four-in-a-row game
License:	GPLv2+ and GFDL
Group:		Games/Boards
URL:		https://wiki.gnome.org/Apps/Four-in-a-row
Source0:	https://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.4.0
BuildRequires:	pkgconfig(libcanberra-gtk3) >= 0.26
BuildRequires:	pkgconfig(librsvg-2.0) >= 2.32.0
BuildRequires:	pkgconfig(zlib)
BuildRequires:	intltool
BuildRequires:	itstool
BuildRequires:	libxml2-utils
Obsoletes:	gnect
# For help
Requires:	yelp

%description
The objective of Four-in-a-row is to build a line of four of your marbles
while trying to stop your opponent (human or computer) building a line
of his or her own.

%prep
%setup -q

%build
%configure
%make

%install
%makeinstall_std

%find_lang %{name} --all-name --with-gnome 

%files -f %{name}.lang
%doc COPYING
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}
%{_datadir}/glib-2.0/schemas/org.gnome.%{name}.gschema.xml
%{_iconsdir}/*/*/apps/%{name}*.*
%{_mandir}/man6/%{name}.6*
%{_datadir}/appdata/%{name}.appdata.xml


%changelog
* Tue Feb 17 2015 wally <wally> 3.14.2-2.mga5
+ Revision: 815336
- require yelp for showing help

* Tue Nov 11 2014 ovitters <ovitters> 3.14.2-1.mga5
+ Revision: 796301
- new version 3.14.2

* Wed Oct 15 2014 umeabot <umeabot> 3.14.1-2.mga5
+ Revision: 738937
- Second Mageia 5 Mass Rebuild

* Fri Oct 10 2014 ovitters <ovitters> 3.14.1-1.mga5
+ Revision: 737813
- new version 3.14.1

* Mon Sep 22 2014 ovitters <ovitters> 3.14.0-1.mga5
+ Revision: 719186
- new version 3.14.0

* Tue Sep 16 2014 umeabot <umeabot> 3.13.92-2.mga5
+ Revision: 679309
- Mageia 5 Mass Rebuild

* Tue Sep 16 2014 ovitters <ovitters> 3.13.92-1.mga5
+ Revision: 676958
- new version 3.13.92

* Tue Aug 19 2014 ovitters <ovitters> 3.13.90-1.mga5
+ Revision: 665343
- new version 3.13.90

* Mon Jul 21 2014 ovitters <ovitters> 3.13.4-1.mga5
+ Revision: 655171
- new version 3.13.4

* Tue Jun 24 2014 ovitters <ovitters> 3.13.3-1.mga5
+ Revision: 639209
- new version 3.13.3

* Mon Jun 23 2014 ovitters <ovitters> 3.12.3-2.mga5
+ Revision: 638831
- update url

* Tue Jun 17 2014 ovitters <ovitters> 3.12.3-1.mga5
+ Revision: 637703
- new version 3.12.3

* Mon May 12 2014 ovitters <ovitters> 3.12.2-1.mga5
+ Revision: 622084
- new version 3.12.2

* Mon Apr 14 2014 ovitters <ovitters> 3.12.1-1.mga5
+ Revision: 614070
- new version 3.12.1

* Mon Mar 24 2014 ovitters <ovitters> 3.12.0-1.mga5
+ Revision: 607931
- new version 3.12.0

* Sun Mar 16 2014 ovitters <ovitters> 3.11.92-1.mga5
+ Revision: 604236
- new version 3.11.92

* Tue Feb 18 2014 ovitters <ovitters> 3.11.90-1.mga5
+ Revision: 594238
- new version 3.11.90

* Wed Feb 05 2014 dams <dams> 3.11.3-1.mga5
+ Revision: 582954
- new version 3.11.3

* Tue Oct 22 2013 umeabot <umeabot> 3.10.1-2.mga4
+ Revision: 541378
- Mageia 4 Mass Rebuild

* Sat Oct 12 2013 ovitters <ovitters> 3.10.1-1.mga4
+ Revision: 495800
- new version 3.10.1

* Mon Sep 23 2013 ovitters <ovitters> 3.10.0-1.mga4
+ Revision: 484540
- new version 3.10.0

* Tue Sep 17 2013 ovitters <ovitters> 3.9.92-1.mga4
+ Revision: 480564
- new version 3.9.92

* Wed Aug 21 2013 fwang <fwang> 3.9.90-1.mga4
+ Revision: 468738
- new version 3.9.90
- cleanup spec

* Sun Jun 09 2013 dams <dams> 3.8.1-1.mga4
+ Revision: 440883
- imported package four-in-a-row

