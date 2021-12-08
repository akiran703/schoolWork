from re import L
import bcrypt
from flask import Flask,render_template,url_for,redirect, request,session
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin,login_user,LoginManager,login_required,logout_user,current_user
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,IntegerField
from wtforms.validators import InputRequired,Length,ValidationError
from flask_bcrypt import Bcrypt
from flask_bootstrap import Bootstrap
import sqlite3
from wtforms.widgets.core import EmailInput
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "Practice.db")

storepassword = ""
app = Flask(__name__)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
bootstrap = Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY']='thisisasecertkey'

login_manager  = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(20),unique = True,nullable= False)
    password = db.Column(db.String(80),unique = True,nullable = False)




class RegisterForm(FlaskForm):
    username = StringField(validators=[InputRequired(),Length(min = 4,max=20)],render_kw={"placeholder":"username"})
    email = StringField(validators=[InputRequired(),Length(min = 4,max=20)],render_kw={"placeholder":"email"})
    password = PasswordField(validators=[InputRequired(),Length(min = 4,max=20)],render_kw={"placeholder":"password"})
    submit = SubmitField('Register')
    def validate_user(self,username):
        existingusername = User.query.filter_by(username = username.data).first()
        if existingusername:
            raise ValidationError("the user already exists")

class LoginForm(FlaskForm):
    username = StringField(validators=[InputRequired(),Length(min = 4,max=20)],render_kw={"placeholder":"username"})
    password = PasswordField(validators=[InputRequired(),Length(min = 4,max=20)],render_kw={"placeholder":"password"})
    submit = SubmitField('Log In')

class DishForm(FlaskForm):
    name = StringField(validators=[InputRequired(),Length(min = 1,max=90)],render_kw={"placeholder":"name"})
    id = IntegerField(validators=[InputRequired()],render_kw={"placeholder":"id"})
    minutes = IntegerField(validators=[InputRequired()],render_kw={"placeholder":"minutes"})
    contributor_id = IntegerField(validators=[InputRequired()],render_kw={"placeholder":"contributor id"})
    submitted = StringField(validators=[InputRequired(),Length(min = 1,max=90)],render_kw={"placeholder":"submitted"})
    tags =StringField(validators=[InputRequired(),Length(min = 1,max=90)],render_kw={"placeholder":"tags"})
    nutrition = StringField(validators=[InputRequired(),Length(min = 1,max=90)],render_kw={"placeholder":"nutrition"})
    steps = StringField(validators=[InputRequired(),Length(min = 1,max=90)],render_kw={"placeholder":"steps"})
    n_steps = IntegerField(validators=[InputRequired()],render_kw={"placeholder":"n_steps"})
    description = StringField(validators=[InputRequired(),Length(min = 1,max=50)],render_kw={"placeholder":"description"})
    ingredients = StringField(validators=[InputRequired(),Length(min = 1,max=150)],render_kw={"placeholder":"ingredients"})
    n_ingredients = IntegerField(validators=[InputRequired()],render_kw={"placeholder":"n_ingredients"})
    usernameid =  StringField(validators=[InputRequired(),Length(min = 1,max=50)],render_kw={"placeholder":"usernameid"})
    submit = SubmitField('enter')


class ExerciseForm(FlaskForm):
    exercise = StringField(validators=[InputRequired(),Length(min = 1,max=100)],render_kw={"placeholder":"exercise"})
    equipment = StringField(validators=[InputRequired(),Length(min = 1,max=100)],render_kw={"placeholder":"equipment"})
    exerciseType = StringField(validators=[InputRequired(),Length(min = 1,max=100)],render_kw={"placeholder":"exercise type"})
    MajorMuscle = StringField(validators=[InputRequired(),Length(min = 1,max=100)],render_kw={"placeholder":"MajorMuscle"})
    MinorMuscle = StringField(validators=[InputRequired(),Length(min = 1,max=100)],render_kw={"placeholder":"MinorMuscle"})
    Example = StringField(validators=[InputRequired(),Length(min = 1,max=100)],render_kw={"placeholder":"Example"})
    Notes = StringField(validators=[InputRequired(),Length(min = 1,max=100)],render_kw={"placeholder":"Notes"})
    Modifications = StringField(validators=[InputRequired(),Length(min = 1,max=100)],render_kw={"placeholder":"Modifications"})
    usernameid = StringField(validators=[InputRequired(),Length(min = 1,max=100)],render_kw={"placeholder":"usernameid"})
    submit = SubmitField('enter')



class ChooseDish(FlaskForm):
    password = PasswordField(validators=[InputRequired(),Length(min = 4,max=20)],render_kw={"placeholder":"password"})
    name = StringField(validators=[InputRequired(),Length(min = 1,max=90)],render_kw={"placeholder":"name"})
    submit = SubmitField('enter')


class ChooseExercise(FlaskForm):
    password = PasswordField(validators=[InputRequired(),Length(min = 4,max=20)],render_kw={"placeholder":"password"})
    name = StringField(validators=[InputRequired(),Length(min = 1,max=90)],render_kw={"placeholder":"name"})
    submit = SubmitField('enter')


class weekPlan(FlaskForm):
    password = PasswordField(validators=[InputRequired(),Length(min = 4,max=20)],render_kw={"placeholder":"password"})
    submit = SubmitField('enter')

class weekplanday(FlaskForm):
    day = StringField(validators=[InputRequired(),Length(min = 1,max=90)],render_kw={"placeholder":"day"})
    exercise = StringField(validators=[InputRequired(),Length(min = 1,max=90)],render_kw={"placeholder":"exercise"})
    dish = StringField(validators=[InputRequired(),Length(min = 1,max=90)],render_kw={"placeholder":"dish"})
    submit = SubmitField('enter')
    
class savePlan(FlaskForm):
    password = PasswordField(validators=[InputRequired(),Length(min = 4,max=20)],render_kw={"placeholder":"password"})
    submit = SubmitField('enter')

class deletePlanExercise(FlaskForm):
    password = PasswordField(validators=[InputRequired(),Length(min = 4,max=20)],render_kw={"placeholder":"password"})
    exercise = StringField(validators=[InputRequired(),Length(min = 1,max=90)],render_kw={"placeholder":"exercise"})
    submit = SubmitField('enter')

class deletePlanDish(FlaskForm):
    password = PasswordField(validators=[InputRequired(),Length(min = 4,max=20)],render_kw={"placeholder":"password"})
    dish = StringField(validators=[InputRequired(),Length(min = 1,max=90)],render_kw={"placeholder":"dish"})
    submit = SubmitField('enter')




@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login',methods = ['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username= form.username.data
        password = form.password.data
        username1  = str(username)
        password = str(password)
        print(username1,password)

        with sqlite3.connect(db_path) as con:
            cur = con.cursor()
            temp1 = cur.execute("select Username from userdatabase where Username = ? ",(username1,) )
            abc = temp1.fetchall()
            temp2 = cur.execute("select password from userdatabase where Username = ? ",(username1,) )
            temp3  = str(temp2.fetchone()[0])
            s = temp3.replace(',', '')
        print(s, password)
        if temp1:
            if s == password:
                #login_user(s)
                storepassword = password
                return redirect(url_for('dashboard'))
    return render_template('login.html',form = form)

@app.route('/logout',methods = ['GET','POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))



@app.route('/dashboard',methods = ['GET','POST'])
#@login_required
def dashboard():
    return render_template('dashboard.html')


@app.route('/inputyourownexercise',methods = ['GET','POST'])
#@login_required
def inputyourownexercise():
    form = ExerciseForm()

    if form.validate_on_submit():
        exercise = form.exercise.data
        equipment = form.equipment.data
        exerciseType = form.exerciseType.data
        MajorMuscle = form.MajorMuscle.data
        MinorMuscle = form.MinorMuscle.data
        Example = form.Example.data
        Notes = form.Notes.data
        Modifications = form.Modifications.data
        usernameid = form.usernameid.data
        with sqlite3.connect(db_path) as con:
            cur = con.cursor()
            cur.execute("insert into user_entered_exercise(Exercise,Equipment,ExerciseType,MajorMuscle,MinorMuscle,Example,Notes,Modifications,usernameid) VALUES (?,?,?,?,?,?,?,?,?)",(exercise,equipment,exerciseType,MajorMuscle,MinorMuscle,Example,Notes,Modifications,usernameid))
    return render_template('inputyourownexercise.html',form = form)

@app.route('/inputyourowndish',methods = ['GET','POST'])
#@login_required
def inputyourowndish():
    form = DishForm()

    if form.validate_on_submit():
        name = form.name.data
        id = form.id.data
        minutes = form.minutes.data
        contributor_id = form.contributor_id.data
        submitted = form.submitted.data
        tags = form.tags.data
        nutrition = form.nutrition.data
        steps = form.steps.data
        n_steps = form.n_steps.data
        description = form.description.data
        ingredients = form.ingredients.data
        n_ingredients = form.n_ingredients.data
        usernameid =  form.usernameid.data
        with sqlite3.connect(db_path) as con:
            cur = con.cursor()
            cur.execute("insert into user_entered_dishes(name,id,minutes,contributor_id,submitted,tags,nutrition,n_steps,steps,description,ingredients,n_ingredients,usernameid) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",(name,id,minutes,contributor_id,submitted,tags,nutrition,steps,n_steps,description,ingredients,n_ingredients,usernameid))
    return render_template('inputyourowndish.html',form = form)

@app.route('/inside',methods = ['GET','POST'])
def weekplandayfun():
    form = weekplanday()
    day = form.day.data
    exercise  = form.exercise.data
    dish = form.dish.data
    
    if form.validate_on_submit():
        with sqlite3.connect(db_path) as con:
            cur = con.cursor()
            cur.execute("INSERT INTO weekPlan(dish_name, exercise_name, week_name) values (?,?,?) ",(dish,exercise,day))

    #session['exercisestuff']
    #session['dishstuff'] 
    return render_template('insideweek.html',form =form)

@app.route('/weekplan',methods = ['GET','POST'])
def weekplan():
    form = weekPlan()
    password = form.password.data
    
    if form.validate_on_submit():
        with sqlite3.connect(db_path) as con:
            cur = con.cursor()
            temp = cur.execute("""select dish_name from user_food where password = ?
                               UNION
                                select name 
                                from user_entered_dishes UD , userdatabase U
                                where U.username = UD.usernameid
                                and U.password = ?""",(password,password,))
            food = temp.fetchall()

        with sqlite3.connect(db_path) as con:
            cur = con.cursor()
            temp = cur.execute("""select exercise_name from user_exercise where password = ?
            UNION
            select exercise 
            from user_entered_exercise UE , userdatabase U
            where U.username = UE.usernameid
            and U.password = ?""",(password,password,))
            result = temp.fetchall()
        with sqlite3.connect(db_path) as con:
            cur = con.cursor()
            temp = cur.execute("""SELECT S.numOfInputEx+E.numOfSavedEx+SE.numOfSE
                    FROM(SELECT IFNULL(N1, 0) as numOfInputEx
                        FROM (SELECT username, password FROM userdatabase) R
                        LEFT OUTER JOIN
                            (SELECT pass,IFNULL(num, 0) as N1
                            FROM (SELECT U.password as pass, count(exercise_name_entered) as num
                                    FROM user_exercise_entered UE, userdatabase U
                                    WHERE U.password = UE.password
                                    AND U.password = "{}") U1) W
                        ON R.password = W.pass
                        WHERE R.password = "{}") S,
                        (SELECT IFNULL(N2, 0) as numOfSavedEx
                        FROM (SELECT username, password FROM userdatabase) R
                        LEFT OUTER JOIN
                            (SELECT pass,IFNULL(num, 0) as N2
                            FROM (SELECT U.password as pass, count(exercise_name) as num
                                    FROM user_exercise UE, userdatabase U
                                    WHERE U.password = UE.password
                                    AND U.password = "{}") U2) W1
                        ON R.password = W1.pass
                        WHERE R.password = "{}") E,
                        (SELECT IFNULL(N3, 0) as numOfSE
                        FROM (SELECT username, password FROM userdatabase) R
                        LEFT OUTER JOIN
                            (SELECT pass,IFNULL(num, 0) as N3
                            FROM (SELECT U.password as pass, count(Exercise) as num
                                    FROM user_entered_exercise UE, userdatabase U
                                    WHERE U.Username = UE.usernameid
                                    AND U.password = "{}") U2) W1
                        ON R.password = W1.pass
                        WHERE R.password = "{}") SE""".format(password,password,password,password,password,password))
            countE = temp.fetchall()
        with sqlite3.connect(db_path) as con:
            cur = con.cursor()
            temp = cur.execute("""SELECT S.numOfInputD+E.numOfSavedD+SE.numOfSE
                                FROM(SELECT IFNULL(N1, 0) as numOfInputD
                                    FROM (SELECT username, password FROM userdatabase) R
                                    LEFT OUTER JOIN
                                        (SELECT pass,IFNULL(num, 0) as N1
                                        FROM (SELECT U.password as pass, count(dish_name_entered) as num
                                                FROM user_food_entered UD, userdatabase U
                                                WHERE U.password = UD.password
                                                AND U.password = '{}') U1) W
                                    ON R.password = W.pass
                                    WHERE R.password = '{}') S,
                                    (SELECT IFNULL(N2, 0) as numOfSavedD
                                    FROM (SELECT username, password FROM userdatabase) R
                                    LEFT OUTER JOIN
                                        (SELECT pass,IFNULL(num, 0) as N2
                                        FROM (SELECT U.password as pass, count(dish_name) as num
                                                FROM user_food UD, userdatabase U
                                                WHERE U.password = UD.password
                                                AND U.password = '{}') U2) W1
                                    ON R.password = W1.pass
                                    WHERE R.password = '{}') E,
                                    (SELECT IFNULL(N3, 0) as numOfSE
                                    FROM (SELECT username, password FROM userdatabase) R
                                    LEFT OUTER JOIN
                                        (SELECT pass,IFNULL(num, 0) as N3
                                        FROM (SELECT U.password as pass, count(name) as num
                                                FROM user_entered_dishes UD, userdatabase U
                                                WHERE U.Username = UD.usernameid
                                                AND U.password = "{}") U2) W1
                                    ON R.password = W1.pass
                                    WHERE R.password = "{}") SE""".format(password,password,password,password,password,password))
            countD = temp.fetchall()
        session['countE'] = countE   
        session['countD'] = countD
        session['exercisestuff'] = result
        session['dishstuff'] = food
        return redirect(url_for('weekplandayfun'))
    return render_template('weekplanner.html',form =form)









@app.route('/insidedeleteexercise',methods = ['GET','POST'])
def deletestuffexercise():
    form = deletePlanExercise()
    password = form.password.data 
    exercise  = form.exercise.data

    
    if form.validate_on_submit():
        with sqlite3.connect(db_path) as con:
            cur = con.cursor()
            cur.execute("DELETE from user_exercise where exercise_name = ? and password = ? ",(exercise,password))
        return render_template('delete.html',form = form)

  
    return render_template('delete.html',form = form)

@app.route('/insidedeletedish',methods = ['GET','POST'])
def deletestuffdish():
    
    form1 = deletePlanDish()
    password1 = form1.password.data
    dish = form1.dish.data
    

    if form1.validate_on_submit():
        with sqlite3.connect(db_path) as con:
            cur = con.cursor()
            cur.execute("DELETE from user_food where dish_name = ? and password = ? ",(dish,password1))
        return render_template('deletedish.html',form =form1)
  

    return render_template('deletedish.html',form= form1)



@app.route('/deleteplandish',methods = ['GET','POST'])
def deleteplanfunc():
    form = weekPlan()
    password = form.password.data
    
    if form.validate_on_submit():
        with sqlite3.connect(db_path) as con:
            cur = con.cursor()
            temp = cur.execute("select dish_name from user_food where password = ?",(password,))
            food = temp.fetchall()

    
        session['dishstuff'] = food
        return redirect(url_for('deletestuffdish'))
    return render_template('weekplanner.html',form =form)






@app.route('/deleteplanexercise',methods = ['GET','POST'])
def deleteplanfuncexercise():
    form = weekPlan()
    password = form.password.data
    
    if form.validate_on_submit():
     
        with sqlite3.connect(db_path) as con:
            cur = con.cursor()
            temp = cur.execute("select exercise_name from user_exercise where password = ?",(password,))
            result = temp.fetchall()
        session['exercisestuff'] = result
        return redirect(url_for('deletestuffexercise'))
    return render_template('weekplanner.html',form =form)













@app.route('/register',methods = ['GET','POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        username = form.username.data
        emailinput = form.email.data
        password = form.password.data
        with sqlite3.connect(db_path) as con:
            cur = con.cursor()
            cur.execute("INSERT INTO userdatabase (Username,email,password) VALUES (?,?,?)",(username,emailinput,password) )
        return redirect(url_for('login'))

    return render_template('register.html',form = form)

# HANNAH
@app.route('/searchExercise',methods = ['GET','POST'])
def searchExercise():
    if request.method == 'POST':
        form = request.form
        search_value = form['search_string']
        filter_value = form['filter']
        with sqlite3.connect(db_path) as con:
            cur = con.cursor()
            cur.execute("""SELECT MajorMuscleFilter.Exercise FROM  MajorMuscleFilter, Exercise WHERE MajorMuscleFilter.exercise = exercise.exercise AND MajorMuscleFilter.Exercise LIKE '%{}%' AND MajorMuscle LIKE '%{}%';""".format(search_value,filter_value))
            results = cur.fetchall()
        return render_template('searchE.html', results = results)
    else:
        return render_template('searchE.html')

@app.route('/searchDish',methods = ['GET','POST'])
def searchDish():
    if request.method == 'POST':
        form = request.form
        search_value = form['search_string']
        filter_value = form['filter']
        with sqlite3.connect(db_path) as con:
            cur = con.cursor()
            cur.execute("""SELECT tagFilter.name FROM dishes, tagFilter WHERE tagFilter.name = dishes.name AND tagFilter.name LIKE '%{}%' AND tagFilter.tags LIKE '%{}%';""".format(search_value,filter_value))
            results = cur.fetchall()
        return render_template('searchD.html', results = results)   
    else:
        return render_template('searchD.html')
    



# NOT DONE IDK HOW TO CONNECT TO ONLY SEARCH RESULT
@app.route('/viewExercise/<exercise>',methods = ['GET','POST'])
def viewExercise(exercise):
    form = ChooseExercise()
    with sqlite3.connect(db_path) as con:
        cur = con.cursor()
        cur.execute("""SELECT * FROM exercise WHERE exercise LIKE '%{}%';""".format(exercise))
        results = cur.fetchall()

    if form.validate_on_submit():
        password = form.password.data
        exercise = form.name.data
        with sqlite3.connect(db_path) as con:
            cur = con.cursor()
            cur.execute("INSERT INTO user_exercise (password, exercise_name) VALUES (?,?)",(password,exercise) )
    return render_template('viewE.html', results = results,form = form) 

@app.route('/viewDish/<name>',methods =['GET','POST'])
def viewDish(name):
    form = ChooseDish()
    with sqlite3.connect(db_path) as con:
        cur = con.cursor()
        cur.execute("""SELECT * FROM dishes WHERE name LIKE '%{}%';""".format(name))
        results = cur.fetchall()

    if form.validate_on_submit():
        password = form.password.data
        dish = form.name.data
        with sqlite3.connect(db_path) as con:
            cur = con.cursor()
            cur.execute("INSERT INTO user_food (password, dish_name) VALUES (?,?)",(password,dish) )


    return render_template('viewD.html', results = results,form = form) 

@app.route('/showOutline')
def show():
    return render_template('showOutline.html')

@app.route('/save',methods = ['GET','POST'])
def saveOutline():
    form = savePlan()
    password = form.password.data
    
    if form.validate_on_submit():    
            with sqlite3.connect(db_path) as con:
                cur = con.cursor()
                cur.execute("""SELECT week_name, dish_name, exercise_name
                            FROM weekPlan W
                            WHERE W.dish_name IN (SELECT dish_name FROM user_food WHERE password = "{}")
                            AND W.exercise_name IN (SELECT exercise_name FROM user_exercise WHERE password = "{}")
                            ORDER BY 
                                CASE
                                    WHEN week_name = 'Sunday' THEN 1
                                    WHEN week_name = 'Monday' THEN 2
                                    WHEN week_name = 'Tuesday' THEN 3
                                    WHEN week_name = 'Wednesday' THEN 4
                                    WHEN week_name = 'Thursday' THEN 5
                                    WHEN week_name = 'Friday' THEN 6
                                    WHEN week_name = 'Saturday' THEN 7
                                END ASC""".format(password, password))
                results = cur.fetchall()
            with sqlite3.connect(db_path) as con:
                cur = con.cursor()
                temp = cur.execute("""SELECT R1.week_name, IFNULL(numD, 0) as numOfDish, IFNULL(numE, 0) as numOfExercise
                FROM (SELECT username, password FROM userdatabase) R
                LEFT OUTER JOIN
                    (SELECT UE.password, week_name, count(W.dish_name) as numD, count(W.exercise_name) as numE
                    FROM weekPlan W, user_food UF, user_exercise UE
                    WHERE UF.dish_name = W.dish_name
                    AND UE.exercise_name = W.exercise_name
                    AND UE.password = UF.password
                    AND UF.password = '{}'
                    GROUP BY week_name) R1
                ON R.password = R1.password
                WHERE R.password = '{}'""".format(password,password))
                count = temp.fetchall()
            
            
            
            with sqlite3.connect(db_path) as con:
                cur = con.cursor()
                cur.execute("""SELECT week_name, IFNULL(dish_name,0), IFNULL(exercise_name,0)
                            FROM weekPlan W
                            WHERE W.dish_name IN (SELECT name 
                                                    from user_entered_dishes UD , userdatabase U
                                                    where U.username = UD.usernameid
                                                    and U.password = "{}")
                            OR W.exercise_name IN (SELECT exercise 
                                                    from user_entered_exercise UE , userdatabase U
                                                    where U.username = UE.usernameid
                                                    and U.password = "{}")
                            ORDER BY 
                                CASE
                                    WHEN week_name = 'Sunday' THEN 1
                                    WHEN week_name = 'Monday' THEN 2
                                    WHEN week_name = 'Tuesday' THEN 3
                                    WHEN week_name = 'Wednesday' THEN 4
                                    WHEN week_name = 'Thursday' THEN 5
                                    WHEN week_name = 'Friday' THEN 6
                                    WHEN week_name = 'Saturday' THEN 7
                                END ASC""".format(password, password))
                results2 = cur.fetchall()
            with sqlite3.connect(db_path) as con:
                cur = con.cursor()
                temp = cur.execute("""SELECT R1.week, IFNULL(numD, 0) as numOfDish, IFNULL(numE, 0) as numOfExercise
                                    FROM (SELECT username, password FROM userdatabase) R
                                    LEFT OUTER JOIN
                                        (SELECT T1.pass as P1, W.week_name as week, count(W.dish_name) as numD, count(W.exercise_name) as numE
                                        FROM weekPlan W, (SELECT U.password as pass,name 
                                                            from user_entered_dishes UD , userdatabase U
                                                            where U.username = UD.usernameid
                                                            and U.password = "{}") T1, (SELECT U.password as pass, exercise 
                                                                from user_entered_exercise UE , userdatabase U
                                                                where U.username = UE.usernameid
                                                                and U.password = "{}") T2
                                        WHERE W.dish_name = T1.name
                                        AND W.exercise_name = T2.exercise
                                        GROUP BY week_name) R1
                                    ON R.password = R1.P1
                                    WHERE R.password = '{}'""".format(password,password,password))
                count2 = temp.fetchall()
            return render_template('showOutline.html', results=results,form = form, count = count, results2=results2, count2=count2)
    return render_template('save.html', form = form)
if __name__ == '__main__':
    app.run(debug=True)
