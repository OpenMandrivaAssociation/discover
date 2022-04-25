%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)

Summary:	Plasma 5 package manager
Name:		discover
Version:	5.24.4
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://www.kde.org/
Source0:	http://download.kde.org/%{stable}/plasma/%(echo %{version} |cut -d. -f1-3)/%{name}-%{version}.tar.xz
Source1:	discover-wrapper
Patch0:		discover-5.17.5-default-sort-by-name.patch
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(AppStreamQt) >= 0.10.4
BuildRequires:	pkgconfig(packagekitqt5)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	pkgconfig(Qt5Network)
BuildRequires:	pkgconfig(Qt5Xml)
BuildRequires:	pkgconfig(Qt5X11Extras)
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
BuildRequires:	cmake(KF5Package)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5Plasma)
BuildRequires:	cmake(KF5Wallet)
BuildRequires:	cmake(KF5Crash)
BuildRequires:	cmake(KF5Declarative)
BuildRequires:	cmake(KF5ItemModels)
BuildRequires:	cmake(KF5Kirigami2)
BuildRequires:	cmake(KF5Service)
BuildRequires:	cmake(KF5Bookmarks)
BuildRequires:	cmake(KF5Completion)
BuildRequires:	cmake(KF5ItemViews)
BuildRequires:	cmake(KF5JobWidgets)
BuildRequires:	cmake(KF5Solid)
BuildRequires:	cmake(KF5Auth)
BuildRequires:	cmake(KF5Codecs)
BuildRequires:	cmake(KF5ConfigWidgets)
BuildRequires:	cmake(KF5KCMUtils)
BuildRequires:	cmake(KF5IdleTime)
BuildRequires:	cmake(KUserFeedback)
BuildRequires:	git-core
BuildRequires:	pkgconfig(flatpak)
BuildRequires:	pkgconfig(libmarkdown)
%ifarch %{x86_64} %{ix86} %{aarch64}
BuildRequires:	pkgconfig(fwupd)
Suggests:	%{name}-backend-fwupd
%endif
Requires:	%{name}-backend-kns
Requires:	kirigami2 >= 5.38.0
Requires:	qt5-qtquickcontrols2
%rename muon
%rename %{_lib}muon-qml
%rename libmuon-qml
%rename libmuon-common
Obsoletes:	%{mklibname MuonCommon 5} < 5.5.0
Obsoletes:	%{mklibname MuonNotifiers 5} < 5.5.0
Obsoletes:	%{mklibname DiscoverNotifiers 5} < 5.6.0
Obsoletes:	%{mklibname DiscoverCommon 5} < 5.6.0
Suggests:	%{name}-backend-packagekit
Suggests:	%{name}-backend-flatpak

%description
Plasma 5 package manager.

%files -f all.lang
%{_datadir}/qlogging-categories5/discover.categories
%dir %{_libdir}/plasma-discover
%dir %{_datadir}/kxmlgui5/plasmadiscover
%dir %{_libdir}/libexec/kf5/discover
%{_datadir}/applications/*.desktop
%{_datadir}/discover
%{_bindir}/discover
%{_bindir}/plasma-discover
%{_bindir}/plasma-discover-update
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
%rename muon-backend-kns

%description backend-kns
KNewStuff backend for %{name}.

%files backend-kns
%{_libdir}/qt5/plugins/discover/kns-backend.so

#----------------------------------------------------------------------------

%package backend-packagekit
Summary:	PackageKit backend for %{name}
Group:		Graphical desktop/KDE
%rename muon-backend-packagekit
Requires:	packagekit
Requires:	dnf-plugins-core

%description backend-packagekit
PackageKit backend for %{name}.

%files backend-packagekit
%{_libdir}/qt5/plugins/discover/packagekit-backend.so
%{_libdir}/qt5/plugins/discover-notifier/DiscoverPackageKitNotifier.so
%{_datadir}/libdiscover/categories/packagekit-backend-categories.xml
%{_datadir}/metainfo/org.kde.discover.packagekit.appdata.xml

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
%{_iconsdir}/hicolor/scalable/apps/flatpak-discover.svg
%{_datadir}/metainfo/org.kde.discover.flatpak.appdata.xml

#----------------------------------------------------------------------------

%ifarch %{x86_64} %{ix86} %{aarch64}
%package backend-fwupd
Summary:	Fwupd backend for %{name}
Group:		Graphical desktop/KDE
Requires:	fwupd >= 1.1.2

%description backend-fwupd
Fwupd backend for %{name}.

%files backend-fwupd
%{_libdir}/qt5/plugins/discover/fwupd-backend.so
%endif

#----------------------------------------------------------------------------
%package notifier
Summary:	%{name} notifier
Group:		Graphical desktop/KDE
Requires:	%{name} = %{EVRD}
%rename plasma5-applet-muonnotifier
%rename muon-notifier

%description notifier
%{name} notifier plasmoid.

%files notifier
%{_sysconfdir}/xdg/autostart/org.kde.discover.notifier.desktop
%{_libdir}/libexec/DiscoverNotifier

#----------------------------------------------------------------------------
%package updater-kcm
Summary:	KDE Control Center module for installing updates
Group:		Graphical desktop/KDE
Requires:	%{name} = %{EVRD}

%description updater-kcm
KDE Control Center module for installing updates

%files updater-kcm
%{_datadir}/kpackage/kcms/kcm_updates
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings/kcm_updates.so

#----------------------------------------------------------------------------

%prep
%autosetup -p1
%cmake_kde5 -DCMAKE_SKIP_RPATH:BOOL=OFF

%build
%ninja -C build

%install
%ninja_install -C build
install -c -m 755 %{S:1} %{buildroot}%{_bindir}/discover
# Launch discover through the wrapper
sed -i -e 's,Exec=plasma-discover,Exec=discover,g' %{buildroot}%{_datadir}/applications/org.kde.discover.desktop

%find_lang libdiscover || touch libdiscover.lang
%find_lang plasma-discover || touch plasma-discover.lang
%find_lang plasma-discover-notifier || touch plasma-discover-notifier.lang
%find_lang plasma-discover-updater || touch plasma-discover-updater.lang
%find_lang plasma_applet_org.kde.discovernotifier || touch plasma_applet_org.kde.discovernotifier.lang
%find_lang kcm_updates || touch kcm_updates.lang
cat *.lang > all.lang
