Name: x11-driver-input
Version: 1.0.0
Release: %mkrel 11
Summary: X11 input drivers
Group: System/X11
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
License: GPL

Requires: x11-driver-input-acecad
Requires: x11-driver-input-aiptek
Requires: x11-driver-input-citron
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

%description
Meta-package which requires all X11 input drivers

%files
%defattr(-,root,root)
