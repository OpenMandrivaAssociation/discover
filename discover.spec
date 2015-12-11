%bcond_without packagekit

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
BuildRequires:	pkgconfig(qca-qt5)
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

%description
Plasma 5 package manager.

%files

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

