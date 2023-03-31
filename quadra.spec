Summary:	Multiplayer puzzle game
Name:		quadra
Version:	1.2.0
Release:	17
License:	LGPLv2+
Group:		Games/Arcade
Url:		http://code.google.com/p/quadra/
Source0:	http://quadra.googlecode.com/files/%{name}-%{version}.tar.gz
Source1:	%{name}-icons.tar.bz2
Source5:	%{name}-16.png
Source6:	%{name}-32.png
Source7:	%{name}-48.png
# fix str fmt, patch sent upstream 08 Jun 2009
Patch0:	%{name}-1.2.0-fix-str-fmt.patch
BuildRequires:	bc
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xpm)
BuildRequires:	pkgconfig(xxf86vm)
BuildRequires:	pkgconfig(libpng)

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
%autopatch -p1

cat << EOF > %{name}.desktop
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
%makeinstall_std
#install -s -D source/quadra $RPM_BUILD_ROOT%{_bindir}/quadra
#install -m644 -D source/quadra.res $RPM_BUILD_ROOT%{_datadir}/games/quadra.res

install -D -m644 %{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop
install -D -m644 %SOURCE6 %{buildroot}%{_iconsdir}/%{name}.png
install -D -m644 %SOURCE5 %{buildroot}%{_miconsdir}/%{name}.png
install -D -m644 %SOURCE7 %{buildroot}%{_liconsdir}/%{name}.png

%files
%doc ChangeLog LICENSE README
%{_gamesbindir}/*
%{_gamesdatadir}/quadra.res
%{_datadir}/pixmaps/*
%{_datadir}/applications/*
%{_iconsdir}/*.png
%{_miconsdir}/*.png
%{_liconsdir}/*.png

