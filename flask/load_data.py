"""load_data.py"""
# pylint: disable=R0916, E1101
import sys
import logging
from sqlalchemy import exc

from app import appbuilder, db
from app.models import Task, Project

log = logging.getLogger(__name__)

################## get role Admin ####################
role_admin = appbuilder.sm.find_role(appbuilder.sm.auth_role_admin)
if role_admin is None:
    log.error('Error: please run \'flask fab create-admin\' before loading data!')
    sys.exit(1)

############# configuring role engineers #############
role_engineer = appbuilder.sm.find_role('engineers')
if role_engineer is None:
    appbuilder.sm.add_role('engineers')
    role_engineer = appbuilder.sm.find_role('engineers')

for pv in role_admin.permissions:
    if ('Task' in pv.__repr__() or \
        'TaskModelView' in pv.__repr__() or \
        'Project' in pv.__repr__() or \
        'ProjectModelView' in pv.__repr__() \
       ) and not ( \
        'add' in pv.__repr__() or \
        'delete' in pv.__repr__() or \
        'edit' in pv.__repr__() or \
        'post' in pv.__repr__() or \
        'show' in pv.__repr__() \
       ):
        appbuilder.sm.add_permission_role(role_engineer, pv)
    if 'Task Progress' in pv.__repr__() or \
       'TaskProgressModelView' in pv.__repr__() or \
       'MyPassword' in pv.__repr__() or \
       'mypassword' in pv.__repr__() or \
       ('userinfo' in pv.__repr__() and 'userinfoedit' not in pv.__repr__()) or \
       ('UserInfo' in pv.__repr__() and 'UserInfoEdit' not in pv.__repr__()):
        appbuilder.sm.add_permission_role(role_engineer, pv)

############### configuring role public ##############
role_public = appbuilder.sm.find_role('Public')
if role_public is None:
    appbuilder.sm.add_role('Public')
    role_public = appbuilder.sm.find_role('Public')

for pv in role_admin.permissions:
    if ('Task Progress' in pv.__repr__() or \
        'TaskProgressModelView' in pv.__repr__() or
        'Task Project' in pv.__repr__() \
        ) and not ( \
        'add' in pv.__repr__() or \
        'delete' in pv.__repr__() or \
        'edit' in pv.__repr__() or \
        'post' in pv.__repr__() or \
        'show' in pv.__repr__()):
        appbuilder.sm.add_permission_role(role_public, pv)

######################## adding users #######################
user1 = appbuilder.sm.add_user(
    username='sj', first_name='Steve', last_name='Johnson',
    email='steve.johnson@aol.com', role=role_engineer,
    password='123'
)
user2 = appbuilder.sm.add_user(
    username='js', first_name='Jay', last_name='Smith',
    email='jay.smith@aol.com', role=role_engineer,
    password='123'
)
user3 = appbuilder.sm.add_user(
    username='bh', first_name='Bob', last_name='Hansen',
    email='bob.hansen@aol.com', role=role_engineer,
    password='123'
)

###################### adding projects ################################
try:
    db.session.add(Project(id=1, name="Proj-1"))
    db.session.add(Project(id=2, name="Proj-2"))
    db.session.commit()
except exc.SQLAlchemyError as err:
    log.error("Project creation error: %s", err)
    db.session.rollback()
    sys.exit(1)

############################# adding tasks ############################
try:
    db.session.add(Task(id=1, name="P1T1", project_id=1))
    db.session.add(Task(id=2, name="P1T2", project_id=1))
    db.session.add(Task(id=3, name="P1T3", project_id=1))
    db.session.add(Task(id=4, name="P2T1", project_id=2))
    db.session.add(Task(id=5, name="P2T2", project_id=2))
    db.session.add(Task(id=6, name="P2T3", project_id=2))
    db.session.add(Task(id=7, name="P2T4", project_id=2))
    db.session.add(Task(id=8, name="P2T5", project_id=2))
    db.session.commit()
except exc.SQLAlchemyError as err:
    log.error("Task creation error: %s", err)
    db.session.rollback()
    sys.exit(1)
