# [Who can plug in their cars?](https://compjour-2017-isalian.herokuapp.com/)
 
 *by Isha Salian*
 
 ## Elevator Pitch

 Electric vehicles owners depend on special charging stations to power their cars. This app looks at the geographic distribution of electric vehicle charging stations across California. Each point on the map is the location of an electric charging station, and each shaded area is a California census tract, with darker tracts representing census tracts with higher median incomes. Since electric vehicles are not the cheapest kind of car, the theory is that more electric vehicle charging locations will be found in richer communities. Several articles (see below) have expressed this idea, which can be tested using the app.

 [This is what it looks like.](https://compjour-2017-isalian.herokuapp.com/)

 The more detailed view allows you to choose a CA zip code and learn:
 - number of charging stations in that zip code
 - median household income of the census tract the station is in
 - a table with the number of public v. private stations in the area
 - a table listing the station name, address, and public/private status of all the electric charging stations in that area

 Granular view:
 - From the zip code view, if you click on a particular station the station page gives the station name and address as well as a Google Street View photo of the location
 - Also provides a table with detailed information of owner status, hours, and station telephone number

 ## Inspirations and prior work
 There are electric vehicle charging station maps, and there are articles that talk about the need/efforts to have them better distributed across high- and low-income areas, but I haven't found anything that puts those together.

 ### 1. Maps of all alternative fuel stations or electric vehicle charging stations nationwide.
 * [PlugShare](https://www.plugshare.com/) was the first example I found, with a nice clean map. You can filter by multiple variables, click on an individual station for a more detailed view, or search for a station. It seems geared towrds curious car owners and not trying ot tell any kind of story.
 * Similarly, both the [U.S. Department of Energy](https://www.afdc.energy.gov/locator/stations/) and [U.S. Energy Information Administration](https://www.eia.gov/todayinenergy/detail.php?id=6050) have maps that users can filter on relevant variables, search for a particular station, or plan a driving route with stops to fuel up. Again, more geared towards car owners than analysis. The latter map has some mention of differing levels of access around the country, but not to the granular level my app does.

 ### 2. Maps of income level by census tract
 * Through random Googling, I found [this map](https://www.arcgis.com/home/webmap/viewer.html?useExisting=1&layers=da76de09076b4959ad005e1dc2c48049) that plots nationwide median household income by census tract--the same measure for wealth by region that I chose to use for my analysis. When I made my map of California census tracts color-coded by income, I was able to fact-check it using this map. 

 ### 3. Other analyses of electric vehicles
 * The DOE also has an analysis about the [rise in sales](https://energy.gov/articles/visualizing-electric-vehicle-sales) of electric vehicles nationwide. This backed up my theory that the topic was worth looking into and visualizing cross-community differences around electric vehicles. 


 ## Articles
 * **[EV Charging Stations Coming to Low Income Neighborhoods](http://www.sfweekly.com/news/ev-charging-stations-coming-low-income-neighborhoods/)** This SFWeekly piece from December 2016 celebrated the California Public Utilities Commission decision to install more than 1,000 electric vehicle charging stations in low-income neighborhoods, claiming that this was an important step to making clean-energy cars more accessible to people from all incomes and neighborhoods.

 * **[Pressure mounts for VW to invest in low-income communities](http://www.sfgate.com/business/article/Pressure-mounts-for-VW-to-invest-in-low-income-11176810.php)** This quite recent article from SFGate explains that investing millions in installing new fuel charging stations in California is part of Volkswagen's settlement deal for their emissions-cheating scandal. Apparently, they are supposed to put many of these charging stations in lower-income areas like the Central Valley but their proposal put most along major highways and in already affluent urban areas.

 * **[Edison installs first electric-car charging stations in low-income community](http://www.sgvtribune.com/general-news/20170216/edison-installs-first-electric-car-charging-stations-in-low-income-community)** In Southern California, a February article in the San Gabriel Valley Tribune describes the statewide efforts to install  more charging stations in low-income neighborhoods as an attempt to incentivize more people to choose electric vehicles, since they are still quite rare in the state. 

 ## Data Sources
 ### 1. Nationwide alternative fuel station locations 
 This dataset was posted by [California EPA](https://data.ca.gov/dataset/alternative-fuel-station-locations) as a CSV. It was released by the DOE in August 2016, and includes both public and private alternative fuel stations. However, if there are multiple charging outlets at the same station, it is coded as just one entry. I filtered this dataset down to only include electric charging stations in California.

 ### 2. CA Census Tracts
 These shapefiles are available on the [U.S. Census' website](https://www.census.gov/geo/maps-data/data/cbf/cbf_tracts.html) for download. They do not correspond exactly to city or county boundaries, but rather represent the regional divisions used by the U.S. Census. 

 ### 3. Median Household Income Data
 This data comes from [American Fact Finder](https://factfinder.census.gov/faces/nav/jsf/pages/index.xhtml), which is operated by the U.S. Census. It provides numbers on median household income by census tract, allowing me to layer onto the shapefiles to determine which regions of California are richest.