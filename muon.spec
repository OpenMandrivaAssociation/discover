%bcond_without packagekit

Summary:	Plasma 5 package manager
Name:		muon
Version:	5.3.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://www.kde.org/
Source0:	ftp://ftp.kde.org/pub/kde/stable/plasma/%{version}/%{name}-%{version}.tar.xz
Patch0:		muon-5.3.0-soname.patch
BuildRequires:	extra-cmake-modules
%if %{with packagekit}
BuildRequires:	appstream-qt5-devel
BuildRequires:	pkgconfig(packagekitqt5)
%endif
BuildRequires:	kf5attica-devel
BuildRequires:	kf5config-devel
BuildRequires:	kf5configwidgets-devel
BuildRequires:	kf5coreaddons-devel
BuildRequires:	kf5dbusaddons-devel
BuildRequires:	kf5declarative-devel
BuildRequires:	kf5i18n-devel
BuildRequires:	kf5iconthemes-devel
BuildRequires:	kf5itemviews-devel
BuildRequires:	kf5kdelibs4support-devel
BuildRequires:	kf5kio-devel
BuildRequires:	kf5newstuff-devel
BuildRequires:	kf5notifications-devel
BuildRequires:	kf5plasma-devel
BuildRequires:	kf5solid-devel
BuildRequires:	kf5wallet-devel
BuildRequires:	kf5widgetsaddons-devel
BuildRequires:	pkgconfig(phonon4qt5)
BuildRequires:	pkgconfig(Qt5Concurrent)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5DBus)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Network)
BuildRequires:	pkgconfig(Qt5Qml)
BuildRequires:	pkgconfig(Qt5Quick)
BuildRequires:	pkgconfig(Qt5QuickWidgets)
BuildRequires:	pkgconfig(Qt5Svg)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5Xml)
Requires:	%{name}-backend-kns

%description
Plasma 5 package manager.

%files -f %{name}.lang
%{_kde5_applicationsdir}/muon-discover-category.desktop
%{_kde5_applicationsdir}/muon-discover.desktop
%{_kde5_applicationsdir}/muon-updater.desktop
%{_kde5_bindir}/muon-discover
%{_kde5_bindir}/muon-updater
%{_kde5_datadir}/muondiscover/featured.json
%dir %{_kde5_datadir}/desktoptheme/muon-contenttheme/
%{_kde5_datadir}/desktoptheme/muon-contenttheme/*
%{_kde5_iconsdir}/hicolor/*/apps/muondiscover.*
%{_kde5_xmlguidir}/muondiscover/muondiscoverui.rc
%{_kde5_xmlguidir}/muonupdater/muonupdaterui.rc

#----------------------------------------------------------------------------

%package backend-kns
Summary:	KNewStuff backend for Muon
Group:		Graphical desktop/KDE

%description backend-kns
KNewStuff backend for Muon.

%files backend-kns
%{_kde5_datadir}/libmuon/backends/muon-knscomics-backend.desktop
%{_kde5_datadir}/libmuon/backends/muon-knsplasmoids-backend.desktop
%{_kde5_datadir}/libmuon/categories/muon-knscomics-backend-categories.xml
%{_kde5_datadir}/libmuon/categories/muon-knsplasmoids-backend-categories.xml
%{_qt5_plugindir}/muon/muon-knsbackend.so

#----------------------------------------------------------------------------

%if %{with packagekit}
%package backend-packagekit
Summary:	PackageKit backend for Muon
Group:		Graphical desktop/KDE

%description backend-packagekit
PackageKit backend for Muon.

%files backend-packagekit
%{_kde5_datadir}/libmuon/backends/muon-packagekit-backend.desktop
%{_kde5_datadir}/libmuon/categories/muon-packagekit-backend-categories.xml
%{_qt5_plugindir}/muon/muon-pkbackend.so
%{_qt5_plugindir}/muon-notifier/MuonPackageKitNotifier.so
%endif

#----------------------------------------------------------------------------

%package -n plasma5-applet-muonnotifier
Summary:	Plasma 5 muon notifier plasmoid
Group:		Graphical desktop/KDE
Requires:	%{name}
Requires:	muon-qml = %{EVRD}

%description -n plasma5-applet-muonnotifier
Plasma 5 muon notifier plasmoid.

%files -n plasma5-applet-muonnotifier -f plasma_applet_org.kde.muonnotifier.lang
%dir %{_kde5_datadir}/plasma/plasmoids/org.kde.muonnotifier/
%{_kde5_datadir}/plasma/plasmoids/org.kde.muonnotifier/*
%{_kde5_services}/plasma-applet-org.kde.muonnotifier.desktop
%dir %{_kde5_qmldir}/org/kde/muonnotifier/
%{_kde5_qmldir}/org/kde/muonnotifier/*

#----------------------------------------------------------------------------

%package -n libmuon-common
Summary:	Plasma 5 package manager library common data files
Group:		Graphical desktop/KDE
BuildArch:	noarch

%description -n libmuon-common
Plasma 5 package manager library common data files.

%files -n libmuon-common
%{_kde5_datadir}/libmuon/moo.ogg
%{_kde5_notificationsdir}/muonabstractnotifier.notifyrc

#----------------------------------------------------------------------------

%package -n libmuon-i18n
Summary:	Plasma 5 package manager library translations
Group:		System/Internationalization
BuildArch:	noarch

%description -n libmuon-i18n
Plasma 5 package manager library translations.

%files -n libmuon-i18n -f libmuon.lang

#----------------------------------------------------------------------------

%define qmlmuon %mklibname muon-qml

%package -n %{qmlmuon}
Summary:	QML plugin for Plasma 5 package manager
Group:		System/Libraries
Requires:	kf5plasma-qml
Provides:	muon-qml = %{EVRD}

%description -n %{qmlmuon}
QML plugin for Plasma 5 package manager.

%files -n %{qmlmuon}
%dir %{_kde5_qmldir}/org/kde/muon/
%{_kde5_qmldir}/org/kde/muon/*

#----------------------------------------------------------------------------

%define muoncommon_major 5
%define libmuoncommon %mklibname muoncommon %{muoncommon_major}

%package -n %{libmuoncommon}
Summary:	Plasma 5 package manager shared library
Group:		System/Libraries
Requires:	%{qmlmuon}
Requires:	libmuon-common
Requires:	libmuon-i18n

%description -n %{libmuoncommon}
Plasma 5 package manager shared library.

%files -n %{libmuoncommon}
%{_kde5_libdir}/libMuonCommon.so.%{muoncommon_major}*

#----------------------------------------------------------------------------

%define muonnotifiers_major 5
%define libmuonnotifiers %mklibname notifiers %{muonnotifiers_major}

%package -n %{libmuonnotifiers}
Summary:	Plasma 5 package manager shared library
Group:		System/Libraries
Requires:	%{qmlmuon}
Requires:	libmuon-i18n

%description -n %{libmuonnotifiers}
Plasma 5 package manager shared library.

%files -n %{libmuonnotifiers}
%{_kde5_libdir}/libMuonNotifiers.so.%{muonnotifiers_major}*

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1

%build
%cmake_kde5
%make

%install
%makeinstall_std -C build

rm -f %{buildroot}%{_kde5_libdir}/libMuonCommon.so
rm -f %{buildroot}%{_kde5_libdir}/libMuonNotifiers.so

%find_lang %{name} muon-discover muon-exporter muon-notifier muon-updater %{name}.lang
%find_lang plasma_applet_org.kde.muonnotifier
%find_lang libmuon
