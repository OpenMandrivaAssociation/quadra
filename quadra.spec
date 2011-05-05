%define	name	quadra
%define	version	1.2.0
%define summary	Multiplayer puzzle game

Name:		%{name}
Version:	%{version}
Release:	%mkrel 6
URL:		http://code.google.com/p/quadra/
Source0:	http://quadra.googlecode.com/files/%{name}-%{version}.tar.gz
Source1:	%{name}-icons.tar.bz2
Source5:	%{name}-16.png
Source6:	%{name}-32.png
Source7:	%{name}-48.png
# fix str fmt, patch sent upstream 08 Jun 2009
Patch0:		%{name}-1.2.0-fix-str-fmt.patch
License:	LGPLv2+
Group:		Games/Arcade
Summary:	%{summary}
BuildRequires:	libx11-devel
BuildRequires:	libxext-devel
BuildRequires:	libxpm-devel
BuildRequires:	libxxf86vm-devel
BuildRequires:	libpng-devel
BuildRequires:  bc
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
This is the official release %{version} of Quadra, a full-featured
multiplayer action puzzle game for the X Window System and Svgalib.
Features include:

 - Recursive block chaining
 - Blocks shadows
 - Teams playing
 - TCP/IP networking (free Internet playing! Supports SOCKS proxies)
 - Smooth block falling
 - Sound effects
 - Watches on other players
 - Chat window
 - CD-based music
 - And much more!

%prep
%setup -q
%patch0 -p1 -b .strfmt

cat << EOF > mandriva-%{name}.desktop
[Desktop Entry]
Encoding=UTF-8
Name=Quadra
Comment=%{summary}
Exec=%_gamesbindir/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Game;ArcadeGame;
EOF

%build
%configure2_5x --bindir=%{_gamesbindir}
%make

%install
rm -rf %{buildroot}
%makeinstall_std
#install -s -D source/quadra $RPM_BUILD_ROOT%{_bindir}/quadra
#install -m644 -D source/quadra.res $RPM_BUILD_ROOT%{_datadir}/games/quadra.res

install -D -m644 mandriva-%{name}.desktop %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop
install -D -m644 %SOURCE6 %{buildroot}%{_iconsdir}/%{name}.png
install -D -m644 %SOURCE5 %{buildroot}%{_miconsdir}/%{name}.png
install -D -m644 %SOURCE7 %{buildroot}%{_liconsdir}/%{name}.png

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog LICENSE README
%{_gamesbindir}/*
%{_gamesdatadir}/quadra.res
%{_datadir}/pixmaps/*
%{_datadir}/applications/*
%{_iconsdir}/*.png
%{_miconsdir}/*.png
%{_liconsdir}/*.png
