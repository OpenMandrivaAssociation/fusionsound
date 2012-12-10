%define oname FusionSound

%define major 2
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

%define dfbmoduledir %(pkg-config --variable=moduledir direct)

Name:		fusionsound
Version:	1.6.2
Release:	1
License:	GPLv2+
Group:		System/Libraries
Summary:	An audio sub system
Url:		http://www.directfb.org
Source0:	http://www.directfb.org/downloads/Core/%{oname}-%{version}.tar.gz
Patch0:		FusionSound-1.6.2-ffmpeg1.0.patch
Patch1:		fusionsound-20080311-fix-format-errors.patch
BuildRequires:	ffmpeg-devel
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(directfb)
BuildRequires:	pkgconfig(libcddb)
BuildRequires:	pkgconfig(mad)
BuildRequires:	pkgconfig(vorbis)
Provides:	%{oname} = %{version}-%{release}

%description
FusionSound is a very powerful audio sub system in the
manner of DirectFB and a technical demonstration of Fusion.

FusionSound supports multiple applications using Fusion IPC.
It provides streams, static sound buffers and control over any
number of concurrent playbacks. Sample data is always stored
in shared memory, starting a playback simply adds an entry to
the playlist of the mixer thread in the master application.

%package -n %{libname}
Group:		System/Libraries
Summary:	An audio sub sytem

%description -n %{libname}
FusionSound is a very powerful audio sub system in the
manner of DirectFB and a technical demonstration of Fusion. 

FusionSound supports multiple applications using Fusion IPC.
It provides streams, static sound buffers and control over any
number of concurrent playbacks. Sample data is always stored
in shared memory, starting a playback simply adds an entry to
the playlist of the mixer thread in the master application.

%package -n %{develname}
Group:		Development/Other
Summary:	An audio sub system
Requires:	%{libname} = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
FusionSound is a very powerful audio sub system in the
manner of DirectFB and a technical demonstration of Fusion.

FusionSound supports multiple applications using Fusion IPC.
It provides streams, static sound buffers and control over any
number of concurrent playbacks. Sample data is always stored
in shared memory, starting a playback simply adds an entry to
the playlist of the mixer thread in the master application.


%prep
%setup -q -n %{oname}-%{version}
%patch0 -p1
%patch1 -p2

%build
autoreconf -fi
%configure2_5x
%make

%install
%makeinstall_std

%files
%doc AUTHORS ChangeLog TODO
%{_bindir}/fs*
%{_mandir}/*/%{name}*
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

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%doc AUTHORS ChangeLog TODO
%{_libdir}/pkgconfig/fusionsound*.pc
%{_includedir}/fusionsound
%{_includedir}/fusionsound-internal
%{_libdir}/*.so

