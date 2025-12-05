# Capstone
Digital Futures capstone project

## Dataset

(https://www.kaggle.com/datasets/mexwell/gym-check-ins-and-user-metadata)

I chose my dataset because my main hobby is going to the gym, this data set met the requirements and involved multiple tables with foreign keys allowing me to join them for greater insights. With it being synthetic data it did require some adjustment such as regenerating names as there were many repeats and uncleaning it.

---
---

## Possible questions to answer...

How long is the average gym sessions? (checkout - checkin)

What is the average calories burned?

Most and least popular workout type? (count workout types)

Most and least popular gym? (count number of occurrences)

What do the subscription type demographics look like? (ages, gender by sub plan)

What does the demographic of all the gyms look like? (age, gender by gym by gym)

Revenue by subscription type? (occurrences x price per plan)

Number of users per subscription? (occurrences per sub)

Workout types per gym?

Revenue per gym? (gonna need to modify the dataset for this)

---

Chosen questions:

- How many workouts are of each type?

- How many workouts has each user done?

- How long are peoples workout sessions?

- How many of each subscription type is there?

- Are certain demographics more likely to get a certain subscription?

- How much revenue per month is being made by each subscription type?

- Does subscription plan affect which type of gym you go to?

- What are the top and bottom gym goers (by number of sessions)?

- What does the geographical distribution of users look like?

---
---

## EPICS

### 1. (Extract)

```text
As a Data Engineer,
I want to be able to access all of the raw tables,
So that it can be transformed/processed ready for analysis and Streamlit integration.
```

<details> <summary> Expand </summary>

---

User Story 1.1

    As a Data Engineer,
    I want to be able to access the data from the CSV files,
    So that it can be transformed.

    AC:
    - The data is extracted from the CSVs to a df
    - No errors
    - Data integrity maintained
    - Logger works (successful and otherwise)
    - Good test coverage (all code that isn't just calling other code)

</details>

### 2. (Transform)

```text
As a Data Engineer,
I want to clean, standardised, enriched and aggregated data if needed,
So that it can be analysed and used to draw useful insights from.
```

<details> <summary> Expand </summary>

---

User Story 2.1

    As a Data Engineer,
    I want to be able to access clean, standardised data,
    So that it can be further transformed.

    AC:
    - Nulls are handled gracefully and appropriately
    - The data is standardised on a column by column basis (consistent formatting etc.)
    - No errors
    - Data integrity maintained
    - Logger works (successful and otherwise)
    - Good test coverage (all code that isn't just calling other code)

User Story 2.2

    As a Data Engineer,
    I want to be able to access combined, enriched and aggregated data,
    So that it can be analysed.

    AC:
    - The dfs that need to be should be merged
    - The appropriate enrichments are performed
    - The appropriate aggregates are made
    - No errors
    - Data integrity maintained
    - Logger works (successful and otherwise)
    - Good test coverage (all code that isn't just calling other code)
    
</details>

### 3. (Load)

```text
As a Data Engineer,
I want to store the data to used,
So that it can be analysed and used to draw useful insights from.
```

<details> <summary> Expand </summary>

---

User Story 3.1

    As a Data Engineer,
    I want to be able to save the transformed dfs as CSVs,
    So that it can be analysed and accessed by Streamlit.

    AC:
    - It saves properly in the correct file format
    - Data integrity is maintained
    - It is saved in the correct/specified place in the file system
    - No errors
    - Data integrity maintained
    - Logger works (successful and otherwise)
    - Good test coverage (all code that isn't just calling other code)

</details>

### 4. (Visualise)

```text
As a Data Engineer/Analyst,
I want to present the data and findings in Streamlit,
So that it can be presented.
```

<details> <summary> Expand </summary>

---

User Story 4.1

    As a Data Engineer/Analyst,
    I want to be able to provide insights into the data,
    So that the initial questions can be answered.

    AC:
    - It includes multiple interactive graphs of different types
    - No errors

User Story 4.2

    As a Data Engineer/Analyst,
    I want to be able to present a visually appealing Streamlit site,
    So that the insights are conveyed better and the audiences attention is held.

    AC:
    - A good website structure
    - A consistent format and styling is used
    - Interesting graphs presented

</details>

---
---

## Challenges and takeaway

Challenges: 
- Synthetic data can be too clean in some ways and sometimes be illogical
- Coming up with tests can be hard
- Streamlit can be awkward to work with at times likely due to my limited knowledge
- Coming up with ideas and lines of inquiry

Takeaways:
- Synthetic data is only as good as your prompts
- Documentation is a lot easier to understand with examples alongside
- Notebooks are very useful to test changes away from the main code

---
---

## Future dev

- Answer these question: What are the top and bottom gym goers (by number of sessions)? What does the geographical distribution of users look like?
- Make the users vs gym sessions graph interactive (Click on point -> display that users information)
- Save the data to a database instead of to csv files, for example using AWS services (S3 for the raw data, Glue to implement transformations, RDS for the related tables, EC2 to run the app, (if actual data was used) IAM roles could be used to keep confidentiality)
- The commands could be setup to run the etl and then app with one command.