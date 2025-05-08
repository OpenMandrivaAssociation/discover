%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 -o "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)
#define git 20240222
%define gitbranch Plasma/6.0
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")

Summary:	Plasma 6 package manager
Name:		discover
Version:	6.3.5
Release:	%{?git:0.%{git}.}1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://www.kde.org/
%if 0%{?git:1}
Source0:	https://invent.kde.org/plasma/discover/-/archive/%{gitbranch}/discover-%{gitbranchd}.tar.bz2#/discover-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/plasma/%(echo %{version} |cut -d. -f1-3)/discover-%{version}.tar.xz
%endif
Source1:	discoverrc
Source2:	discover-upgrade
Source10:	discover-wrapper.in
Patch0:		discover-5.17.5-default-sort-by-name.patch
Patch1:		discover-dont-switch-branches.patch
# (tpg) always force refresh, periodic refresh set to 12h instead of 24h
Patch2:		https://src.fedoraproject.org/rpms/plasma-discover/raw/rawhide/f/discover-5.21.4-pk_refresh_force.patch
Patch3:		discover-6.3.3-upgrading-with-packagekit-is-dangerous.patch
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(AppStreamQt) >= 1.0.3
BuildRequires:	cmake(Qt6)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6Network)
BuildRequires:	cmake(Qt6Xml)
BuildRequires:	cmake(Qt6Concurrent)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6Qml)
BuildRequires:	cmake(Qt6QuickControls2)
BuildRequires:	cmake(Qt6QuickWidgets)
BuildRequires:	cmake(Qt6WebView)
BuildRequires:	cmake(QCoro6)
BuildRequires:	cmake(Qca-qt6)
#BuildRequires:	pkgconfig(QtOAuth)
BuildRequires:	cmake(packagekitqt6)
BuildRequires:	cmake(KF6WidgetsAddons)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6Solid)
BuildRequires:	cmake(KF6Archive)
BuildRequires:	cmake(KF6TextWidgets)
BuildRequires:	cmake(KF6Attica)
BuildRequires:	cmake(KF6NewStuff)
BuildRequires:	cmake(KF6KirigamiAddons)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(KF6Package)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(Plasma) >= 5.90.0
BuildRequires:	cmake(KF6Wallet)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(KF6Declarative)
BuildRequires:	cmake(KF6ItemModels)
BuildRequires:	cmake(KF6Kirigami2)
BuildRequires:	cmake(KF6Service)
BuildRequires:	cmake(KF6Bookmarks)
BuildRequires:	cmake(KF6Completion)
BuildRequires:	cmake(KF6ItemViews)
BuildRequires:	cmake(KF6JobWidgets)
BuildRequires:	cmake(KF6Solid)
BuildRequires:	cmake(KF6Auth)
BuildRequires:	cmake(KF6Codecs)
BuildRequires:	cmake(KF6ConfigWidgets)
BuildRequires:	cmake(KF6KCMUtils)
BuildRequires:	cmake(KF6IdleTime)
BuildRequires:	cmake(KF6Purpose)
BuildRequires:	cmake(KF6StatusNotifierItem)
BuildRequires:	cmake(KUserFeedbackQt6)
BuildRequires:	git-core
BuildRequires:	pkgconfig(flatpak)
BuildRequires:	pkgconfig(libmarkdown)
%ifarch %{x86_64} %{ix86} %{aarch64}
BuildRequires:	pkgconfig(fwupd)
Recommends:	%{name}-backend-fwupd
%endif
Requires:	%{name}-backend-kns
Recommends:	%{name}-backend-packagekit
Recommends:	%{name}-backend-flatpak
# For the wrapper script
Requires:	plasma6-kdialog
Requires:	qt6-qttools-dbus
BuildSystem:	cmake
BuildOption:	-DBUILD_QCH:BOOL=ON
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON
# Renamed after 6.0 2025-05-01
%rename plasma6-discover

%description
Plasma 6 package manager.

%files -f %{name}.lang
%{_datadir}/qlogging-categories6/discover.categories
%dir %{_libdir}/plasma-discover
%{_datadir}/kxmlgui5/plasmadiscover
%{_datadir}/applications/*.desktop
%{_sysconfdir}/xdg/discoverrc
%{_bindir}/plasma-discover
%{_bindir}/plasma-discover-main
%{_bindir}/plasma-discover-update
%{_libdir}/plasma-discover/libDiscoverCommon.so
%{_libdir}/plasma-discover/libDiscoverNotifiers.so
%{_iconsdir}/hicolor/*/apps/plasmadiscover.*
%{_datadir}/knotifications6/discoverabstractnotifier.notifyrc
%{_datadir}/metainfo/org.kde.discover.appdata.xml
%{_qtdir}/plugins/plasma/kcms/systemsettings/kcm_updates.so

#----------------------------------------------------------------------------

%package backend-kns
Summary:	KNewStuff backend for %{name}
Group:		Graphical desktop/KDE
%rename muon-backend-kns
# Renamed after 6.0 2025-05-03
%rename plasma6-discover-backend-kns

%description backend-kns
KNewStuff backend for %{name}.

%files backend-kns
%{_qtdir}/plugins/discover/kns-backend.so

#----------------------------------------------------------------------------

%package backend-packagekit
Summary:	PackageKit backend for %{name}
Group:		Graphical desktop/KDE
%rename muon-backend-packagekit
Requires:	packagekit
Requires:	dnf-plugins-core
# Renamed after 6.0 2025-05-03
%rename plasma6-discover-backend-packagekit

%description backend-packagekit
PackageKit backend for %{name}.

%files backend-packagekit
%{_qtdir}/plugins/discover/packagekit-backend.so
%{_qtdir}/plugins/discover-notifier/DiscoverPackageKitNotifier.so
%{_datadir}/libdiscover/categories/packagekit-backend-categories.xml
%{_datadir}/metainfo/org.kde.discover.packagekit.appdata.xml
%{_libexecdir}/discover-upgrade

#----------------------------------------------------------------------------

%package backend-flatpak
Summary:	Flatpak backend for %{name}
Group:		Graphical desktop/KDE
Requires:	flatpak >= 0.8.7
Requires:	(flatpak-kcm if plasma-systemsettings)
# Renamed after 6.0 2025-05-03
%rename plasma6-discover-backend-flatpak

%description backend-flatpak
Flatpak backend for %{name}.

%files backend-flatpak
%{_qtdir}/plugins/discover/flatpak-backend.so
%{_qtdir}/plugins/discover-notifier/FlatpakNotifier.so
%{_datadir}/libdiscover/categories/flatpak-backend-categories.xml
%{_iconsdir}/hicolor/scalable/apps/flatpak-discover.svg
%{_datadir}/metainfo/org.kde.discover.flatpak.appdata.xml

#----------------------------------------------------------------------------

%ifarch %{x86_64} %{ix86} %{aarch64}
%package backend-fwupd
Summary:	Fwupd backend for %{name}
Group:		Graphical desktop/KDE
Requires:	fwupd >= 1.1.2
# Renamed after 6.0 2025-05-03
%rename plasma6-discover-backend-fwupd

%description backend-fwupd
Fwupd backend for %{name}.

%files backend-fwupd
%{_qtdir}/plugins/discover/fwupd-backend.so
%endif

#----------------------------------------------------------------------------
%package notifier
Summary:	%{name} notifier
Group:		Graphical desktop/KDE
Requires:	%{name} = %{EVRD}
# Renamed after 6.0 2025-05-03
%rename plasma6-discover-notifier

%description notifier
%{name} notifier plasmoid.

%files notifier
%{_sysconfdir}/xdg/autostart/org.kde.discover.notifier.desktop
%{_libdir}/libexec/DiscoverNotifier

#----------------------------------------------------------------------------

%prep -a
# This sed statement supplements the upgrading-with-packagekit-is-dangerous patch
sed -i -e 's,@LIBEXECDIR@,%{_libexecdir},g' libdiscover/backends/PackageKitBackend/PackageKitUpdater.cpp

%install -a
install -m 644 -p -D %{SOURCE1} %{buildroot}%{_sysconfdir}/xdg/discoverrc
mv %{buildroot}%{_bindir}/plasma-discover %{buildroot}%{_bindir}/plasma-discover-main
sed -e 's,@QTDIR@,%{_qtdir},g' %{S:10} >%{buildroot}%{_bindir}/plasma-discover
chmod 0755 %{buildroot}%{_bindir}/plasma-discover

mkdir -p %{buildroot}%{_libexecdir}
install -c -m 755 %{S:2} %{buildroot}%{_libexecdir}/
