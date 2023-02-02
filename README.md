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
|tile_1667993866759|Ausgewählte Erdgaslieferungen nach Deutschland|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667993866759|
|data_bau_bauleistungspreise|Baupreisindizes|www.dashboard-deutschland.de/api/tile/indicators?ids=data_bau_bauleistungspreise|
|tile_1667211885741|Wöchentlicher Aktivitätsindex|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667211885741|
|tile_1667288019608|ifo Geschäftsklima|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667288019608|
|tile_1663664931250|Exporte und Importe von Wärmepumpen und Photovoltaikanlagen|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1663664931250|
|data_mobilitaet_mobilfunk|Mobilitätsindikatoren auf Grundlage von Mobilfunkdaten|www.dashboard-deutschland.de/api/tile/indicators?ids=data_mobilitaet_mobilfunk|
|tile_1667226778807|Täglicher LKW-Maut-Fahrleistungsindex|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667226778807|
|tile_1667989324139|Flugverkehr weltweit|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667989324139|
|data_woh_energieverbrauch_energietraeger|Energieverbrauch für Wohnen nach Energieträgern|www.dashboard-deutschland.de/api/tile/indicators?ids=data_woh_energieverbrauch_energietraeger|
|tile_1666960227357|Pegelstände am Rhein|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1666960227357|
|tile_1667826504852|Energiepreisentwicklung|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667826504852|
|ginsy_ges_infra_ausst_intensivbetten_de|Krankenhauskapazitäten|www.dashboard-deutschland.de/api/tile/indicators?ids=ginsy_ges_infra_ausst_intensivbetten_de|
|tile_1666960710868|Automobilindustrie|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1666960710868|
|tile_1666961555651|Nettostromerzeugung|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1666961555651|
|tile_1663664545105|Benzinpreise im EU-Vergleich|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1663664545105|
|tile_1666958835081|Arbeitslosigkeit und offene Stellen|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1666958835081|
|tile_1654000747086|Fertiggestellte Neubauten nach überwiegend verwendeter Heizenergie|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1654000747086|
|tile_1669192154976|Wohngebäude nach Gebäudegröße und Energieträger der Heizung in Deutschland|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669192154976|
|tile_1667817211258|Neue Hypothekenverträge|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667817211258|
|tile_1663665904253|Nettonennleistung der Anlagen zur Elektrizitätserzeugung|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1663665904253|
|tile_1669284915997|Wohngebäude nach Gebäudegröße und Energieträger der Heizung in Brandenburg|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669284915997|
|data_woh_nettokaltmiete|Verbraucherpreisindex für Nettokaltmiete nach Kreistypen|www.dashboard-deutschland.de/api/tile/indicators?ids=data_woh_nettokaltmiete|
|tile_1667217389888|Wechselkurs US-Dollar/Euro|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667217389888|
|tile_1667987544456|Flugverkehr Deutschland|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667987544456|
|tile_1667995046610|Bonitätschecks von Wohnungssuchenden|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667995046610|
|tile_1669296178221|Wohngebäude nach Gebäudegröße und Energieträger der Heizung in Schleswig-Holstein|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669296178221|
|data_woh_bruttokaltmiete|Verbraucherpreisindex für Nettokaltmiete, Wohnungsnebenkosten und Haushaltsenergie|www.dashboard-deutschland.de/api/tile/indicators?ids=data_woh_bruttokaltmiete|
|data_auftragseingang_ausgewaehlte_branchen|Auftragseingang in Branchen des Verarbeitenden Gewerbes|www.dashboard-deutschland.de/api/tile/indicators?ids=data_auftragseingang_ausgewaehlte_branchen|
|data_gemeindesteuern|Kassenmäßige Steuereinnahmen aus Gemeindesteuern|www.dashboard-deutschland.de/api/tile/indicators?ids=data_gemeindesteuern|
|tile_1667830902757|Außenhandel|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667830902757|
|tile_1667890765659|Produktion im Baugewerbe|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667890765659|
|tile_1667921381760|Kraftstoffpreise an öffentlichen Tankstellen|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667921381760|
|tile_1666962783823|Exporterwartungen und Containerumschlag|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1666962783823|
|tile_1667215458776|HWWI-Rohstoffpreisindex|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667215458776|
|data_vdma_blitzumfragen|Blitzumfragen im Maschinen- und Anlagenbau|www.dashboard-deutschland.de/api/tile/indicators?ids=data_vdma_blitzumfragen|
|tile_1654070793733|Umsatz im Ausbaugewerbe|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1654070793733|
|data_woh_preise_immobilien_hpi_wohnungen|Preisindex für Eigentumswohnungen nach Kreistypen|www.dashboard-deutschland.de/api/tile/indicators?ids=data_woh_preise_immobilien_hpi_wohnungen|
|defacto_ges_diag_covid19_hospitalizationincidence_map_de|Covid-19-Hospitalisierungen|www.dashboard-deutschland.de/api/tile/indicators?ids=defacto_ges_diag_covid19_hospitalizationincidence_map_de|
|tile_1650978797816|Verschuldung des Bundeshaushalts und seiner Sondervermögen|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1650978797816|
|ginsy_ges_bev_sterbl_abs_sterbl_de|Wöchentliche Sterbefallzahlen in Deutschland|www.dashboard-deutschland.de/api/tile/indicators?ids=ginsy_ges_bev_sterbl_abs_sterbl_de|
|tile_1667214343714|Stromverbrauch|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667214343714|
|data_preise_gold_kupfer|Gold- und Kupferpreis|www.dashboard-deutschland.de/api/tile/indicators?ids=data_preise_gold_kupfer|
|tile_1669108022095|Wohngebäude nach Heizungsart|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669108022095|
|tile_1669285361958|Wohngebäude nach Gebäudegröße und Energieträger der Heizung in Bremen|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669285361958|
|tile_1669293977917|Wohngebäude nach Gebäudegröße und Energieträger der Heizung in Rheinland-Pfalz|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669293977917|
|tile_1666960424161|Baltic Dry Index|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1666960424161|
|data_ba_kurzarbeit|Kurzarbeit|www.dashboard-deutschland.de/api/tile/indicators?ids=data_ba_kurzarbeit|
|tile_1667289768923|ifo Knappheitsindikator|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667289768923|
|tile_1667289137702|ifo Produktionserwartungen|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667289137702|
|ginsy_ges_diag_covid19_7_tage_inzidenz_map_de|7-Tage-Inzidenz|www.dashboard-deutschland.de/api/tile/indicators?ids=ginsy_ges_diag_covid19_7_tage_inzidenz_map_de|
|ginsy_ges_bev_sterbl_rel_sterbl_map_de|Relative Sterbefallzahlen in Deutschland im Vergleich|www.dashboard-deutschland.de/api/tile/indicators?ids=ginsy_ges_bev_sterbl_rel_sterbl_map_de|
|tile_1669284482727|Wohngebäude nach Gebäudegröße und Energieträger der Heizung in Berlin|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669284482727|
|tile_1666961011248|DIW Konjunkturbarometer|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1666961011248|
|tile_1669196133752|Wohngebäude nach Baujahr und Energieträger der Heizung in Niedersachsen|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669196133752|
|data_gemeinschaft_bundes_landessteuern|Kassenmäßige Steuereinnahmen aus Gemeinschaft-, Bundes- und Landessteuern|www.dashboard-deutschland.de/api/tile/indicators?ids=data_gemeinschaft_bundes_landessteuern|
|tile_1669189367122|Wohngebäude nach Baujahr und Energieträger der Heizung in Hamburg|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669189367122|
|tile_1667810908930|Umsatz im Gastgewerbe|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667810908930|
|tile_1667811574092|Entwicklung des Bruttoinlandsprodukts|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667811574092|
|ginsy_ges_impfung_covid19_impfstatus_map_de|Covid-19-Impfstatus|www.dashboard-deutschland.de/api/tile/indicators?ids=ginsy_ges_impfung_covid19_impfstatus_map_de|
|data_preise_strom|Strompreis|www.dashboard-deutschland.de/api/tile/indicators?ids=data_preise_strom|
|tile_1669196285543|Wohngebäude nach Baujahr und Energieträger der Heizung in Nordrhein-Westfalen|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669196285543|
|tile_1668694599167|Preisentwicklung|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1668694599167|
|data_steuereinnahmen_bund_laender|Kassenmäßige Steuereinnahmen von Bund und Ländern|www.dashboard-deutschland.de/api/tile/indicators?ids=data_steuereinnahmen_bund_laender|
|tile_1650979109395|Anteil der Grünen Bundeswertpapiere an der Verschuldung des Bundes inklusive Darlehensfinanzierung|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1650979109395|
|tile_1669368380310|Durchschnittliche Wohnkosten für Hauptmiethaushalte je Quadratmeter nach Haushaltsgröße|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669368380310|
|tile_1669209397487|Wohngebäude nach Gebäudegröße und Energieträger der Heizung in Baden-Württemberg|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669209397487|
|tile_1663667563512|Produktion von Solarkollektoren, Solarmodulen und Wärmepumpen|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1663667563512|
|tile_1669296388975|Wohngebäude nach Gebäudegröße und Energieträger der Heizung in Thüringen|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669296388975|
|tile_1667227714015|Füllstand deutscher Erdgasspeicher|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667227714015|
|tile_1669290437600|Wohngebäude nach Gebäudegröße und Energieträger der Heizung in Hamburg|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669290437600|
|tile_1667832713510|Außenhandel mit ausgewählten Ländern|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667832713510|
|tile_1667822587333|Erwerbstätigkeit|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667822587333|
|data_umsatz_ausgewaehlte_branchen|Umsatz in Branchen des Verarbeitenden Gewerbes|www.dashboard-deutschland.de/api/tile/indicators?ids=data_umsatz_ausgewaehlte_branchen|
|data_zinsspread_10_j_anleihen|Renditespreads 10-jähriger Staatsanleihen gegenüber Deutschland|www.dashboard-deutschland.de/api/tile/indicators?ids=data_zinsspread_10_j_anleihen|
|tile_1667460685909|Einzelhandelsumsatz|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667460685909|
|tile_1663665588691|Verbrauch von Mineralölprodukten in Deutschland|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1663665588691|
|tile_1669121170132|Wohngebäude nach Baujahr und Energieträger der Heizung in Baden-Württemberg|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669121170132|
|tile_1669199513126|Wohngebäude nach Baujahr und Energieträger der Heizung in Sachsen-Anhalt|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669199513126|
|tile_1669291731814|Wohngebäude nach Gebäudegröße und Energieträger der Heizung in Nordrhein-Westfalen|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669291731814|
|tile_1669189699623|Wohngebäude nach Baujahr und Energieträger der Heizung in Mecklenburg-Vorpommern|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669189699623|
|tile_1667982573430|Passantenfrequenzindex|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667982573430|
|ginsy_ges_impfung_covid19_gesamtzahl_de|Gesamtzahl der Covid-19-Impfungen|www.dashboard-deutschland.de/api/tile/indicators?ids=ginsy_ges_impfung_covid19_gesamtzahl_de|
|tile_1669291473838|Wohngebäude nach Gebäudegröße und Energieträger der Heizung in Niedersachsen|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669291473838|
|tile_1669366140497|Anteil des Einkommens, den Miethaushalte für eine warme Wohnung (einschl. Strom) ausgeben, nach Haushaltsgröße|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669366140497|
|tile_1669199369233|Wohngebäude nach Baujahr und Energieträger der Heizung in Sachsen|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669199369233|
|tile_1667824915093|Produktion im Produzierenden Gewerbe|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667824915093|
|data_einnahmen_gemeinschaft_bundes_landessteuern|Bereinigte kassenmäßige Steuereinnahmen aus Gemeinschaft-, Bundes- und Landessteuern|www.dashboard-deutschland.de/api/tile/indicators?ids=data_einnahmen_gemeinschaft_bundes_landessteuern|
|tile_1667825347006|Dienstleistungsproduktion|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667825347006|
|tile_1669368695741|Durchschnittliche Wohnkosten für Hauptmiethaushalte je Wohnung nach Haushaltsgröße|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669368695741|
|tile_1667978809506|Kreditvergaben und Online-Transaktionen|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667978809506|
|tile_1650978274644|Verschuldung des Bundeshaushalts inklusive Darlehensfinanzierung nach Restlaufzeiten|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1650978274644|
|tile_1669199670270|Wohngebäude nach Baujahr und Energieträger der Heizung in Schleswig-Holstein|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669199670270|
|tile_1667205800085|Lkw-Maut-Fahrleistungsindex|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667205800085|
|tile_1653306303133|Ausgewählte Erdgaslieferungen nach Deutschland|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1653306303133|
|tile_1669189535447|Wohngebäude nach Baujahr und Energieträger der Heizung in Hessen|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669189535447|
|data_mobilitaet_mobilfunk_karte|Tägliche Veränderung der Mobilität auf Kreisebene auf Grundlage von Mobilfunkdaten|www.dashboard-deutschland.de/api/tile/indicators?ids=data_mobilitaet_mobilfunk_karte|
|tile_1667828804581|Umsatz im Verarbeitenden Gewerbe|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667828804581|
|data_aussenhandelsbilanz|Außenhandelsbilanz|www.dashboard-deutschland.de/api/tile/indicators?ids=data_aussenhandelsbilanz|
|data_umlaufrenditen_bundesanleihen|Renditen Bundeswertpapiere|www.dashboard-deutschland.de/api/tile/indicators?ids=data_umlaufrenditen_bundesanleihen|
|tile_1669120080204|Wohngebäude nach Baujahr und Energieträger der Heizung in Deutschland|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669120080204|
|tile_1654068021178|Umsatz im Bauhauptgewerbe|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1654068021178|
|tile_1669189080637|Wohngebäude nach Baujahr und Energieträger der Heizung in Bremen|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669189080637|
|tile_1651060108903|Energieverbrauch für Wohnen nach Anwendungsbereichen|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1651060108903|
|tile_1669199838683|Wohngebäude nach Baujahr und Energieträger der Heizung in Thüringen|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669199838683|
|tile_1669197166529|Wohngebäude nach Baujahr und Energieträger der Heizung im Saarland|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669197166529|
|data_aussenhandel_laendergruppen|Außenhandel mit ausgewählten Ländergruppen|www.dashboard-deutschland.de/api/tile/indicators?ids=data_aussenhandel_laendergruppen|
|tile_1656076602735|Preisindizes zu Bau oder Erwerb von Wohneigentum|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1656076602735|
|tile_1669196505323|Wohngebäude nach Baujahr und Energieträger der Heizung in Rheinland-Pfalz|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669196505323|
|tile_1669290807065|Wohngebäude nach Gebäudegröße und Energieträger der Heizung in Hessen|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669290807065|
|tile_1663666467966|Neuzulassungen von Personenkraftwagen nach Antriebsarten|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1663666467966|
|tile_1669295963925|Wohngebäude nach Gebäudegröße und Energieträger der Heizung in Sachsen-Anhalt|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669295963925|
|tile_1666961477511|Entwicklung des deutschen Arbeitsmarktes anhand von Stellenausschreibungen auf Indeed|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1666961477511|
|data_woh_genehmigte_u_fertiggestellte_wohnungen|Genehmigte und fertiggestellte Wohnungen|www.dashboard-deutschland.de/api/tile/indicators?ids=data_woh_genehmigte_u_fertiggestellte_wohnungen|
|tile_1667210963256|Aktienindizes|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667210963256|
|data_bau_kapazitaetsauslastung_bbsr|Kapazitätsauslastung im Baugewerbe|www.dashboard-deutschland.de/api/tile/indicators?ids=data_bau_kapazitaetsauslastung_bbsr|
|tile_1665656599909|Umsatz mit Maßnahmen zur Verbesserung der Energieeffizienz von Gebäuden|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1665656599909|
|tile_1669367676459|Anteil des Einkommens, den Miethaushalte für eine warme Wohnung (einschl. Strom) ausgeben, nach Haushaltsgröße und Ländern|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669367676459|
|tile_1667308898055|Preisentwicklung für ausgewählte Baumaterialien|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667308898055|
|tile_1663665272454|Genehmigte neu zu errichtende Wohngebäude mit ein und zwei Wohnungen nach überwiegend verwendeter Heizenergie|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1663665272454|
|tile_1667982123933|S&P Global/BME Einkaufsmanagerindex|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667982123933|
|data_steuereinnahmen_insgesamt_gemeinden|Kassenmäßige Steuereinnahmen insgesamt und der Gemeinden/Gemeindeverbände|www.dashboard-deutschland.de/api/tile/indicators?ids=data_steuereinnahmen_insgesamt_gemeinden|
|tile_1669121404231|Wohngebäude nach Baujahr und Energieträger der Heizung in Bayern|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669121404231|
|tile_1650977632272|Verschuldung der größten Sondervermögen des Bundes|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1650977632272|
|data_staats_und_unt_anleihen|Umlaufrenditen Staats- und Unternehmensanleihen|www.dashboard-deutschland.de/api/tile/indicators?ids=data_staats_und_unt_anleihen|
|tile_1667814729862|Entwicklung ausgewählter Aggregate des Bruttoinlandsprodukts|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667814729862|
|tile_1667821076015|Absatz von Warengruppen im Lebensmitteleinzelhandel|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667821076015|
|tile_1663666887687|Preisentwicklung für Energie (Strom, Gas und andere Brennstoffe) im EU-Vergleich|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1663666887687|
|data_woh_preise_immobilien_hpi_haueser|Preisindex für Ein- und Zweifamilienhäuser nach Kreistypen|www.dashboard-deutschland.de/api/tile/indicators?ids=data_woh_preise_immobilien_hpi_haueser|
|data_mobilitaet_hystreet|Passantenfrequenzen: Veränderung in ausgewählten Großstädten|www.dashboard-deutschland.de/api/tile/indicators?ids=data_mobilitaet_hystreet|
|tile_1667821569597|Außenhandel nach VGR-Konzept|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667821569597|
|data_bau_auftragseingang|Auftragseingang im Bauhauptgewerbe|www.dashboard-deutschland.de/api/tile/indicators?ids=data_bau_auftragseingang|
|ginsy_ges_diag_covid19_faelle_de|Covid-19-Fälle|www.dashboard-deutschland.de/api/tile/indicators?ids=ginsy_ges_diag_covid19_faelle_de|
|data_produktion_ausgewaehlte_branchen|Produktion in Branchen des Produzierenden Gewerbes|www.dashboard-deutschland.de/api/tile/indicators?ids=data_produktion_ausgewaehlte_branchen|
|data_iab_ifo_barometer|Stimmungsindikatoren Arbeitsmarkt|www.dashboard-deutschland.de/api/tile/indicators?ids=data_iab_ifo_barometer|
|tile_1673880739519|Entwicklung des deutschen Arbeitsmarktes anhand der LinkedIn Hiring Rate|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1673880739519|
|tile_1669295737260|Wohngebäude nach Gebäudegröße und Energieträger der Heizung in Sachsen|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669295737260|
|tile_1669283059085|Wohngebäude nach Gebäudegröße und Energieträger der Heizung in Bayern|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669283059085|
|tile_1667228531297|ZEW Konjunkturausblick|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667228531297|
|data_woh_baugenehmigungen_wohnungen|Anzahl genehmigter Wohnungen im Neubau nach Gebäudeart|www.dashboard-deutschland.de/api/tile/indicators?ids=data_woh_baugenehmigungen_wohnungen|
|tile_1669122207624|Wohngebäude nach Baujahr und Energieträger der Heizung in Berlin|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669122207624|
|tile_1654002609295|Energieverbrauch der Industrie nach Energieträgern|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1654002609295|
|tile_1663667870377|Umsatz mit Motorenkraftstoffen an Tankstellen|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1663667870377|
|tile_1667983271066|Stimmungsindikatoren Konsum|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667983271066|
|data_bau_beschaeftigung_vgr|Beschäftigung im Baugewerbe|www.dashboard-deutschland.de/api/tile/indicators?ids=data_bau_beschaeftigung_vgr|
|tile_1654002158461|Importe und Exporte von Wasserstoff|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1654002158461|
|tile_1654606920834|Weltmarktpreise für Weizen|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1654606920834|
|tile_1669291142943|Wohngebäude nach Gebäudegröße und Energieträger der Heizung in Mecklenburg-Vorpommern|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669291142943|
|data_woh_baugenehmigungen_bautraeger|Anzahl der genehmigten Wohnungen nach Bauherr|www.dashboard-deutschland.de/api/tile/indicators?ids=data_woh_baugenehmigungen_bautraeger|
|tile_1667995478843|Ölpreis (Sorte Brent)|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667995478843|
|tile_1669294221255|Wohngebäude nach Gebäudegröße und Energieträger der Heizung im Saarland|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669294221255|
|tile_1667828024262|Auftragseingang im Verarbeitenden Gewerbe|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667828024262|
|tile_1654001211812|Importe fossiler Energieträger|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1654001211812|
|tile_1669128138583|Wohngebäude nach Baujahr und Energieträger der Heizung in Brandenburg|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669128138583|
|ginsy_ges_diag_covid19_neuinfektionen_de|Infektionsgeschehen|www.dashboard-deutschland.de/api/tile/indicators?ids=ginsy_ges_diag_covid19_neuinfektionen_de|
|data_mobilitaet_mobilfunk_hotspot|Tägliche Mobilitätsveränderung und 7-Tage-Inzidenz auf Kreisebene auf Grundlage von Mobilfunkdaten|www.dashboard-deutschland.de/api/tile/indicators?ids=data_mobilitaet_mobilfunk_hotspot|
|tile_1667208064878|Tischreservierungen über OpenTable|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667208064878|
|data_woh_baugenehmigungen_wohnflaeche|Wohnfläche in genehmigten Neubauwohnungen|www.dashboard-deutschland.de/api/tile/indicators?ids=data_woh_baugenehmigungen_wohnflaeche|


## Geojson

**URL:** www.dashboard-deutschland.de/geojson/de-all.geo.json
	
Die API ermöglicht Zugriff auf Geojson-Daten zu Deutschland und den Ländern (00-DE_admin1_400).


## Beispiel

```bash
indicators=$(curl -m 60 'https://www.dashboard-deutschland.de/api/tile/indicators?ids=data_adv_flugverkehr;data_aussenhandel;data_ba_arbeitslose_und_stellen;data_bruttoinlandsprodukt;data_corona_zuschuesse;data_einnahmen_gemeinschaft_bundes_landessteuern;data_ifo_geschaeftsklima;data_kfw_sondermassnahme_neu;data_preisentwicklung;data_umsatz_ausgewaehlte_branchen;defacto_ges_diag_covid19_hospitalizationincidence_map_de;ginsy_ges_bev_sterbl_abs_sterbl_de;ginsy_ges_diag_covid19_7_tage_inzidenz_map_de;tile_1648135639982
')
```
