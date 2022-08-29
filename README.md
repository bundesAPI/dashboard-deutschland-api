# Dashboard Deutschland API

Auf https://www.dashboard-deutschland.de bietet das Statistische Bundesamt DESTATIS einen Überblick zu gesellschaftlich und wirtschaftlich relevanten Daten aus unterschiedlichen Themenbereichen. Diese werden durch Grafiken und Texte ergänzt und regelmäßig aktualisiert. Damit soll eine Möglichkeit geboten werden, aktuelle Kennzahlen und deren Entwicklung übersichtlich darzustellen.


## Get

**URL:** https://www.dashboard-deutschland.de/api/dashboard/get
	
Die API ermöglicht über diese URL den Zugriff auf alle gültigen Einträge des id-Parameters getrennt nach id-Kategorien (siehe unten, Indikatoren). 


## Indikatoren

**URL:** www.dashboard-deutschland.de/api/tile/indicators
	
Die API ermöglicht über diese URL Zugriff auf unterschiedliche Indikatoren im JSON-Format über einfache GET-requests mit nur einem Parameter (namens *ids*). Der Parameter ids spezifiziert den gewünschten Indikator. Mögliche Ausprägungen sind im Folgenden tabellarisch dargestellt. Mehrere Semikolon-getrennte Angaben sind möglich. Gesundheitsindikatoren (beginnend mit "ginsy_ges") lassen sich über eine Variation der u.g. id auch nach Regionen von Bundesländern unterteilt anfordern - durch Ergänzung eines Unterstrichs, gefolgt von einer das Bundesland repräsentierenden Zahl (z.B. 9 für Bayern).

|ids|Bedeutung|Beispiel-URL|
|---|---|---|
|data_produktion_ausgewaehlte_branchen|Produktion in Branchen des Produzierenden Gewerbes|www.dashboard-deutschland.de/api/tile/indicators?ids=data_produktion_ausgewaehlte_branchen|
|data_woh_preise_immobilien_hpi_wohnungen|Preisindex für Eigentumswohnungen nach Kreistypen|www.dashboard-deutschland.de/api/tile/indicators?ids=data_woh_preise_immobilien_hpi_wohnungen|
|data_mobilitaet_mobilfunk_karte|Tägliche Veränderung der Mobilität auf Kreisebene auf Grundlage von Mobilfunkdaten|www.dashboard-deutschland.de/api/tile/indicators?ids=data_mobilitaet_mobilfunk_karte|
|data_steuereinnahmen_bund_laender|Kassenmäßige Steuereinnahmen von Bund und Ländern|www.dashboard-deutschland.de/api/tile/indicators?ids=data_steuereinnahmen_bund_laender|
|tile_1650978797816|Verschuldung des Bundeshaushalts und seiner Sondervermögen|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1650978797816|
|data_destatis_lkw_maut_fahrleistungsindex|LKW-Maut-Fahrleistungsindex|www.dashboard-deutschland.de/api/tile/indicators?ids=data_destatis_lkw_maut_fahrleistungsindex|
|ginsy_ges_diag_covid19_neuinfektionen_de|Infektionsgeschehen|www.dashboard-deutschland.de/api/tile/indicators?ids=ginsy_ges_diag_covid19_neuinfektionen_de|
|tile_1650547629071|Mobilitätstrends: Besuche des Arbeitsplatzes im bundesweiten Vergleich|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1650547629071|
|data_auftragseingang_ausgewaehlte_branchen|Auftragseingang in Branchen des Verarbeitenden Gewerbes|www.dashboard-deutschland.de/api/tile/indicators?ids=data_auftragseingang_ausgewaehlte_branchen|
|tile_1654002158461|Importe und Exporte von Wasserstoff|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1654002158461|
|tile_1649694802780|Nettostromerzeugung|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1649694802780|
|data_aussenhandel|Außenhandel|www.dashboard-deutschland.de/api/tile/indicators?ids=data_aussenhandel|
|ginsy_ges_infra_ausst_intensivbetten_de|Krankenhauskapazitäten|www.dashboard-deutschland.de/api/tile/indicators?ids=ginsy_ges_infra_ausst_intensivbetten_de|
|ginsy_ges_bev_sterbl_abs_sterbl_de|Wöchentliche Sterbefallzahlen in Deutschland|www.dashboard-deutschland.de/api/tile/indicators?ids=ginsy_ges_bev_sterbl_abs_sterbl_de|
|data_mobilitaet_mobilfunk|Mobilitätsindikatoren auf Grundlage von Mobilfunkdaten|www.dashboard-deutschland.de/api/tile/indicators?ids=data_mobilitaet_mobilfunk|
|data_flightradar24_flugverkehr|Flugverkehr weltweit|www.dashboard-deutschland.de/api/tile/indicators?ids=data_flightradar24_flugverkehr|
|data_bnetza_realisierter_stromverbrauch|Stromverbrauch|www.dashboard-deutschland.de/api/tile/indicators?ids=data_bnetza_realisierter_stromverbrauch|
|data_kfw_sondermassnahme_neu|KfW-Sonderprogramm|www.dashboard-deutschland.de/api/tile/indicators?ids=data_kfw_sondermassnahme_neu|
|data_vda_pkw|Automobilindustrie|www.dashboard-deutschland.de/api/tile/indicators?ids=data_vda_pkw|
|tile_1651060108903|Energieverbrauch für Wohnen nach Anwendungsbereichen|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1651060108903|
|data_bruttoinlandsprodukt|Entwicklung des Bruttoinlandsprodukts|www.dashboard-deutschland.de/api/tile/indicators?ids=data_bruttoinlandsprodukt|
|tile_1654070793733|Umsatz im Ausbaugewerbe|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1654070793733|
|data_wechselkurs_usd_eur|Wechselkurs US-Dollar/Euro|www.dashboard-deutschland.de/api/tile/indicators?ids=data_wechselkurs_usd_eur|
|data_bau_kapazitaetsauslastung_bbsr|Kapazitätsauslastung im Baugewerbe|www.dashboard-deutschland.de/api/tile/indicators?ids=data_bau_kapazitaetsauslastung_bbsr|
|tile_1654001211812|Importe fossiler Energieträger|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1654001211812|
|data_bau_verbesserung_energieeffizienz|Umsatz mit Maßnahmen zur Verbesserung der Energieeffizienz von Gebäuden|www.dashboard-deutschland.de/api/tile/indicators?ids=data_bau_verbesserung_energieeffizienz|
|data_staats_und_unt_anleihen|Umlaufrenditen Staats- und Unternehmensanleihen|www.dashboard-deutschland.de/api/tile/indicators?ids=data_staats_und_unt_anleihen|
|data_preise_oel|Ölpreis (Sorte Brent)|www.dashboard-deutschland.de/api/tile/indicators?ids=data_preise_oel|
|tile_1650979109395|Anteil der Grünen Bundeswertpapiere an der Verschuldung des Bundes inklusive Darlehensfinanzierung|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1650979109395|
|data_preisentwicklung|Preisentwicklung|www.dashboard-deutschland.de/api/tile/indicators?ids=data_preisentwicklung|
|data_woh_bruttokaltmiete|Verbraucherpreisindex für Nettokaltmiete, Wohnungsnebenkosten und Haushaltsenergie|www.dashboard-deutschland.de/api/tile/indicators?ids=data_woh_bruttokaltmiete|
|data_woh_preise_immobilien_hpi_haueser|Preisindex für Ein- und Zweifamilienhäuser nach Kreistypen|www.dashboard-deutschland.de/api/tile/indicators?ids=data_woh_preise_immobilien_hpi_haueser|
|data_ifo_rwi_exporte_container|Exporterwartungen und Containerumschlag|www.dashboard-deutschland.de/api/tile/indicators?ids=data_ifo_rwi_exporte_container|
|defacto_ges_diag_covid19_hospitalizationincidence_map_de|Covid-19-Hospitalisierungen|www.dashboard-deutschland.de/api/tile/indicators?ids=defacto_ges_diag_covid19_hospitalizationincidence_map_de|
|data_woh_nettokaltmiete|Verbraucherpreisindex für Nettokaltmiete nach Kreistypen|www.dashboard-deutschland.de/api/tile/indicators?ids=data_woh_nettokaltmiete|
|data_ba_kurzarbeit|Kurzarbeit|www.dashboard-deutschland.de/api/tile/indicators?ids=data_ba_kurzarbeit|
|data_produktion_vg|Produktion im Produzierenden Gewerbe|www.dashboard-deutschland.de/api/tile/indicators?ids=data_produktion_vg|
|ginsy_ges_bev_sterbl_rel_sterbl_map_de|Relative Sterbefallzahlen in Deutschland im Vergleich|www.dashboard-deutschland.de/api/tile/indicators?ids=ginsy_ges_bev_sterbl_rel_sterbl_map_de|
|data_aussenhandel_laendergruppen|Außenhandel mit ausgewählten Ländergruppen|www.dashboard-deutschland.de/api/tile/indicators?ids=data_aussenhandel_laendergruppen|
|data_woh_baugenehmigungen_wohnflaeche|Wohnfläche in genehmigten Neubauwohnungen|www.dashboard-deutschland.de/api/tile/indicators?ids=data_woh_baugenehmigungen_wohnflaeche|
|data_woh_energieverbrauch_energietraeger|Energieverbrauch für Wohnen nach Energieträgern|www.dashboard-deutschland.de/api/tile/indicators?ids=data_woh_energieverbrauch_energietraeger|
|data_aussenhandel_laender|Außenhandel mit ausgewählten Ländern|www.dashboard-deutschland.de/api/tile/indicators?ids=data_aussenhandel_laender|
|tile_1654000747086|Fertiggestellte Neubauten nach überwiegend verwendeter Heizenergie|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1654000747086|
|data_mobilitaet_hystreet|Passantenfrequenzen: Veränderung in ausgewählten Großstädten|www.dashboard-deutschland.de/api/tile/indicators?ids=data_mobilitaet_hystreet|
|data_auftragseingang_vg|Auftragseingang im Verarbeitenden Gewerbe|www.dashboard-deutschland.de/api/tile/indicators?ids=data_auftragseingang_vg|
|data_mobilitaet_mobilfunk_hotspot|Tägliche Mobilitätsveränderung und 7-Tage-Inzidenz auf Kreisebene auf Grundlage von Mobilfunkdaten|www.dashboard-deutschland.de/api/tile/indicators?ids=data_mobilitaet_mobilfunk_hotspot|
|tile_1653306303133|Ausgewählte Erdgaslieferungen nach Deutschland|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1653306303133|
|tile_1654002609295|Energieverbrauch der Industrie nach Energieträgern|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1654002609295|
|data_gemeindesteuern|Kassenmäßige Steuereinnahmen aus Gemeindesteuern|www.dashboard-deutschland.de/api/tile/indicators?ids=data_gemeindesteuern|
|data_bau_produktionsindex_baugewerbe|Produktion im Baugewerbe|www.dashboard-deutschland.de/api/tile/indicators?ids=data_bau_produktionsindex_baugewerbe|
|tile_1650548254089|Mobilitätstrends: Besuche des Arbeitsplatzes im europäischen Vergleich|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1650548254089|
|data_adv_flugverkehr|Flugverkehr Deutschland|www.dashboard-deutschland.de/api/tile/indicators?ids=data_adv_flugverkehr|
|ginsy_ges_impfung_covid19_impfstatus_map_de|Covid-19-Impfstatus|www.dashboard-deutschland.de/api/tile/indicators?ids=ginsy_ges_impfung_covid19_impfstatus_map_de|
|data_umsatz_ausgewaehlte_branchen|Umsatz in Branchen des Verarbeitenden Gewerbes|www.dashboard-deutschland.de/api/tile/indicators?ids=data_umsatz_ausgewaehlte_branchen|
|ginsy_ges_diag_covid19_7_tage_inzidenz_map_de|7-Tage-Inzidenz|www.dashboard-deutschland.de/api/tile/indicators?ids=ginsy_ges_diag_covid19_7_tage_inzidenz_map_de|
|tile_1654068021178|Umsatz im Bauhauptgewerbe|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1654068021178|
|data_bau_bauleistungspreise|Baupreisindizes|www.dashboard-deutschland.de/api/tile/indicators?ids=data_bau_bauleistungspreise|
|data_vdma_blitzumfragen|Blitzumfragen im Maschinen- und Anlagenbau|www.dashboard-deutschland.de/api/tile/indicators?ids=data_vdma_blitzumfragen|
|data_woh_genehmigte_u_fertiggestellte_wohnungen|Genehmigte und fertiggestellte Wohnungen|www.dashboard-deutschland.de/api/tile/indicators?ids=data_woh_genehmigte_u_fertiggestellte_wohnungen|
|data_markit_bme_einkaufsmanager|S&P Global/BME Einkaufsmanagerindex|www.dashboard-deutschland.de/api/tile/indicators?ids=data_markit_bme_einkaufsmanager|
|tile_1651053194613|Bürgschaften|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1651053194613|
|data_corona_zuschuesse|Corona-Zuschüsse|www.dashboard-deutschland.de/api/tile/indicators?ids=data_corona_zuschuesse|
|ginsy_ges_impfung_covid19_gesamtzahl_de|Gesamtzahl der Covid-19-Impfungen|www.dashboard-deutschland.de/api/tile/indicators?ids=ginsy_ges_impfung_covid19_gesamtzahl_de|
|data_aussenhandelsbilanz|Außenhandelsbilanz|www.dashboard-deutschland.de/api/tile/indicators?ids=data_aussenhandelsbilanz|
|tile_1650550636596|Mobilitätstrends: Besuche von Einzelhandel und Erholungseinrichtungen im bundesweiten Vergleich|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1650550636596|
|data_ifo_geschaeftsklima|ifo Geschäftsklima|www.dashboard-deutschland.de/api/tile/indicators?ids=data_ifo_geschaeftsklima|
|ginsy_ges_diag_covid19_faelle_de|Covid-19-Fälle|www.dashboard-deutschland.de/api/tile/indicators?ids=ginsy_ges_diag_covid19_faelle_de|
|data_kreditwirtschaft|Kreditvergaben und Online-Transaktionen|www.dashboard-deutschland.de/api/tile/indicators?ids=data_kreditwirtschaft|
|data_einnahmen_gemeinschaft_bundes_landessteuern|Bereinigte kassenmäßige Steuereinnahmen aus Gemeinschaft-, Bundes- und Landessteuern|www.dashboard-deutschland.de/api/tile/indicators?ids=data_einnahmen_gemeinschaft_bundes_landessteuern|
|data_preise_gold_kupfer|Gold- und Kupferpreis|www.dashboard-deutschland.de/api/tile/indicators?ids=data_preise_gold_kupfer|
|data_ba_arbeitslose_und_stellen|Arbeitslosigkeit und offene Stellen|www.dashboard-deutschland.de/api/tile/indicators?ids=data_ba_arbeitslose_und_stellen|
|data_umlaufrenditen_bundesanleihen|Renditen Bundeswertpapiere|www.dashboard-deutschland.de/api/tile/indicators?ids=data_umlaufrenditen_bundesanleihen|
|data_woh_baugenehmigungen_wohnungen|Anzahl genehmigter Wohnungen im Neubau nach Gebäudeart|www.dashboard-deutschland.de/api/tile/indicators?ids=data_woh_baugenehmigungen_wohnungen|
|data_zinsspread_10_j_anleihen|Renditespreads 10-jähriger Staatsanleihen gegenüber Deutschland|www.dashboard-deutschland.de/api/tile/indicators?ids=data_zinsspread_10_j_anleihen|
|tile_1648135639982|Kraftstoffpreise an öffentlichen Tankstellen|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1648135639982|
|tile_1651058916171|Wirtschaftsstabilisierungsfonds|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1651058916171|
|tile_1650977632272|Verschuldung der größten Sondervermögen des Bundes|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1650977632272|
|data_woh_baugenehmigungen_bautraeger|Anzahl der genehmigten Wohnungen nach Bauherr|www.dashboard-deutschland.de/api/tile/indicators?ids=data_woh_baugenehmigungen_bautraeger|
|data_preise_strom|Strompreis|www.dashboard-deutschland.de/api/tile/indicators?ids=data_preise_strom|
|data_einzelhandelsumsatz_vergleich_internet|Einzelhandelsumsatz|www.dashboard-deutschland.de/api/tile/indicators?ids=data_einzelhandelsumsatz_vergleich_internet|
|data_steuereinnahmen_insgesamt_gemeinden|Kassenmäßige Steuereinnahmen insgesamt und der Gemeinden/Gemeindeverbände|www.dashboard-deutschland.de/api/tile/indicators?ids=data_steuereinnahmen_insgesamt_gemeinden|
|tile_1656076602735|Preisindizes zu Bau oder Erwerb von Wohneigentum|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1656076602735|
|tile_1654606920834|Weltmarktpreise für Weizen|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1654606920834|
|data_erwerbstaetige|Erwerbstätigkeit|www.dashboard-deutschland.de/api/tile/indicators?ids=data_erwerbstaetige|
|data_umsatz_vg|Umsatz im Verarbeitenden Gewerbe|www.dashboard-deutschland.de/api/tile/indicators?ids=data_umsatz_vg|
|data_umsatz_gastgewerbe_beherbergung|Umsatz im Gastgewerbe|www.dashboard-deutschland.de/api/tile/indicators?ids=data_umsatz_gastgewerbe_beherbergung|
|data_zew_konjunktur|ZEW Konjunkturausblick|www.dashboard-deutschland.de/api/tile/indicators?ids=data_zew_konjunktur|
|data_bau_auftragseingang|Auftragseingang im Bauhauptgewerbe|www.dashboard-deutschland.de/api/tile/indicators?ids=data_bau_auftragseingang|
|data_bundesbank_aktivitaetsindex|Wöchentlicher Aktivitätsindex|www.dashboard-deutschland.de/api/tile/indicators?ids=data_bundesbank_aktivitaetsindex|
|data_gfk_hde_konsum|Stimmungsindikatoren Konsum|www.dashboard-deutschland.de/api/tile/indicators?ids=data_gfk_hde_konsum|
|data_gemeinschaft_bundes_landessteuern|Kassenmäßige Steuereinnahmen aus Gemeinschaft-, Bundes- und Landessteuern|www.dashboard-deutschland.de/api/tile/indicators?ids=data_gemeinschaft_bundes_landessteuern|
|tile_1650548728319|Mobilitätstrends: Besuche von Einzelhandel und Erholungseinrichtungen im europäischen Vergleich|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1650548728319|
|data_ifo_produktionserwartungen|ifo Produktionserwartungen|www.dashboard-deutschland.de/api/tile/indicators?ids=data_ifo_produktionserwartungen|
|data_bau_beschaeftigung_vgr|Beschäftigung im Baugewerbe|www.dashboard-deutschland.de/api/tile/indicators?ids=data_bau_beschaeftigung_vgr|
|data_iab_ifo_barometer|Stimmungsindikatoren Arbeitsmarkt|www.dashboard-deutschland.de/api/tile/indicators?ids=data_iab_ifo_barometer|
|data_boersenkurse|Aktienindizes|www.dashboard-deutschland.de/api/tile/indicators?ids=data_boersenkurse|
|tile_1650978274644|Verschuldung des Bundeshaushalts inklusive Darlehensfinanzierung nach Restlaufzeiten|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1650978274644|
|tile_1649679768351|Füllstand deutscher Erdgasspeicher|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1649679768351|
|tile_1654001812693|Energiepreisentwicklung|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1654001812693|


## Geojson

**URL:** www.dashboard-deutschland.de/geojson/de-all.geo.json
	
Die API ermöglicht Zugriff auf Geojson-Daten zu Deutschland und den Ländern (00-DE_admin1_400).


## Beispiel

```bash
indicators=$(curl -m 60 'https://www.dashboard-deutschland.de/api/tile/indicators?ids=data_adv_flugverkehr;data_aussenhandel;data_ba_arbeitslose_und_stellen;data_bruttoinlandsprodukt;data_corona_zuschuesse;data_einnahmen_gemeinschaft_bundes_landessteuern;data_ifo_geschaeftsklima;data_kfw_sondermassnahme_neu;data_preisentwicklung;data_umsatz_ausgewaehlte_branchen;defacto_ges_diag_covid19_hospitalizationincidence_map_de;ginsy_ges_bev_sterbl_abs_sterbl_de;ginsy_ges_diag_covid19_7_tage_inzidenz_map_de;tile_1648135639982
')
```
