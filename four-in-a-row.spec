%define url_ver	%(echo %{version}|cut -d. -f1,2)
%define _disable_rebuild_configure 1

Name:		four-in-a-row
Version:	3.28.0
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
%{_datadir}/metainfo/%{name}.appdata.xml

