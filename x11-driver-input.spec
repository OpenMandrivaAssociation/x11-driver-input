Name: x11-driver-input
Version: 1.0.0
Release: %mkrel 9
Summary: X11 input drivers
Group: System/X11
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
License: GPL
Requires: x11-driver-input-acecad
Requires: x11-driver-input-aiptek
Requires: x11-driver-input-calcomp
Requires: x11-driver-input-citron
Requires: x11-driver-input-digitaledge
Requires: x11-driver-input-dmc
Requires: x11-driver-input-dynapro
Requires: x11-driver-input-elo2300
Requires: x11-driver-input-elographics
Requires: x11-driver-input-evdev
Requires: x11-driver-input-fpit
Requires: x11-driver-input-hyperpen
Requires: x11-driver-input-jamstudio
Requires: x11-driver-input-joystick
Requires: x11-driver-input-keyboard
Requires: x11-driver-input-magellan
Requires: x11-driver-input-magictouch
Requires: x11-driver-input-microtouch
Requires: x11-driver-input-mouse
Requires: x11-driver-input-mutouch
Requires: x11-driver-input-palmax
Requires: x11-driver-input-penmount
Requires: x11-driver-input-spaceorb
Requires: x11-driver-input-summa
Requires: x11-driver-input-tek4957
Requires: x11-driver-input-ur98
Requires: x11-driver-input-void

%description
Meta-package which requires all X11 input drivers

%files
%defattr(-,root,root)
