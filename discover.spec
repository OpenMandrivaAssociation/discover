%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)

Summary:	Plasma 5 package manager
Name:		discover
Version:	5.13.90
Release:	2
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://www.kde.org/
Source0:	http://download.kde.org/%{stable}/plasma/%{version}/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(AppStreamQt) >= 0.10.4
BuildRequires:	pkgconfig(packagekitqt5)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	pkgconfig(Qt5Network)
BuildRequires:	pkgconfig(Qt5Xml)
BuildRequires:	pkgconfig(Qt5Concurrent)
BuildRequires:	pkgconfig(Qt5DBus)
BuildRequires:	pkgconfig(Qt5Svg)
BuildRequires:	pkgconfig(Qt5Qml)
BuildRequires:	pkgconfig(Qt5QuickWidgets)
BuildRequires:	pkgconfig(qca2-qt5)
#BuildRequires:	pkgconfig(QtOAuth)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5Crash)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5Solid)
BuildRequires:	cmake(KF5Archive)
BuildRequires:	cmake(KF5TextWidgets)
BuildRequires:	cmake(KF5Attica)
BuildRequires:	cmake(KF5NewStuff)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5Plasma)
BuildRequires:	cmake(KF5Wallet)
BuildRequires:	cmake(KF5Crash)
BuildRequires:	cmake(KF5Declarative)
BuildRequires:	cmake(KF5ItemModels)
BuildRequires:	cmake(KF5Kirigami2)
BuildRequires:	git-core
BuildRequires:	pkgconfig(flatpak)
BuildRequires:	cmake(Snappy)
BuildRequires:	pkgconfig(fwup)
Requires:	%{name}-backend-kns
Requires:	kirigami2 >= 5.38.0
Requires:	qt5-qtquickcontrols2
%rename	muon
%rename %{_lib}muon-qml
%rename libmuon-qml
%rename libmuon-common
Obsoletes:	%{mklibname MuonCommon 5} < 5.5.0
Obsoletes:	%{mklibname MuonNotifiers 5} < 5.5.0
Obsoletes:	%{mklibname DiscoverNotifiers 5} < 5.6.0
Obsoletes:	%{mklibname DiscoverCommon 5} < 5.6.0
Recommends:	%{name}-backend-kns
Recommends:	%{name}-backend-packagekit
Recommends:	%{name}-backend-flatpak

%description
Plasma 5 package manager.

%files -f all.lang
%{_sysconfdir}/xdg/discover.categories
%dir %{_libdir}/plasma-discover
%dir %{_datadir}/kxmlgui5/plasmadiscover
%dir %{_libdir}/libexec/kf5/discover
%{_datadir}/applications/*.desktop
%{_datadir}/discover
%{_bindir}/plasma-discover
%{_libdir}/libexec/kf5/discover/runservice
%{_libdir}/plasma-discover/libDiscoverCommon.so
%{_libdir}/plasma-discover/libDiscoverNotifiers.so
%{_iconsdir}/hicolor/*/apps/plasmadiscover.*
%{_datadir}/kxmlgui5/plasmadiscover/plasmadiscoverui.rc
%{_datadir}/knotifications5/discoverabstractnotifier.notifyrc
%{_datadir}/metainfo/org.kde.discover.appdata.xml

#----------------------------------------------------------------------------

%package backend-kns
Summary:	KNewStuff backend for %{name}
Group:		Graphical desktop/KDE
%rename	muon-backend-kns

%description backend-kns
KNewStuff backend for %{name}.

%files backend-kns
%{_sysconfdir}/xdg/discover_ktexteditor_codesnippets_core.knsrc
%{_libdir}/qt5/plugins/discover/kns-backend.so

#----------------------------------------------------------------------------

%package backend-packagekit
Summary:	PackageKit backend for %{name}
Group:		Graphical desktop/KDE
%rename	muon-backend-packagekit

%description backend-packagekit
PackageKit backend for %{name}.

%files backend-packagekit
%{_libdir}/qt5/plugins/discover/packagekit-backend.so
%{_libdir}/qt5/plugins/discover-notifier/DiscoverPackageKitNotifier.so
%{_datadir}/libdiscover/categories/packagekit-backend-categories.xml

#----------------------------------------------------------------------------

%package backend-flatpak
Summary:	Flatpak backend for %{name}
Group:		Graphical desktop/KDE
Requires:	flatpak >= 0.8.7

%description backend-flatpak
Flatpak backend for %{name}.

%files backend-flatpak
%{_libdir}/qt5/plugins/discover/flatpak-backend.so
%{_libdir}/qt5/plugins/discover-notifier/FlatpakNotifier.so
%{_datadir}/libdiscover/categories/flatpak-backend-categories.xml

#----------------------------------------------------------------------------

%package notifier
Summary:	%{name} notifier
Group:		Graphical desktop/KDE
Requires:	%{name} = %{EVRD}
%rename	plasma5-applet-muonnotifier
%rename	muon-notifier
Requires:	%{name}-backend-packagekit = %{EVRD}
Requires:	%{name}-backend-flatpak = %{EVRD}

%description notifier
%{name} notifier plasmoid.

%files notifier
%dir %{_datadir}/plasma/plasmoids/org.kde.discovernotifier
%{_datadir}/plasma/plasmoids/org.kde.discovernotifier/*
%{_datadir}/metainfo/org.kde.discovernotifier.appdata.xml
%{_datadir}/kservices5/plasma-applet-org.kde.discovernotifier.desktop
%{_libdir}/qt5/qml/org/kde/discovernotifier
%{_datadir}/metainfo/org.kde.discover.flatpak.appdata.xml
%{_datadir}/metainfo/org.kde.discover.packagekit.appdata.xml

#----------------------------------------------------------------------------

%prep
%autosetup -p1
%cmake_kde5 -DCMAKE_SKIP_RPATH:BOOL=OFF

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang libdiscover || touch libdiscover.lang
%find_lang plasma-discover || touch plasma-discover.lang
%find_lang plasma-discover-notifier || touch plasma-discover-notifier.lang
%find_lang plasma-discover-updater || touch plasma-discover-updater.lang
%find_lang plasma_applet_org.kde.discovernotifier || touch plasma_applet_org.kde.discovernotifier.lang
cat *.lang > all.lang
