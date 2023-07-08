<p align="center">
  <img alt="Coding" width="650" src="https://github.com/shridharkamathe/Hotel-Data-Analysis/assets/124047047/34820e3c-dfd1-4eec-8fae-90ddcf379e08">
</p>

# InstaHyre Job Skills Analysis and Webpage

This repository contains a project that involves analyzing job skills data from the InstaHyre job portal and creating a webpage to display a summary of job skills. The project utilizes Python, Jupyter Notebook, Selenium, BeautifulSoup, Pandas, and HTML.

<img align="right" alt="Coding" width="400" src="https://github.com/shridharkamathe/Hotel-Data-Analysis/assets/124047047/cb3615d7-a13e-4086-89c9-1a7a1a896024">

## Dataset

The dataset used for this project was obtained by scraping and cleaning the InstaHyre website. The dataset contains information about job skills, including skills like Python, SQL, Excel, and various other programming languages.

The cleaned dataset is stored in an Excel file and used for further analysis and visualization.

## Tools used
||
|--|
|Python|
|Jupyter Notebook|
|NLTK Library|
|Flask|
|HTML|
|Excel|
|Pandas|
|Selenium|

## Analysis

The project involves the following steps:

1. **Web Scraping and Cleaning:** The InstaHyre website was scraped using Selenium and BeautifulSoup libraries in Python. The data obtained was then cleaned using Pandas to remove any inconsistencies or irrelevant information.

2. **Data Analysis:** After cleaning the dataset, various data analysis techniques were applied. This includes creating pivot tables to summarize the job skills data. The analysis provides insights into the total job openings, locations with the most jobs, and the most common positions for job openings.

3. **Webpage Creation:** A webpage was created using HTML to display the summary of job skills. Users can enter a skill, such as Python, SQL, Excel, or other languages, and the webpage will display relevant information. This includes the total job openings, the location with the most jobs related to the skill, and the most common positions for job openings.

|Key Insights|
|---|
|Java is the most in demand skill followed by Python and JavaScript.|
|Mid Senior Level Positions has most number of openings and Director position has the least.|
|IT Services, Banking, Financial Services, Business Consultation are most popular industries as per applications.|
|Larger Firms are offering more jobs than that of smaller firms.|
|IT and SOFTWARE sectors are leading on LinkedIn in terms of followers, followed by  Consumer Electronics and Finance sector.|

## Web Page

##### Home Page
<img width="900" alt="Screenshot 2023-05-04 at 4 21 14 PM" src="https://github.com/shridharkamathe/Hotel-Data-Analysis/assets/124047047/0198480a-fd66-4224-bf9e-604ba186dae7">

##### Search Results Page
<img width="900" alt="Screenshot 2023-05-01 at 12 45 35 PM" src="https://github.com/shridharkamathe/Hotel-Data-Analysis/assets/124047047/611b3607-0874-4baf-aaaf-5e6c71f4c36d">

## Challenges Faced

One of the major challenges we encountered during the data scraping process was extracting information from LinkedIn profiles. This task proved to be particularly difficult due to the varying structure of each profile and the absence of a consistent XPath for data extraction.

LinkedIn profiles are highly customizable, allowing users to arrange sections and elements in different ways. As a result, finding a universal XPath that could reliably capture the desired data across all profiles was not feasible. We had to devise a solution that could adapt to the unique structure of each profile and extract the relevant information effectively.

To overcome this challenge, we developed a dynamic scraping algorithm that utilized intelligent pattern matching and element identification techniques. Instead of relying on a fixed XPath, our algorithm analyzed the structure and content of each profile to identify the appropriate elements and extract the desired data accurately. This adaptive approach allowed us to handle the diverse layouts and configurations of LinkedIn profiles successfully.

Another challenge we encountered during the data processing phase was dealing with misspelt words in the dataset. To address this issue, we leveraged the Natural Language Toolkit (NLTK) library. NLTK provides powerful tools for natural language processing, including features for spell-checking and correction. We integrated these functionalities into our system, enabling a search option that could accommodate misspelt words and enhance the overall accuracy of the data.

By utilizing NLTK's spell-checking capabilities, we were able to ensure that the search functionality of our dataset remained robust, even in cases where users made typographical errors or misspelt certain words.

The combined efforts to tackle the challenges posed by LinkedIn profile scraping and misspelt words have significantly improved the quality and usability of our dataset. The methodologies and techniques employed are detailed in the accompanying code and documentation available in this GitHub repository.

For further insights into the approach used and the intricacies of the data scraping and processing pipeline, please refer to the relevant sections and code files in the repository.


## Repository Structure

The repository is structured as follows:

- **data:** This directory contains the cleaned dataset stored in an Excel file.

- **notebooks:** This directory includes Jupyter notebooks used for web scraping, data cleaning, and data analysis.

- **webpage:** This directory contains the HTML files and any necessary CSS or JavaScript files for the webpage.

- **README.md:** This file, providing an overview of the repository and its contents.

## Contributing

Contributions to this repository are welcome. If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.

## Acknowledgments

We would like to acknowledge the efforts put into this project. The web scraping, data cleaning, analysis, and webpage creation are based on thorough research and utilization of relevant libraries and technologies

Please note that this project is a proposal and should be further evaluated and adapted based on the specific requirements and objectives of your application.
