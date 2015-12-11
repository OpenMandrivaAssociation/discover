#%bcond_without packagekit

Summary:	Plasma 5 package manager
Name:		discover
Version:	5.5.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://www.kde.org/
Source0:	http://download.kde.org/stable/%{name}/%{version}/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
%if %{with packagekit}
BuildRequires:	pkgconfig(AppstreamQt)
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
BuildRequires:	pkgconfig(Qca-qt5)
BuildRequires:	pkgconfig(QtOAuth)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5Solid)
BuildRequires:	cmake(KF5Archive)
BuildRequires:	cmake(KF5TextWidgets)
BuildRequires:	cmake(KF5Attica)
BuildRequires:	cmake(KF5NewStuff)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5Plasma)
Requires:	%{name}-backend-kns

%description
Plasma 5 package manager.

%files
#-f all.lang
#%{_datadir}/applications/*.desktop
#%{_bindir}/muon-discover
#%{_bindir}/muon-updater
#%{_datadir}/muondiscover/featured.json
#%dir %{_datadir}/desktoptheme/muon-contenttheme/
#%{_datadir}/desktoptheme/muon-contenttheme/*
#%{_iconsdir}/hicolor/*/apps/muondiscover.*
#%{_datadir}/kxmlgui5/muondiscover/muondiscoverui.rc
#%{_datadir}/kxmlgui5/muonupdater/muonupdaterui.rc

#----------------------------------------------------------------------------

#%package backend-kns
#Summary:	KNewStuff backend for Muon
#Group:		Graphical desktop/KDE

#%description backend-kns
#KNewStuff backend for Muon.

#%files backend-kns
#%{_datadir}/libmuon/backends/muon-knscomics-backend.desktop
#%{_datadir}/libmuon/backends/muon-knsplasmoids-backend.desktop
#%{_datadir}/libmuon/categories/muon-knscomics-backend-categories.xml
#%{_datadir}/libmuon/categories/muon-knsplasmoids-backend-categories.xml
#%{_libdir}/qt5/plugins/muon/muon-knsbackend.so

#----------------------------------------------------------------------------

#%if %{with packagekit}
#%package backend-packagekit
#Summary:	PackageKit backend for Muon
#Group:		Graphical desktop/KDE

#%description backend-packagekit
#PackageKit backend for Muon.

#%files backend-packagekit
#%{_datadir}/libmuon/backends/muon-packagekit-backend.desktop
#%{_datadir}/libmuon/categories/muon-packagekit-backend-categories.xml
#%{_libdir}/qt5/plugins/muon/muon-pkbackend.so
#%{_libdir}/qt5/plugins/muon-notifier/MuonPackageKitNotifier.so
#%endif

#----------------------------------------------------------------------------

#%package	notifier
#Summary:	%{name} notifier
#Group:		Graphical desktop/KDE
#Requires:	%{name} = %{EVRD}
#Requires:	muon-qml = %{EVRD}
#%rename	plasma5-applet-muonnotifier
#%if %{with packagekit}
#Requires:	%{name}-backend-packagekit = %{EVRD}
#%endif

#%description notifier
#%{name} notifier plasmoid.

#%files notifier -f plasma_applet_org.kde.muonnotifier.lang
#%dir %{_datadir}/plasma/plasmoids/org.kde.muonnotifier/
#%{_datadir}/plasma/plasmoids/org.kde.muonnotifier/*
#%{_datadir}/kservices5/plasma-applet-org.kde.muonnotifier.desktop
#%dir %{_libdir}/qt5/qml/org/kde/muonnotifier/
#%{_libdir}/qt5/qml/org/kde/muonnotifier/*

#----------------------------------------------------------------------------

#%package -n libmuon-common
#Summary:	Plasma 5 package manager library common data files
#Group:		Graphical desktop/KDE
#BuildArch:	noarch
#%rename libmuon-i18n

#%description -n libmuon-common
#Plasma 5 package manager library common data files.

#%files -n libmuon-common -f libmuon.lang
#%{_datadir}/knotifications5/muonabstractnotifier.notifyrc

#----------------------------------------------------------------------------

#%define qmlmuon %mklibname muon-qml

#%package -n %{qmlmuon}
#Summary:	QML plugin for Plasma 5 package manager
#Group:		System/Libraries
#Requires:	plasma-framework
#Provides:	muon-qml = %{EVRD}

#%description -n %{qmlmuon}
#QML plugin for Plasma 5 package manager.

#%files -n %{qmlmuon}
#%dir %{_libdir}/qt5/qml/org/kde/muon/
#%{_libdir}/qt5/qml/org/kde/muon/*

#----------------------------------------------------------------------------

#%define libMuonCommon_major 5
#%define libMuonCommon %mklibname MuonCommon %{libMuonCommon_major}

#%package -n %{libMuonCommon}
#Summary:	Plasma 5 package manager shared library
#Group:		System/Libraries
#Requires:	%{qmlmuon}
#Requires:	libmuon-common

#%description -n %{libMuonCommon}
#Plasma 5 package manager shared library.

#%files -n %{libMuonCommon}
#%{_libdir}/libMuonCommon.so.%{libMuonCommon_major}*

#----------------------------------------------------------------------------

#%define libMuonNotifiers_major 5
#%define libMuonNotifiers %mklibname MuonNotifiers %{libMuonNotifiers_major}

#%package -n %{libMuonNotifiers}
#Summary:	Plasma 5 package manager shared library
#Group:		System/Libraries
#Requires:	%{qmlmuon}
#Requires:	libmuon-common

#%description -n %{libMuonNotifiers}
#Plasma 5 package manager shared library.

#%files -n %{libMuonNotifiers}
#%{_libdir}/libMuonNotifiers.so.%{libMuonNotifiers_major}*

#----------------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

#rm -f %{buildroot}%{_libdir}/libMuonCommon.so
#rm -f %{buildroot}%{_libdir}/libMuonNotifiers.so

#%find_lang %{name}
#%find_lang muon-discover
#%find_lang muon-exporter
#%find_lang muon-notifier
#%find_lang muon-updater
#cat *.lang > all.lang

#%find_lang plasma_applet_org.kde.muonnotifier
#%find_lang libmuon
