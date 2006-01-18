#$Revision: 1.26 $,  $Date: 2006-01-18 13:02:52 $

%define		theme	LiquidWeatherPlus

Summary:	superkaramba - LiquidWeatherPlus theme
Summary(pl):	superkaramba - motyw LiquidWeatherPlus
Name:		superkaramba-theme-%{theme}
Version:	8.9.2
Release:	2
License:	GPL
Group:		Themes
Source0:	http://www.message.co.nz/~matt-sarah/lwp-%{version}.skz
# Source0-md5:	ff322cb338ae2cfe290818b2321d0145
URL:		http://www.message.co.nz/~matt-sarah/
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
Motyw LiquidWeatherPlus do superkaramby. Wy�wietlane informacje:
 - Prognoza pogody z weather.com oraz BBC z wi�kszo�ci miast �wiata.
 - Warunki pogodowe.
 - Zapowied� pogody oraz szczeg�ly dla aktualnego dnia oraz nast�pnych
   czterech dni.
 - Przewidywanie pogody dla nast�pnych 12 godzin, je�eli u�ywamy
   weather.com jako �r�d�o danych.
 - Wszystkie rodzaje r�nych map pogody dla wszystkich wa�niejszych
   rejon�w, r�wnie� Antarktyki.
 - Widok z 5 kamer internetowych.
 - Wszystkie dane uaktualniane s� co 1, 2 lub 3 godziny.
 - R�ne rodzaje t�a oraz motywy ikon.
 - Graficzna konfiguracja przez menu konfiguracyjne.

%prep
%setup -q -c

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}%{_liquiddir} \
	$RPM_BUILD_ROOT%{_datadir}%{_liquiddir}/{background,earthquake,fonts} \
	$RPM_BUILD_ROOT%{_datadir}%{_liquiddir}/icons/{Liquid,Umicons}/{large_icons,small_icons} \
	$RPM_BUILD_ROOT%{_datadir}%{_liquiddir}/wind_icons/{flat,liquid}/{medium,strong,weak}
install *.{html,pot,py,pyc,png,theme,ui,xml} $RPM_BUILD_ROOT%{_datadir}%{_liquiddir}
install trans_snippet $RPM_BUILD_ROOT%{_datadir}%{_liquiddir}
install background/*.png $RPM_BUILD_ROOT%{_datadir}%{_liquiddir}/background
install earthquake/*.{html,css} $RPM_BUILD_ROOT%{_datadir}%{_liquiddir}/earthquake
install fonts/*.ttf $RPM_BUILD_ROOT%{_datadir}%{_liquiddir}/fonts
cp -r locale/ $RPM_BUILD_ROOT%{_datadir}
install wind_icons/flat/*.png $RPM_BUILD_ROOT%{_datadir}%{_liquiddir}/wind_icons/flat
install wind_icons/liquid/*.png $RPM_BUILD_ROOT%{_datadir}%{_liquiddir}/wind_icons/liquid

for www in {Liquid,Umicons};
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
