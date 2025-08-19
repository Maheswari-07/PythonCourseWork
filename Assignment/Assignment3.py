# 🗄️ DBMS Quiz Game in Python

def run_quiz():
    print("Welcome to the DBMS Quiz Game!\n")

    questions = [
        {
            "question": "1. What does DBMS stand for?",
            "options": {
                "a": "Database Management System",
                "b": "Data Backup Management Software",
                "c": "DataBase Maintenance Service",
                "d": "Data Backup Monitoring System"
            },
            "answer": "a"
        },
        {
            "question": "2. Which type of database stores data in tables?",
            "options": {
                "a": "Relational Database",
                "b": "Hierarchical Database",
                "c": "Network Database",
                "d": "Object-Oriented Database"
            },
            "answer": "a"
        },
        {
            "question": "3. Which SQL command is used to retrieve data from a database?",
            "options": {
                "a": "GET",
                "b": "SELECT",
                "c": "FETCH",
                "d": "EXTRACT"
            },
            "answer": "b"
        },
        {
            "question": "4. What is a primary key?",
            "options": {
                "a": "A unique identifier for each record",
                "b": "A field that can be null",
                "c": "A foreign key in another table",
                "d": "A duplicate value field"
            },
            "answer": "a"
        },
        {
            "question": "5. Which SQL clause is used to filter records?",
            "options": {
                "a": "WHERE",
                "b": "FILTER",
                "c": "SORT",
                "d": "LIMIT"
            },
            "answer": "a"
        },
        {
            "question": "6. Which normal form removes partial dependency?",
            "options": {
                "a": "1NF",
                "b": "2NF",
                "c": "3NF",
                "d": "BCNF"
            },
            "answer": "b"
        },
        {
            "question": "7. What does the SQL command 'DELETE' do?",
            "options": {
                "a": "Removes all rows from a table",
                "b": "Removes specific rows from a table",
                "c": "Removes the table structure",
                "d": "Removes database connection"
            },
            "answer": "b"
        },
        {
            "question": "8. Which of the following is NOT a type of join in SQL?",
            "options": {
                "a": "INNER JOIN",
                "b": "OUTER JOIN",
                "c": "CROSS JOIN",
                "d": "TOP JOIN"
            },
            "answer": "d"
        },
        {
            "question": "9. What is a foreign key?",
            "options": {
                "a": "A key that links two tables",
                "b": "A duplicate of the primary key",
                "c": "A key used only for sorting",
                "d": "A key that stores passwords"
            },
            "answer": "a"
        },
        {
            "question": "10. Which SQL statement is used to update data in a table?",
            "options": {
                "a": "MODIFY",
                "b": "UPDATE",
                "c": "CHANGE",
                "d": "ALTER"
            },
            "answer": "b"
        }
    ]

    score = 0
    for q in questions:
        print(q["question"])
        for key, value in q["options"].items():
            print(f"{key}) {value}")
        answer = input("Your answer (a/b/c/d): ").lower()
        if answer == q["answer"]:
            print(" Correct!\n")
            score += 1
        else:
            print(f" Wrong! The correct answer is '{q['answer']}'\n")

    print(f" Your Final Score: {score}/{len(questions)}")
    if score == len(questions):
        print(" Perfect! You're a DBMS master!")
    elif score >= 15:
        print(" Great job! Keep practicing!")
    else:
        print(" You can improve! Review DBMS basics.")


# Run the game
run_quiz()

#Output:
'''Welcome to the DBMS Quiz Game!

1. What does DBMS stand for?
a) Database Management System
b) Data Backup Management Software
c) DataBase Maintenance Service
d) Data Backup Monitoring System
Your answer (a/b/c/d): a
 Correct!

2. Which type of database stores data in tables?
a) Relational Database
b) Hierarchical Database
c) Network Database
d) Object-Oriented Database
Your answer (a/b/c/d): a
 Correct!

3. Which SQL command is used to retrieve data from a database?
a) GET
b) SELECT
c) FETCH
d) EXTRACT
Your answer (a/b/c/d): b
 Correct!

4. What is a primary key?
a) A unique identifier for each record
b) A field that can be null
c) A foreign key in another table
d) A duplicate value field
Your answer (a/b/c/d): a
 Correct!

5. Which SQL clause is used to filter records?
a) WHERE
b) FILTER
c) SORT
d) LIMIT
Your answer (a/b/c/d): a
 Correct!

6. Which normal form removes partial dependency?
a) 1NF
b) 2NF
c) 3NF
d) BCNF
Your answer (a/b/c/d): b
 Correct!

7. What does the SQL command 'DELETE' do?
a) Removes all rows from a table
b) Removes specific rows from a table
c) Removes the table structure
d) Removes database connection
Your answer (a/b/c/d): b
 Correct!

8. Which of the following is NOT a type of join in SQL?
a) INNER JOIN
b) OUTER JOIN
c) CROSS JOIN
d) TOP JOIN
Your answer (a/b/c/d): d
 Correct!

9. What is a foreign key?
a) A key that links two tables
b) A duplicate of the primary key
c) A key used only for sorting
d) A key that stores passwords
Your answer (a/b/c/d): a
 Correct!

10. Which SQL statement is used to update data in a table?
a) MODIFY
b) UPDATE
c) CHANGE
d) ALTER
Your answer (a/b/c/d): b
 Correct!

 Your Final Score: 10/10
 Perfect! You're a DBMS master!'''


