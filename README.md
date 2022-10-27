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
|Automobilindustrie|data_vda_pkw|www.dashboard-deutschland.de/api/tile/indicators?ids=data_vda_pkw|
|Gesamtzahl der Covid-19-Impfungen|ginsy_ges_impfung_covid19_gesamtzahl_de|www.dashboard-deutschland.de/api/tile/indicators?ids=ginsy_ges_impfung_covid19_gesamtzahl_de|
|Mobilitätstrends: Besuche von Einzelhandel und Erholungseinrichtungen im bundesweiten Vergleich|tile_1650550636596|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1650550636596|
|Tägliche Mobilitätsveränderung und 7-Tage-Inzidenz auf Kreisebene auf Grundlage von Mobilfunkdaten|data_mobilitaet_mobilfunk_hotspot|www.dashboard-deutschland.de/api/tile/indicators?ids=data_mobilitaet_mobilfunk_hotspot|
|Tägliche Veränderung der Mobilität auf Kreisebene auf Grundlage von Mobilfunkdaten|data_mobilitaet_mobilfunk_karte|www.dashboard-deutschland.de/api/tile/indicators?ids=data_mobilitaet_mobilfunk_karte|
|Wöchentliche Sterbefallzahlen in Deutschland|ginsy_ges_bev_sterbl_abs_sterbl_de|www.dashboard-deutschland.de/api/tile/indicators?ids=ginsy_ges_bev_sterbl_abs_sterbl_de|
|Ölpreis (Sorte Brent)|data_preise_oel|www.dashboard-deutschland.de/api/tile/indicators?ids=data_preise_oel|
|Mobilitätstrends: Besuche des Arbeitsplatzes im bundesweiten Vergleich|tile_1650547629071|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1650547629071|
|Stimmungsindikatoren Konsum|data_gfk_hde_konsum|www.dashboard-deutschland.de/api/tile/indicators?ids=data_gfk_hde_konsum|
|Energieverbrauch für Wohnen nach Energieträgern|data_woh_energieverbrauch_energietraeger|www.dashboard-deutschland.de/api/tile/indicators?ids=data_woh_energieverbrauch_energietraeger|
|Flugverkehr Deutschland|data_adv_flugverkehr|www.dashboard-deutschland.de/api/tile/indicators?ids=data_adv_flugverkehr|
|Importe fossiler Energieträger|tile_1654001211812|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1654001211812|
|Neuzulassungen von Personenkraftwagen nach Antriebsarten|tile_1663666467966|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1663666467966|
|Krankenhauskapazitäten|ginsy_ges_infra_ausst_intensivbetten_de|www.dashboard-deutschland.de/api/tile/indicators?ids=ginsy_ges_infra_ausst_intensivbetten_de|
|Mobilitätsindikatoren auf Grundlage von Mobilfunkdaten|data_mobilitaet_mobilfunk|www.dashboard-deutschland.de/api/tile/indicators?ids=data_mobilitaet_mobilfunk|
|Kassenmäßige Steuereinnahmen von Bund und Ländern|data_steuereinnahmen_bund_laender|www.dashboard-deutschland.de/api/tile/indicators?ids=data_steuereinnahmen_bund_laender|
|Kurzarbeit|data_ba_kurzarbeit|www.dashboard-deutschland.de/api/tile/indicators?ids=data_ba_kurzarbeit|
|Auftragseingang in Branchen des Verarbeitenden Gewerbes|data_auftragseingang_ausgewaehlte_branchen|www.dashboard-deutschland.de/api/tile/indicators?ids=data_auftragseingang_ausgewaehlte_branchen|
|Flugverkehr weltweit|data_flightradar24_flugverkehr|www.dashboard-deutschland.de/api/tile/indicators?ids=data_flightradar24_flugverkehr|
|Anzahl der genehmigten Wohnungen nach Bauherr|data_woh_baugenehmigungen_bautraeger|www.dashboard-deutschland.de/api/tile/indicators?ids=data_woh_baugenehmigungen_bautraeger|
|Produktion im Produzierenden Gewerbe|data_produktion_vg|www.dashboard-deutschland.de/api/tile/indicators?ids=data_produktion_vg|
|Verschuldung des Bundeshaushalts inklusive Darlehensfinanzierung nach Restlaufzeiten|tile_1650978274644|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1650978274644|
|Erwerbstätigkeit|data_erwerbstaetige|www.dashboard-deutschland.de/api/tile/indicators?ids=data_erwerbstaetige|
|Preisindex für Ein- und Zweifamilienhäuser nach Kreistypen|data_woh_preise_immobilien_hpi_haueser|www.dashboard-deutschland.de/api/tile/indicators?ids=data_woh_preise_immobilien_hpi_haueser|
|Mobilitätstrends: Besuche von Einzelhandel und Erholungseinrichtungen im europäischen Vergleich|tile_1650548728319|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1650548728319|
|Preisentwicklung für Energie (Strom, Gas und andere Brennstoffe) im EU-Vergleich|tile_1663666887687|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1663666887687|
|Außenhandel mit ausgewählten Ländern|data_aussenhandel_laender|www.dashboard-deutschland.de/api/tile/indicators?ids=data_aussenhandel_laender|
|Strompreis|data_preise_strom|www.dashboard-deutschland.de/api/tile/indicators?ids=data_preise_strom|
|Produktion von Solarkollektoren, Solarmodulen und Wärmepumpen|tile_1663667563512|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1663667563512|
|Relative Sterbefallzahlen in Deutschland im Vergleich|ginsy_ges_bev_sterbl_rel_sterbl_map_de|www.dashboard-deutschland.de/api/tile/indicators?ids=ginsy_ges_bev_sterbl_rel_sterbl_map_de|
|Kassenmäßige Steuereinnahmen aus Gemeinschaft-, Bundes- und Landessteuern|data_gemeinschaft_bundes_landessteuern|www.dashboard-deutschland.de/api/tile/indicators?ids=data_gemeinschaft_bundes_landessteuern|
|Umsatz mit Motorenkraftstoffen an Tankstellen|tile_1663667870377|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1663667870377|
|Verbraucherpreisindex für Nettokaltmiete nach Kreistypen|data_woh_nettokaltmiete|www.dashboard-deutschland.de/api/tile/indicators?ids=data_woh_nettokaltmiete|
|Einzelhandelsumsatz|data_einzelhandelsumsatz_vergleich_internet|www.dashboard-deutschland.de/api/tile/indicators?ids=data_einzelhandelsumsatz_vergleich_internet|
|Covid-19-Fälle|ginsy_ges_diag_covid19_faelle_de|www.dashboard-deutschland.de/api/tile/indicators?ids=ginsy_ges_diag_covid19_faelle_de|
|Exporterwartungen und Containerumschlag|data_ifo_rwi_exporte_container|www.dashboard-deutschland.de/api/tile/indicators?ids=data_ifo_rwi_exporte_container|
|Kassenmäßige Steuereinnahmen insgesamt und der Gemeinden/Gemeindeverbände|data_steuereinnahmen_insgesamt_gemeinden|www.dashboard-deutschland.de/api/tile/indicators?ids=data_steuereinnahmen_insgesamt_gemeinden|
|Umsatz in Branchen des Verarbeitenden Gewerbes|data_umsatz_ausgewaehlte_branchen|www.dashboard-deutschland.de/api/tile/indicators?ids=data_umsatz_ausgewaehlte_branchen|
|Füllstand deutscher Erdgasspeicher|tile_1649679768351|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1649679768351|
|Renditen Bundeswertpapiere|data_umlaufrenditen_bundesanleihen|www.dashboard-deutschland.de/api/tile/indicators?ids=data_umlaufrenditen_bundesanleihen|
|LKW-Maut-Fahrleistungsindex|data_destatis_lkw_maut_fahrleistungsindex|www.dashboard-deutschland.de/api/tile/indicators?ids=data_destatis_lkw_maut_fahrleistungsindex|
|Außenhandel mit ausgewählten Ländergruppen|data_aussenhandel_laendergruppen|www.dashboard-deutschland.de/api/tile/indicators?ids=data_aussenhandel_laendergruppen|
|Anteil der Grünen Bundeswertpapiere an der Verschuldung des Bundes inklusive Darlehensfinanzierung|tile_1650979109395|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1650979109395|
|Gold- und Kupferpreis|data_preise_gold_kupfer|www.dashboard-deutschland.de/api/tile/indicators?ids=data_preise_gold_kupfer|
|Produktion im Baugewerbe|data_bau_produktionsindex_baugewerbe|www.dashboard-deutschland.de/api/tile/indicators?ids=data_bau_produktionsindex_baugewerbe|
|Importe und Exporte von Wasserstoff|tile_1654002158461|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1654002158461|
|Bürgschaften|tile_1651053194613|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1651053194613|
|Entwicklung des Bruttoinlandsprodukts|data_bruttoinlandsprodukt|www.dashboard-deutschland.de/api/tile/indicators?ids=data_bruttoinlandsprodukt|
|Benzinpreise im EU-Vergleich|tile_1663664545105|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1663664545105|
|Stimmungsindikatoren Arbeitsmarkt|data_iab_ifo_barometer|www.dashboard-deutschland.de/api/tile/indicators?ids=data_iab_ifo_barometer|
|ifo Geschäftsklima|data_ifo_geschaeftsklima|www.dashboard-deutschland.de/api/tile/indicators?ids=data_ifo_geschaeftsklima|
|Genehmigte und fertiggestellte Wohnungen|data_woh_genehmigte_u_fertiggestellte_wohnungen|www.dashboard-deutschland.de/api/tile/indicators?ids=data_woh_genehmigte_u_fertiggestellte_wohnungen|
|Wöchentlicher Aktivitätsindex|data_bundesbank_aktivitaetsindex|www.dashboard-deutschland.de/api/tile/indicators?ids=data_bundesbank_aktivitaetsindex|
|Umlaufrenditen Staats- und Unternehmensanleihen|data_staats_und_unt_anleihen|www.dashboard-deutschland.de/api/tile/indicators?ids=data_staats_und_unt_anleihen|
|Nettonennleistung der Anlagen zur Elektrizitätserzeugung|tile_1663665904253|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1663665904253|
|Auftragseingang im Verarbeitenden Gewerbe|data_auftragseingang_vg|www.dashboard-deutschland.de/api/tile/indicators?ids=data_auftragseingang_vg|
|Verschuldung der größten Sondervermögen des Bundes|tile_1650977632272|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1650977632272|
|S&P Global/BME Einkaufsmanagerindex|data_markit_bme_einkaufsmanager|www.dashboard-deutschland.de/api/tile/indicators?ids=data_markit_bme_einkaufsmanager|
|Stromverbrauch|data_bnetza_realisierter_stromverbrauch|www.dashboard-deutschland.de/api/tile/indicators?ids=data_bnetza_realisierter_stromverbrauch|
|Umsatz mit Maßnahmen zur Verbesserung der Energieeffizienz von Gebäuden|tile_1665656599909|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1665656599909|
|Aufkommen und Verwendung von Wasserstoff|tile_1663663630535|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1663663630535|
|Kraftstoffpreise an öffentlichen Tankstellen|tile_1648135639982|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1648135639982|
|Kapazitätsauslastung im Baugewerbe|data_bau_kapazitaetsauslastung_bbsr|www.dashboard-deutschland.de/api/tile/indicators?ids=data_bau_kapazitaetsauslastung_bbsr|
|Umsatz im Ausbaugewerbe|tile_1654070793733|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1654070793733|
|Aktienindizes|data_boersenkurse|www.dashboard-deutschland.de/api/tile/indicators?ids=data_boersenkurse|
|Umsatz im Bauhauptgewerbe|tile_1654068021178|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1654068021178|
|Fertiggestellte Neubauten nach überwiegend verwendeter Heizenergie|tile_1654000747086|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1654000747086|
|Außenhandel|data_aussenhandel|www.dashboard-deutschland.de/api/tile/indicators?ids=data_aussenhandel|
|Infektionsgeschehen|ginsy_ges_diag_covid19_neuinfektionen_de|www.dashboard-deutschland.de/api/tile/indicators?ids=ginsy_ges_diag_covid19_neuinfektionen_de|
|Preisindex für Eigentumswohnungen nach Kreistypen|data_woh_preise_immobilien_hpi_wohnungen|www.dashboard-deutschland.de/api/tile/indicators?ids=data_woh_preise_immobilien_hpi_wohnungen|
|Ausgewählte Erdgaslieferungen nach Deutschland|tile_1653306303133|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1653306303133|
|ifo Produktionserwartungen|data_ifo_produktionserwartungen|www.dashboard-deutschland.de/api/tile/indicators?ids=data_ifo_produktionserwartungen|
|Umsatz im Gastgewerbe|data_umsatz_gastgewerbe_beherbergung|www.dashboard-deutschland.de/api/tile/indicators?ids=data_umsatz_gastgewerbe_beherbergung|
|Energieverbrauch der Industrie nach Energieträgern|tile_1654002609295|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1654002609295|
|Genehmigte neu zu errichtende Wohngebäude mit ein und zwei Wohnungen nach überwiegend verwendeter Heizenergie|tile_1663665272454|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1663665272454|
|Covid-19-Hospitalisierungen|defacto_ges_diag_covid19_hospitalizationincidence_map_de|www.dashboard-deutschland.de/api/tile/indicators?ids=defacto_ges_diag_covid19_hospitalizationincidence_map_de|
|Wirtschaftsstabilisierungsfonds|tile_1651058916171|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1651058916171|
|Umsatz im Verarbeitenden Gewerbe|data_umsatz_vg|www.dashboard-deutschland.de/api/tile/indicators?ids=data_umsatz_vg|
|Blitzumfragen im Maschinen- und Anlagenbau|data_vdma_blitzumfragen|www.dashboard-deutschland.de/api/tile/indicators?ids=data_vdma_blitzumfragen|
|Arbeitslosigkeit und offene Stellen|data_ba_arbeitslose_und_stellen|www.dashboard-deutschland.de/api/tile/indicators?ids=data_ba_arbeitslose_und_stellen|
|7-Tage-Inzidenz|ginsy_ges_diag_covid19_7_tage_inzidenz_map_de|www.dashboard-deutschland.de/api/tile/indicators?ids=ginsy_ges_diag_covid19_7_tage_inzidenz_map_de|
|Verbraucherpreisindex für Nettokaltmiete, Wohnungsnebenkosten und Haushaltsenergie|data_woh_bruttokaltmiete|www.dashboard-deutschland.de/api/tile/indicators?ids=data_woh_bruttokaltmiete|
|Verschuldung des Bundeshaushalts und seiner Sondervermögen|tile_1650978797816|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1650978797816|
|Exporte und Importe von Wärmepumpen und Photovoltaikanlagen|tile_1663664931250|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1663664931250|
|Corona-Zuschüsse|data_corona_zuschuesse|www.dashboard-deutschland.de/api/tile/indicators?ids=data_corona_zuschuesse|
|Auftragseingang im Bauhauptgewerbe|data_bau_auftragseingang|www.dashboard-deutschland.de/api/tile/indicators?ids=data_bau_auftragseingang|
|Wohnfläche in genehmigten Neubauwohnungen|data_woh_baugenehmigungen_wohnflaeche|www.dashboard-deutschland.de/api/tile/indicators?ids=data_woh_baugenehmigungen_wohnflaeche|
|Baupreisindizes|data_bau_bauleistungspreise|www.dashboard-deutschland.de/api/tile/indicators?ids=data_bau_bauleistungspreise|
|Renditespreads 10-jähriger Staatsanleihen gegenüber Deutschland|data_zinsspread_10_j_anleihen|www.dashboard-deutschland.de/api/tile/indicators?ids=data_zinsspread_10_j_anleihen|
|Energiepreisentwicklung|tile_1654001812693|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1654001812693|
|Nettostromerzeugung|tile_1649694802780|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1649694802780|
|Beschäftigung im Baugewerbe|data_bau_beschaeftigung_vgr|www.dashboard-deutschland.de/api/tile/indicators?ids=data_bau_beschaeftigung_vgr|
|Preisindizes zu Bau oder Erwerb von Wohneigentum|tile_1656076602735|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1656076602735|
|Bereinigte kassenmäßige Steuereinnahmen aus Gemeinschaft-, Bundes- und Landessteuern|data_einnahmen_gemeinschaft_bundes_landessteuern|www.dashboard-deutschland.de/api/tile/indicators?ids=data_einnahmen_gemeinschaft_bundes_landessteuern|
|Passantenfrequenzen: Veränderung in ausgewählten Großstädten|data_mobilitaet_hystreet|www.dashboard-deutschland.de/api/tile/indicators?ids=data_mobilitaet_hystreet|
|KfW-Sonderprogramm|data_kfw_sondermassnahme_neu|www.dashboard-deutschland.de/api/tile/indicators?ids=data_kfw_sondermassnahme_neu|
|Covid-19-Impfstatus|ginsy_ges_impfung_covid19_impfstatus_map_de|www.dashboard-deutschland.de/api/tile/indicators?ids=ginsy_ges_impfung_covid19_impfstatus_map_de|
|Anzahl genehmigter Wohnungen im Neubau nach Gebäudeart|data_woh_baugenehmigungen_wohnungen|www.dashboard-deutschland.de/api/tile/indicators?ids=data_woh_baugenehmigungen_wohnungen|
|Kreditvergaben und Online-Transaktionen|data_kreditwirtschaft|www.dashboard-deutschland.de/api/tile/indicators?ids=data_kreditwirtschaft|
|Produktion in Branchen des Produzierenden Gewerbes|data_produktion_ausgewaehlte_branchen|www.dashboard-deutschland.de/api/tile/indicators?ids=data_produktion_ausgewaehlte_branchen|
|Verbrauch von Mineralölprodukten in Deutschland|tile_1663665588691|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1663665588691|
|Mobilitätstrends: Besuche des Arbeitsplatzes im europäischen Vergleich|tile_1650548254089|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1650548254089|
|Wechselkurs US-Dollar/Euro|data_wechselkurs_usd_eur|www.dashboard-deutschland.de/api/tile/indicators?ids=data_wechselkurs_usd_eur|
|Energieverbrauch für Wohnen nach Anwendungsbereichen|tile_1651060108903|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1651060108903|
|Außenhandelsbilanz|data_aussenhandelsbilanz|www.dashboard-deutschland.de/api/tile/indicators?ids=data_aussenhandelsbilanz|
|ZEW Konjunkturausblick|data_zew_konjunktur|www.dashboard-deutschland.de/api/tile/indicators?ids=data_zew_konjunktur|
|Kassenmäßige Steuereinnahmen aus Gemeindesteuern|data_gemeindesteuern|www.dashboard-deutschland.de/api/tile/indicators?ids=data_gemeindesteuern|
|Preisentwicklung|data_preisentwicklung|www.dashboard-deutschland.de/api/tile/indicators?ids=data_preisentwicklung|
|Weltmarktpreise für Weizen|tile_1654606920834|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1654606920834|


## Geojson

**URL:** www.dashboard-deutschland.de/geojson/de-all.geo.json
	
Die API ermöglicht Zugriff auf Geojson-Daten zu Deutschland und den Ländern (00-DE_admin1_400).


## Beispiel

```bash
indicators=$(curl -m 60 'https://www.dashboard-deutschland.de/api/tile/indicators?ids=data_adv_flugverkehr;data_aussenhandel;data_ba_arbeitslose_und_stellen;data_bruttoinlandsprodukt;data_corona_zuschuesse;data_einnahmen_gemeinschaft_bundes_landessteuern;data_ifo_geschaeftsklima;data_kfw_sondermassnahme_neu;data_preisentwicklung;data_umsatz_ausgewaehlte_branchen;defacto_ges_diag_covid19_hospitalizationincidence_map_de;ginsy_ges_bev_sterbl_abs_sterbl_de;ginsy_ges_diag_covid19_7_tage_inzidenz_map_de;tile_1648135639982
')
```
