import pytest
import uuid
from .participants_repository import ParticipantsRepository
from src.models.settings.db_connection_handler import db_connection_handler

db_connection_handler.connect()
participant_id = str(uuid.uuid4())
trip_id = str(uuid.uuid4())
#trip_id = "6a74b30a-f209-4a26-8f9d-afcc041776cb"
emails_to_invite_id = str(uuid.uuid4())

#@pytest.mark.skip(reason="interacao com o banco")
def test_registry_participant():
    conn = db_connection_handler.get_connection()
    participants_repository = ParticipantsRepository(conn)

    participant_infos = {
        "id": participant_id,
        "trip_id": trip_id,
        "emails_to_invite_id": emails_to_invite_id,
        "name": "Renato"
    }

    participants_repository.registry_participant(participant_infos)

#@pytest.mark.skip(reason="interacao com o banco")
def test_find_participants_from_trip():
    conn = db_connection_handler.get_connection()
    participants_repository = ParticipantsRepository(conn)

    participants = participants_repository.find_participants_from_trip(trip_id)
    print()
    print(participants)