%define name    fusionsound
%define version 1.1.1
%define snapdate 20081101
%define release %mkrel 2.%{snapdate}.1

%define api 1.1
%define major 1
%define libname %mklibname %{name} %{api} %{major}
%define develname %mklibname %name -d
%define directfbver %version
%define dfbmoduledir %(pkg-config --variable=moduledir direct)

Name:           %{name}
Version:        %{version}
Release:        %{release}
License:        GPLv2+
Group:          System/Libraries
Summary:        An audio sub system
Url:            http://www.directfb.org/index.php?path=Platform%2FFusionSound
Source0:        http://www.directfb.org/downloads/Core/FusionSound-%{snapdate}.tar.bz2
Patch1:		    fusionsound-20080311-fix-format-errors.patch
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
%setup -q -n FusionSound
%patch1 -p2

%build
autoreconf -fi
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
%dir %{dfbmoduledir}/interfaces/IFusionSound
%{dfbmoduledir}/interfaces/IFusionSound/libifusionsound.*
%dir %{dfbmoduledir}/interfaces/IFusionSoundMusicProvider
%{dfbmoduledir}/interfaces/IFusionSoundMusicProvider/libifusionsoundmusicprovider_cdda.*
%{dfbmoduledir}/interfaces/IFusionSoundMusicProvider/libifusionsoundmusicprovider_ffmpeg.*
%{dfbmoduledir}/interfaces/IFusionSoundMusicProvider/libifusionsoundmusicprovider_mad.*
%{dfbmoduledir}/interfaces/IFusionSoundMusicProvider/libifusionsoundmusicprovider_playlist.*
%{dfbmoduledir}/interfaces/IFusionSoundMusicProvider/libifusionsoundmusicprovider_vorbis.*
%{dfbmoduledir}/interfaces/IFusionSoundMusicProvider/libifusionsoundmusicprovider_wave.*
%dir %{dfbmoduledir}/snddrivers
%{dfbmoduledir}/snddrivers/libfusionsound_alsa.*
%{dfbmoduledir}/snddrivers/libfusionsound_oss.*
%{dfbmoduledir}/snddrivers/libfusionsound_wave.*

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
