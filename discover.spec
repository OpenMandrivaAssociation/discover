%bcond_without packagekit

Summary:	Plasma 5 package manager
Name:		discover
Version:	5.5.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://www.kde.org/
Source0:	http://download.kde.org/stable/%{name}/%{version}/%{name}-%{version}.tar.xz
Patch0:		discover-5.5.0-soname.patch
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

%description
Plasma 5 package manager.

%files -f all.lang
%{_datadir}/applications/*.desktop
%{_bindir}/muon-discover
%{_bindir}/muon-updater
%{_libdir}/qt5/qml/org/kde/discover
%{_datadir}/muondiscover/featured.json
%{_iconsdir}/hicolor/*/apps/muondiscover.*
%{_datadir}/kxmlgui5/muondiscover/muondiscoverui.rc
%{_datadir}/kxmlgui5/muonupdater/muonupdaterui.rc
%{_datadir}/knotifications5/muonabstractnotifier.notifyrc

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
%{_libdir}/qt5/plugins/discover-notifier/MuonPackageKitNotifier.so
%{_libdir}/qt5/qml/org/kde/discovernotifier
#----------------------------------------------------------------------------

%define libDiscoverCommon_major 5
%define libDiscoverCommon %mklibname DiscoverCommon %{libDiscoverCommon_major}

%package -n %{libDiscoverCommon}
Summary:	Plasma 5 package manager shared library
Group:		System/Libraries
Obsoletes:	%{mklibname MuonCommon 5} < 5.5.0

%description -n %{libDiscoverCommon}
Plasma 5 package manager shared library.

%files -n %{libDiscoverCommon}
%{_libdir}/libDiscoverCommon.so.%{libDiscoverCommon_major}*

#----------------------------------------------------------------------------

%define libDiscovernNotifiers_major 5
%define libDiscoverNotifiers %mklibname DiscoverNotifiers %{libDiscoverNotifiers_major}

%package -n %{libDiscoverNotifiers}
Summary:	Plasma 5 package manager shared library
Group:		System/Libraries
Obsoletes:	%{mklibname MuonNotifiers 5} < 5.5.0

%description -n %{libDiscoverNotifiers}
Plasma 5 package manager shared library.

%files -n %{libDiscoverNotifiers}
%{_libdir}/libDiscoverNotifiers.so.%{libDiscoverNotifiers_major}*

#----------------------------------------------------------------------------

%prep
%setup -q
%apply_patches
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

rm -f %{buildroot}%{_libdir}/libDiscoverCommon.so
rm -f %{buildroot}%{_libdir}/libDiscoverNotifiers.so

%find_lang libdiscover
%find_lang muon-discover
%find_lang muon-exporter
%find_lang muon-notifier
%find_lang muon-updater
cat *.lang > all.lang

%find_lang plasma_applet_org.kde.muonnotifier
