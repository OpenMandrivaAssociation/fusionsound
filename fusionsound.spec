%define name    fusionsound
%define version 0.9.25
%define release %mkrel 2

%define major 0
%define libname %mklibname %{name} %{major}
%define obslibname %{_lib}FusionSound

%define directfbver %version

Name:           %{name}
Version:        %{version}
Release:        %{release}
License:        GPL
Url:            http://directfb.org/fusionsound.xml
Source0:        FusionSound-%{version}.tar.bz2
Group:          System/Libraries
Summary:        An audio sub system
BuildRequires:  DirectFB-devel => %directfbver
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Provides:	FusionSound
Obsoletes:	FusionSound

%description
FusionSound is a very powerful audio sub system in the
manner of DirectFB and a technical demonstration of Fusion.

FusionSound supports multiple applications using Fusion IPC.
It provides streams, static sound buffers and control over any
number of concurrent playbacks. Sample data is always stored
in shared memory, starting a playback simply adds an entry to
the playlist of the mixer thread in the master application.

%package -n %libname
Group:          System/Libraries
Summary:        An audio sub sytem
Provides:	lib%{name} = %version-%release
Provides:       %obslibname
Obsoletes:      %obslibname

%description -n %libname
FusionSound is a very powerful audio sub system in the
manner of DirectFB and a technical demonstration of Fusion. 

FusionSound supports multiple applications using Fusion IPC.
It provides streams, static sound buffers and control over any
number of concurrent playbacks. Sample data is always stored
in shared memory, starting a playback simply adds an entry to
the playlist of the mixer thread in the master application.

%package -n %libname-devel
Group:          Development/Other
Summary:        An audio sub system
Requires:	%libname = %version-%release
Provides:	lib%name-devel = %version-%release
Provides:	%obslibname-devel
Obsoletes:	%obslibname-devel

%description -n %libname-devel
FusionSound is a very powerful audio sub system in the
manner of DirectFB and a technical demonstration of Fusion.

FusionSound supports multiple applications using Fusion IPC.
It provides streams, static sound buffers and control over any
number of concurrent playbacks. Sample data is always stored
in shared memory, starting a playback simply adds an entry to
the playlist of the mixer thread in the master application.


%prep
%setup -q -n FusionSound-%{version}

%build
%configure
%make

%install
%makeinstall_std

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%post -n %libname -p /sbin/ldconfig
%postun -n %libname -p /sbin/ldconfig

%files -n %name
%defattr(-,root,root)
%doc AUTHORS ChangeLog TODO
%dir %_libdir/directfb-*/interfaces/IFusionSound
%dir %_libdir/directfb-*/interfaces/IFusionSoundMusicProvider
%_libdir/directfb-*/interfaces/*/*.so
%_bindir/fsmaster

%files -n %libname
%defattr(-,root,root)
%doc AUTHORS ChangeLog TODO
%_libdir/*.so.*

%files -n %libname-devel
%defattr(-,root,root)
%doc AUTHORS ChangeLog TODO
%_libdir/directfb-*/interfaces/*/*.la
%_libdir/pkgconfig/fusionsound.pc
%_includedir/fusionsound 
%_includedir/fusionsound-internal
%_libdir/*.so
%_libdir/*.la


