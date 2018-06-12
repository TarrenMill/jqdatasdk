# coding: utf-8
import datetime
from sqlalchemy import Date, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql import TINYINT, TIMESTAMP, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class STK_STATUS_CHANGE(Base):

    __tablename__ = 'STK_STATUS_CHANGE'

    id = Column(Integer, primary_key=True)
    company_id = Column(Integer, nullable=False, comment="公司ID")
    code = Column(String(12), nullable=False, comment="证券代码")
    name = Column(String(40), comment="证券简称")
    pub_date = Column(Date, nullable=False, comment="公告日期")
    change_date = Column(Date, nullable=False, comment="变更日期")
    change_reason = Column(String(500), comment="变更原因")
    change_type_id = Column(Integer, comment="变更类型编码")
    change_type = Column(String(60), comment="变更类型")
    comments = Column(String(255), comment="备注")
    status = Column(TINYINT(display_width=4), default=0, comment="是否同步,0:未同步,1:已同步")
    addTime = Column(TIMESTAMP, default=datetime.datetime.now, comment="插入时间")
    modTime = Column(TIMESTAMP, default=datetime.datetime.now, comment="最后修改时间")


