"""models.py"""
from sqlalchemy import Column, DateTime, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship

from flask import url_for, Markup

from flask_appbuilder import Model
from flask_appbuilder.models.decorators import renders
from flask_appbuilder.models.mixins import AuditMixin


class Project(Model):
    """Project Table"""
    id           = Column(Integer, primary_key=True)
    name         = Column(String(50), unique = True, nullable=False)
    description  = Column(String(300), nullable=True)

    def __repr__(self):
        return self.name.__str__()


class Task(Model):
    """Task Table"""
    id          = Column(Integer, primary_key=True)
    name        = Column(String(50), unique=True, nullable=False)
    description = Column(String(300), nullable=True)
    project_id  = Column(Integer, ForeignKey(Project.id))
    project     = relationship('Project', foreign_keys='Task.project_id')

    def __repr__(self):
        return self.name.__str__()

    @renders('project.name')
    def project_url(self):
        url = url_for('ProjectModelView.show', pk=str(self.project_id))
        return Markup(f'<a href="{url}">{self.project.name}</a>')


class TaskProgress(AuditMixin, Model):
    """TaskProgress Table"""
    id          = Column(Integer, primary_key=True)
    task_id     = Column(Integer, ForeignKey(Task.id))
    start_time  = Column(DateTime, nullable=False)
    end_time    = Column(DateTime, nullable=True)
    status      = Column(Enum('QUEUED', 'STARTED', 'FINISHED', 'FAILED',
                              'PAUSED', 'CANCELED', name='StatusEnum'),
                         default='STARTED', nullable=False)
    comment     = Column(String(300), nullable=True)
    task        = relationship('Task', foreign_keys='TaskProgress.task_id')
