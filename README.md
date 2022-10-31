# LSE_DA_NHS_analysis
NHS Diagnostic Analysis Using Python

Week 1

My Github was set up with a main branch and a branch called Weekly Update Branch. Pull requests will be made to merge update from the Weekly Udpate Branch to the Main Branch.

Github enables data analysts to store their own working codes, while at the same time allowing teams to contribute to collaborative work with proper version controls. In particular, Github enables storage of different versions of one set of code base, so that each team member can extract a specific version of the codes for his own development, then merge updates with the original codes through pull requests to the main branch.


Week 2

The first thing to do at the initial stage is to get contexts over the business problem and familiarise oneself with the available data. To enable data analysis performed in the form of dataframe, pandas library has been imported alongside the 3 data sets.

The 3 dataframes are then sense checked with the below syntax:

.shape - provides overview on the dataframe size (no. of rows and columns)
.dtypes - provides datatype info of each column, it is helpful for future analysis as certain analytical approach may require datatype conversion (e.g. string is required for measure fields in Seaborn data visualisation)
.columns - provides the name of each column
.isnull().sum() - provides a total no. of missing values in the dataframe
.head() - displays the first 5 rows of the dataframe 

And their metadata are also looked into, .info() provides a summary of the dataframe and .describe() provides their basic statistical details. The df.count_values() syntax enables sum of the total appearance of a specific categorical attribute (e.g. location, service setting etc.), and a for loop used in Question 2 allows iterative processing of the syntax to display results from the first 5 rows.


Week 3

Since the date data in the data sets were initially provided in the form of text strings, to enable further analysis on a by-month basis, conversion of dates into year-month-day format was required and was done through the Python datetime module. The .groupby() function allowed aggregation of the appointment count with respect to the monthly window, which in turn provided an overview on the monthly appointment trend. Subsets of dataframes were created during these steps to ensure while the dataframes were being modified, the original data sets would remain intact.

North West London, being the leading appointment location in the data set, was seen having GP as the most popular service setting among appointments, and this had given an indicative view over the demand for GP. October and November, being the 2 months with the highest no. of appointments, were the period that would require further deep diving for sure.
