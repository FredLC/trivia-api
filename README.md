# Udacity Trivia

This is an app that allow users to play a trivia game and test their knowledge on various subjects such as Art and Geography. This project is still in its early phase. At the moment, users can see questions and answers based on category.They can also choose to have random questions generated on all topics or just a specific one, and have their score displayed at the end of the game. Users also have the possibility to create questions and search for questions.

## Local Setup

### Backend

Make sure you have **Python 3** installed.

- Clone this repository
- Create a virtual environment (follow this [link](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/) if you are not sure how to do that)
- Navigate to the backend directory and run:

```
pip install -r requirements.txt
```

#### Setup databases for local use and tests:

```
psql trivia < trivia.psql
```

```
psql trivia_test < trivia.psql
```

#### Start the server

Export the app name variable:

```
export FLASK_APP=flaskr
```

Then run:

```
flask run --reload
```

#### Tests

Here is the command to run the tests:

```
python test_flaskr.py
```

### Frontend

Navigate to the backend directory and install dependencies by running:

```
npm install
```

Start the app:

```
npm start
```

## API documentation

**Base url:** `http://127.0.0.1:5000`

### Endpoints

#### GET /categories

Returns a list of all categories and success value.

**Sample:** `http://127.0.0.1:5000/categories`

```
{
    "categories": [
        {
            "id": 1,
            "type": "Science"
        },
        {
            "id": 2,
            "type": "Art"
        },
        {
            "id": 3,
            "type": "Geography"
        },
        {
            "id": 4,
            "type": "History"
        },
        {
            "id": 5,
            "type": "Entertainment"
        },
        {
            "id": 6,
            "type": "Sports"
        }
    ],
    "success": true
}
```

#### GET /questions

Queries all questions in the database, paginated by default with ten questions per page. It also returns the total number of questions, current category and list of categories.

**Sample:** `http://127.0.0.1:5000/questions?page=2`

```
{
    "categories": [
        {
            "id": 1,
            "type": "Science"
        },
        {
            "id": 2,
            "type": "Art"
        },
        {
            "id": 3,
            "type": "Geography"
        },
        {
            "id": 4,
            "type": "History"
        },
        {
            "id": 5,
            "type": "Entertainment"
        },
        {
            "id": 6,
            "type": "Sports"
        }
    ],
    "current_category": 1,
    "questions": [
        {
            "answer": "Agra",
            "category": 3,
            "difficulty": 2,
            "id": 15,
            "question": "The Taj Mahal is located in which Indian city?"
        },
        {
            "answer": "Escher",
            "category": 2,
            "difficulty": 1,
            "id": 16,
            "question": "Which Dutch graphic artist–initials M C was a creator of optical illusions?"
        },
        {
            "answer": "Mona Lisa",
            "category": 2,
            "difficulty": 3,
            "id": 17,
            "question": "La Giaconda is better known as what?"
        },
        {
            "answer": "One",
            "category": 2,
            "difficulty": 4,
            "id": 18,
            "question": "How many paintings did Van Gogh sell in his lifetime?"
        },
        {
            "answer": "Jackson Pollock",
            "category": 2,
            "difficulty": 2,
            "id": 19,
            "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
        },
        {
            "answer": "The Liver",
            "category": 1,
            "difficulty": 4,
            "id": 20,
            "question": "What is the heaviest organ in the human body?"
        },
        {
            "answer": "Alexander Fleming",
            "category": 1,
            "difficulty": 3,
            "id": 21,
            "question": "Who discovered penicillin?"
        },
        {
            "answer": "Blood",
            "category": 1,
            "difficulty": 4,
            "id": 22,
            "question": "Hematology is a branch of medicine involving the study of what?"
        },
        {
            "answer": "Scarab",
            "category": 4,
            "difficulty": 4,
            "id": 23,
            "question": "Which dung beetle was worshipped by the ancient Egyptians?"
        }
    ],
    "success": true,
    "total_questions": 19
}
```

#### GET /categories/{category_id}/questions

Get all questions for given category. Returns a success value, a list of questions, total number of questions and current category.

**Sample:** `http://127.0.0.1/categories/4/questions`

```
{
    "current_category": 4,
    "questions": [
        {
            "answer": "Maya Angelou",
            "category": 4,
            "difficulty": 2,
            "id": 5,
            "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
        },
        {
            "answer": "Muhammad Ali",
            "category": 4,
            "difficulty": 1,
            "id": 9,
            "question": "What boxer's original name is Cassius Clay?"
        },
        {
            "answer": "George Washington Carver",
            "category": 4,
            "difficulty": 2,
            "id": 12,
            "question": "Who invented Peanut Butter?"
        },
        {
            "answer": "Scarab",
            "category": 4,
            "difficulty": 4,
            "id": 23,
            "question": "Which dung beetle was worshipped by the ancient Egyptians?"
        }
    ],
    "success": true,
    "total_questions": 4
}
```

#### DELETE /questions/{question_id}

Deletes question using given id if it exists. Returns a success value, the id of the deleted question, a list of current questions, total number of questions and current category.

**Sample:** `http://127.0.0.1/questions/2`

```
{
    "current_category": 1,
    "deleted": 2,
    "questions": [
        {
            "answer": "Maya Angelou",
            "category": 4,
            "difficulty": 2,
            "id": 5,
            "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
        },
        {
            "answer": "Muhammad Ali",
            "category": 4,
            "difficulty": 1,
            "id": 9,
            "question": "What boxer's original name is Cassius Clay?"
        },
        {
            "answer": "Tom Cruise",
            "category": 5,
            "difficulty": 4,
            "id": 4,
            "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
        },
        {
            "answer": "Edward Scissorhands",
            "category": 5,
            "difficulty": 3,
            "id": 6,
            "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
        },
        {
            "answer": "Brazil",
            "category": 6,
            "difficulty": 3,
            "id": 10,
            "question": "Which is the only team to play in every soccer World Cup tournament?"
        },
        {
            "answer": "Uruguay",
            "category": 6,
            "difficulty": 4,
            "id": 11,
            "question": "Which country won the first ever soccer World Cup in 1930?"
        },
        {
            "answer": "George Washington Carver",
            "category": 4,
            "difficulty": 2,
            "id": 12,
            "question": "Who invented Peanut Butter?"
        },
        {
            "answer": "Lake Victoria",
            "category": 3,
            "difficulty": 2,
            "id": 13,
            "question": "What is the largest lake in Africa?"
        },
        {
            "answer": "The Palace of Versailles",
            "category": 3,
            "difficulty": 3,
            "id": 14,
            "question": "In which royal palace would you find the Hall of Mirrors?"
        },
        {
            "answer": "Agra",
            "category": 3,
            "difficulty": 2,
            "id": 15,
            "question": "The Taj Mahal is located in which Indian city?"
        }
    ],
    "success": true,
    "total_questions": 18
}
```

#### POST /questions

Creates a new question using submitted question value, answer, difficulty and category. If a search term is present as a parameter, it will filter the list of questions to match the search term. When a question is posted, the endpoint will return a success value, the id of the created question, a list of questions, total number of questions and current category. If a search term is present, it will return a success value, a list of questions matching the search term and total number of questions filtered.

**Sample:** `curl http://127.0.0.1:5000/questions -X POST -H "Content-Type: application/json" -d '{"question":"What is the only state in the United States that does not have a flag in a shape with 4 edges?", "answer":"Ohio", "difficulty": 1, "category": 3}'`

```
{
   "created":25,
   "current_category":1,
   "questions":[
      {
         "answer":"Maya Angelou",
         "category":4,
         "difficulty":2,
         "id":5,
         "question":"Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
      },
      {
         "answer":"Muhammad Ali",
         "category":4,
         "difficulty":1,
         "id":9,
         "question":"What boxer's original name is Cassius Clay?"
      },
      {
         "answer":"Tom Cruise",
         "category":5,
         "difficulty":4,
         "id":4,
         "question":"What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
      },
      {
         "answer":"Edward Scissorhands",
         "category":5,
         "difficulty":3,
         "id":6,
         "question":"What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
      },
      {
         "answer":"Brazil",
         "category":6,
         "difficulty":3,
         "id":10,
         "question":"Which is the only team to play in every soccer World Cup tournament?"
      },
      {
         "answer":"Uruguay",
         "category":6,
         "difficulty":4,
         "id":11,
         "question":"Which country won the first ever soccer World Cup in 1930?"
      },
      {
         "answer":"George Washington Carver",
         "category":4,
         "difficulty":2,
         "id":12,
         "question":"Who invented Peanut Butter?"
      },
      {
         "answer":"Lake Victoria",
         "category":3,
         "difficulty":2,
         "id":13,
         "question":"What is the largest lake in Africa?"
      },
      {
         "answer":"The Palace of Versailles",
         "category":3,
         "difficulty":3,
         "id":14,
         "question":"In which royal palace would you find the Hall of Mirrors?"
      },
      {
         "answer":"Agra",
         "category":3,
         "difficulty":2,
         "id":15,
         "question":"The Taj Mahal is located in which Indian city?"
      }
   ],
   "success":true,
   "total_questions":19
}
```

**Sample search:** `curl http://127.0.0.1:5000/questions -X POST -H "Content-Type: application/json" -d '{"searchTerm": "1990"}'`

```
{
   "questions":[
      {
         "answer":"Edward Scissorhands",
         "category":5,
         "difficulty":3,
         "id":6,
         "question":"What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
      }
   ],
   "success":true,
   "total_questions":1
}
```

#### POST /quizzes

Generates a random question in a given category (if no category was submitted, it generates a random question in all categories). The endpoint also takes in a list of previous questions to make sure the randomly generated question was not asked before.

**Sample:** `curl http://127.0.0.1:5000/quizzes -X POST -H "Content-Type: application/json" -d '{"previous_questions": [], "quiz_category": {"type": "Science", "id": 1}}'`

```
{
   "question":{
      "answer":"The Liver",
      "category":1,
      "difficulty":4,
      "id":20,
      "question":"What is the heaviest organ in the human body?"
   },
   "success":true
}
```

### Error responses

The following error codes are handled by the app:

- 400 Bad Request
- 404 Not Found
- 405 Method Not Allowed
- 422 Unprocessable

**Sample:**

```
{
    "error": 404,
    "message": "resource not found",
    "success": false
}
```
