# Question: What are some Scalable solutions for handling Large datasets

# 1) Using databases - e.g. MySQL
- If the text file is too large, a database can efficiently store and process the words.

# How can this be achieved:
- Import the list of words from the text file into a relational database like MySQL.
- Create a table with a column for words.
- Write a query using sorted_word which will find all the anagrams.

# Why use databases:
- Databases are designed to handle large volumes of data efficiently. 
- So, when you're working with a huge dataset, a database will be optimal.
- A databases querying capabilities allow you to write complex queries to search, filter and aggregate data;
all of which contributes to less memory usage and thus more scalability.

# 2) Using Dataframes - e.g. Pandas
# Why Dataframes:
- Dataframes like Pandas achieves scalability through several ways, and one of them is its ability to 
handle data step-by-step and focus on specific parts of the data when needed.
- By loading and processing data in chunks or batches, pandas can efficiently work with datasets that are too large 
to fit into memory all at once.
- This incremental processing approach allows pandas to scale up to handle very large datasets.
- Pandas has inbuilt data manipulation and analysis functions that are optimized for performance. 
By using these functions, pandas avoid traditional looping and iterative approaches, which can be slower 
and more memory-intensive.

# 3) Parquet Format
# Why Parquet Format:
- You can convert a dataframe to Parquet format which stores data more efficiently.
- This is useful when even dataframes get overwhelmed and can't handle the required amount of data.

# How:
- Parquet achieves scalability through its efficient storage format. Files are smaller and data is compressed well, 
hence making it easier to store more data.
- Because of its efficient method of data storage, it's quicker to read and write data stored in Parquet format; 
thus freeing up memory.
- Example illustration: A list of words stored in Parquet format will take up less space than the same list of words 
stored in a txt file.

# 4) Cloud Services e.g. AWS
 # Why Cloud Services:
- Cloud services offer scalable storage solutions that can hold vast amounts of data.

# How:
- Cloud services use advanced tech like clever storage systems and adaptable computing power.
- These storage systems can easily grow or shrink depending on how much you need, making them efficient and flexible.
- For example: if you have 10 words, their storage will shrink to meet this level. On the other hand, if you have 1 billion, storage will grow to meet this level.
- Ultimately it can do this because of good computational systems.
