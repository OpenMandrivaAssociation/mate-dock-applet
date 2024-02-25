Summary:	An application dock applet for the MATE panel
Name:		mate-dock-applet
Version:	21.10.0
Release:	1
Group:		Graphical desktop/Other
License:	GPLv3
Url:		https://github.com/ubuntu-mate/mate-dock-applet/
Source0:	https://github.com/ubuntu-mate/mate-dock-applet/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: pkgconfig(python)
BuildRequires: pkgconfig(glib-2.0)

Requires: python
Requires: mate-panel
Requires: python%{pyver}dist(pyxdg)
Requires: python%{pyver}dist(pycairo)
Requires: python%{pyver}dist(pygobject)
Requires: python%{pyver}dist(pillow)
Requires: python%{pyver}dist(python-xlib)

BuildArch:	noarch

%description
MATE Dock Applet is a MATE Panel applet that displays
running application windows as icons. The applet features
options to pin applications to the dock, supports multiple
workspaces, and can be added to any MATE Panel, regardless
of size and orientation

%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog README
%{_datadir}/dbus-1/services/org.mate.panel.applet.DockAppletFactory.service
%{_datadir}/glib-2.0/schemas/org.mate.panel.applet.dock.gschema.xml
%{_datadir}/mate-panel/applets/org.mate.panel.DockApplet.mate-panel-applet
%{_datadir}/mate-applets/mate-dock-applet/

#-----------------------------------------------------------------------

%prep
%autosetup -p1

#Fix applet path, no includes libs so move to datadir
sed -i "s|libdir|datadir|g" src/Makefile.am

%build
autoreconf -fiv
%configure \
	--with-gtk3
%make_build

%install
%make_install

# locales
%find_lang %{name} --with-gnome --all-name

