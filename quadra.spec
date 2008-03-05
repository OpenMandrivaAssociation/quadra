%define	name	quadra
%define	version	1.1.8
%define summary	Multiplayer puzzle game

Name:		%{name}
Version:	%{version}
Release:	%mkrel 16
URL:		http://quadra.sf.net/
Source0:	http://download.sourceforge.net/quadra/%{name}-%{version}.tar.bz2
Source1:	%{name}-icons.tar.bz2
Source5:	%{name}-16.png
Source6:	%{name}-32.png
Source7:	%{name}-48.png
Patch0:		quadra-1.1.8-includes.patch
Patch1:		quadra-1.1.8-c++fixes.patch
Patch2:		%{name}-1.1.8-link.patch
Patch3:		quadra-1.1.8-gcc3.3.patch
Patch4:		quadra-1.1.8-64bit-fixes.patch
Patch5:		quadra-1.1.8-fix-compilation.patch
License:	LGPL
Group:		Games/Arcade
Summary:	%{summary}
BuildRequires:	libpng-devel
BuildRequires:	X11-devel
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
%patch0 -p1 -b .includes
%patch1 -p1 -b .c++fixes
%patch2 -p0 -b .perovyind
%patch3 -p1 -b .gcc3.3
%patch4 -p1 -b .64bit-fixes
%patch5 -p1 -b .compilation

cat <<EOF > %{name}.menu
?package(%{name}):command="%{_gamesbindir}/%{name}" \
		  icon=%{name}.png \
		  needs="x11" \
		  section="More Applications/Games/Arcade" \
		  title="Quadra"\
		  longtitle="%{summary}" xdg="true"
EOF

cat << EOF > mandriva-%{name}.desktop
[Desktop Entry]
Encoding=UTF-8
Name=Quadra
Comment=%{summary}
Exec=%_gamesbindir/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Game;ArcadeGame;X-MandrivaLinux-MoreApplications-Games-Arcade;
EOF

%build
X_EXTRA_LIBS="-lz" \
%configure --without-svgalib
%make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT
%makeinstall bindir=$RPM_BUILD_ROOT%{_gamesbindir}
#install -s -D source/quadra $RPM_BUILD_ROOT%{_bindir}/quadra
#install -m644 -D source/quadra.res $RPM_BUILD_ROOT%{_datadir}/games/quadra.res

install -D -m644 mandriva-%{name}.desktop $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop
install -D -m644 %SOURCE6 $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
install -D -m644 %SOURCE5 $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png
install -D -m644 %SOURCE7 $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png

%post
%update_menus

%postun
%clean_menus

%clean
rm -rf $RPM_BUILD_ROOT

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
