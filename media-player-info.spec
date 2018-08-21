#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : media-player-info
Version  : 24
Release  : 2
URL      : https://www.freedesktop.org/software/media-player-info/media-player-info-24.tar.gz
Source0  : https://www.freedesktop.org/software/media-player-info/media-player-info-24.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0
Requires: media-player-info-config
Requires: media-player-info-license
Requires: media-player-info-data
BuildRequires : pkgconfig(udev)

%description
No detailed description available

%package config
Summary: config components for the media-player-info package.
Group: Default

%description config
config components for the media-player-info package.


%package data
Summary: data components for the media-player-info package.
Group: Data

%description data
data components for the media-player-info package.


%package license
Summary: license components for the media-player-info package.
Group: Default

%description license
license components for the media-player-info package.


%prep
%setup -q -n media-player-info-24

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1534889457
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1534889457
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/media-player-info
cp COPYING %{buildroot}/usr/share/doc/media-player-info/COPYING
cp tools/COPYING %{buildroot}/usr/share/doc/media-player-info/tools_COPYING
%make_install

%files
%defattr(-,root,root,-)
/usr/lib/udev/hwdb.d/20-usb-media-players.hwdb

%files config
%defattr(-,root,root,-)
/usr/lib/udev/rules.d/40-usb-media-players.rules

%files data
%defattr(-,root,root,-)
/usr/share/media-player-info/acer_liquid.mpi
/usr/share/media-player-info/actions-semiconductor_0x1100_0x1101.mpi
/usr/share/media-player-info/ali_0x5661-0x5667.mpi
/usr/share/media-player-info/amazon_kindle.mpi
/usr/share/media-player-info/apple_ipod.mpi
/usr/share/media-player-info/apple_video-ipod.mpi
/usr/share/media-player-info/archos_0x1109_0x1300.mpi
/usr/share/media-player-info/archos_32-it.mpi
/usr/share/media-player-info/archos_5.mpi
/usr/share/media-player-info/archos_5imt.mpi
/usr/share/media-player-info/archos_5it.mpi
/usr/share/media-player-info/archos_a43.mpi
/usr/share/media-player-info/archos_key.mpi
/usr/share/media-player-info/archos_xs-100.mpi
/usr/share/media-player-info/barnes-and-noble_nook.mpi
/usr/share/media-player-info/coby_mp300.mpi
/usr/share/media-player-info/coby_mp705-4g.mpi
/usr/share/media-player-info/coby_mp705-8g.mpi
/usr/share/media-player-info/coby_mpc843_mpc853.mpi
/usr/share/media-player-info/cowon_0x0510_0x0520_0x0710_0x0730_0x0750.mpi
/usr/share/media-player-info/cowon_0x0601_0x0602_0x0604.mpi
/usr/share/media-player-info/cowon_d2.mpi
/usr/share/media-player-info/cowon_iaudio-7.mpi
/usr/share/media-player-info/cowon_iaudio-9.mpi
/usr/share/media-player-info/cowon_iaudio-e2.mpi
/usr/share/media-player-info/cowon_iaudio-m3.mpi
/usr/share/media-player-info/cowon_iaudio-u2.mpi
/usr/share/media-player-info/cowon_iaudio-u3.mpi
/usr/share/media-player-info/cowon_iaudio-u5_g2.mpi
/usr/share/media-player-info/cowon_iaudio-x5.mpi
/usr/share/media-player-info/cowon_j3.mpi
/usr/share/media-player-info/cowon_s9.mpi
/usr/share/media-player-info/creative_0x4xxx.mpi
/usr/share/media-player-info/creative_muvo-v100.mpi
/usr/share/media-player-info/creative_muvo-v200.mpi
/usr/share/media-player-info/creative_zen-mx.mpi
/usr/share/media-player-info/creative_zen-nano-plus.mpi
/usr/share/media-player-info/creative_zen-nano.mpi
/usr/share/media-player-info/creative_zen-stone-plus.mpi
/usr/share/media-player-info/creative_zen-stone.mpi
/usr/share/media-player-info/creative_zen-style-300.mpi
/usr/share/media-player-info/creative_zen-x-fi-2.mpi
/usr/share/media-player-info/creative_zen-x-fi-style.mpi
/usr/share/media-player-info/dane-elec_music-mediatouch.mpi
/usr/share/media-player-info/danger_hiptop_sidekick.mpi
/usr/share/media-player-info/domain-technologies_0x3203.mpi
/usr/share/media-player-info/google_nexus-one.mpi
/usr/share/media-player-info/google_nexus-s.mpi
/usr/share/media-player-info/hama_dmp-100.mpi
/usr/share/media-player-info/hp_pre3.mpi
/usr/share/media-player-info/hp_touchpad.mpi
/usr/share/media-player-info/hp_veer.mpi
/usr/share/media-player-info/htc_desire_hero_evo-4g_legend.mpi
/usr/share/media-player-info/htc_diamond.mpi
/usr/share/media-player-info/htc_dream_adp1_g1_magic_tattoo.mpi
/usr/share/media-player-info/htc_incredible.mpi
/usr/share/media-player-info/htc_snap.mpi
/usr/share/media-player-info/htc_touch-hd.mpi
/usr/share/media-player-info/htc_vision.mpi
/usr/share/media-player-info/huawei_ideos.mpi
/usr/share/media-player-info/huawei_pulse.mpi
/usr/share/media-player-info/huawei_u8120.mpi
/usr/share/media-player-info/insignia_ns-8v24.mpi
/usr/share/media-player-info/iriver_0x1101_0x1103_0x1105_0x1111.mpi
/usr/share/media-player-info/iriver_0x1xxx.mpi
/usr/share/media-player-info/iriver_0x3001_0x3002.mpi
/usr/share/media-player-info/iriver_e100.mpi
/usr/share/media-player-info/iriver_e30.mpi
/usr/share/media-player-info/iriver_h320_h340.mpi
/usr/share/media-player-info/iriver_s10.mpi
/usr/share/media-player-info/iriver_t30.mpi
/usr/share/media-player-info/iriver_t60.mpi
/usr/share/media-player-info/iriver_t7-volcano.mpi
/usr/share/media-player-info/jens-of-sweeden_mp-120.mpi
/usr/share/media-player-info/jens-of-sweeden_mp-130.mpi
/usr/share/media-player-info/jetflash_0x8000_0x8008_0x8206_0x821f_0x829c_0x82e0_0x835d.mpi
/usr/share/media-player-info/jetflash_0x8004.mpi
/usr/share/media-player-info/jetflash_0x8038.mpi
/usr/share/media-player-info/jetflash_alba-mp3128d6.mpi
/usr/share/media-player-info/jetflash_digital-live250.mpi
/usr/share/media-player-info/lg_0x6018.mpi
/usr/share/media-player-info/lg_ally_optimus-one_vortex.mpi
/usr/share/media-player-info/lg_kc910-renoir.mpi
/usr/share/media-player-info/lg_optimus-one-p500.mpi
/usr/share/media-player-info/lg_optimus-s.mpi
/usr/share/media-player-info/lyra_th1100a.mpi
/usr/share/media-player-info/m-cody_m20.mpi
/usr/share/media-player-info/maxfield_max-sin-touch.mpi
/usr/share/media-player-info/meizu-mini_player_m6.mpi
/usr/share/media-player-info/micromax_a60.mpi
/usr/share/media-player-info/mobile-media_0x0001.mpi
/usr/share/media-player-info/motorola_atrix.mpi
/usr/share/media-player-info/motorola_cliq.mpi
/usr/share/media-player-info/motorola_droid-2.mpi
/usr/share/media-player-info/motorola_droid-4.mpi
/usr/share/media-player-info/motorola_droid-x.mpi
/usr/share/media-player-info/motorola_droid_milestone.mpi
/usr/share/media-player-info/motorola_i1.mpi
/usr/share/media-player-info/motorola_itunes-phone.mpi
/usr/share/media-player-info/motorola_rokr-e2.mpi
/usr/share/media-player-info/motorola_v3i.mpi
/usr/share/media-player-info/msi-megastick-1_flash_stick.mpi
/usr/share/media-player-info/nec_lifetouch-note.mpi
/usr/share/media-player-info/nexia-1013.mpi
/usr/share/media-player-info/nokia_0x0431_0x04c3_0x0096.mpi
/usr/share/media-player-info/nokia_5300.mpi
/usr/share/media-player-info/nokia_5310.mpi
/usr/share/media-player-info/nokia_5800.mpi
/usr/share/media-player-info/nokia_6110.mpi
/usr/share/media-player-info/nokia_6120.mpi
/usr/share/media-player-info/nokia_6300.mpi
/usr/share/media-player-info/nokia_6303.mpi
/usr/share/media-player-info/nokia_6600i.mpi
/usr/share/media-player-info/nokia_6700.mpi
/usr/share/media-player-info/nokia_6730.mpi
/usr/share/media-player-info/nokia_c7-00.mpi
/usr/share/media-player-info/nokia_e71.mpi
/usr/share/media-player-info/nokia_n9.mpi
/usr/share/media-player-info/nokia_n900.mpi
/usr/share/media-player-info/nokia_n91.mpi
/usr/share/media-player-info/nokia_n95.mpi
/usr/share/media-player-info/nokia_n950.mpi
/usr/share/media-player-info/nokia_n97.mpi
/usr/share/media-player-info/nokia_series-60-phones.mpi
/usr/share/media-player-info/notion-ink_adam.mpi
/usr/share/media-player-info/olympus_ds-2.mpi
/usr/share/media-player-info/palm_pre.mpi
/usr/share/media-player-info/panasonic_sv-mp31v.mpi
/usr/share/media-player-info/pantech_sirius-alpha.mpi
/usr/share/media-player-info/peak_0x1651.mpi
/usr/share/media-player-info/philips_gogear-aria.mpi
/usr/share/media-player-info/philips_gogear-mix.mpi
/usr/share/media-player-info/philips_gogear-opus.mpi
/usr/share/media-player-info/philips_gogear-raga.mpi
/usr/share/media-player-info/philips_gogear-sa1100.mpi
/usr/share/media-player-info/philips_gogear-sa1330.mpi
/usr/share/media-player-info/philips_gogear-sa1942.mpi
/usr/share/media-player-info/philips_gogear-sa2rga.mpi
/usr/share/media-player-info/philips_gogear-sa3125.mpi
/usr/share/media-player-info/philips_gogear-sa52xx.mpi
/usr/share/media-player-info/philips_gogear-vibe.mpi
/usr/share/media-player-info/q-be_0x9111.mpi
/usr/share/media-player-info/qualcomm_0x05c6_0x1000.mpi
/usr/share/media-player-info/rca_0x0713_0x0718_0x0756_0x0767.mpi
/usr/share/media-player-info/rca_h100a.mpi
/usr/share/media-player-info/rim_blackberry.mpi
/usr/share/media-player-info/rockbox.mpi
/usr/share/media-player-info/samsung_0x6601-phones.mpi
/usr/share/media-player-info/samsung_galaxy-ace_gio.mpi
/usr/share/media-player-info/samsung_galaxy-s2.mpi
/usr/share/media-player-info/samsung_galaxy.mpi
/usr/share/media-player-info/samsung_gt-s8000-jet.mpi
/usr/share/media-player-info/samsung_meizu-m6-miniplayer.mpi
/usr/share/media-player-info/samsung_reality.mpi
/usr/share/media-player-info/samsung_u5.mpi
/usr/share/media-player-info/samsung_u6.mpi
/usr/share/media-player-info/samsung_yepp-yp-35.mpi
/usr/share/media-player-info/samsung_yepp-yp-k3.mpi
/usr/share/media-player-info/samsung_yepp-yp-m1.mpi
/usr/share/media-player-info/samsung_yepp-yp-p3.mpi
/usr/share/media-player-info/samsung_yepp-yp-st5.mpi
/usr/share/media-player-info/samsung_yp-f1.mpi
/usr/share/media-player-info/samsung_yp-f2r.mpi
/usr/share/media-player-info/samsung_yp-j70.mpi
/usr/share/media-player-info/samsung_yp-mt6v.mpi
/usr/share/media-player-info/samsung_yp-p2.mpi
/usr/share/media-player-info/samsung_yp-q2.mpi
/usr/share/media-player-info/samsung_yp-s2.mpi
/usr/share/media-player-info/samsung_yp-s3.mpi
/usr/share/media-player-info/samsung_yp-s5.mpi
/usr/share/media-player-info/samsung_yp-t10.mpi
/usr/share/media-player-info/samsung_yp-t7.mpi
/usr/share/media-player-info/samsung_yp-t7f.mpi
/usr/share/media-player-info/samsung_yp-t9.mpi
/usr/share/media-player-info/samsung_yp-u1.mpi
/usr/share/media-player-info/samsung_yp-u2.mpi
/usr/share/media-player-info/samsung_yp-u4.mpi
/usr/share/media-player-info/samsung_yp-z5.mpi
/usr/share/media-player-info/sandisk_sansa-c250.mpi
/usr/share/media-player-info/sandisk_sansa-clip-plus.mpi
/usr/share/media-player-info/sandisk_sansa-clip-sport.mpi
/usr/share/media-player-info/sandisk_sansa-clip-v2.mpi
/usr/share/media-player-info/sandisk_sansa-clip-zip.mpi
/usr/share/media-player-info/sandisk_sansa-clip.mpi
/usr/share/media-player-info/sandisk_sansa-e100-series.mpi
/usr/share/media-player-info/sandisk_sansa-e200-series-v2.mpi
/usr/share/media-player-info/sandisk_sansa-e200-series.mpi
/usr/share/media-player-info/sandisk_sansa-fuze-plus.mpi
/usr/share/media-player-info/sandisk_sansa-fuze-v2.mpi
/usr/share/media-player-info/sandisk_sansa-fuze.mpi
/usr/share/media-player-info/sandisk_sansa-m200-series-v4.mpi
/usr/share/media-player-info/sandisk_sansa-m200-series.mpi
/usr/share/media-player-info/sandisk_sansa-view.mpi
/usr/share/media-player-info/sharp-is01.mpi
/usr/share/media-player-info/sharp-is03.mpi
/usr/share/media-player-info/sonicblue_0x5042.mpi
/usr/share/media-player-info/sonicblue_rio-carbon.mpi
/usr/share/media-player-info/sonicblue_rio-karma.mpi
/usr/share/media-player-info/sony-ericsson_c902.mpi
/usr/share/media-player-info/sony-ericsson_c905.mpi
/usr/share/media-player-info/sony-ericsson_k320i.mpi
/usr/share/media-player-info/sony-ericsson_k610i.mpi
/usr/share/media-player-info/sony-ericsson_k750i.mpi
/usr/share/media-player-info/sony-ericsson_k800i.mpi
/usr/share/media-player-info/sony-ericsson_k810i.mpi
/usr/share/media-player-info/sony-ericsson_k850i.mpi
/usr/share/media-player-info/sony-ericsson_p1i.mpi
/usr/share/media-player-info/sony-ericsson_v630i.mpi
/usr/share/media-player-info/sony-ericsson_v640i.mpi
/usr/share/media-player-info/sony-ericsson_vivaz.mpi
/usr/share/media-player-info/sony-ericsson_w200.mpi
/usr/share/media-player-info/sony-ericsson_w300i.mpi
/usr/share/media-player-info/sony-ericsson_w302i.mpi
/usr/share/media-player-info/sony-ericsson_w580i.mpi
/usr/share/media-player-info/sony-ericsson_w595.mpi
/usr/share/media-player-info/sony-ericsson_w660i.mpi
/usr/share/media-player-info/sony-ericsson_w705.mpi
/usr/share/media-player-info/sony-ericsson_w800i.mpi
/usr/share/media-player-info/sony-ericsson_w810i.mpi
/usr/share/media-player-info/sony-ericsson_w910i.mpi
/usr/share/media-player-info/sony-ericsson_w950i.mpi
/usr/share/media-player-info/sony-ericsson_w995.mpi
/usr/share/media-player-info/sony-ericsson_xperia-mini-pro.mpi
/usr/share/media-player-info/sony-ericsson_xperia-mini.mpi
/usr/share/media-player-info/sony-ericsson_xperia-play.mpi
/usr/share/media-player-info/sony-ericsson_xperia-x1.mpi
/usr/share/media-player-info/sony-ericsson_xperia-x10-mini-pro.mpi
/usr/share/media-player-info/sony-ericsson_xperia-x10-mini.mpi
/usr/share/media-player-info/sony-ericsson_xperia-x10.mpi
/usr/share/media-player-info/sony-ericsson_xperia-x12.mpi
/usr/share/media-player-info/sony-ericsson_xperia-x8.mpi
/usr/share/media-player-info/sony_0x035b_0x035c.mpi
/usr/share/media-player-info/sony_0xe068_0xe0b3.mpi
/usr/share/media-player-info/sony_igp-100.mpi
/usr/share/media-player-info/sony_network-walkman.mpi
/usr/share/media-player-info/sony_psp.mpi
/usr/share/media-player-info/sony_walkman-nwd-b105.mpi
/usr/share/media-player-info/sony_walkman-nwz-135f.mpi
/usr/share/media-player-info/sony_walkman-nwz-a800.mpi
/usr/share/media-player-info/sony_walkman-nwz-e355.mpi
/usr/share/media-player-info/sony_walkman-nwz-e443.mpi
/usr/share/media-player-info/sony_walkman-nwz-s500.mpi
/usr/share/media-player-info/sony_walkman-nwz-s638f.mpi
/usr/share/media-player-info/sony_walkman-nwz-s750.mpi
/usr/share/media-player-info/sony_walkman-nwz-s760.mpi
/usr/share/media-player-info/teac_mp-375sd.mpi
/usr/share/media-player-info/thomson_pdp9512fm.mpi
/usr/share/media-player-info/touchstone_ts-300.mpi
/usr/share/media-player-info/transcend_t.sonic-520.mpi
/usr/share/media-player-info/trekstor_i.beat-blaxx.mpi
/usr/share/media-player-info/trekstor_i.beat-cebrax-fx.mpi
/usr/share/media-player-info/trekstor_i.beat-jess.mpi
/usr/share/media-player-info/trekstor_i.beat-rock.mpi
/usr/share/media-player-info/trekstor_vibez.mpi

%files license
%defattr(-,root,root,-)
/usr/share/doc/media-player-info/COPYING
/usr/share/doc/media-player-info/tools_COPYING
