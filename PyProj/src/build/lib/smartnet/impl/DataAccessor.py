from elixir import *
from smartnet.impl import DataService
from DataService import Community, GeographicalData, Admin
from datetime import datetime
from smartnet.utils.CommunityStatus import CommunityStatus

DataService.initialize()

def GetCommunities():
    return Community.query.all()

def GetCommunity(CommunityId):
    try:
        community = Community.query.filter_by(id=CommunityId).one()
        return community
    except:
        return None
    
def admin_login(obj):
    try:
        return Admin.query.filter_by(email=obj.email, password=obj.password).one()
    except:
        return None
def get_list_of_communities(obj):
    return Community.query.filter_by(created_by=obj.adminId,status=obj.status).all()
    

def create_community(communtity_obj):
    geo_data = GeographicalData.query.filter_by(google_place_id = communtity_obj.place_id).all()
    if geo_data:
        return False
    try:
        geo_data = GeographicalData()
        geo_data.google_place_id = communtity_obj.place_id
        geo_data.lat = communtity_obj.lat
        geo_data.lon = communtity_obj.lon
        session.commit()
        obj = Community()
        obj.name = communtity_obj.name
        obj.city = communtity_obj.city
        obj.street_address = communtity_obj.street_address
        obj.state = communtity_obj.state
        obj.country = communtity_obj.country
        obj.zipcode = communtity_obj.zipcode
        obj.created_by = communtity_obj.created_by
        obj.created_timestamp = datetime.now()
        obj.geo_id = geo_data.id
        obj.type = communtity_obj.type
        obj.status = CommunityStatus.created.value
        session.commit()
        return True
    except:
        return False