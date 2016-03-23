%bcond_without packagekit

Summary:	Plasma 5 package manager
Name:		discover
Version:	5.6.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://www.kde.org/
Source0:	http://download.kde.org/stable/%{name}/%{version}/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
%if %{with packagekit}
BuildRequires:	cmake(AppstreamQt)
BuildRequires:	pkgconfig(packagekitqt5)
%endif
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
BuildRequires:	cmake(KF5Solid)
BuildRequires:	cmake(KF5Archive)
BuildRequires:	cmake(KF5TextWidgets)
BuildRequires:	cmake(KF5Attica)
BuildRequires:	cmake(KF5NewStuff)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5Plasma)
BuildRequires:	cmake(KF5Wallet)
Requires:	%{name}-backend-kns
%rename	muon
%rename %{_lib}muon-qml
%rename libmuon-qml
%rename libmuon-common
Obsoletes:	%{mklibname MuonCommon 5} < 5.5.0
Obsoletes:	%{mklibname MuonNotifiers 5} < 5.5.0
Obsoletes:	%{mklibname DiscoverNotifiers 5} < 5.6.0
Obsoletes:	%{mklibname DiscoverCommon 5} < 5.6.0

%description
Plasma 5 package manager.

%files -f all.lang
%dir %{_libdir}/plasma-discover
%dir %{_datadir}/plasmadiscover
%dir %{_datadir}/kxmlgui5/plasmadiscover
%dir %{_datadir}/kxmlgui5/plasmadiscoverupdater

%{_datadir}/applications/*.desktop
%{_bindir}/plasma-discover
%{_bindir}/plasma-discover-updater
%{_libdir}/plasma-discover/libDiscoverCommon.so
%{_libdir}/plasma-discover/libDiscoverNotifiers.so
%{_libdir}/qt5/qml/org/kde/discover
%{_datadir}/plasmadiscover/featured.json
%{_iconsdir}/hicolor/*/apps/plasmadiscover.*
%{_datadir}/kxmlgui5/plasmadiscover/plasmadiscoverui.rc
%{_datadir}/kxmlgui5/plasmadiscoverupdater/plasmadiscoverupdaterui.rc
%{_datadir}/knotifications5/discoverabstractnotifier.notifyrc

#----------------------------------------------------------------------------

%package backend-kns
Summary:	KNewStuff backend for %{name}
Group:		Graphical desktop/KDE
%rename	muon-backend-kns

%description backend-kns
KNewStuff backend for %{name}.

%files backend-kns
%{_libdir}/qt5/plugins/discover/kns-backend.so
%{_datadir}/libdiscover/backends/knscomics-backend.desktop
%{_datadir}/libdiscover/backends/knsplasmoids-backend.desktop
%{_datadir}/libdiscover/categories/knscomics-backend-categories.xml
%{_datadir}/libdiscover/categories/knsplasmoids-backend-categories.xml

#----------------------------------------------------------------------------

%if %{with packagekit}
%package backend-packagekit
Summary:	PackageKit backend for %{name}
Group:		Graphical desktop/KDE
%rename	muon-backend-packagekit

%description backend-packagekit
PackageKit backend for %{name}.

%files backend-packagekit
%{_libdir}/qt5/plugins/discover/packagekit-backend.so
%{_datadir}/libdiscover/categories/packagekit-backend-categories.xml
%{_datadir}/libdiscover/backends/packagekit-backend.desktop
%endif

#----------------------------------------------------------------------------

%package notifier
Summary:	%{name} notifier
Group:		Graphical desktop/KDE
Requires:	%{name} = %{EVRD}
%rename	plasma5-applet-muonnotifier
%rename	muon-notifier
%if %{with packagekit}
Requires:	%{name}-backend-packagekit = %{EVRD}
%endif

%description notifier
%{name} notifier plasmoid.

%files notifier -f plasma_applet_org.kde.muonnotifier.lang
%dir %{_datadir}/plasma/plasmoids/org.kde.discovernotifier
%{_datadir}/plasma/plasmoids/org.kde.discovernotifier/*
%{_datadir}/kservices5/plasma-applet-org.kde.discovernotifier.desktop
%{_libdir}/qt5/plugins/discover-notifier/DiscoverPackageKitNotifier.so
%{_libdir}/qt5/qml/org/kde/discovernotifier
#----------------------------------------------------------------------------

%prep
%setup -q
%apply_patches
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang libdiscover
%find_lang plasma-discover
%find_lang plasma-discover-notifier
%find_lang plasma-discover-exporter
%find_lang plasma-discover-updater
cat *.lang > all.lang

%find_lang plasma_applet_org.kde.muonnotifier
