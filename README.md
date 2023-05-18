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
|Anteil des Einkommens, den Miethaushalte für eine warme Wohnung (einschl. Strom) ausgeben, nach Haushaltsgröße und Ländern|tile_1669367676459|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669367676459|
|Importe und Exporte von Wasserstoff|tile_1654002158461|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1654002158461|
|Wohngebäude nach Baujahr und Energieträger der Heizung in Hamburg|tile_1669189367122|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669189367122|
|Wohngebäude nach Gebäudegröße und Energieträger der Heizung in Schleswig-Holstein|tile_1669296178221|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669296178221|
|Entwicklung des deutschen Arbeitsmarktes anhand der LinkedIn Hiring Rate|tile_1673880739519|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1673880739519|
|Krankenhauskapazitäten|ginsy_ges_infra_ausst_intensivbetten_de|www.dashboard-deutschland.de/api/tile/indicators?ids=ginsy_ges_infra_ausst_intensivbetten_de|
|Kassenmäßige Steuereinnahmen insgesamt und der Gemeinden/Gemeindeverbände|data_steuereinnahmen_insgesamt_gemeinden|www.dashboard-deutschland.de/api/tile/indicators?ids=data_steuereinnahmen_insgesamt_gemeinden|
|Wohngebäude nach Baujahr und Energieträger der Heizung in Niedersachsen|tile_1669196133752|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669196133752|
|Verschuldung des Bundeshaushalts inklusive Darlehensfinanzierung nach Restlaufzeiten|tile_1650978274644|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1650978274644|
|Wohngebäude nach Gebäudegröße und Energieträger der Heizung in Deutschland|tile_1669192154976|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669192154976|
|Einzelhandelsumsatz|tile_1667460685909|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667460685909|
|Wohngebäude nach Gebäudegröße und Energieträger der Heizung in Berlin|tile_1669284482727|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669284482727|
|Wohngebäude nach Baujahr und Energieträger der Heizung in Bayern|tile_1669121404231|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669121404231|
|Auftragseingang im Verarbeitenden Gewerbe|tile_1667828024262|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667828024262|
|ifo Produktionserwartungen|tile_1667289137702|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667289137702|
|Ölpreis (Sorte Brent)|tile_1667995478843|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667995478843|
|Preisindex für Eigentumswohnungen nach Kreistypen|data_woh_preise_immobilien_hpi_wohnungen|www.dashboard-deutschland.de/api/tile/indicators?ids=data_woh_preise_immobilien_hpi_wohnungen|
|Fertiggestellte Neubauten nach überwiegend verwendeter Heizenergie|tile_1654000747086|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1654000747086|
|Entwicklung des Bruttoinlandsprodukts|tile_1667811574092|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667811574092|
|Wohngebäude nach Gebäudegröße und Energieträger der Heizung in Brandenburg|tile_1669284915997|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669284915997|
|Wohngebäude nach Baujahr und Energieträger der Heizung in Sachsen|tile_1669199369233|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669199369233|
|Verbraucherpreisindex für Nettokaltmiete, Wohnungsnebenkosten und Haushaltsenergie|data_woh_bruttokaltmiete|www.dashboard-deutschland.de/api/tile/indicators?ids=data_woh_bruttokaltmiete|
|Baltic Dry Index|tile_1666960424161|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1666960424161|
|Verbrauch von Mineralölprodukten in Deutschland|tile_1663665588691|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1663665588691|
|Wohngebäude nach Gebäudegröße und Energieträger der Heizung in Bayern|tile_1669283059085|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669283059085|
|Produktion im Baugewerbe|tile_1667890765659|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667890765659|
|Kapazitätsauslastung im Baugewerbe|data_bau_kapazitaetsauslastung_bbsr|www.dashboard-deutschland.de/api/tile/indicators?ids=data_bau_kapazitaetsauslastung_bbsr|
|Produktion von Solarkollektoren, Solarmodulen und Wärmepumpen|tile_1663667563512|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1663667563512|
|Energieverbrauch für Wohnen nach Anwendungsbereichen|tile_1651060108903|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1651060108903|
|Wohngebäude nach Gebäudegröße und Energieträger der Heizung in Nordrhein-Westfalen|tile_1669291731814|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669291731814|
|Umsatz mit Motorenkraftstoffen an Tankstellen|tile_1663667870377|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1663667870377|
|Entwicklung ausgewählter Aggregate des Bruttoinlandsprodukts|tile_1667814729862|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667814729862|
|Baupreisindizes|data_bau_bauleistungspreise|www.dashboard-deutschland.de/api/tile/indicators?ids=data_bau_bauleistungspreise|
|Kassenmäßige Steuereinnahmen aus Gemeinschaft-, Bundes- und Landessteuern|data_gemeinschaft_bundes_landessteuern|www.dashboard-deutschland.de/api/tile/indicators?ids=data_gemeinschaft_bundes_landessteuern|
|Kassenmäßige Steuereinnahmen von Bund und Ländern|data_steuereinnahmen_bund_laender|www.dashboard-deutschland.de/api/tile/indicators?ids=data_steuereinnahmen_bund_laender|
|Weltmarktpreise für Weizen|tile_1654606920834|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1654606920834|
|Stimmungsindikatoren Arbeitsmarkt|data_iab_ifo_barometer|www.dashboard-deutschland.de/api/tile/indicators?ids=data_iab_ifo_barometer|
|Exporterwartungen und Containerumschlag|tile_1666962783823|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1666962783823|
|Außenhandel mit ausgewählten Ländergruppen|data_aussenhandel_laendergruppen|www.dashboard-deutschland.de/api/tile/indicators?ids=data_aussenhandel_laendergruppen|
|Tischreservierungen über OpenTable|tile_1667208064878|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667208064878|
|Wohngebäude nach Baujahr und Energieträger der Heizung in Nordrhein-Westfalen|tile_1669196285543|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669196285543|
|Energieverbrauch für Wohnen nach Energieträgern|data_woh_energieverbrauch_energietraeger|www.dashboard-deutschland.de/api/tile/indicators?ids=data_woh_energieverbrauch_energietraeger|
|Wohngebäude nach Gebäudegröße und Energieträger der Heizung in Bremen|tile_1669285361958|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669285361958|
|Verschuldung des Bundeshaushalts und seiner Sondervermögen|tile_1650978797816|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1650978797816|
|Aufkommen und Verwendung von Wasserstoff|tile_1663663630535|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1663663630535|
|HWWI-Rohstoffpreisindex|tile_1667215458776|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667215458776|
|Preisveränderung|tile_1668694599167|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1668694599167|
|Strompreis|data_preise_strom|www.dashboard-deutschland.de/api/tile/indicators?ids=data_preise_strom|
|Wohngebäude nach Baujahr und Energieträger der Heizung in Bremen|tile_1669189080637|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669189080637|
|Wohngebäude nach Baujahr und Energieträger der Heizung in Brandenburg|tile_1669128138583|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669128138583|
|Kraftstoffpreise an öffentlichen Tankstellen|tile_1667921381760|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667921381760|
|Umsatz im Gastgewerbe|tile_1667810908930|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667810908930|
|Aktienindizes|tile_1667210963256|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667210963256|
|Wohngebäude nach Gebäudegröße und Energieträger der Heizung in Niedersachsen|tile_1669291473838|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669291473838|
|Wohngebäude nach Gebäudegröße und Energieträger der Heizung im Saarland|tile_1669294221255|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669294221255|
|Wohngebäude nach Gebäudegröße und Energieträger der Heizung in Hessen|tile_1669290807065|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669290807065|
|Importe fossiler Energieträger|tile_1654001211812|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1654001211812|
|Energieverbrauch der Industrie nach Energieträgern|tile_1654002609295|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1654002609295|
|Beschäftigung im Baugewerbe|data_bau_beschaeftigung_vgr|www.dashboard-deutschland.de/api/tile/indicators?ids=data_bau_beschaeftigung_vgr|
|DIW Konjunkturbarometer|tile_1666961011248|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1666961011248|
|Stromverbrauch|tile_1667214343714|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667214343714|
|Exporte und Importe von Wärmepumpen und Photovoltaikanlagen|tile_1663664931250|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1663664931250|
|Wohngebäude nach Baujahr und Energieträger der Heizung in Rheinland-Pfalz|tile_1669196505323|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669196505323|
|Wohngebäude nach Gebäudegröße und Energieträger der Heizung in Hamburg|tile_1669290437600|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669290437600|
|Preisentwicklung für ausgewählte Baumaterialien|tile_1667308898055|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667308898055|
|Produktion im Produzierenden Gewerbe|tile_1667824915093|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667824915093|
|Preisentwicklung für Energie (Strom, Gas und andere Brennstoffe) im EU-Vergleich|tile_1663666887687|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1663666887687|
|Anzahl genehmigter Wohnungen im Neubau nach Gebäudeart|data_woh_baugenehmigungen_wohnungen|www.dashboard-deutschland.de/api/tile/indicators?ids=data_woh_baugenehmigungen_wohnungen|
|Anteil der Grünen Bundeswertpapiere an der Verschuldung des Bundes inklusive Darlehensfinanzierung|tile_1650979109395|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1650979109395|
|Umsatz im Verarbeitenden Gewerbe|tile_1667828804581|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667828804581|
|Neuzulassungen von Personenkraftwagen nach Antriebsarten|tile_1663666467966|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1663666467966|
|Wohngebäude nach Gebäudegröße und Energieträger der Heizung in Sachsen|tile_1669295737260|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669295737260|
|Wohngebäude nach Baujahr und Energieträger der Heizung in Baden-Württemberg|tile_1669121170132|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669121170132|
|Wohngebäude nach Baujahr und Energieträger der Heizung im Saarland|tile_1669197166529|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669197166529|
|ifo Geschäftsklima|tile_1667288019608|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667288019608|
|Außenhandelsbilanz|data_aussenhandelsbilanz|www.dashboard-deutschland.de/api/tile/indicators?ids=data_aussenhandelsbilanz|
|Genehmigte und fertiggestellte Wohnungen|tile_1678111428688|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1678111428688|
|Wohngebäude nach Baujahr und Energieträger der Heizung in Deutschland|tile_1669120080204|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669120080204|
|Wohngebäude nach Baujahr und Energieträger der Heizung in Hessen|tile_1669189535447|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669189535447|
|Produktion in Branchen des Produzierenden Gewerbes|data_produktion_ausgewaehlte_branchen|www.dashboard-deutschland.de/api/tile/indicators?ids=data_produktion_ausgewaehlte_branchen|
|Wohngebäude nach Gebäudegröße und Energieträger der Heizung in Sachsen-Anhalt|tile_1669295963925|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669295963925|
|Lkw-Maut-Fahrleistungsindex|tile_1667205800085|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667205800085|
|Anzahl der genehmigten Wohnungen nach Bauherr|data_woh_baugenehmigungen_bautraeger|www.dashboard-deutschland.de/api/tile/indicators?ids=data_woh_baugenehmigungen_bautraeger|
|Gasimporte nach Deutschland|tile_1667993866759|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667993866759|
|Dienstleistungsproduktion|tile_1667825347006|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667825347006|
|Umsatz im Ausbaugewerbe|tile_1654070793733|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1654070793733|
|Umlaufrenditen Staats- und Unternehmensanleihen|data_staats_und_unt_anleihen|www.dashboard-deutschland.de/api/tile/indicators?ids=data_staats_und_unt_anleihen|
|Bereinigte kassenmäßige Steuereinnahmen aus Gemeinschaft-, Bundes- und Landessteuern|data_einnahmen_gemeinschaft_bundes_landessteuern|www.dashboard-deutschland.de/api/tile/indicators?ids=data_einnahmen_gemeinschaft_bundes_landessteuern|
|Wohngebäude nach Baujahr und Energieträger der Heizung in Thüringen|tile_1669199838683|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669199838683|
|Umsatz mit Maßnahmen zur Verbesserung der Energieeffizienz von Gebäuden|tile_1665656599909|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1665656599909|
|Auftragseingang im Bauhauptgewerbe|data_bau_auftragseingang|www.dashboard-deutschland.de/api/tile/indicators?ids=data_bau_auftragseingang|
|Wohngebäude nach Gebäudegröße und Energieträger der Heizung in Mecklenburg-Vorpommern|tile_1669291142943|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669291142943|
|Wohngebäude nach Gebäudegröße und Energieträger der Heizung in Baden-Württemberg|tile_1669209397487|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669209397487|
|Flugverkehr Deutschland|tile_1667987544456|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667987544456|
|Außenhandel mit ausgewählten Ländern|tile_1667832713510|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667832713510|
|Außenhandel|tile_1667830902757|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667830902757|
|Covid-19-Hospitalisierungen|defacto_ges_diag_covid19_hospitalizationincidence_map_de|www.dashboard-deutschland.de/api/tile/indicators?ids=defacto_ges_diag_covid19_hospitalizationincidence_map_de|
|Wohngebäude nach Baujahr und Energieträger der Heizung in Berlin|tile_1669122207624|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669122207624|
|Flugverkehr weltweit|tile_1667989324139|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667989324139|
|Wohngebäude nach Gebäudegröße und Energieträger der Heizung in Rheinland-Pfalz|tile_1669293977917|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669293977917|
|Auftragseingang in Branchen des Verarbeitenden Gewerbes|data_auftragseingang_ausgewaehlte_branchen|www.dashboard-deutschland.de/api/tile/indicators?ids=data_auftragseingang_ausgewaehlte_branchen|
|Nettostromerzeugung|tile_1666961555651|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1666961555651|
|Nettonennleistung der Anlagen zur Elektrizitätserzeugung|tile_1663665904253|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1663665904253|
|Umsatz in Branchen des Verarbeitenden Gewerbes|data_umsatz_ausgewaehlte_branchen|www.dashboard-deutschland.de/api/tile/indicators?ids=data_umsatz_ausgewaehlte_branchen|
|Gold- und Kupferpreis|data_preise_gold_kupfer|www.dashboard-deutschland.de/api/tile/indicators?ids=data_preise_gold_kupfer|
|Wohngebäude nach Baujahr und Energieträger der Heizung in Mecklenburg-Vorpommern|tile_1669189699623|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669189699623|
|Preisindizes zu Bau oder Erwerb von Wohneigentum|tile_1656076602735|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1656076602735|
|Absatz von Warengruppen im Lebensmitteleinzelhandel|tile_1667821076015|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667821076015|
|Pegelstände am Rhein|tile_1666960227357|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1666960227357|
|ifo Knappheitsindikator|tile_1667289768923|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667289768923|
|Passantenfrequenzen: Veränderung in ausgewählten Großstädten|data_mobilitaet_hystreet|www.dashboard-deutschland.de/api/tile/indicators?ids=data_mobilitaet_hystreet|
|Passantenfrequenzindex|tile_1667982573430|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667982573430|
|Wohngebäude nach Baujahr und Energieträger der Heizung in Schleswig-Holstein|tile_1669199670270|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669199670270|
|Anteil des Einkommens, den Miethaushalte für eine warme Wohnung (einschl. Strom) ausgeben, nach Haushaltsgröße|tile_1669366140497|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669366140497|
|Bonitätschecks von Wohnungssuchenden|tile_1667995046610|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667995046610|
|Relative Sterbefallzahlen in Deutschland im Vergleich|ginsy_ges_bev_sterbl_rel_sterbl_map_de|www.dashboard-deutschland.de/api/tile/indicators?ids=ginsy_ges_bev_sterbl_rel_sterbl_map_de|
|Wechselkurs US-Dollar/Euro|tile_1667217389888|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667217389888|
|Renditen Bundeswertpapiere|data_umlaufrenditen_bundesanleihen|www.dashboard-deutschland.de/api/tile/indicators?ids=data_umlaufrenditen_bundesanleihen|
|Wohngebäude nach Heizungsart|tile_1669108022095|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669108022095|
|Verschuldung der bedeutendsten Sondervermögen des Bundes|tile_1650977632272|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1650977632272|
|Wöchentlicher Aktivitätsindex|tile_1667211885741|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667211885741|
|Automobilindustrie|tile_1666960710868|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1666960710868|
|Erwerbstätigkeit|tile_1667822587333|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667822587333|
|Blitzumfragen im Maschinen- und Anlagenbau|data_vdma_blitzumfragen|www.dashboard-deutschland.de/api/tile/indicators?ids=data_vdma_blitzumfragen|
|Wohngebäude nach Gebäudegröße und Energieträger der Heizung in Thüringen|tile_1669296388975|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669296388975|
|Wohnfläche in genehmigten Neubauwohnungen|data_woh_baugenehmigungen_wohnflaeche|www.dashboard-deutschland.de/api/tile/indicators?ids=data_woh_baugenehmigungen_wohnflaeche|
|HCOB Einkaufsmanagerindex|tile_1667982123933|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667982123933|
|Täglicher LKW-Maut-Fahrleistungsindex|tile_1667226778807|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667226778807|
|ZEW Konjunkturausblick|tile_1667228531297|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667228531297|
|Durchschnittliche Wohnkosten für Hauptmiethaushalte je Wohnung nach Haushaltsgröße|tile_1669368695741|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669368695741|
|Genehmigte neu zu errichtende Wohngebäude mit ein und zwei Wohnungen nach überwiegend verwendeter Heizenergie|tile_1663665272454|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1663665272454|
|Durchschnittliche Wohnkosten für Hauptmiethaushalte je Quadratmeter nach Haushaltsgröße|tile_1669368380310|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669368380310|
|Energiepreisveränderung|tile_1667826504852|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667826504852|
|Füllstand deutscher Erdgasspeicher|tile_1667227714015|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667227714015|
|Außenhandel nach VGR-Konzept|tile_1667821569597|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667821569597|
|Umsatz im Bauhauptgewerbe|tile_1654068021178|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1654068021178|
|Arbeitslosigkeit und offene Stellen|tile_1666958835081|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1666958835081|
|Wöchentliche Sterbefallzahlen in Deutschland|ginsy_ges_bev_sterbl_abs_sterbl_de|www.dashboard-deutschland.de/api/tile/indicators?ids=ginsy_ges_bev_sterbl_abs_sterbl_de|
|Entwicklung des deutschen Arbeitsmarktes anhand von Stellenausschreibungen auf Indeed|tile_1666961477511|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1666961477511|
|Renditespreads 10-jähriger Staatsanleihen gegenüber Deutschland|data_zinsspread_10_j_anleihen|www.dashboard-deutschland.de/api/tile/indicators?ids=data_zinsspread_10_j_anleihen|
|Kassenmäßige Steuereinnahmen aus Gemeindesteuern|data_gemeindesteuern|www.dashboard-deutschland.de/api/tile/indicators?ids=data_gemeindesteuern|
|Neue Hypothekenverträge|tile_1667817211258|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667817211258|
|Wohngebäude nach Baujahr und Energieträger der Heizung in Sachsen-Anhalt|tile_1669199513126|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1669199513126|
|Verbraucherpreisindex für Nettokaltmiete nach Kreistypen|data_woh_nettokaltmiete|www.dashboard-deutschland.de/api/tile/indicators?ids=data_woh_nettokaltmiete|
|Preisindex für Ein- und Zweifamilienhäuser nach Kreistypen|data_woh_preise_immobilien_hpi_haueser|www.dashboard-deutschland.de/api/tile/indicators?ids=data_woh_preise_immobilien_hpi_haueser|
|Kurzarbeit|data_ba_kurzarbeit|www.dashboard-deutschland.de/api/tile/indicators?ids=data_ba_kurzarbeit|
|Stimmungsindikatoren Konsum|tile_1667983271066|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667983271066|
|Kreditvergaben und Online-Transaktionen|tile_1667978809506|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1667978809506|
|Benzinpreise im EU-Vergleich|tile_1663664545105|www.dashboard-deutschland.de/api/tile/indicators?ids=tile_1663664545105|


## Geojson

**URL:** www.dashboard-deutschland.de/geojson/de-all.geo.json
	
Die API ermöglicht Zugriff auf Geojson-Daten zu Deutschland und den Ländern (00-DE_admin1_400).


## Beispiel

```bash
indicators=$(curl -m 60 'https://www.dashboard-deutschland.de/api/tile/indicators?ids=data_adv_flugverkehr;data_aussenhandel;data_ba_arbeitslose_und_stellen;data_bruttoinlandsprodukt;data_corona_zuschuesse;data_einnahmen_gemeinschaft_bundes_landessteuern;data_ifo_geschaeftsklima;data_kfw_sondermassnahme_neu;data_preisentwicklung;data_umsatz_ausgewaehlte_branchen;defacto_ges_diag_covid19_hospitalizationincidence_map_de;ginsy_ges_bev_sterbl_abs_sterbl_de;ginsy_ges_diag_covid19_7_tage_inzidenz_map_de;tile_1648135639982
')
```
