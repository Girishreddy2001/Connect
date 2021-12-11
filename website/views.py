from flask import Blueprint, render_template, request, flash, jsonify,redirect,url_for
from flask_login import login_required, current_user
from sqlalchemy.sql.elements import Null
from .models import adj_list,User 
from .code import Graph1 
from . import db
import json
from .visualize import visual

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    nodes = User.query.all()
    edges = adj_list.query.all()
    g = Graph1(nodes,edges)
    level1 = g.level_1(current_user.id)
    friends = []
    friends_2 = []
    if len(level1) == 0:
        for i in nodes:
           if current_user.college == i.college:
    
               friends_2.append([i.id,i.first_name,i.skill," "])
        return render_template("home.html", user=current_user,friends=friends,friends_2=friends_2)
    
    for i in nodes:
        if i.id in level1:
            friends.append(i)


    level2 = g.level_2(current_user.id)
    sim = g.jacc_similarity(current_user.id,level2)
    
    sim = dict(sim)
    for i in nodes:
        if i.id in level2:
            friends_2.append([i.id,i.first_name,i.skill,sim[i.id]])
    friends_2 = sorted(friends_2,key=lambda x:x[3],reverse=True)        
    
    
    return render_template("home.html", user=current_user,friends=friends,friends_2=friends_2[:5],sim=sim)

@views.route('/add/<int:friend_id>', methods=['GET', 'POST'])
def add(friend_id):
        
        add_adj = adj_list(user_id=current_user.id,friend=friend_id)
        db.session.add(add_adj)
        db.session.commit()
        return redirect("/")   

@views.route('/remove/<int:friend_id>', methods=['GET', 'POST'])
def remove(friend_id):
        
        remove_adj = adj_list.query.filter_by(user_id = current_user.id, friend=friend_id).first()
        if remove_adj!=None:
            db.session.delete(remove_adj)
            db.session.commit()
        else:
            remove_adj = adj_list.query.filter_by(user_id = friend_id, friend=current_user.id).first()
            db.session.delete(remove_adj)
            db.session.commit()
        return redirect("/")   

@views.route('/showgraph')
def showgraph():
    net = visual()
    return redirect("/admin")
@views.route('/welcome')
def welcome():
    return render_template("welcome.html",user=current_user)


