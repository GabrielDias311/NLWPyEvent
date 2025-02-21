import pytest
from .subscribers_repository import SubscribersRepository

@pytest.mark.skip("Insert in DB")
def test_insert():
    subscriber_info = {
        "name": "meuNomenomeMeu",
        "email": "mailito@email.com",
        "link": "meuLink",
        "evento_id": 4
  }
    subs_repo = SubscribersRepository()
    subs_repo.insert(subscriber_info)
    
@pytest.mark.skip("Insert in DB")
def test_select_subscribers():
     email = "mailito@email.com"
     evento_id = 4
     
     
     subs_repo = SubscribersRepository()
     resp =subs_repo.select_subscribers(email, evento_id)
     print(resp.email)
@pytest.mark.skip("Insert in DB")     
def test_ranking():
    event_id = 3
    subs_repo = SubscribersRepository()
    resp = subs_repo.get_ranking(event_id)
    
    for elem in resp:
        print(f"Link: {elem.link}, Total de inscritos: {elem.total}")