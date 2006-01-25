#$Revision: 1.27 $,  $Date: 2006-01-25 16:07:15 $

%define		theme	LiquidWeatherPlus

Summary:	superkaramba - LiquidWeatherPlus theme
Summary(pl):	superkaramba - motyw LiquidWeatherPlus
Name:		superkaramba-theme-%{theme}
Version:	8.9.2
Release:	3
License:	GPL
Group:		Themes
Source0:	http://www.message.co.nz/~matt-sarah/lwp-%{version}.skz
# Source0-md5:	ff322cb338ae2cfe290818b2321d0145
Source1:	http://mirrors.borgnet.us/matt-lw/Glossy.tar.bz2
# Source1-md5:	f56593dccd5086a23f6b545c4663325f
Source2:	http://mirrors.borgnet.us/matt-lw/Kapsules.tar.bz2
# Source2-md5:	e7fcffa5f00914117926b963ca80095b
URL:		http://liquidweather.net/
Requires:	ImageMagick
Requires:	python-PyQt >= 3.13
Requires:	superkaramba >= 0.37
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
%define _liquiddir /themes/superkaramba/liquid_weather_plus
 #directory in rpm
%define _lwp liquid_weather_plus
 #directory in source

%description
LiquidWeatherPlus theme for superkaramba. Features:
 - Weather forecasts from weather.com or BBC for most cities worldwide.
 - Details of current conditions.
 - Daily forecasts and weather details for today and the following 4
   days.
 - Hourly forecasts for the next 12 hours, if using weather.com as a
   data source.
 - All sorts of different weather maps for all major world regions,
   including Antarctica.
 - View up to 5 web cams.
 - All data updates automatically every 1, 2 or 3 hours.
 - Multiple background and icon themes.
 - Gui configuration for everything through the configuration menu.

%description -l pl
Motyw LiquidWeatherPlus do superkaramby. Wy¶wietlane informacje:
 - Prognoza pogody z weather.com oraz BBC z wiêkszo¶ci miast ¶wiata.
 - Warunki pogodowe.
 - Zapowied¼ pogody oraz szczególy dla aktualnego dnia oraz nastêpnych
   czterech dni.
 - Przewidywanie pogody dla nastêpnych 12 godzin, je¿eli u¿ywamy
   weather.com jako ¼ród³o danych.
 - Wszystkie rodzaje ró¿nych map pogody dla wszystkich wa¿niejszych
   rejonów, równie¿ Antarktyki.
 - Widok z 5 kamer internetowych.
 - Wszystkie dane uaktualniane s± co 1, 2 lub 3 godziny.
 - Ró¿ne rodzaje t³a oraz motywy ikon.
 - Graficzna konfiguracja przez menu konfiguracyjne.

%prep
%setup -q -c

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}%{_liquiddir} \
	$RPM_BUILD_ROOT%{_datadir}%{_liquiddir}/{earthquake,fonts,moon_icons} \
	$RPM_BUILD_ROOT%{_datadir}%{_liquiddir}/icons/{Glossy,Kapsules,Liquid,Umicons}/{large_icons,small_icons} \
	$RPM_BUILD_ROOT%{_datadir}%{_liquiddir}/wind_icons/{flat,liquid}/{medium,strong,weak}
install *.{html,pot,py,pyc,png,theme,ui,xml} $RPM_BUILD_ROOT%{_datadir}%{_liquiddir}
install trans_snippet $RPM_BUILD_ROOT%{_datadir}%{_liquiddir}
#install background/*.png $RPM_BUILD_ROOT%{_datadir}%{_liquiddir}/background
install earthquake/*.{html,css} $RPM_BUILD_ROOT%{_datadir}%{_liquiddir}/earthquake
install fonts/*.ttf $RPM_BUILD_ROOT%{_datadir}%{_liquiddir}/fonts
#install moon_icons/*.png $RPM_BUILD_ROOT%{_datadir}%{_liquiddir}/moon_icons
# moon_icons will be added in 9.2 (but 9.2 is buggy)

cp -r locale/ $RPM_BUILD_ROOT%{_datadir}

install wind_icons/flat/*.png $RPM_BUILD_ROOT%{_datadir}%{_liquiddir}/wind_icons/flat
install wind_icons/liquid/*.png $RPM_BUILD_ROOT%{_datadir}%{_liquiddir}/wind_icons/liquid
# directory contains subfolders wig  spaces and "(", ")", so cp -r is easest way to copy.
cp -r background/  $RPM_BUILD_ROOT%{_datadir}%{_liquiddir}/background/

# install Glossy,Kapsules icons
cd  icons/
tar fvxj %{SOURCE1}
tar fvxj %{SOURCE2}
cd -

for www in {Glossy,Kapsules,Liquid,Umicons};
 do
install icons/$www/large_icons/*.png $RPM_BUILD_ROOT%{_datadir}%{_liquiddir}/icons/$www/large_icons
install icons/$www/small_icons/*.png $RPM_BUILD_ROOT%{_datadir}%{_liquiddir}/icons/$www/small_icons
done

for www in {medium,strong,weak};
 do
install wind_icons/flat/$www/*.png $RPM_BUILD_ROOT%{_datadir}%{_liquiddir}/wind_icons/flat/$www
install wind_icons/liquid/$www/*.png $RPM_BUILD_ROOT%{_datadir}%{_liquiddir}/wind_icons/liquid/$www
done

#cleaning
rm $RPM_BUILD_ROOT%{_datadir}/locale/*/LC_MESSAGES/liquid_weather.po*

# locale hack
cd $RPM_BUILD_ROOT%{_datadir}%{_liquiddir}
ln -s ../../../locale/ locale 
cd -

%find_lang liquid_weather --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f liquid_weather.lang
%defattr(644,root,root,755)
%{_datadir}%{_liquiddir}/
