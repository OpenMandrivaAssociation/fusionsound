%define name    fusionsound
%define version 1.1.1
%define release %mkrel 2

%define api 1.1
%define major 1
%define libname %mklibname %{name} %{api} %{major}
%define develname %mklibname %name -d
%define directfbver %version

Name:           %{name}
Version:        %{version}
Release:        %{release}
License:        GPL
Url:            http://www.directfb.org/index.php?path=Platform%2FFusionSound
Source0:        http://www.directfb.org/downloads/Core/FusionSound-%{version}.tar.gz
Patch0:		fusionsound-1.1.1-new-ffmpeg-header.patch
Group:          System/Libraries
Summary:        An audio sub system
BuildRequires:  DirectFB-devel => %directfbver
BuildRequires:	libcddb-devel
BuildRequires:	ffmpeg-devel
BuildRequires:	libalsa-devel
BuildRequires:	oggvorbis-devel
BuildRequires:	mad-devel
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

%description -n %libname
FusionSound is a very powerful audio sub system in the
manner of DirectFB and a technical demonstration of Fusion. 

FusionSound supports multiple applications using Fusion IPC.
It provides streams, static sound buffers and control over any
number of concurrent playbacks. Sample data is always stored
in shared memory, starting a playback simply adds an entry to
the playlist of the mixer thread in the master application.

%package -n %develname
Group:          Development/Other
Summary:        An audio sub system
Requires:	%libname = %version-%release
Provides:	lib%name-devel = %version-%release
Provides:	%name-devel = %version-%release
Obsoletes:	%mklibname -d FusionSound
Obsoletes:	%mklibname -d fusionsound 0

%description -n %develname
FusionSound is a very powerful audio sub system in the
manner of DirectFB and a technical demonstration of Fusion.

FusionSound supports multiple applications using Fusion IPC.
It provides streams, static sound buffers and control over any
number of concurrent playbacks. Sample data is always stored
in shared memory, starting a playback simply adds an entry to
the playlist of the mixer thread in the master application.


%prep
%setup -q -n FusionSound-%{version}
%patch0 -p1

%build
%configure2_5x
%make

%install
rm -fr %buildroot
%makeinstall_std

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post -n %libname -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libname -p /sbin/ldconfig
%endif

%files -n %name
%defattr(-,root,root)
%doc AUTHORS ChangeLog TODO
%_bindir/fs*
%_mandir/*/%{name}*
%dir %_libdir/interfaces/IFusionSound
%_libdir/interfaces/IFusionSound/libifusionsound.*
%dir %_libdir/interfaces/IFusionSoundMusicProvider
%_libdir/interfaces/IFusionSoundMusicProvider/libifusionsoundmusicprovider_cdda.*
%_libdir/interfaces/IFusionSoundMusicProvider/libifusionsoundmusicprovider_ffmpeg.*
%_libdir/interfaces/IFusionSoundMusicProvider/libifusionsoundmusicprovider_mad.*
%_libdir/interfaces/IFusionSoundMusicProvider/libifusionsoundmusicprovider_playlist.*
%_libdir/interfaces/IFusionSoundMusicProvider/libifusionsoundmusicprovider_vorbis.*
%_libdir/interfaces/IFusionSoundMusicProvider/libifusionsoundmusicprovider_wave.*
%dir %_libdir/snddrivers
%_libdir/snddrivers/libfusionsound_alsa.*
%_libdir/snddrivers/libfusionsound_oss.*
%_libdir/snddrivers/libfusionsound_wave.*

%files -n %libname
%defattr(-,root,root)
%doc AUTHORS ChangeLog TODO
%_libdir/*.so.%{major}*

%files -n %develname
%defattr(-,root,root)
%doc AUTHORS ChangeLog TODO
%_libdir/pkgconfig/fusionsound*.pc
%_includedir/fusionsound 
%_includedir/fusionsound-internal
%_libdir/*.so
%_libdir/*.la
