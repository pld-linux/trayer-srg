# TODO: optflags
Summary:	A lightweight GTK2-based systray for UNIX desktop
Summary(pl.UTF-8):	Lekki, bazujący na GTK2 dok systemowy (systray)
Name:		trayer-srg
Version:	1.1.5
Release:	1
License:	BSD
Group:		X11/Window Managers
Source0:	https://github.com/sargon/trayer-srg/archive/trayer-%{version}.tar.gz
# Source0-md5:	b2be3dcb40797e0d4447db45ddd9b0a6
URL:		https://github.com/sargon/trayer-srg
BuildRequires:	gtk+2-devel
BuildRequires:	pkgconfig
BuildRequires:	xorg-lib-libXmu-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Trayer is small program designed to provide system tray similar to
these in GNOME/KDE desktop environments for window managers which does
not support that function.

%description -l pl.UTF-8
Trayer jest małym programem zaprojektowanym by dostarczać funkcje doku
systemowego znanego z GNOME/KDE dla środowisk okienkowych nie
posiadających tej funkcjonalności.

%prep
%setup -q -n %{name}-trayer-%{version}

%build
%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install \
	PREFIX=$RPM_BUILD_ROOT%{_prefix}

install -d $RPM_BUILD_ROOT%{_mandir}/man1
install man/trayer.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG CREDITS
%attr(755,root,root) %{_bindir}/trayer
%{_mandir}/man1/trayer.1*
