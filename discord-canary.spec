%global         debug_package %{nil}
%global         __strip /bin/true
%global         __requires_exclude libffmpeg.so
%global         _build_id_links none
###############################Exclude Private bundled libs###########################
%global __provides_exclude_from %{_libdir}/discord-canary/.*\\.s

Name:           discord-canary
# Version managed by tito
Version:        0.0.536
# Release managed by tito
Release:        2
Summary:        All-in-one voice and text chat

# License Information: https://bugzilla.rpmfusion.org/show_bug.cgi?id=4441#c14
License:        Proprietary
URL:            https://discordapp.com/
Source0:        https://canary.dl2.discordapp.net/apps/linux/%{version}/%{name}-%{version}.tar.gz#/discord-canary.tar.gz
# Adapted from https://raw.githubusercontent.com/flathub/com.discordapp.Discord/master/com.discordapp.Discord.appdata.xml
Source1:        discord-canary.metainfo.xml
Source2:        wrapper.sh
Source3:        disable-breaking-updates.py
ExclusiveArch:  x86_64

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

# From official discord-0.0.58.deb
# Depends: libc6, libasound2, libatomic1, libnotify4, libnspr4, libnss3, libstdc++6, libxss1, libxtst6
# Recommends: libappindicator1 | libayatana-appindicator1

Requires:       glibc%{_isa}
Requires:       alsa-lib%{_isa}
Requires:       libatomic%{_isa}
Requires:       libnotify%{_isa}
Requires:       nspr%{_isa} >= 4.13
Requires:       nss%{_isa} >= 3.27
Requires:       libstdc++%{_isa}
Requires:       libXtst%{_isa} >= 1.2
Requires:       hicolor-icon-theme

%if !0%{?el7}
Recommends:     (libayatana-appindicator-gtk3%{_isa} if gtk3%{_isa})
Recommends:     google-noto-emoji-color-fonts
Recommends:     libXScrnSaver
%endif

%description
Linux Release for Discord Canary, the experimental version of a free proprietary VoIP application

%prep
%autosetup -n DiscordCanary

%build

%install
mkdir -p %{buildroot}/%{_bindir}/
mkdir -p %{buildroot}/%{_libdir}/discord-canary
mkdir -p %{buildroot}/%{_datadir}/applications
mkdir -p %{buildroot}%{_metainfodir}/

desktop-file-install                                  \
--set-icon=%{name}                                    \
--set-key=Exec --set-value=%{_bindir}/DiscordCanary   \
--remove-key=Path                                     \
--delete-original                                     \
--dir=%{buildroot}/%{_datadir}/applications           \
discord-canary.desktop

cp -r * %{buildroot}/%{_libdir}/discord-canary/
ln -sf ../%{_lib}/discord-canary/wrapper.sh %{buildroot}/%{_bindir}/DiscordCanary
install -p -D -m 644 discord.png \
        %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/%{name}.png

install -p -m 0644 %{SOURCE1} %{buildroot}%{_metainfodir}/
install -p -m 755 %{SOURCE2} %{buildroot}%{_libdir}/discord-canary/
install -p -m 755 %{SOURCE3} %{buildroot}%{_libdir}/discord-canary/

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.metainfo.xml

%files
%{_libdir}/discord-canary/
%{_bindir}/DiscordCanary
%{_datadir}/applications/discord-canary.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_metainfodir}/%{name}.metainfo.xml


%changelog
* Wed Dec 11 2024 garzj <johannes@garz.dev> 0.0.536-2
- fix: discord lib path name (johannes@garz.dev)
* Sun Dec 08 2024 garzj <johannes@garz.dev> 0.0.536-1
- Fork https://github.com/rpmfusion/discord/tree/master, adapt for Discord Canary
- Initial build at version 0.0.536