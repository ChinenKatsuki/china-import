from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, SMALLINT, Text, Boolean
from config.database import Base
from sqlalchemy.orm import relationship
import datetime
import sys
sys.dont_write_bytecode = True

class User(Base):
    __tablename__ = 'user'
    __table_args__ = {'comment': 'アカウント情報を管理するトランザクションテーブル'}

    user_id = Column(Integer, primary_key=True, comment='ユーザーID')
    first_name = Column(String(20), nullable=False, comment='氏名(名)')
    last_name = Column(String(20), nullable=False, comment='氏名(姓)')
    first_name_kana = Column(String(30), nullable=False, comment='カナ名')
    last_name_kana = Column(String(30), nullable=False, comment='カナ姓')
    email = Column(String(255), nullable=False, comment='メールアドレス')
    created_at = Column(DateTime, default=datetime.datetime.now(), nullable=False, comment='作成日時')
    updated_at = Column(DateTime, default=datetime.datetime.now(), onupdate=datetime.datetime.now(), nullable=False, comment='更新日時')
    deleted_at = Column(DateTime, nullable=True, comment='削除日時')
    auth = relationship('Auth', back_populates='user')
    rakumart_order_all_cost = relationship('RakumartOrderAllCost', back_populates='user')


class Auth(Base):
    __tablename__ = 'auth'
    __table_args__ = {'comment': '認証情報を管理するトランザクションテーブル'}

    auth_id = Column(Integer, primary_key=True, comment='authID')
    user_id = Column(Integer, ForeignKey(User.user_id), comment='ユーザーID')
    passwd = Column(String(255), nullable=False, comment='ログインパスワード sha256を利用する')
    token = Column(String(255), default=1, nullable=False, comment='トークン')
    active_flg = Column(SMALLINT, default=1, nullable=False, comment='有効・無効フラグ')
    created_at = Column(DateTime, default=datetime.datetime.now(), nullable=False, comment='作成日時')
    updated_at = Column(DateTime, default=datetime.datetime.now(), onupdate=datetime.datetime.now(), nullable=False, comment='更新日時')
    deleted_at = Column(DateTime, nullable=True, comment='削除日時')
    user = relationship('User', back_populates='auth')

class RakumartOrderAllCost(Base):
    __tablename__ = 'rakumart_order_all_cost'
    __tabel_args__ = {'comment': 'ラクマート発注経費管理テーブル'}

    purchase_order_id = Column(Integer, primary_key=True, comment='注文書ID')
    user_id = Column(Integer, ForeignKey(User.user_id), comment='ユーザーID')
    purchase_order_name = Column(String(100), nullable=False, comment='注文書名')
    jpy_equivalent = Column(Integer, nullable=True, comment='1元日本円換算')
    domestic_postage = Column(Integer, nullable=True, comment='国内送料(日本円)')
    international_postage = Column(Integer, nullable=True, comment='国際送料(日本円)')
    commision = Column(Integer, nullable=True, comment='手数料(日本円)')
    tariff = Column(Integer, nullable=True, comment='関税')
    order_product_total_price = Column(Integer, nullable=True, comment='注文商品代金合計')
    created_at = Column(DateTime, default=datetime.datetime.now(), nullable=False, comment='作成日時')
    updated_at = Column(DateTime, default=datetime.datetime.now(), onupdate=datetime.datetime.now(), nullable=False, comment='更新日時')
    deleted_at = Column(DateTime, nullable=True, comment='削除日時')
    rakumart_goods = relationship('RakumartGoods', back_populates='rakumart_order_all_cost')
    user = relationship('User', back_populates='rakumart_order_all_cost')


class RakumartGoods(Base):
    __tablename__ = 'rakumart_goods'
    __tabel_args__ = {'comment': 'ラクマート商品管理トランザクションテーブル'}

    goods_id = Column(Integer, primary_key=True, comment='ラクマート商品管理ID')
    purchase_order_id = Column(Integer, ForeignKey(RakumartOrderAllCost.purchase_order_id), comment='注文書ID')
    good_name = Column(String(100), nullable=False, comment='ラクマート商品名')
    goods_quantiry = Column(SMALLINT, nullable=False, comment='ラクマート発注個数')
    goods_cost = Column(Integer, nullable=False, comment='ラクマート商品原価')
    merucari_goods_page_url = Column(Text, nullable=False, comment='メルカリ商品ページURL')
    rakumart_Dgoods_page_url = Column(Text, nullable=False, comment='ラクマート商品ページURL')
    created_at = Column(DateTime, default=datetime.datetime.now(), nullable=False, comment='作成日時')
    updated_at = Column(DateTime, default=datetime.datetime.now(), onupdate=datetime.datetime.now(), nullable=False, comment='更新日時')
    deleted_at = Column(DateTime, nullable=True, comment='削除日時')
    rakumart_order_all_cost = relationship('RakumartOrderAllCost', back_populates=('rakumart_goods'))