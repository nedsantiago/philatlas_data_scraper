# PhilAtlas Data Scraper

#### Video Demo: [PhilAtlas Data Scraper](https://youtu.be/H82yLyQt-LA)

#### Description:

When conducting environmental-social consultancy work, gathering a location's demographic data is often important. [PhilAtlas](https://www.philatlas.com/) has been a convenient source of demographic data for Filipino consultants. However, without programming knowledge, consultants are forced to perform the monotonous task of manually gathering data for hundreds of locations. When budget and time allow, interns or encoders are usually tasked with this job. Software programs can make this task redundant, freeing up employees to be more engaged in their work. Thus, the aim of this program is to automate the data gathering process.

Summary of features:
* Link Following
* JSON data exporting
* Design Pattern - Factory (see philatlas\spiders\readers\factories.py)
* Design Pattern - Abstract Factory (see philatlas\spiders\readers\factories.py)
* Five (5) second sleep per query to prevent overloading servers

This project uses the [Scrapy library](https://scrapy.org/) to automate the demographic data collection process. Scrapy provides tools and parts for creating bots, which Scrapy calls "spiders". This project implements a Scrapy spider that goes through the PhilAtlas website, gathering data from its tables using the step-by-step process seen in the spider's `parse` method:

1. Sleeps for five (5) seconds.
2. Looks for the summary table.
3. Passes the summary table to an interpreter for information boxes and appends the interpreter’s results to a dictionary.
4. Looks for the households table.
5. Passes the households table to an interpreter for tables with dates and appends the interpreter’s results to a dictionary.
6. Looks for a population by age group table.
7. Passes the population by age group table to an interpreter for generic tables and appends the interpreter’s results to a dictionary.
8. Looks for a historical population table.
9. Passes the historical population table to an interpreter for tables with dates and appends the interpreter’s results to a dictionary.
10. Yields the results (which will be used by other parts of the spider).
11. Finds all links that are inside a table. In test cases, this is always where links to barangays (the smallest political territory in the Philippines, similar to a district) are found.
12. Adds those links to the list of URLs the spider will look at.
13. Goes to the next link in the list of URLs.

The sleep step was implemented to slow down the spider's query speed. This should reduce the burden on PhilAtlas servers. The spider mainly uses table ID's to find tables. Most webpages in PhilAtlas use the same ID's for all its webpages. PhilAtlas pages tend to show the subsidiary administrative territories in their own tables. The spider uses these patterns to its advantage.

The project recommends giving it a link to the largest administrative territory.
```
python project.py https://www.philatlas.com/luzon/ncr/san-juan.html
```
For example, when the spider is given the link to San Juan City, it will read the demographic data of San Juan City then read the data of all its 21 barangays. You can also provide links to a region, like the National Capital Region. The spider would then look for all the cities inside the region and then for all the barangays under each city. The spider will not look for new urls when given a barangay webpage.


## 🧑🏽‍💻 Author
### Ned Santiago

## 🎯 Purpose

When conducting environmental-social consultancy work, gathering a location's demographic data is often important. PhilAtlas has been a convenient source of demographic data for Filipino consultants. However, without programming knowledge, consultants are forced to perform the monotonous task of manually gathering data for hundreds of locations. When budget and time allow, interns or encoders are usually tasked with this job. Software programs can make this task redundant, freeing up employees to be more engaged in their work.

## 📖 Documentation

### ⚡Usage

For Windows
```
python project.py [HTML URL]
```
For Linux
```
python3 project.py [URL HERE]
```
