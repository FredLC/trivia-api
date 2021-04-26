import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10

def create_app(test_config=None):
  app = Flask(__name__)
  setup_db(app)
  CORS(app)
  
  # Setup CORS
  @app.after_request
  def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
    response.headers.add('Access-Control-Allow-Methods', 'GET,POST,DELETE,OPTIONS')
    return response

  
  def paginate_questions(request, list):
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE

    questions = [question.format() for question in list]

    return questions[start:end]

  
  @app.route('/categories')
  def get_categories():
    categories = Category.query.all()
    formatted_categories = [category.format() for category in categories]

    if len(categories) == 0:
      abort(404)

    return jsonify({
      'success': True,
      'categories': formatted_categories
    })


  @app.route('/questions')
  def get_questions():
    questions = Question.query.all()
    current_questions = paginate_questions(request, questions)

    if len(current_questions) == 0:
      abort(404)

    categories = Category.query.all()
    formatted_categories = [category.format() for category in categories]

    return jsonify({
      'success': True,
      'questions': current_questions,
      'total_questions': len(questions),
      'current_category': 1,
      'categories': formatted_categories
    })

  
  @app.route('/questions/<int:question_id>', methods=['DELETE'])
  def delete_question(question_id):
    try:
      question = Question.query.filter(Question.id == question_id).one_or_none()

      if question is None:
        abort(404)

      question.delete()

      questions = Question.query.all()
      current_questions = paginate_questions(request, questions)

      return jsonify({
        'success': True,
        'deleted': question.id,
        'questions': current_questions,
        'total_questions': len(questions),
        'current_category': 1
      })

    except:
      abort(422)


  @app.route('/questions', methods=['POST'])
  def create_question():
    body = request.get_json()

    question = body.get('question', None)
    answer = body.get('answer', None)
    difficulty = body.get('difficulty', None)
    category = body.get('category', None)
    search_term = body.get('searchTerm', None)

    try:
      if search_term:
        questions = Question.query.filter(Question.question.ilike(f"%{search_term}%")).all()
        current_questions = paginate_questions(request, questions)

        return jsonify({
          'success': True,
          'questions': current_questions,
          'total_questions': len(questions)
        })
      else:
        question = Question(question=question, answer=answer, difficulty=difficulty, category=category)

        question.insert()

        questions = Question.query.all()
        current_questions = paginate_questions(request, questions)

        return jsonify({
          'success': True,
          'created': question.id,
          'questions': current_questions,
          'total_questions': len(questions),
          'current_category': 1
        })

    except:
      abort(422)

  
  @app.route('/categories/<int:category_id>/questions')
  def get_questions_by_category(category_id):
    category = Category.query.filter(Category.id == category_id).one_or_none()

    if category is None:
      abort(404)

    questions = Question.query.filter(Question.category == category.id).all()
    formatted_questions = [question.format() for question in questions]

    if len(questions) == 0:
      abort(404)

    return jsonify({
      'success': True,
      'questions': formatted_questions,
      'total_questions': len(questions),
      'current_category': category.id
    })


  def random_with_exclude(exclude_list, choice_list):
    rand = random.choice(choice_list)
    return random_with_exclude(exclude_list, choice_list) if rand['id'] in exclude_list else rand

  @app.route('/quizzes', methods=['POST'])
  def generate_random_question():
    body = request.get_json()

    previous_questions = body.get('previous_questions', None)
    quiz_category = body.get('quiz_category', None)

    if quiz_category['id'] == 0:
      questions = Question.query.all()
    else:
      questions = Question.query.filter(Question.category == quiz_category['id']).all()

    formatted_questions = [question.format() for question in questions]

    if len(previous_questions) != len(questions): 
      question = random_with_exclude(previous_questions, formatted_questions)
    else:
      question = None
  
    return jsonify({
      'success': True,
      'question': question
    })
    

  @app.errorhandler(405)
  def method_not_allowed(error):
    return jsonify({
      'success': False,
      'error': 405,
      'message': 'method not allowed'
    }), 405


  @app.errorhandler(404)
  def resource_not_found(error):
    return jsonify({
      'success': False,
      'error': 404,
      'message': 'resource not found'
    }), 404


  @app.errorhandler(422)
  def unprocessable(error):
    return jsonify({
      'success': False,
      'error': 422,
      'message': 'unprocessable'
    }), 422


  @app.errorhandler(400)
  def bad_request(error):
    return jsonify({
      'success': False,
      'error': 400,
      'message': 'bad request'
    }), 400

  
  return app

    