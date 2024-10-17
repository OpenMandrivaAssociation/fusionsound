%bcond_with bootstrap

%define oname FusionSound
%define major 2
%define api 1.6
%define libname %mklibname %{name} %{api} %{major}
%define devname %mklibname %{name} %{api} -d

%define dfbmoduledir %(pkg-config --variable=moduledir direct)

Name:		fusionsound
Version:	1.6.3
Release:	5
License:	GPLv2+
Group:		System/Libraries
Summary:	An audio sub system
Url:		https://www.directfb.org
Source0:	http://www.directfb.org/downloads/Core/FusionSound/%{oname}-%{version}.tar.gz
Patch0:		FusionSound-1.6.3-ffmpeg2.patch
Patch1:		FusionSound-1.6.3-ffmpeg2.4.patch
%if !%{with bootstrap}
BuildRequires:	ffmpeg-devel
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(directfb)
BuildRequires:	pkgconfig(libcddb)
BuildRequires:	pkgconfig(mad)
BuildRequires:	pkgconfig(vorbis)
%endif
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

%package -n %{devname}
Group:		Development/Other
Summary:	An audio sub system
Requires:	%{libname} = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
FusionSound is a very powerful audio sub system in the
manner of DirectFB and a technical demonstration of Fusion.

FusionSound supports multiple applications using Fusion IPC.
It provides streams, static sound buffers and control over any
number of concurrent playbacks. Sample data is always stored
in shared memory, starting a playback simply adds an entry to
the playlist of the mixer thread in the master application.


%prep
%setup -q -n %{oname}-%{version}
%apply_patches
autoreconf -fi

%build
%configure \
		--with-cdda \
		--with-ffmpeg \
		--with-mad \
		--with-timidity \
		--with-wave \
		--with-playlist \
		--with-voodoo \
		--with-vorbis \
		--enable-ieee-floats \
		--enable-module
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
%if !%{with bootstrap}
%{dfbmoduledir}/interfaces/IFusionSoundMusicProvider/libifusionsoundmusicprovider_ffmpeg.*
%{dfbmoduledir}/interfaces/IFusionSoundMusicProvider/libifusionsoundmusicprovider_mad.*
%{dfbmoduledir}/interfaces/IFusionSoundMusicProvider/libifusionsoundmusicprovider_vorbis.*
%dir %{dfbmoduledir}/snddrivers
%{dfbmoduledir}/snddrivers/libfusionsound_alsa.*
%endif
%{dfbmoduledir}/interfaces/IFusionSoundMusicProvider/libifusionsoundmusicprovider_playlist.*
%{dfbmoduledir}/interfaces/IFusionSoundMusicProvider/libifusionsoundmusicprovider_wave.*
%{dfbmoduledir}/snddrivers/libfusionsound_dummy.*
%{dfbmoduledir}/snddrivers/libfusionsound_oss.*
%{dfbmoduledir}/snddrivers/libfusionsound_wave.*

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%{_libdir}/pkgconfig/fusionsound*.pc
%{_includedir}/fusionsound
%{_includedir}/fusionsound-internal
%{_libdir}/*.so
