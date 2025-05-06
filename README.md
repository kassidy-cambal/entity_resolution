# Entity Resolution 

# An Overview of Entity Resolution
Entity resolution is the process that identifies and links records from different data sources that allude to the same real-world entity.
This multistep technique plays an essential role in overcoming variations and inconsistencies during the data ingestion and integration 
process to enhance overall data quality and accuracy. The first step handles standardizing and cleaning in order to reduce the noise 
across the datasets. This is followed by blocking or grouping similar records to reduce the number of comparisons needed. 
Then, feature extraction is performed to determine similarity scores such as Jaro-Winkler or Levenshtein distance between pairs 
of names and attributes. This leads into the classification and clustering phase that uses machine learning methods to predict
if two records match. The final step encaptures the matching, or merging, of the data to create unified entries ultimately 
eliminating duplication due to error. 

# Data Sources 
Patent Data (ad20250218.zip): contains data on individuals or groups who have been awarded a patent 
NPI Data (npidata_pfile_20240205-20240211.csv): contains doctor/ medical professionals data that we wish to match with patentee data
Grant Data (RePORTER_PRJ_C_FY2024.csv): contains data on individuals and institutions that have received funding for research

# The Goal of This Entity Resolution Application
This application seeks to find identical records across three different datasets containing information on patents. The goal is 
to match the doctor with the patent linked to them, ultimately eliminating duplicates due to data entry error. The unified 
results will be read into a SQL table that will offer a more accurate and interpretable representation of doctor and patent data. 

# Cleaning and Standardizing the Data 
Grant Data: The grant data contains information of the organization responsible for funding and overlooking the patent. 
The structure of the data was modified to have column names represented in all lowercase letters, rather than all uppercase letters. 
To standardize the PI names, a data entry row was created for each doctor name that corresponded with a value in a column that represented if 
the doctor was a contact.  

NPI Data: The NPI data was cleaned in a way that renamed columns to have simpler, lowercase names. 

Patent Data: The patent reader parsed through an xml file and implemented rules that kept only valid entries.
Assignors must have nonempty forenames and surnames (formatted 'last, first'), assignees must have a name 
and complete address (at least one address line with city, state, and postal code), and the patent must have a name, 
assignor, and assignee linked to it. Patent info is verified and validated to elimate duplicates and invalid structured entries. 

# Blocking Data
In the name matcher class, data blocking is performed by grouping the data based on the first letter of doctor 
surname from both the doctor and patent dataframes. 

# Feature Extraction
In the name matcher class, both jarowinkler and levenschtein distance is performed under the calculate distance function. 
Jarowinkler is used to measure the similarity between two strings, specifically in this case between the forenames and surnames 
of doctors and patentees. Levenschtein distance is used to measure the number of single character edits, including insertions, deletions, 
and substitutions, to transform one string into another. This is again applied to both the forenames and surnames of 
doctors and patentees. The similarity features are input into a dataframe that is later used for training and predictions. 

# Classification 
The purpose of the classification step in the entity resolution process is to 
make predictions on whether a doctor and patentee name refer to the same individual based on features. 
To train the classifier, labeled simulated data is created. Then, Jarowinkler and Levenshtein are used to calculate 
the similarity metrics on the name pairs. The trained model is then used to make predictions on new doctor-patentee name pairs.
Matches are labeled with a 1 and nonmatches are labeled with a 0. If the doctor-patentee name pair
is labeled as a match it is stored in the output SQL database. 

This application of entity resolution uses an XG Boost classifier to learn and predict matches.
The features are taken from the name similarity metrics from Jaro-Winkler or Levenshtein. The
labels represented by a 0 or 1 represent non-match (0) versus match (1).

# Merging and Matching 
Doctor-patentee name pair matches are labeled with a 1 if they are classified as a match and 
labeled with 0 if they are classified as a non-match. The name pairs labeled with a 1
are saved into a doctor-patentee match table, which represents the merging step of the 
entity matching of doctor and patentee names.

# Conclusion 
Overall, entity resolution is an integral step when referring to multiple datasets.
This step aims to effectively and accurately merge data entries that refer to the same real world
record, leading to a more accurate representation of the data that allows for a more accurate and
efficient analysis. 

This specific project uses the entity resolution process to match doctor and patentee
names based on string similarity metrics calculated using Jaro-winkler and Levenshtein 
distance. To reduce the complexity of the problem, a blocking technique was used to
group likely pairs (based on the first letter of the surname). Using the calculated string 
distances as features, simulated training data was created and an XG-Boost classifier
was trained to classify doctor-patentee name pairs as a match (labeled with a 1) or a non-match 
(labeled with a 0). The name pairs classified as matches were then merged and saved to a new table,
exemplifying an accurate representation of real world data. 