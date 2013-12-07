%define	name	quadra
%define	version	1.2.0
%define summary	Multiplayer puzzle game

Name:		%{name}
Version:	%{version}
Release:	10
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
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xpm)
BuildRequires:	pkgconfig(xxf86vm)
BuildRequires:	pkgconfig(libpng)
BuildRequires:  bc

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


%changelog
* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 1.2.0-6mdv2011.0
+ Revision: 669392
- mass rebuild

* Sat Jan 01 2011 Funda Wang <fwang@mandriva.org> 1.2.0-5mdv2011.0
+ Revision: 626972
- tighten BR

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 1.2.0-4mdv2011.0
+ Revision: 607265
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 1.2.0-2mdv2010.1
+ Revision: 523886
- rebuilt for 2010.1

* Mon Jun 08 2009 JÃ©rÃ´me Brenier <incubusss@mandriva.org> 1.2.0-1mdv2010.0
+ Revision: 383822
- [prw]
- update to new version 1.2.0
- drop 6 patches (merged upstream or no more needed)
- add 1 patch to fix str fmt (sent upstream)
- clean spec file
- fix license

  + Christophe Fergeau <cfergeau@mandriva.com>
    - fix compilation with gcc4.4 (still link issues)

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Wed Mar 05 2008 Oden Eriksson <oeriksson@mandriva.com> 1.1.8-16mdv2008.1
+ Revision: 179411
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - drop old menu
    - kill re-definition of %%buildroot on Pixel's request
    - buildrequires X11-devel instead of XFree86-devel

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Aug 30 2007 Pixel <pixel@mandriva.com> 1.1.8-15mdv2008.0
+ Revision: 75476
- fix build with g++ 4.2

  + Oden Eriksson <oeriksson@mandriva.com>
    - Import quadra



* Fri Jul  7 2006 Pixel <pixel@mandriva.com> 1.1.8-14mdv2007.0
- use mkrel
- switch to XDG menu

* Tue Oct 11 2005 Pixel <pixel@mandriva.com> 1.1.8-13mdk
- rebuild

* Mon Aug 16 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 1.1.8-12mdk
- Rebuild with new menu

* Fri Jun  4 2004 Pixel <pixel@mandrakesoft.com> 1.1.8-11mdk
- rebuild
- fix build

* Tue Oct 21 2003 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 1.1.8-10mdk
- 64-bit fixes

* Wed Jul 30 2003 Götz Waschk <waschk@linux-mandrake.com> 1.1.8-9mdk
- patch3 fixes a C++ syntax error found by gcc 3.3
- buildrequires

* Mon Jul 14 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 1.1.8-8mdk
- make sure it links against necessary libraies when linking against png (P2)

* Wed Nov 13 2002 Per Øyvind Karlsen <peroyvind@delonic.no> 1.1.8-7mdk
- Added menuitem
- Added icons
- Cleanups
- Install stuff in the right places
- Use %%makeinstall, since it works, why use anything else?
- Remove ExclusiveArch: x86 as we do not build against svgalib anymore

* Wed Aug 14 2002 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 1.1.8-6mdk
- Automated rebuild with gcc 3.2-0.3mdk

* Thu Jul 25 2002 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 1.1.8-5mdk
- Automated rebuild with gcc3.2

* Thu May 30 2002 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 1.1.8-4mdk
- Remove BuildRequires: svgalib-devel
- Patch0: Add missing includes. Don't conflict with basename() from <libgen.h>
- Patch1: ISO C++ fixes. vector<>::insert() does take an iterator, not
  a pointer to an element. I prefer catching references to exceptions

* Sat Feb  2 2002 Pixel <pixel@mandrakesoft.com> 1.1.8-3mdk
- fix URL

* Fri Nov 16 2001 Jeff Garzik <jgarzik@mandrakesoft.com> 1.1.8-2mdk
- use %%old_makeinstall

* Fri Oct 26 2001 Pixel <pixel@mandrakesoft.com> 1.1.8-1mdk
- new version

* Thu Oct 11 2001 Pixel <pixel@mandrakesoft.com> 1.1.7-4mdk
- rebuilding for libpng3

* Sun Jul 15 2001 Jeff Garzik <jgarzik@mandrakesoft.com> 1.1.7-3mdk
- ExclusiveArch: x86, the only svgalib platform

* Sun Jul 01 2001 Stefan van der Eijk <stefan@eijk.nu> 1.1.7-2mdk
- BuildRequires:	libpng-devel svgalib-devel XFree86-devel xpm-devel

* Fri May  4 2001 Pixel <pixel@mandrakesoft.com> 1.1.7-1mdk
- new version

* Thu Jan 18 2001 David BAUDENS <baudens@mandrakesoft.com> 1.1.5-3mdk
- ExcludeArch: ppc

* Thu Nov 16 2000 Pixel <pixel@mandrakesoft.com> 1.1.5-2mdk
- libstd rebuild

* Wed Oct 18 2000 Pixel <pixel@mandrakesoft.com> 1.1.5-1mdk
- first mdk version
