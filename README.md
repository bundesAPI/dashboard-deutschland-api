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
|Entwicklung ausgewählter Aggregate des Bruttoinlandsprodukts|tile_1667814729862|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667814729862|
|Produktion in Branchen des Produzierenden Gewerbes|data_produktion_ausgewaehlte_branchen|www.dashboard-deutschland.de/api/tile/indicators?ids=data_produktion_ausgewaehlte_branchen|
|Wohngebäude nach Baujahr und Energieträger der Heizung in Nordrhein-Westfalen|tile_1669196285543|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669196285543|
|Beschäftigung im Baugewerbe|data_bau_beschaeftigung_vgr|www.dashboard-deutschland.de/api/tile/indicators?ids=data_bau_beschaeftigung_vgr|
|Wohngebäude nach Gebäudegröße und Energieträger der Heizung in Hamburg|tile_1669290437600|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669290437600|
|S&P Global/BME Einkaufsmanagerindex|tile_1667982123933|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667982123933|
|Tägliche Mobilitätsveränderung und 7-Tage-Inzidenz auf Kreisebene auf Grundlage von Mobilfunkdaten|data_mobilitaet_mobilfunk_hotspot|www.dashboard-deutschland.de/api/tile/indicators?ids=data_mobilitaet_mobilfunk_hotspot|
|ifo Produktionserwartungen|tile_1667289137702|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667289137702|
|Erwerbstätigkeit|tile_1667822587333|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667822587333|
|Anzahl genehmigter Wohnungen im Neubau nach Gebäudeart|data_woh_baugenehmigungen_wohnungen|www.dashboard-deutschland.de/api/tile/indicators?ids=data_woh_baugenehmigungen_wohnungen|
|Wohngebäude nach Gebäudegröße und Energieträger der Heizung in Schleswig-Holstein|tile_1669296178221|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669296178221|
|Auftragseingang in Branchen des Verarbeitenden Gewerbes|data_auftragseingang_ausgewaehlte_branchen|www.dashboard-deutschland.de/api/tile/indicators?ids=data_auftragseingang_ausgewaehlte_branchen|
|Stimmungsindikatoren Konsum|tile_1667983271066|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667983271066|
|Auftragseingang im Verarbeitenden Gewerbe|tile_1667828024262|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667828024262|
|Umsatz im Verarbeitenden Gewerbe|tile_1667828804581|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667828804581|
|ifo Geschäftsklima|tile_1667288019608|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667288019608|
|Wohngebäude nach Baujahr und Energieträger der Heizung in Sachsen-Anhalt|tile_1669199513126|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669199513126|
|Wohngebäude nach Gebäudegröße und Energieträger der Heizung in Bremen|tile_1669285361958|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669285361958|
|HWWI-Rohstoffpreisindex|tile_1667215458776|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667215458776|
|Außenhandel mit ausgewählten Ländern|tile_1667832713510|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667832713510|
|Preisentwicklung für ausgewählte Baumaterialien|tile_1667308898055|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667308898055|
|Außenhandel mit ausgewählten Ländergruppen|data_aussenhandel_laendergruppen|www.dashboard-deutschland.de/api/tile/indicators?ids=data_aussenhandel_laendergruppen|
|Preisindizes zu Bau oder Erwerb von Wohneigentum|tile_1656076602735|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1656076602735|
|Tägliche Veränderung der Mobilität auf Kreisebene auf Grundlage von Mobilfunkdaten|data_mobilitaet_mobilfunk_karte|www.dashboard-deutschland.de/api/tile/indicators?ids=data_mobilitaet_mobilfunk_karte|
|Baupreisindizes|data_bau_bauleistungspreise|www.dashboard-deutschland.de/api/tile/indicators?ids=data_bau_bauleistungspreise|
|Nettonennleistung der Anlagen zur Elektrizitätserzeugung|tile_1663665904253|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1663665904253|
|Ausgewählte Erdgaslieferungen nach Deutschland|tile_1653306303133|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1653306303133|
|Genehmigte neu zu errichtende Wohngebäude mit ein und zwei Wohnungen nach überwiegend verwendeter Heizenergie|tile_1663665272454|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1663665272454|
|Infektionsgeschehen|ginsy_ges_diag_covid19_neuinfektionen_de|www.dashboard-deutschland.de/api/tile/indicators?ids=ginsy_ges_diag_covid19_neuinfektionen_de|
|Wöchentliche Sterbefallzahlen in Deutschland|ginsy_ges_bev_sterbl_abs_sterbl_de|www.dashboard-deutschland.de/api/tile/indicators?ids=ginsy_ges_bev_sterbl_abs_sterbl_de|
|Kassenmäßige Steuereinnahmen insgesamt und der Gemeinden/Gemeindeverbände|data_steuereinnahmen_insgesamt_gemeinden|www.dashboard-deutschland.de/api/tile/indicators?ids=data_steuereinnahmen_insgesamt_gemeinden|
|Täglicher LKW-Maut-Fahrleistungsindex|tile_1667226778807|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667226778807|
|Neuzulassungen von Personenkraftwagen nach Antriebsarten|tile_1663666467966|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1663666467966|
|Entwicklung des Bruttoinlandsprodukts|tile_1667811574092|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667811574092|
|Preisentwicklung|tile_1668694599167|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1668694599167|
|Produktion von Solarkollektoren, Solarmodulen und Wärmepumpen|tile_1663667563512|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1663667563512|
|Exporte und Importe von Wärmepumpen und Photovoltaikanlagen|tile_1663664931250|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1663664931250|
|Durchschnittliche Wohnkosten für Hauptmiethaushalte je Quadratmeter nach Haushaltsgröße|tile_1669368380310|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669368380310|
|Passantenfrequenzindex|tile_1667982573430|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667982573430|
|Kassenmäßige Steuereinnahmen von Bund und Ländern|data_steuereinnahmen_bund_laender|www.dashboard-deutschland.de/api/tile/indicators?ids=data_steuereinnahmen_bund_laender|
|Wohngebäude nach Gebäudegröße und Energieträger der Heizung in Nordrhein-Westfalen|tile_1669291731814|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669291731814|
|Kraftstoffpreise an öffentlichen Tankstellen|tile_1667921381760|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667921381760|
|Außenhandel|tile_1667830902757|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667830902757|
|Verbraucherpreisindex für Nettokaltmiete nach Kreistypen|data_woh_nettokaltmiete|www.dashboard-deutschland.de/api/tile/indicators?ids=data_woh_nettokaltmiete|
|Genehmigte und fertiggestellte Wohnungen|data_woh_genehmigte_u_fertiggestellte_wohnungen|www.dashboard-deutschland.de/api/tile/indicators?ids=data_woh_genehmigte_u_fertiggestellte_wohnungen|
|Produktion im Baugewerbe|tile_1667890765659|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667890765659|
|Neue Hypothekenverträge|tile_1667817211258|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667817211258|
|Bereinigte kassenmäßige Steuereinnahmen aus Gemeinschaft-, Bundes- und Landessteuern|data_einnahmen_gemeinschaft_bundes_landessteuern|www.dashboard-deutschland.de/api/tile/indicators?ids=data_einnahmen_gemeinschaft_bundes_landessteuern|
|Wechselkurs US-Dollar/Euro|tile_1667217389888|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667217389888|
|Benzinpreise im EU-Vergleich|tile_1663664545105|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1663664545105|
|Wohngebäude nach Baujahr und Energieträger der Heizung in Thüringen|tile_1669199838683|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669199838683|
|Außenhandel nach VGR-Konzept|tile_1667821569597|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667821569597|
|Bonitätschecks von Wohnungssuchenden|tile_1667995046610|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667995046610|
|Umsatz in Branchen des Verarbeitenden Gewerbes|data_umsatz_ausgewaehlte_branchen|www.dashboard-deutschland.de/api/tile/indicators?ids=data_umsatz_ausgewaehlte_branchen|
|Absatz von Warengruppen im Lebensmitteleinzelhandel|tile_1667821076015|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667821076015|
|Entwicklung des deutschen Arbeitsmarktes anhand der LinkedIn Hiring Rate|tile_1673880739519|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1673880739519|
|Strompreis|data_preise_strom|www.dashboard-deutschland.de/api/tile/indicators?ids=data_preise_strom|
|Passantenfrequenzen: Veränderung in ausgewählten Großstädten|data_mobilitaet_hystreet|www.dashboard-deutschland.de/api/tile/indicators?ids=data_mobilitaet_hystreet|
|Covid-19-Hospitalisierungen|defacto_ges_diag_covid19_hospitalizationincidence_map_de|www.dashboard-deutschland.de/api/tile/indicators?ids=defacto_ges_diag_covid19_hospitalizationincidence_map_de|
|Umsatz im Ausbaugewerbe|tile_1654070793733|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1654070793733|
|Anteil des Einkommens, den Miethaushalte für eine warme Wohnung (einschl. Strom) ausgeben, nach Haushaltsgröße und Ländern|tile_1669367676459|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669367676459|
|Füllstand deutscher Erdgasspeicher|tile_1667227714015|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667227714015|
|Energieverbrauch der Industrie nach Energieträgern|tile_1654002609295|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1654002609295|
|Tischreservierungen über OpenTable|tile_1667208064878|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667208064878|
|Verbraucherpreisindex für Nettokaltmiete, Wohnungsnebenkosten und Haushaltsenergie|data_woh_bruttokaltmiete|www.dashboard-deutschland.de/api/tile/indicators?ids=data_woh_bruttokaltmiete|
|Wohngebäude nach Gebäudegröße und Energieträger der Heizung in Rheinland-Pfalz|tile_1669293977917|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669293977917|
|Verschuldung des Bundeshaushalts inklusive Darlehensfinanzierung nach Restlaufzeiten|tile_1650978274644|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1650978274644|
|Wohngebäude nach Gebäudegröße und Energieträger der Heizung in Bayern|tile_1669283059085|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669283059085|
|Pegelstände am Rhein|tile_1666960227357|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1666960227357|
|Preisentwicklung für Energie (Strom, Gas und andere Brennstoffe) im EU-Vergleich|tile_1663666887687|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1663666887687|
|Kassenmäßige Steuereinnahmen aus Gemeindesteuern|data_gemeindesteuern|www.dashboard-deutschland.de/api/tile/indicators?ids=data_gemeindesteuern|
|Umsatz im Gastgewerbe|tile_1667810908930|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667810908930|
|Ölpreis (Sorte Brent)|tile_1667995478843|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667995478843|
|Mobilitätsindikatoren auf Grundlage von Mobilfunkdaten|data_mobilitaet_mobilfunk|www.dashboard-deutschland.de/api/tile/indicators?ids=data_mobilitaet_mobilfunk|
|Importe und Exporte von Wasserstoff|tile_1654002158461|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1654002158461|
|Umsatz im Bauhauptgewerbe|tile_1654068021178|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1654068021178|
|Auftragseingang im Bauhauptgewerbe|data_bau_auftragseingang|www.dashboard-deutschland.de/api/tile/indicators?ids=data_bau_auftragseingang|
|Wohngebäude nach Baujahr und Energieträger der Heizung in Schleswig-Holstein|tile_1669199670270|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669199670270|
|Fertiggestellte Neubauten nach überwiegend verwendeter Heizenergie|tile_1654000747086|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1654000747086|
|Renditen Bundeswertpapiere|data_umlaufrenditen_bundesanleihen|www.dashboard-deutschland.de/api/tile/indicators?ids=data_umlaufrenditen_bundesanleihen|
|Energieverbrauch für Wohnen nach Anwendungsbereichen|tile_1651060108903|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1651060108903|
|Gesamtzahl der Covid-19-Impfungen|ginsy_ges_impfung_covid19_gesamtzahl_de|www.dashboard-deutschland.de/api/tile/indicators?ids=ginsy_ges_impfung_covid19_gesamtzahl_de|
|Umsatz mit Motorenkraftstoffen an Tankstellen|tile_1663667870377|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1663667870377|
|Kapazitätsauslastung im Baugewerbe|data_bau_kapazitaetsauslastung_bbsr|www.dashboard-deutschland.de/api/tile/indicators?ids=data_bau_kapazitaetsauslastung_bbsr|
|Wohngebäude nach Baujahr und Energieträger der Heizung im Saarland|tile_1669197166529|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669197166529|
|Wohngebäude nach Baujahr und Energieträger der Heizung in Sachsen|tile_1669199369233|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669199369233|
|Kreditvergaben und Online-Transaktionen|tile_1667978809506|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667978809506|
|Verschuldung der größten Sondervermögen des Bundes|tile_1650977632272|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1650977632272|
|Wohngebäude nach Baujahr und Energieträger der Heizung in Berlin|tile_1669122207624|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669122207624|
|Stromverbrauch|tile_1667214343714|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667214343714|
|Außenhandelsbilanz|data_aussenhandelsbilanz|www.dashboard-deutschland.de/api/tile/indicators?ids=data_aussenhandelsbilanz|
|Blitzumfragen im Maschinen- und Anlagenbau|data_vdma_blitzumfragen|www.dashboard-deutschland.de/api/tile/indicators?ids=data_vdma_blitzumfragen|
|Wöchentlicher Aktivitätsindex|tile_1667211885741|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667211885741|
|Wohngebäude nach Gebäudegröße und Energieträger der Heizung im Saarland|tile_1669294221255|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669294221255|
|Wohngebäude nach Gebäudegröße und Energieträger der Heizung in Hessen|tile_1669290807065|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669290807065|
|Wohnfläche in genehmigten Neubauwohnungen|data_woh_baugenehmigungen_wohnflaeche|www.dashboard-deutschland.de/api/tile/indicators?ids=data_woh_baugenehmigungen_wohnflaeche|
|Umlaufrenditen Staats- und Unternehmensanleihen|data_staats_und_unt_anleihen|www.dashboard-deutschland.de/api/tile/indicators?ids=data_staats_und_unt_anleihen|
|DIW Konjunkturbarometer|tile_1666961011248|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1666961011248|
|Anteil des Einkommens, den Miethaushalte für eine warme Wohnung (einschl. Strom) ausgeben, nach Haushaltsgröße|tile_1669366140497|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669366140497|
|Gold- und Kupferpreis|data_preise_gold_kupfer|www.dashboard-deutschland.de/api/tile/indicators?ids=data_preise_gold_kupfer|
|Krankenhauskapazitäten|ginsy_ges_infra_ausst_intensivbetten_de|www.dashboard-deutschland.de/api/tile/indicators?ids=ginsy_ges_infra_ausst_intensivbetten_de|
|ifo Knappheitsindikator|tile_1667289768923|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667289768923|
|Einzelhandelsumsatz|tile_1667460685909|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667460685909|
|Covid-19-Impfstatus|ginsy_ges_impfung_covid19_impfstatus_map_de|www.dashboard-deutschland.de/api/tile/indicators?ids=ginsy_ges_impfung_covid19_impfstatus_map_de|
|Baltic Dry Index|tile_1666960424161|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1666960424161|
|Energieverbrauch für Wohnen nach Energieträgern|data_woh_energieverbrauch_energietraeger|www.dashboard-deutschland.de/api/tile/indicators?ids=data_woh_energieverbrauch_energietraeger|
|Kurzarbeit|data_ba_kurzarbeit|www.dashboard-deutschland.de/api/tile/indicators?ids=data_ba_kurzarbeit|
|Wohngebäude nach Baujahr und Energieträger der Heizung in Niedersachsen|tile_1669196133752|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669196133752|
|Ausgewählte Erdgaslieferungen nach Deutschland|tile_1667993866759|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667993866759|
|Flugverkehr Deutschland|tile_1667987544456|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667987544456|
|Wohngebäude nach Baujahr und Energieträger der Heizung in Deutschland|tile_1669120080204|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669120080204|
|ZEW Konjunkturausblick|tile_1667228531297|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667228531297|
|Wohngebäude nach Baujahr und Energieträger der Heizung in Baden-Württemberg|tile_1669121170132|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669121170132|
|Kassenmäßige Steuereinnahmen aus Gemeinschaft-, Bundes- und Landessteuern|data_gemeinschaft_bundes_landessteuern|www.dashboard-deutschland.de/api/tile/indicators?ids=data_gemeinschaft_bundes_landessteuern|
|7-Tage-Inzidenz|ginsy_ges_diag_covid19_7_tage_inzidenz_map_de|www.dashboard-deutschland.de/api/tile/indicators?ids=ginsy_ges_diag_covid19_7_tage_inzidenz_map_de|
|Dienstleistungsproduktion|tile_1667825347006|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667825347006|
|Anzahl der genehmigten Wohnungen nach Bauherr|data_woh_baugenehmigungen_bautraeger|www.dashboard-deutschland.de/api/tile/indicators?ids=data_woh_baugenehmigungen_bautraeger|
|Weltmarktpreise für Weizen|tile_1654606920834|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1654606920834|
|Flugverkehr weltweit|tile_1667989324139|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667989324139|
|Wohngebäude nach Baujahr und Energieträger der Heizung in Hessen|tile_1669189535447|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669189535447|
|Wohngebäude nach Baujahr und Energieträger der Heizung in Rheinland-Pfalz|tile_1669196505323|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669196505323|
|Produktion im Produzierenden Gewerbe|tile_1667824915093|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667824915093|
|Wohngebäude nach Gebäudegröße und Energieträger der Heizung in Brandenburg|tile_1669284915997|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669284915997|
|Relative Sterbefallzahlen in Deutschland im Vergleich|ginsy_ges_bev_sterbl_rel_sterbl_map_de|www.dashboard-deutschland.de/api/tile/indicators?ids=ginsy_ges_bev_sterbl_rel_sterbl_map_de|
|Automobilindustrie|tile_1666960710868|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1666960710868|
|Verbrauch von Mineralölprodukten in Deutschland|tile_1663665588691|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1663665588691|
|Wohngebäude nach Gebäudegröße und Energieträger der Heizung in Sachsen|tile_1669295737260|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669295737260|
|Verschuldung des Bundeshaushalts und seiner Sondervermögen|tile_1650978797816|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1650978797816|
|Nettostromerzeugung|tile_1666961555651|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1666961555651|
|Covid-19-Fälle|ginsy_ges_diag_covid19_faelle_de|www.dashboard-deutschland.de/api/tile/indicators?ids=ginsy_ges_diag_covid19_faelle_de|
|Preisindex für Ein- und Zweifamilienhäuser nach Kreistypen|data_woh_preise_immobilien_hpi_haueser|www.dashboard-deutschland.de/api/tile/indicators?ids=data_woh_preise_immobilien_hpi_haueser|
|Renditespreads 10-jähriger Staatsanleihen gegenüber Deutschland|data_zinsspread_10_j_anleihen|www.dashboard-deutschland.de/api/tile/indicators?ids=data_zinsspread_10_j_anleihen|
|Aktienindizes|tile_1667210963256|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667210963256|
|Wohngebäude nach Gebäudegröße und Energieträger der Heizung in Baden-Württemberg|tile_1669209397487|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669209397487|
|Arbeitslosigkeit und offene Stellen|tile_1666958835081|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1666958835081|
|Umsatz mit Maßnahmen zur Verbesserung der Energieeffizienz von Gebäuden|tile_1665656599909|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1665656599909|
|Wohngebäude nach Gebäudegröße und Energieträger der Heizung in Deutschland|tile_1669192154976|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669192154976|
|Durchschnittliche Wohnkosten für Hauptmiethaushalte je Wohnung nach Haushaltsgröße|tile_1669368695741|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669368695741|
|Stimmungsindikatoren Arbeitsmarkt|data_iab_ifo_barometer|www.dashboard-deutschland.de/api/tile/indicators?ids=data_iab_ifo_barometer|
|Wohngebäude nach Gebäudegröße und Energieträger der Heizung in Niedersachsen|tile_1669291473838|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669291473838|
|Exporterwartungen und Containerumschlag|tile_1666962783823|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1666962783823|
|Wohngebäude nach Gebäudegröße und Energieträger der Heizung in Sachsen-Anhalt|tile_1669295963925|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669295963925|
|Entwicklung des deutschen Arbeitsmarktes anhand von Stellenausschreibungen auf Indeed|tile_1666961477511|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1666961477511|
|Wohngebäude nach Gebäudegröße und Energieträger der Heizung in Thüringen|tile_1669296388975|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669296388975|
|Wohngebäude nach Baujahr und Energieträger der Heizung in Bremen|tile_1669189080637|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669189080637|
|Wohngebäude nach Gebäudegröße und Energieträger der Heizung in Berlin|tile_1669284482727|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669284482727|
|Wohngebäude nach Baujahr und Energieträger der Heizung in Brandenburg|tile_1669128138583|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669128138583|
|Preisindex für Eigentumswohnungen nach Kreistypen|data_woh_preise_immobilien_hpi_wohnungen|www.dashboard-deutschland.de/api/tile/indicators?ids=data_woh_preise_immobilien_hpi_wohnungen|
|Anteil der Grünen Bundeswertpapiere an der Verschuldung des Bundes inklusive Darlehensfinanzierung|tile_1650979109395|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1650979109395|
|Lkw-Maut-Fahrleistungsindex|tile_1667205800085|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667205800085|
|Wohngebäude nach Heizungsart|tile_1669108022095|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669108022095|
|Importe fossiler Energieträger|tile_1654001211812|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1654001211812|
|Wohngebäude nach Baujahr und Energieträger der Heizung in Hamburg|tile_1669189367122|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669189367122|
|Wohngebäude nach Baujahr und Energieträger der Heizung in Mecklenburg-Vorpommern|tile_1669189699623|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669189699623|
|Energiepreisentwicklung|tile_1667826504852|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667826504852|
|Wohngebäude nach Gebäudegröße und Energieträger der Heizung in Mecklenburg-Vorpommern|tile_1669291142943|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669291142943|
|Wohngebäude nach Baujahr und Energieträger der Heizung in Bayern|tile_1669121404231|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669121404231|




## Geojson

**URL:** www.dashboard-deutschland.de/geojson/de-all.geo.json
	
Die API ermöglicht Zugriff auf Geojson-Daten zu Deutschland und den Ländern (00-DE_admin1_400).


## Beispiel

```bash
indicators=$(curl -m 60 'https://www.dashboard-deutschland.de/api/tile/indicators?ids=data_adv_flugverkehr;data_aussenhandel;data_ba_arbeitslose_und_stellen;data_bruttoinlandsprodukt;data_corona_zuschuesse;data_einnahmen_gemeinschaft_bundes_landessteuern;data_ifo_geschaeftsklima;data_kfw_sondermassnahme_neu;data_preisentwicklung;data_umsatz_ausgewaehlte_branchen;defacto_ges_diag_covid19_hospitalizationincidence_map_de;ginsy_ges_bev_sterbl_abs_sterbl_de;ginsy_ges_diag_covid19_7_tage_inzidenz_map_de;tile_1648135639982
')
```
