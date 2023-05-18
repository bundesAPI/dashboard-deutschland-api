# Get all indicator-ids
#----------------------
url0="https://www.dashboard-deutschland.de/api/dashboard/get"
dat0=httr::content(httr::GET(url0))
clusterIDs=sapply(dat0,function(x)x$id)
indicatorIDs=sapply(dat0,function(x)sapply(x$layoutTiles,function(y)y$indicatorid))
names(indicatorIDs)=clusterIDs

# Get all data on all indicator-ids
#----------------------------------
url1=paste0("www.dashboard-deutschland.de/api/tile/indicators?ids=",paste(unlist(indicatorIDs),collapse=";"))
dat1=httr::content(httr::GET(url1))
length(dat1)==length(unique(unlist(indicatorIDs)))
json=sapply(dat1,function(x)rjson::fromJSON(x$json))

# Output Markdown-table
#----------------------
tab=paste(c("|Indikator|ids-value|Beispiel-URL|","|---|---|---|",
		sapply(dat1,function(x)paste0("|",x$title,"|",x$id,"|www.dashboard-deutschland.de/api/tile/indicators?ids=",x$id,"|"))),
	collapse="\n")
writeLines(tab,"table.txt")

writeLines(paste(sapply(dat1,function(x)paste0("- ",x$id," (",x$title,")")),collapse="\n"),"list.txt")

