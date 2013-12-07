Name: x11-driver-input
Version: 1.0.0
Release: 18
Summary: X11 input drivers
Group: System/X11
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
License: GPL

Requires: x11-driver-input-acecad
Requires: x11-driver-input-aiptek
Requires: x11-driver-input-evdev
Requires: x11-driver-input-fpit
Requires: x11-driver-input-hyperpen
Requires: x11-driver-input-joystick
Requires: x11-driver-input-keyboard
Requires: x11-driver-input-mouse
Requires: x11-driver-input-mutouch
Requires: x11-driver-input-penmount
Requires: x11-driver-input-synaptics
Requires: x11-driver-input-void
Requires: x11-driver-input-wacom

Obsoletes: x11-driver-input-calcomp
Obsoletes: x11-driver-input-digitaledge
Obsoletes: x11-driver-input-dmc
Obsoletes: x11-driver-input-dynapro
Obsoletes: x11-driver-input-elo2300
Obsoletes: x11-driver-input-elographics
Obsoletes: x11-driver-input-jamstudio
Obsoletes: x11-driver-input-magellan
Obsoletes: x11-driver-input-magictouch
Obsoletes: x11-driver-input-microtouch
Obsoletes: x11-driver-input-palmax
Obsoletes: x11-driver-input-spaceorb
Obsoletes: x11-driver-input-summa
Obsoletes: x11-driver-input-tek4957
Obsoletes: x11-driver-input-ur98
Obsoletes: x11-driver-input-wiimote

%description
Meta-package which requires all X11 input drivers

%files
%defattr(-,root,root)


%changelog
* Thu Jun 09 2011 Eugeni Dodonov <eugeni@mandriva.com> 1.0.0-15mdv2011.0
+ Revision: 683785
- Do not request evtouch driver anymore.

* Fri Apr 15 2011 Eugeni Dodonov <eugeni@mandriva.com> 1.0.0-14
+ Revision: 653195
- Do not require x11-driver-input-citron

* Sun Oct 10 2010 Thierry Vignaud <tv@mandriva.org> 1.0.0-13mdv2011.0
+ Revision: 584626
- bump release before rebuilding for xserver 1.9

* Tue Apr 13 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.0.0-12mdv2010.1
+ Revision: 534519
- Add missing drivers: evtouch and wacom
- Obsolete x11-driver-input-wiimote

* Tue Jan 19 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.0.0-11mdv2010.1
+ Revision: 493627
- Obsolete unmaintained input drivers

* Sun Nov 30 2008 Thierry Vignaud <tv@mandriva.org> 1.0.0-10mdv2009.1
+ Revision: 308660
- require x11-driver-input-synaptics too as it obsoletes synaptics

* Tue Sep 09 2008 Olivier Blin <oblin@mandriva.com> 1.0.0-9mdv2009.0
+ Revision: 282977
- do not require x11-driver-input-vboxmouse, this is handled in rpmsrate

* Mon Sep 08 2008 Thierry Vignaud <tv@mandriva.org> 1.0.0-8mdv2009.0
+ Revision: 282696
- requires x11-driver-input-vboxmouse so that it work out of the box in vbox

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.0.0-7mdv2009.0
+ Revision: 225942
- rebuild
- fix no-buildroot-tag

* Mon Oct 15 2007 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 1.0.0-6mdv2008.1
+ Revision: 98613
- minor package description improvement

* Thu Aug 30 2007 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-5mdv2008.0
+ Revision: 75596
- rebuild


* Mon Sep 18 2006 Pixel <pixel@mandriva.com>
+ 2006-09-18 16:18:32 (61943)
- do not obsolete xorg-x11-server which is still a package in 2007.0

* Thu Jun 08 2006 Thierry Vignaud <tvignaud@mandriva.com>
+ 2006-06-08 16:47:26 (36813)
- fix group

* Wed May 31 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-31 18:32:34 (31796)
- rebuild to fix cooker uploading

* Mon May 29 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-05-29 14:36:37 (31646)
- renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 21:25:17 (26918)
- increment release

* Thu Apr 27 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-04-27 04:02:05 (26704)
- Adding X.org 7.0 to the repository

