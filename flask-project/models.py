  2 from flask_sqlalchemy import SQLAlchemy
  3
  4
  5 db = SQLAlchemy()
  6
  7 class Ticket(db.Model):
  8     id = db.Column(db.Integer, primary_key=True)
  9     name = db.Column(db.String(100), nullable=False)
 10     status = db.Column(db.Integer, nullable=False)
 11     url = db.Column(db.String(100), nullable=True)
 12
 13     statuses_dict = {
 14         0: 'Reported',
 15         1: 'In Progress',
 16         2: 'In Review',
 17         3: 'Resolved'
 18     }
 19
 20 def status_string(self):
 21     return self.statuses_dict[self.status]
