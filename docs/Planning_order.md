# Planning

## Brain storm of what needs doing (roughly in order)

1. Data

    - Search Kaggle

    - Create short list
    
    - Choose one dataset
    
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

    - Take in the csv or (better) load the df

    - Make analysis plots (must be a few and some interactive ones)

    - Make app pretty (CSS, pages)

6. Plan future stuff (aws etc), next steps

    - Think and write about if this app was going to be run commerically/in production

7. Presentation

    - Tidy up Streamlit and README so it is ready to present

    - Script/plan what I'm going to say

