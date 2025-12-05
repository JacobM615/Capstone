# Planning

## The stuff that needs doing roughly in order

1. Data

    - Search Kaggle

    - Create short list
    
    - Choose oen dataset
    
    - Double check it meets requirements

    - Possibly run it by Ed or Ryan

    - Download it (probably csv), save in raw data folder

    - Some rough initial exploration

    - (Possibly unclean it if needed)

2. Extract

    - Extract csv(s) into df

        - Include exception handling

    - Get good logger coverage of extract

        - Might need to update logging utils

    - Get good test coverage of extract

3. Transform

    - Import extracted dataset(s)

    - Use notebooks to investigate what needs transforming

    - Apply transforms

        - Deal with nulls

        - Deal with duplicates

        - Enrich

        - Join/merge if needed

    - Save in processed (csv)

        - File utils

    - Get good logger coverage of extract

    - Get good test coverage of extract

4. Load

    - Save in processed (csv)
    
    - Get good logger coverage of extract

    - Get good test coverage of extract

5. App

    - Take in the csv or (better) the load df

    - Make analysis plots (must be a few and some interactive ones)

    - Make pretty app (CSS, pages)

6. Plan future stuff (aws etc), next steps

    - Think and write about if this app was going to be run commerically/in production

7. Presentation

    - Tidy up Streamlit and README so it is ready to present

    - Script/plan what I'm going to say

---
---

## Possiible questions to answer...

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

How many workouts are of each type?

How many workouts has each user done?

How long are peoples workout sessions?

How many of each subscription type is there?

Are certain demographics more likely to get a certain subscription?

How much revenue per month is being made by each subscription type?

Does subscription plan affect which type of gym you go to?

What are the top and bottom gym goers (by number of sessions)?

What does the geographical distribution of users look like?

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