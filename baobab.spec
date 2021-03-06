Summary:	Graphical directory tree analyzer
Summary(pl.UTF-8):	Graficzny analizator drzew katalogów
Name:		baobab
Version:	3.8.2
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/baobab/3.8/%{name}-%{version}.tar.xz
# Source0-md5:	768edf897d3626140a56a568b7083241
Patch0:		%{name}-desktop.patch
URL:		http://live.gnome.org/GnomeUtils
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.11
BuildRequires:	gettext-devel >= 0.17
BuildRequires:	glib2-devel >= 1:2.30.0
BuildRequires:	gtk+3-devel >= 3.8.0
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libgtop-devel
BuildRequires:	pkgconfig >= 1:0.22
BuildRequires:	rpmbuild(find_lang) >= 1.35
BuildRequires:	rpmbuild(macros) >= 1.592
BuildRequires:	yelp-tools
Requires(post,postun):	glib2 >= 1:2.26.0
Requires(post,postun):	gtk-update-icon-cache
Requires:	glib2 >= 1:2.30.0
Requires:	gtk+3 >= 3.8.0
Requires:	hicolor-icon-theme
Provides:	gnome-utils-baobab = 1:%{version}-%{release}
Obsoletes:	gnome-utils-baobab < 1:3.3.2-1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
baobab is a graphical directory tree analyzer.

%description -l pl.UTF-8
baobab jest graficznym analizatorem drzew katalogów.

%prep
%setup -q
%patch0 -p1

%build
%{__intltoolize}
%{__aclocal} -I m4 -I libgd
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache HighContrast
%update_icon_cache hicolor
%glib_compile_schemas

%postun
%update_icon_cache HighContrast
%update_icon_cache hicolor
%glib_compile_schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/baobab
%{_desktopdir}/baobab.desktop
%{_iconsdir}/hicolor/*/*/*.png
%{_iconsdir}/hicolor/*/*/*.svg
%{_iconsdir}/HighContrast/*/*/*.png
%{_datadir}/glib-2.0/schemas/org.gnome.baobab.gschema.xml
%{_mandir}/man1/baobab.1*
