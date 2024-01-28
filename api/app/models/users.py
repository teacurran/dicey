from datetime import datetime
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, ForeignKey, String, DateTime, Enum, Boolean, UniqueConstraint, BigInteger
from app import db
print('importing module %s' % __name__)


class User(db.Model):
    __tablename__ = 'users'

    id = Column(BigInteger, primary_key=True)
    name = Column(String(255))
    ip_address = Column(String(255))
    session_id = Column(String(255))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)
    connected = Column(Boolean, default=False)

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)

    def to_json(self):
        json = {
            'id': self.id,
            'name': self.name,
            'ip_address': self.ip_address,
            'connected': self.connected,
            'ship': self.ship,
            'move': self.move,
            'ready': self.ready,
            'npc': self.npc,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }
        return json

    @staticmethod
    def from_json(json):
        instance = User(
            name=json.get('name'),
            ip_address=json.get('ip_address')
        )
        return instance
