import datetime

from elixir import metadata, setup_all
import elixir
from elixir.entity import Entity
from elixir.fields import Field
from elixir.options import using_options, using_table_options
from elixir.relationships import OneToMany, ManyToOne
from sqlalchemy import create_engine
from sqlalchemy.types import Integer, String, DateTime, Float, Boolean, Text, Enum, BigInteger, Date
from MySQLdb.constants.FLAG import AUTO_INCREMENT


class Community(Entity):
    id = Field(Integer,primary_key=True)
    name = Field(String(255))
    street_address = Field(String(255))
    city = Field(String(20))
    state = Field(String(20))
    zipcode = Field(String(6))
    country = Field(String(20))
    created_by = Field(Integer)
    created_timestamp = Field(DateTime)
    geo_id = Field(Integer)
    type = Field(Integer)
    status = Field(Integer)
    using_options(tablename="Community")
    using_table_options(mysql_engine="InnoDB")
    
class GeographicalData(Entity):
    id = Field(Integer,primary_key=True)
    google_place_id = Field(String(255))
    lat = Field(String(20))
    lon = Field(String(20))
    using_options(tablename="GeoData")
    using_table_options(mysql_engine="InnoDB")
    
class Admin(Entity):
    id = Field(Integer,primary_key=True)
    first_name = Field(String(20))
    last_name = Field(String(20))
    password = Field(String(255))
    email = Field(String(50))
    phone_number = Field(String(20))
    role = Field(Integer)
    using_options(tablename="admin")
    using_table_options(mysql_engine="InnoDB")
    
    



def initialize(dbname='SmartCommunity', db_hostname="localhost", setup=True):
    cengine = create_engine('mysql://root:pioneer@' + db_hostname + '/' + dbname, pool_recycle=7200)
    metadata.bind = cengine
    metadata.bind.echo = True
    setup_all(setup)

if __name__=="__main__":

    initialize()
