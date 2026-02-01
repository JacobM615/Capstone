# Reflections

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
