%global         debug_package %{nil}
%global         __strip /bin/true
%global         __requires_exclude libffmpeg.so
%global         _build_id_links none
###############################Exclude Private bundled libs###########################
%global __provides_exclude_from %{_libdir}/discord-canary/.*\\.s

Name:           discord-canary
# Version managed by tito
Version:        0.0.718
# Release managed by tito
Release:        1
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
* Wed Jul 16 2025 garzj <pkg@garz.dev> 0.0.718-1
- Update to 0.0.718

* Fri Jul 11 2025 garzj <pkg@garz.dev> 0.0.717-1
- Update to 0.0.717

* Thu Jul 10 2025 garzj <pkg@garz.dev> 0.0.716-1
- Update to 0.0.716

* Wed Jul 09 2025 garzj <pkg@garz.dev> 0.0.715-1
- Update to 0.0.715

* Tue Jul 08 2025 garzj <pkg@garz.dev> 0.0.713-1
- Update to 0.0.713

* Fri Jul 04 2025 garzj <pkg@garz.dev> 0.0.712-1
- Update to 0.0.712

* Thu Jul 03 2025 garzj <pkg@garz.dev> 0.0.711-1
- Update to 0.0.711

* Wed Jul 02 2025 garzj <pkg@garz.dev> 0.0.709-1
- Update to 0.0.709

* Fri Jun 27 2025 garzj <pkg@garz.dev> 0.0.706-1
- Update to 0.0.706

* Wed Jun 25 2025 garzj <pkg@garz.dev> 0.0.705-1
- Update to 0.0.705

* Tue Jun 24 2025 garzj <pkg@garz.dev> 0.0.703-1
- Update to 0.0.703

* Thu Jun 19 2025 garzj <pkg@garz.dev> 0.0.702-1
- Update to 0.0.702

* Wed Jun 18 2025 garzj <pkg@garz.dev> 0.0.701-1
- Update to 0.0.701

* Tue Jun 17 2025 garzj <pkg@garz.dev> 0.0.700-1
- Update to 0.0.700

* Sat Jun 14 2025 garzj <pkg@garz.dev> 0.0.697-1
- Update to 0.0.697

* Thu Jun 12 2025 garzj <pkg@garz.dev> 0.0.696-1
- Update to 0.0.696

* Wed Jun 11 2025 garzj <pkg@garz.dev> 0.0.695-1
- Update to 0.0.695

* Tue Jun 10 2025 garzj <pkg@garz.dev> 0.0.693-1
- Update to 0.0.693

* Sat Jun 07 2025 garzj <pkg@garz.dev> 0.0.692-1
- Update to 0.0.692

* Fri Jun 06 2025 garzj <pkg@garz.dev> 0.0.690-1
- Update to 0.0.690

* Thu Jun 05 2025 garzj <pkg@garz.dev> 0.0.688-1
- Update to 0.0.688

* Thu May 29 2025 garzj <pkg@garz.dev> 0.0.687-1
- Update to 0.0.687

* Sun May 25 2025 garzj <pkg@garz.dev> 0.0.685-1
- Update to 0.0.685

* Sat May 24 2025 garzj <pkg@garz.dev> 0.0.683-1
- Update to 0.0.683

* Fri May 23 2025 garzj <pkg@garz.dev> 0.0.682-1
- Update to 0.0.682

* Thu May 22 2025 garzj <pkg@garz.dev> 0.0.680-1
- Update to 0.0.680

* Wed May 21 2025 garzj <pkg@garz.dev> 0.0.679-1
- Update to 0.0.679

* Sat May 17 2025 garzj <pkg@garz.dev> 0.0.678-1
- Update to 0.0.678

* Fri May 16 2025 garzj <pkg@garz.dev> 0.0.677-1
- Update to 0.0.677

* Thu May 15 2025 garzj <pkg@garz.dev> 0.0.676-1
- Update to 0.0.676

* Wed May 14 2025 garzj <pkg@garz.dev> 0.0.674-1
- Update to 0.0.674

* Tue May 13 2025 garzj <pkg@garz.dev> 0.0.673-1
- Update to 0.0.673

* Fri May 09 2025 garzj <pkg@garz.dev> 0.0.671-1
- Update to 0.0.671

* Wed May 07 2025 garzj <pkg@garz.dev> 0.0.670-1
- Update to 0.0.670

* Tue May 06 2025 garzj <pkg@garz.dev> 0.0.669-1
- Update to 0.0.669

* Sat May 03 2025 garzj <pkg@garz.dev> 0.0.668-1
- Update to 0.0.668

* Thu May 01 2025 garzj <pkg@garz.dev> 0.0.667-1
- Update to 0.0.667

* Wed Apr 30 2025 garzj <pkg@garz.dev> 0.0.666-1
- Update to 0.0.666

* Tue Apr 29 2025 garzj <pkg@garz.dev> 0.0.662-1
- Update to 0.0.662

* Mon Apr 28 2025 garzj <pkg@garz.dev> 0.0.661-1
- Update to 0.0.661

* Sat Apr 26 2025 garzj <pkg@garz.dev> 0.0.660-1
- Update to 0.0.660

* Thu Apr 24 2025 garzj <pkg@garz.dev> 0.0.659-1
- Update to 0.0.659

* Tue Apr 22 2025 garzj <pkg@garz.dev> 0.0.656-1
- Update to 0.0.656

* Sun Apr 20 2025 garzj <pkg@garz.dev> 0.0.649-1
- Update to 0.0.649

* Sat Apr 19 2025 garzj <pkg@garz.dev> 0.0.648-1
- Update to 0.0.648

* Fri Apr 18 2025 garzj <pkg@garz.dev> 0.0.645-1
- Update to 0.0.645

* Thu Apr 17 2025 garzj <pkg@garz.dev> 0.0.643-1
- Update to 0.0.643

* Wed Apr 16 2025 garzj <pkg@garz.dev> 0.0.642-1
- Update to 0.0.642

* Tue Apr 15 2025 garzj <pkg@garz.dev> 0.0.641-1
- Update to 0.0.641

* Sat Apr 12 2025 garzj <pkg@garz.dev> 0.0.638-1
- Update to 0.0.638

* Fri Apr 11 2025 garzj <pkg@garz.dev> 0.0.636-1
- Update to 0.0.636

* Thu Apr 10 2025 garzj <pkg@garz.dev> 0.0.632-1
- Update to 0.0.632

* Tue Apr 08 2025 garzj <pkg@garz.dev> 0.0.627-1
- Update to 0.0.627

* Sun Apr 06 2025 garzj <pkg@garz.dev> 0.0.626-1
- Update to 0.0.626

* Sat Apr 05 2025 garzj <pkg@garz.dev> 0.0.625-1
- Update to 0.0.625

* Fri Apr 04 2025 garzj <pkg@garz.dev> 0.0.623-1
- Update to 0.0.623

* Wed Apr 02 2025 garzj <pkg@garz.dev> 0.0.622-1
- Update to 0.0.622

* Fri Mar 28 2025 garzj <pkg@garz.dev> 0.0.621-1
- Update to 0.0.621

* Thu Mar 27 2025 garzj <pkg@garz.dev> 0.0.620-1
- Update to 0.0.620

* Tue Mar 25 2025 garzj <pkg@garz.dev> 0.0.619-1
- Update to 0.0.619

* Sat Mar 22 2025 garzj <pkg@garz.dev> 0.0.618-1
- Update to 0.0.618

* Fri Mar 21 2025 garzj <pkg@garz.dev> 0.0.616-1
- Update to 0.0.616

* Thu Mar 20 2025 garzj <pkg@garz.dev> 0.0.612-1
- Update to 0.0.612

* Wed Mar 19 2025 garzj <pkg@garz.dev> 0.0.610-1
- Update to 0.0.610

* Fri Mar 14 2025 garzj <pkg@garz.dev> 0.0.608-1
- Update to 0.0.608

* Sat Mar 08 2025 garzj <pkg@garz.dev> 0.0.606-1
- Update to 0.0.606

* Wed Mar 05 2025 garzj <pkg@garz.dev> 0.0.605-1
- Update to 0.0.605

* Mon Mar 03 2025 garzj <pkg@garz.dev> 0.0.602-1
- Update to 0.0.602

* Sat Mar 01 2025 garzj <pkg@garz.dev> 0.0.601-1
- Update to 0.0.601

* Fri Feb 28 2025 garzj <pkg@garz.dev> 0.0.600-1
- Update to 0.0.600

* Thu Feb 27 2025 garzj <pkg@garz.dev> 0.0.599-1
- Update to 0.0.599

* Wed Feb 26 2025 garzj <pkg@garz.dev> 0.0.598-1
- Update to 0.0.598

* Tue Feb 25 2025 garzj <pkg@garz.dev> 0.0.596-1
- Update to 0.0.596

* Fri Feb 21 2025 garzj <pkg@garz.dev> 0.0.594-1
- Update to 0.0.594

* Thu Feb 20 2025 garzj <pkg@garz.dev> 0.0.593-1
- Update to 0.0.593

* Fri Feb 14 2025 garzj <pkg@garz.dev> 0.0.591-1
- Update to 0.0.591

* Thu Feb 13 2025 garzj <pkg@garz.dev> 0.0.589-1
- Update to 0.0.589

* Wed Feb 12 2025 garzj <pkg@garz.dev> 0.0.587-1
- Update to 0.0.587

* Tue Feb 11 2025 garzj <pkg@garz.dev> 0.0.586-1
- Update to 0.0.586

* Sat Feb 08 2025 garzj <pkg@garz.dev> 0.0.585-1
- Update to 0.0.585

* Wed Feb 05 2025 garzj <pkg@garz.dev> 0.0.583-1
- Update to 0.0.583

* Sat Feb 01 2025 garzj <pkg@garz.dev> 0.0.581-1
- Update to 0.0.581

* Fri Jan 31 2025 garzj <pkg@garz.dev> 0.0.580-1
- Update to 0.0.580

* Thu Jan 30 2025 garzj <pkg@garz.dev> 0.0.578-1
- Update to 0.0.578

* Wed Jan 29 2025 garzj <pkg@garz.dev> 0.0.577-1
- Update to 0.0.577

* Tue Jan 28 2025 garzj <pkg@garz.dev> 0.0.575-1
- Update to 0.0.575

* Fri Jan 24 2025 garzj <pkg@garz.dev> 0.0.574-1
- Update to 0.0.574

* Thu Jan 23 2025 garzj <pkg@garz.dev> 0.0.573-1
- Update to 0.0.573

* Wed Jan 22 2025 garzj <pkg@garz.dev> 0.0.572-1
- Update to 0.0.572

* Sun Jan 19 2025 garzj <pkg@garz.dev> 0.0.571-1
- Update to 0.0.571

* Sat Jan 18 2025 garzj <pkg@garz.dev> 0.0.570-1
- Update to 0.0.570

* Fri Jan 17 2025 garzj <pkg@garz.dev> 0.0.569-1
- Update to 0.0.569

* Thu Jan 16 2025 garzj <pkg@garz.dev> 0.0.567-1
- Update to 0.0.567

* Wed Jan 15 2025 garzj <pkg@garz.dev> 0.0.563-1
- Update to 0.0.563

* Tue Jan 14 2025 garzj <pkg@garz.dev> 0.0.560-1
- Update to 0.0.560

* Sat Jan 11 2025 garzj <pkg@garz.dev> 0.0.559-1
- Update to 0.0.559

* Fri Jan 10 2025 garzj <pkg@garz.dev> 0.0.558-1
- Update to 0.0.558

* Tue Jan 07 2025 garzj <pkg@garz.dev> 0.0.556-1
- Update to 0.0.556

* Sat Jan 04 2025 garzj <pkg@garz.dev> 0.0.555-1
- Update to 0.0.555

* Fri Jan 03 2025 garzj <pkg@garz.dev> 0.0.552-1
- Update to 0.0.552

* Fri Dec 20 2024 garzj <pkg@garz.dev> 0.0.550-1
- Update to 0.0.550

* Wed Dec 18 2024 garzj <pkg@garz.dev> 0.0.549-1
- Update to 0.0.549

* Tue Dec 17 2024 garzj <pkg@garz.dev> 0.0.548-1
- Update to 0.0.548

* Sat Dec 14 2024 garzj <pkg@garz.dev> 0.0.546-1
- Update to 0.0.546

* Fri Dec 13 2024 garzj <pkg@garz.dev> 0.0.542-1
- Update to 0.0.542

* Wed Dec 11 2024 garzj <johannes@garz.dev> 0.0.537-1
- Update to 0.0.537

* Wed Dec 11 2024 garzj <johannes@garz.dev> 0.0.536-2
- fix: discord lib path name (johannes@garz.dev)

* Sun Dec 08 2024 garzj <johannes@garz.dev> 0.0.536-1
- Fork https://github.com/rpmfusion/discord/tree/master, adapt for Discord Canary
- Initial build at version 0.0.536
