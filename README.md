# Dashboard Deutschland API

Auf https://www.dashboard-deutschland.de bietet das Statistische Bundesamt DESTATIS einen Überblick zu gesellschaftlich und wirtschaftlich relevanten Daten aus unterschiedlichen Themenbereichen. Diese werden durch Grafiken und Texte ergänzt und regelmäßig aktualisiert. Damit soll eine Möglichkeit geboten werden, aktuelle Kennzahlen und deren Entwicklung übersichtlich darzustellen.


## Get

**URL:** https://www.dashboard-deutschland.de/api/dashboard/get
	
Die API ermöglicht über diese URL den Zugriff auf alle gültigen Einträge des ids-Parameters getrennt nach Kategorien (siehe unten, Indikatoren). 


## Indikatoren

**URL:** www.dashboard-deutschland.de/api/tile/indicators
	
Die API ermöglicht über diese URL Zugriff auf unterschiedliche Indikatoren im JSON-Format über einfache GET-requests mit nur einem Parameter (namens *ids*). 
Der Parameter ids spezifiziert den gewünschten Indikator. 
Mögliche Ausprägungen sind im Folgenden tabellarisch dargestellt. 
Mehrere Semikolon-getrennte Angaben sind möglich. 

|Indikator|ids-value|Beispiel-URL|
|---|---|---|
|Importe und Exporte von Wasserstoff|tile_1654002158461|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1654002158461|
|Täglicher LKW-Maut-Fahrleistungsindex|tile_1667226778807|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667226778807|
|Lkw-Maut-Fahrleistungsindex|tile_1667205800085|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667205800085|
|Preisindex für Eigentumswohnungen nach Kreistypen|data_woh_preise_immobilien_hpi_wohnungen|www.dashboard-deutschland.de/api/tile/indicators?ids=data_woh_preise_immobilien_hpi_wohnungen|
|HCOB Einkaufsmanagerindex|tile_1667982123933|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667982123933|
|Umsatz im Ausbaugewerbe|tile_1654070793733|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1654070793733|
|Kapazitätsauslastung im Baugewerbe|data_bau_kapazitaetsauslastung_bbsr|www.dashboard-deutschland.de/api/tile/indicators?ids=data_bau_kapazitaetsauslastung_bbsr|
|Weltmarktpreise für Weizen|tile_1654606920834|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1654606920834|
|Automobilindustrie|tile_1666960710868|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1666960710868|
|Entwicklung der Nominallöhne nach Quintilen|tile_1684316122432|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1684316122432|
|Entwicklung des deutschen Arbeitsmarktes anhand der LinkedIn Hiring Rate|tile_1673880739519|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1673880739519|
|Flugverkehr weltweit|tile_1667989324139|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667989324139|
|Anzahl genehmigter Wohnungen im Neubau nach Gebäudeart|data_woh_baugenehmigungen_wohnungen|www.dashboard-deutschland.de/api/tile/indicators?ids=data_woh_baugenehmigungen_wohnungen|
|Verbrauch von Mineralölprodukten in Deutschland|tile_1663665588691|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1663665588691|
|Füllstand deutscher Erdgasspeicher|tile_1667227714015|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667227714015|
|Fertiggestellte Neubauten nach überwiegend verwendeter Heizenergie|tile_1654000747086|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1654000747086|
|Genehmigte neu zu errichtende Wohngebäude mit ein und zwei Wohnungen nach überwiegend verwendeter Heizenergie|tile_1663665272454|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1663665272454|
|Auftragseingang im Bauhauptgewerbe|data_bau_auftragseingang|www.dashboard-deutschland.de/api/tile/indicators?ids=data_bau_auftragseingang|
|Energieverbrauch für Wohnen nach Anwendungsbereichen|tile_1651060108903|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1651060108903|
|ifo Geschäftsklima|tile_1667288019608|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667288019608|
|Umsatz im Gastgewerbe|tile_1667810908930|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667810908930|
|Genehmigte und fertiggestellte Wohnungen|tile_1678111428688|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1678111428688|
|Verbraucherpreisindex für Nettokaltmiete, Wohnungsnebenkosten und Haushaltsenergie|data_woh_bruttokaltmiete|www.dashboard-deutschland.de/api/tile/indicators?ids=data_woh_bruttokaltmiete|
|Stimmungsindikatoren Konsum|tile_1667983271066|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667983271066|
|Gold- und Kupferpreis|data_preise_gold_kupfer|www.dashboard-deutschland.de/api/tile/indicators?ids=data_preise_gold_kupfer|
|Verschuldung der bedeutendsten Sondervermögen des Bundes|tile_1650977632272|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1650977632272|
|Verbraucherpreisindex für Nettokaltmiete nach Kreistypen|data_woh_nettokaltmiete|www.dashboard-deutschland.de/api/tile/indicators?ids=data_woh_nettokaltmiete|
|Umsatz in Branchen des Verarbeitenden Gewerbes|data_umsatz_ausgewaehlte_branchen|www.dashboard-deutschland.de/api/tile/indicators?ids=data_umsatz_ausgewaehlte_branchen|
|HWWI-Rohstoffpreisindex|tile_1667215458776|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667215458776|
|Kassenmäßige Steuereinnahmen aus Gemeindesteuern|data_gemeindesteuern|www.dashboard-deutschland.de/api/tile/indicators?ids=data_gemeindesteuern|
|Umlaufrenditen Staats- und Unternehmensanleihen|data_staats_und_unt_anleihen|www.dashboard-deutschland.de/api/tile/indicators?ids=data_staats_und_unt_anleihen|
|Kassenmäßige Steuereinnahmen insgesamt und der Gemeinden/Gemeindeverbände|data_steuereinnahmen_insgesamt_gemeinden|www.dashboard-deutschland.de/api/tile/indicators?ids=data_steuereinnahmen_insgesamt_gemeinden|
|Dienstleistungsproduktion|tile_1667825347006|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667825347006|
|ZEW Konjunkturausblick|tile_1667228531297|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667228531297|
|Exporterwartungen und Containerumschlag|tile_1666962783823|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1666962783823|
|Passantenfrequenzindex|tile_1667982573430|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667982573430|
|Flugverkehr Deutschland|tile_1667987544456|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667987544456|
|Preisentwicklung für ausgewählte Baumaterialien|tile_1667308898055|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667308898055|
|Baupreisindizes|data_bau_bauleistungspreise|www.dashboard-deutschland.de/api/tile/indicators?ids=data_bau_bauleistungspreise|
|Produktion im Produzierenden Gewerbe|tile_1667824915093|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667824915093|
|Auftragseingang in Branchen des Verarbeitenden Gewerbes|data_auftragseingang_ausgewaehlte_branchen|www.dashboard-deutschland.de/api/tile/indicators?ids=data_auftragseingang_ausgewaehlte_branchen|
|ifo Produktionserwartungen|tile_1667289137702|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667289137702|
|Auftragseingang im Verarbeitenden Gewerbe|tile_1667828024262|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667828024262|
|Entwicklung der Nominallöhne nach Beschäftigungsart|tile_1684314533676|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1684314533676|
|Umsatz mit Maßnahmen zur Verbesserung der Energieeffizienz von Gebäuden|tile_1665656599909|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1665656599909|
|Umsatz mit Motorenkraftstoffen an Tankstellen|tile_1663667870377|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1663667870377|
|Arbeitslosigkeit und offene Stellen|tile_1666958835081|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1666958835081|
|Preisveränderung|tile_1668694599167|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1668694599167|
|Entwicklung ausgewählter Aggregate des Bruttoinlandsprodukts|tile_1667814729862|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667814729862|
|Gasimporte nach Deutschland|tile_1667993866759|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667993866759|
|Einzelhandelsumsatz|tile_1667460685909|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667460685909|
|Kassenmäßige Steuereinnahmen aus Gemeinschaft-, Bundes- und Landessteuern|data_gemeinschaft_bundes_landessteuern|www.dashboard-deutschland.de/api/tile/indicators?ids=data_gemeinschaft_bundes_landessteuern|
|Außenhandelsbilanz|data_aussenhandelsbilanz|www.dashboard-deutschland.de/api/tile/indicators?ids=data_aussenhandelsbilanz|
|Verschuldung des Bundes inklusive Darlehensfinanzierung nach Restlaufzeiten|tile_1650978274644|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1650978274644|
|Stromverbrauch|tile_1667214343714|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667214343714|
|Wohnfläche in genehmigten Neubauwohnungen|data_woh_baugenehmigungen_wohnflaeche|www.dashboard-deutschland.de/api/tile/indicators?ids=data_woh_baugenehmigungen_wohnflaeche|
|Energieverbrauch für Wohnen nach Energieträgern|data_woh_energieverbrauch_energietraeger|www.dashboard-deutschland.de/api/tile/indicators?ids=data_woh_energieverbrauch_energietraeger|
|Passantenfrequenzen: Veränderung in ausgewählten Großstädten|data_mobilitaet_hystreet|www.dashboard-deutschland.de/api/tile/indicators?ids=data_mobilitaet_hystreet|
|Bereinigte kassenmäßige Steuereinnahmen aus Gemeinschaft-, Bundes- und Landessteuern|data_einnahmen_gemeinschaft_bundes_landessteuern|www.dashboard-deutschland.de/api/tile/indicators?ids=data_einnahmen_gemeinschaft_bundes_landessteuern|
|Außenhandel|tile_1667830902757|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667830902757|
|Ölpreis (Sorte Brent)|tile_1667995478843|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667995478843|
|Energiepreisveränderung|tile_1667826504852|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667826504852|
|Stimmungsindikatoren Arbeitsmarkt|data_iab_ifo_barometer|www.dashboard-deutschland.de/api/tile/indicators?ids=data_iab_ifo_barometer|
|Kraftstoffpreise an öffentlichen Tankstellen|tile_1667921381760|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667921381760|
|Neue Hypothekenverträge|tile_1667817211258|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667817211258|
|Anteil der Grünen Bundeswertpapiere an der Verschuldung des Bundes inklusive Darlehensfinanzierung|tile_1650979109395|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1650979109395|
|Kassenmäßige Steuereinnahmen von Bund und Ländern|data_steuereinnahmen_bund_laender|www.dashboard-deutschland.de/api/tile/indicators?ids=data_steuereinnahmen_bund_laender|
|Außenhandel mit ausgewählten Ländern|tile_1667832713510|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667832713510|
|Entwicklung des deutschen Arbeitsmarktes anhand von Stellenausschreibungen auf Indeed|tile_1666961477511|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1666961477511|
|Entwicklung des Bruttoinlandsprodukts|tile_1667811574092|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667811574092|
|Baltic Dry Index|tile_1666960424161|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1666960424161|
|Außenhandel mit ausgewählten Ländergruppen|data_aussenhandel_laendergruppen|www.dashboard-deutschland.de/api/tile/indicators?ids=data_aussenhandel_laendergruppen|
|Verschuldung des Bundeshaushalts und seiner Sondervermögen|tile_1650978797816|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1650978797816|
|Produktion von Solarkollektoren, Solarmodulen und Wärmepumpen|tile_1663667563512|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1663667563512|
|Wechselkurs Euro/US-Dollar|tile_1667217389888|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667217389888|
|Anzahl der genehmigten Wohnungen nach Bauherr|data_woh_baugenehmigungen_bautraeger|www.dashboard-deutschland.de/api/tile/indicators?ids=data_woh_baugenehmigungen_bautraeger|
|Kreditvergaben und Online-Transaktionen|tile_1667978809506|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667978809506|
|Erwerbstätigkeit|tile_1667822587333|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667822587333|
|Umsatz im Verarbeitenden Gewerbe|tile_1667828804581|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667828804581|
|Benzinpreise im EU-Vergleich|tile_1663664545105|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1663664545105|
|ifo Knappheitsindikator|tile_1667289768923|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667289768923|
|Renditespreads 10-jähriger Staatsanleihen gegenüber Deutschland|data_zinsspread_10_j_anleihen|www.dashboard-deutschland.de/api/tile/indicators?ids=data_zinsspread_10_j_anleihen|
|Strompreis|data_preise_strom|www.dashboard-deutschland.de/api/tile/indicators?ids=data_preise_strom|
|Wöchentlicher Aktivitätsindex|tile_1667211885741|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667211885741|
|Beschäftigung im Baugewerbe|data_bau_beschaeftigung_vgr|www.dashboard-deutschland.de/api/tile/indicators?ids=data_bau_beschaeftigung_vgr|
|DIW Konjunkturbarometer|tile_1666961011248|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1666961011248|
|Preisindex für Ein- und Zweifamilienhäuser nach Kreistypen|data_woh_preise_immobilien_hpi_haueser|www.dashboard-deutschland.de/api/tile/indicators?ids=data_woh_preise_immobilien_hpi_haueser|
|Produktion in Branchen des Produzierenden Gewerbes|data_produktion_ausgewaehlte_branchen|www.dashboard-deutschland.de/api/tile/indicators?ids=data_produktion_ausgewaehlte_branchen|
|Pegelstände am Rhein|tile_1666960227357|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1666960227357|
|Preisentwicklung für Energie (Strom, Gas und andere Brennstoffe) im EU-Vergleich|tile_1663666887687|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1663666887687|
|Produktion im Baugewerbe|tile_1667890765659|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667890765659|
|Energieverbrauch der Industrie nach Energieträgern|tile_1654002609295|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1654002609295|
|Nettostromerzeugung|tile_1666961555651|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1666961555651|
|Neuzulassungen von Personenkraftwagen nach Antriebsarten|tile_1663666467966|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1663666467966|
|Umsatz im Bauhauptgewerbe|tile_1654068021178|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1654068021178|
|Tischreservierungen über OpenTable|tile_1667208064878|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667208064878|
|Exporte und Importe von Wärmepumpen und Photovoltaikanlagen|tile_1663664931250|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1663664931250|
|Renditen Bundeswertpapiere|data_umlaufrenditen_bundesanleihen|www.dashboard-deutschland.de/api/tile/indicators?ids=data_umlaufrenditen_bundesanleihen|
|Importe fossiler Energieträger|tile_1654001211812|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1654001211812|
|Bonitätschecks von Wohnungssuchenden|tile_1667995046610|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667995046610|
|Preisindizes zu Bau oder Erwerb von Wohneigentum|tile_1656076602735|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1656076602735|
|Absatz von Warengruppen im Lebensmitteleinzelhandel|tile_1667821076015|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667821076015|
|Außenhandel nach VGR-Konzept|tile_1667821569597|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667821569597|
|Aktienindizes|tile_1667210963256|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667210963256|
|Nettonennleistung der Anlagen zur Elektrizitätserzeugung|tile_1722432860129|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1722432860129|


## Geojson

**URL:** www.dashboard-deutschland.de/geojson/de-all.geo.json
	
Die API ermöglicht Zugriff auf Geojson-Daten zu Deutschland und den Ländern (00-DE_admin1_400).


## Beispiel

```bash
indicators=$(curl -m 60 'https://www.dashboard-deutschland.de/api/tile/indicators?ids=data_adv_flugverkehr;data_aussenhandel;data_ba_arbeitslose_und_stellen;data_bruttoinlandsprodukt;data_corona_zuschuesse;data_einnahmen_gemeinschaft_bundes_landessteuern;data_ifo_geschaeftsklima;data_kfw_sondermassnahme_neu;data_preisentwicklung;data_umsatz_ausgewaehlte_branchen;defacto_ges_diag_covid19_hospitalizationincidence_map_de;ginsy_ges_bev_sterbl_abs_sterbl_de;ginsy_ges_diag_covid19_7_tage_inzidenz_map_de;tile_1648135639982
')
```
