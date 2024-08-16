# PhilAtlas Data Scraper

#### Video Demo: <URL HERE>

#### Description:
Filipino consultants use [PhilAtlas](https://www.philatlas.com/) as a convenient source of demographic data in their analyses. However, manually gathering data is a low-value and monotonous task. This project uses the [Scrapy library](https://scrapy.org/) to automate the process demographic of data collection. The project features:
* Link Following
* JSON data exporting
* Object Oriented Programming - Factory (see philatlas\spiders\readers\factories.py)
* Object Oriented Programming - Abstract Factory (see philatlas\spiders\readers\factories.py)
* Five (5) second sleep per query to prevent overloading servers

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

